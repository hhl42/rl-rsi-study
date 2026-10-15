"""Independent check of the binary calibration admission probability.

Part A: closed form from my reading of band.py / results.py (no upstream imports).
Part B: drive the real upstream band.calibrate() with a scripted runner for all 256
         outcome sequences, so the actual async control flow (draw, _draw_scored,
         needs_more_rollouts, expansion, CalibrationReport) decides each verdict.
"""
import asyncio, itertools, sys, tempfile
from fractions import Fraction as F
from math import comb
from pathlib import Path

def binom(n, k, p):
    return comb(n, k) * p**k * (1 - p)**(n - k)

def closed_form(p):
    p = F(p)
    # 4 initial binary draws: mean k/4. Expansion when min(|m-.25|,|m-.75|) <= .15 (either side).
    # k=1 -> m=.25 (dist 0) expand; k=3 -> m=.75 expand; k=0,2,4 -> dist .25 no expand.
    # Without expansion: k=2 -> mean .5, pstdev .5 -> admitted; k=0 too_hard; k=4 too_easy.
    # With expansion to 8: admitted iff total s in [2,6] (mean in [.25,.75]); pstdev>=.433 > .1 there.
    adm = binom(4, 2, p)
    adm += binom(4, 1, p) * sum(binom(4, l, p) for l in range(5) if 2 <= 1 + l <= 6)
    adm += binom(4, 3, p) * sum(binom(4, l, p) for l in range(5) if 2 <= 3 + l <= 6)
    exp_n = 4 + 4 * (binom(4, 1, p) + binom(4, 3, p))
    return adm, exp_n

def upstream_check(checkout):
    sys.path.insert(0, str(checkout))
    from autoenvscaling.calibration import band
    from autoenvscaling.calibration.solver import SolverEndpoint
    from autoenvscaling.config import Settings
    from autoenvscaling.tasks import HarborTask
    from autoenvscaling.validation.harbor_runner import RunResult, TrialOutcome

    class Seq:
        def __init__(self, bits):
            self.bits = list(bits); self.used = 0
        async def run(self, task_dir, agent, *, n_attempts=1, **kw):
            out = self.bits[self.used:self.used + n_attempts]; self.used += n_attempts
            return RunResult(outcomes=[TrialOutcome(trial_name=f"t{self.used}-{i}", reward=float(b))
                                       for i, b in enumerate(out)])

    results = {}
    with tempfile.TemporaryDirectory() as d:
        root = Path(d); t = root / "task"
        for name, c in {"task.toml": 'version = "1.0"\n', "instruction.md": "x\n",
                        "environment/Dockerfile": "FROM scratch\n", "solution/solve.sh": "true\n",
                        "tests/test.sh": "true\n"}.items():
            (t / name).parent.mkdir(parents=True, exist_ok=True); (t / name).write_text(c)
        task = HarborTask(t); s = Settings(); s.work_dir = root / "work"
        s.calibration.hint_probe_below_band = False
        solver = SolverEndpoint("http://unused.invalid/v1", "x", api_key_env="NOPE_UNUSED")
        for bits in itertools.product((0, 1), repeat=8):
            r = Seq(bits)
            rep = asyncio.run(band.calibrate(task, solver, s, runner=r))
            results[bits] = (rep.passed, len(rep.rewards), r.used)
    return results

if __name__ == "__main__":
    ps = [F(1, 10), F(1, 4), F(1, 2), F(3, 4), F(9, 10)]
    print("closed form:")
    for p in ps:
        a, n = closed_form(p)
        print(f"  p={float(p):.2f} admit={float(a):.8f} expected_n={float(n):.4f}")
    if len(sys.argv) > 1:
        res = upstream_check(Path(sys.argv[1]))
        print("upstream calibrate() over 256 sequences:")
        for p in ps:
            a = sum(F(p)**sum(b) * (1 - F(p))**(8 - sum(b)) for b, (ok, n, used) in res.items() if ok)
            n = sum(F(p)**sum(b) * (1 - F(p))**(8 - sum(b)) * nn for b, (ok, nn, used) in res.items())
            print(f"  p={float(p):.2f} admit={float(a):.8f} expected_n={float(n):.4f}")
        # Also show which 4-prefix counts triggered expansion
        exp = sorted({sum(b[:4]) for b, (ok, n, used) in res.items() if n == 8})
        print("  initial success counts that expanded:", exp)
