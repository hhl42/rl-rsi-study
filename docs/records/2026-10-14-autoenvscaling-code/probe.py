"""Offline probes of a pinned AutoEnvScaling checkout; no models or sandboxes run.

Run with the upstream package's dependencies installed. Pass the checkout path.
JSON is written to stdout; temporary task artifacts are discarded.
"""

import argparse
import asyncio
import itertools
import json
import random
import subprocess
import sys
import tempfile
from pathlib import Path

REVISION = "2b38259ac0ab5983c7de21df0f50696ab43e8869"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path)
    args = parser.parse_args()
    checkout = args.checkout.resolve()
    revision = subprocess.check_output(
        ["git", "-C", str(checkout), "rev-parse", "HEAD"], text=True
    ).strip()
    if revision != REVISION:
        raise SystemExit(f"Expected {REVISION}, got {revision}")
    if subprocess.check_output(["git", "-C", str(checkout), "diff", "HEAD", "--"], text=True):
        raise SystemExit("Tracked upstream files differ from the pinned revision")
    sys.path.insert(0, str(checkout))

    from autoenvscaling.calibration import band
    from autoenvscaling.calibration.solver import SolverEndpoint
    from autoenvscaling.config import Settings
    from autoenvscaling.pipeline import GenerationPipeline, ProposerSpec, plan_assignments
    from autoenvscaling.pool import Pool, ReplacementRequest
    from autoenvscaling.proposer.assignment import build_assignment
    from autoenvscaling.proposer.workspace import save_persistent
    from autoenvscaling.results import CalibrationReport, CheckResult, ValidationReport
    from autoenvscaling.tasks import HarborTask
    from autoenvscaling.trajectories.export import proposer_rl_groups, scored_proposer_reward
    from autoenvscaling.trajectories.schema import Assignment, ProposerTrajectory, SolverTrajectory, Turn
    from autoenvscaling.validation.harbor_runner import RunResult, TrialOutcome

    output = {"revision": revision, "scope": "synthetic offline probes, not training or reproduction"}

    class ScriptedRunner:
        def __init__(self):
            self.batches = [[0.25, 0.75, None, None], [None, None]]
            self.requested = []

        async def run(self, task_dir, agent, *, n_attempts=1, **kwargs):
            rewards = self.batches.pop(0)
            assert len(rewards) == n_attempts
            self.requested.append(n_attempts)
            return RunResult(outcomes=[
                TrialOutcome(trial_name=f"draw-{len(self.requested)}-{i}", reward=r,
                             infra_error=r is None,
                             exception_type="ApiError" if r is None else None)
                for i, r in enumerate(rewards)
            ])

    with tempfile.TemporaryDirectory(prefix="aes-study-") as scratch:
        root = Path(scratch)
        task_dir = root / "task"
        files = {
            "task.toml": 'version = "1.0"\n',
            "instruction.md": "Restore the service.\n",
            "environment/Dockerfile": "FROM scratch\n",
            "solution/solve.sh": "#!/bin/sh\ntrue\n",
            "tests/test.sh": "#!/bin/sh\ntrue\n",
        }
        for name, content in files.items():
            path = task_dir / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
        task = HarborTask(task_dir)
        settings = Settings()
        settings.work_dir = root / "work"
        solver = SolverEndpoint("http://unused.invalid/v1", "synthetic", api_key_env="AES_STUDY_UNUSED_KEY")
        runner = ScriptedRunner()
        report = asyncio.run(band.calibrate(task, solver, settings, runner=runner))
        output["calibration_after_infrastructure_failures"] = {
            "requested_per_call": runner.requested, "scored_rewards": report.rewards,
            "verdict": report.verdict, "mean": report.mean, "std": report.std,
        }

        assignment = Assignment("shared-assignment", "parent", 0.5)

        async def fake_episode(*args, **kwargs):
            return ProposerTrajectory(
                "infra", assignment, "synthetic", "pi", task_dir=str(task_dir),
                turns=[Turn("user", "Create a task."), Turn("assistant", "Task files written.")],
            )

        async def fake_validate(*args, **kwargs):
            return ValidationReport("task", [CheckResult(
                "build", False, "Synthetic endpoint failure", {"infra_error": True})])

        async def forbidden_calibration(*args, **kwargs):
            raise AssertionError("Calibration must not run after failed validation")

        pipeline = GenerationPipeline(
            settings, proposer=ProposerSpec("pi", "synthetic"), solver=solver,
            out_dir=root / "pipeline", episode_fn=fake_episode,
            validate_fn=fake_validate, calibrate_fn=forbidden_calibration,
        )
        chain = asyncio.run(pipeline.run_chain(
            assignment, sample=0, round_dir=root / "round", workspace_dir=root,
            sink=lambda trajectory: None,
        ))
        failed = chain[0]
        good = ProposerTrajectory(
            "good", assignment, "synthetic", "pi", reward=1.0,
            turns=[Turn("user", "Create a task."), Turn("assistant", "Task accepted.")],
        )
        groups, _ = proposer_rl_groups([failed, good])
        output["infrastructure_error_export"] = {
            "pipeline_reward": failed.reward,
            "validation_infra_error": failed.validation["checks"][0]["data"]["infra_error"],
            "exported_reward": scored_proposer_reward(failed),
            "group_rewards": groups[0].rewards,
            "training_sample_ids": [sample.trajectory_id for sample in groups[0].samples],
        }

        pool = Pool(root / "pool")
        entry = pool.seed([task_dir])[0]
        rollouts = [SolverTrajectory(f"s{i}", entry.task_id, "synthetic", reward=r,
                                    verifier_output="FAILED check_recovery")
                    for i, r in enumerate([0.0, 0.5, 1.0, 1.0])]
        pool.record_rollouts(entry.task_id, rollouts, step=0)
        request = ReplacementRequest(entry.task_id, str(task_dir), 0.625, "in_pool")
        ablated = plan_assignments(pool, [request], 1, round_id="probe", rng=random.Random(0),
                                   solver_feedback=False)[0]
        output["no_solver_feedback_assignment"] = {
            "common_failure": ablated.common_failure,
            "pass_rate": ablated.solver_pass_rate,
            "direction": ablated.direction,
            "extra": {k: v for k, v in ablated.extra.items() if k != "parent_task_dir"},
        }
        partial = build_assignment("partial", [
            SolverTrajectory(f"p{i}", "partial", "synthetic", reward=0.75) for i in range(4)
        ])
        output["partial_reward_assignment"] = {
            "pass_rate": partial.solver_pass_rate, "mean_reward": partial.extra["mean_reward"],
            "direction": partial.direction,
        }

        for name, text in [("first", "keep an earlier lesson"), ("last", "keep a later lesson")]:
            memory = root / name / "memory"
            memory.mkdir(parents=True)
            (memory / "lesson.txt").write_text(text)
            save_persistent(root / name, root / "persistent")
        output["persistent_memory"] = {
            "retained_text": (root / "persistent/memory/lesson.txt").read_text(),
            "selection_rule": "latest copied directory; no merge or reward-based selection",
        }

    output["rubric_skipped"] = list(settings.validation.rubric_skip)
    output["binary_calibration_model"] = []
    cal = settings.calibration
    # Exact enumeration of all 256 possible sequences; no Monte Carlo error.
    # Model assumption: independent binary rewards with fixed success probability p.
    for p in (0.1, 0.25, 0.5, 0.75, 0.9):
        accepted = 0.0
        expected_samples = 0.0
        for bits in itertools.product((0, 1), repeat=cal.max_rollouts):
            probability = p ** sum(bits) * (1 - p) ** (len(bits) - sum(bits))
            first = bits[:cal.initial_rollouts]
            expand = band.needs_more_rollouts(sum(first) / len(first), cal)
            used = bits if expand else first
            outcome = CalibrationReport("binary", list(used), cal.band_low, cal.band_high,
                                        cal.min_reward_std)
            accepted += probability * outcome.passed
            expected_samples += probability * len(used)
        output["binary_calibration_model"].append({
            "true_success_probability": p, "admission_probability": round(accepted, 8),
            "expected_scored_attempts": round(expected_samples, 8),
        })
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
