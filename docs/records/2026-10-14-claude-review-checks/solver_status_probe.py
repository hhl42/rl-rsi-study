"""Synthetic check: how solver trials with agent-side endpoint failures are classified and exported."""
import json, sys, tempfile
from pathlib import Path
sys.path.insert(0, sys.argv[1])
from autoenvscaling.validation.harbor_runner import parse_trial
from autoenvscaling.calibration.solver import to_trajectory, SolverEndpoint
from autoenvscaling.tasks import HarborTask
from autoenvscaling.trajectories.export import scored_solver_reward, solver_rl_groups
from autoenvscaling.proposer.assignment import attempt_reward
from autoenvscaling.trajectories.schema import SolverTrajectory, Turn

def trial(d, name, exc_type, msg, reward):
    td = Path(d) / name; (td / "verifier").mkdir(parents=True)
    (td / "verifier" / "ctrf.json").write_text(json.dumps({"results": {"summary": {"passed": 1, "tests": 4}}}))
    data = {"trial_name": name, "environment_setup": {}, "agent_setup": {}, "agent_execution": {},
            "exception_info": {"exception_type": exc_type, "exception_message": msg},
            "verifier_result": {"rewards": {"reward": reward}}}
    return parse_trial(data, td)

out = {}
with tempfile.TemporaryDirectory() as d:
    task_dir = Path(d) / "task"; task_dir.mkdir()
    (task_dir / "instruction.md").write_text("x")
    task = HarborTask(task_dir)
    ep = SolverEndpoint("http://unused.invalid/v1", "m", api_key_env="NOPE_UNUSED")
    cases = {
        "nonzero_exit_rate_limit_msg": ("NonZeroAgentExitCodeError", "pi exited 1: 429 Too Many Requests", 0.25),
        "nonzero_exit_other_endpoint_msg": ("NonZeroAgentExitCodeError", "pi exited 1: upstream model server returned invalid JSON", 0.25),
    }
    trajs = []
    for name, (t, m, r) in cases.items():
        o = trial(d, name, t, m, r)
        tr = to_trajectory(task, ep, o, "x")
        tr.turns.append(Turn("assistant", "did something"))
        trajs.append(tr)
        out[name] = {"infra_error": o.infra_error, "trial_reward": o.reward,
                     "trajectory_reward": tr.reward, "tests": [tr.tests_passed, tr.tests_total],
                     "export_reward": scored_solver_reward(tr), "assignment_reward": attempt_reward(tr)}
    ok = SolverTrajectory("good", task.task_id, "m", turns=[Turn("user", "x"), Turn("assistant", "y")], reward=1.0)
    groups, stats = solver_rl_groups(trajs + [ok])
    out["solver_group_rewards"] = groups[0].rewards if groups else None
print(json.dumps(out, indent=2))
