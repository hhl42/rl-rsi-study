# Review checks of the AutoEnvScaling code study: 2026-10-14

**Question:** Do the findings in the [AES code study](../../studies/autoenvscaling-code.md) hold when someone else repeats them? Are there other places where an infrastructure failure becomes a task or agent result?

**Source:** the same upstream checkout as the [original record](../2026-10-14-autoenvscaling-code/README.md), commit `2b38259ac0ab5983c7de21df0f50696ab43e8869`, with tracked files unchanged. The same virtual environment was reused; its 106 package versions match that record's `environment.json`. The [Claude review](../../reviews/claude-init-review-1.md#23-the-aes-code-study) uses these results.

## What ran

- The original record's test command: **198 passed**, one Starlette deprecation warning. The only change was adding `-p no:cacheprovider` so pytest wrote no cache into the checkout.
- The original probe: its output was byte-identical to the committed `probe-results.json`.
- [enum_check.py](enum_check.py): an independent check of the calibration admission probabilities. It computes them in closed form, then drives the real `band.calibrate()` through all 256 eight-attempt binary sequences. [Output](enum_check.out).
- [solver_status_probe.py](solver_status_probe.py): passes two synthetic solver trials through the real parsing, trajectory, assignment, and export functions. Both trials exit with an agent error and a verifier report of 1 of 4 tests passed. [Output](solver_status_probe.out).

No model, sandbox, container, or training run was used. The solver endpoint address is a placeholder that is never contacted.

## Results

| Check | Observed output | Interpretation |
| --- | --- | --- |
| Calibration enumeration | Admission probability 0.1525, 0.5460, 0.8438 for success probability 0.1, 0.25, 0.5 (mirrored above 0.5); both methods agree | Confirms the original record. Expansion to eight attempts happens only after 1 or 3 successes in the first 4. |
| Solver trial whose error message matches the infrastructure pattern | Trial marked as infrastructure error with reward `null`; export and assignment both give 0.25; it enters the training group `[0.25, 0.25, 1.0]` | The export defect in the code study also exists on the solver side. Export falls back to test counts when the reward is missing. |
| Solver trial with a different endpoint error message | Not marked as infrastructure; reward 0.25 | Whether a failure counts as infrastructure depends on matching the error text. |

The solver-side result depends on two things not run live: Harbor still running the verifier after the agent exits with an error, and the task writing a CTRF or JUnit test report. A quick reading of Harbor 0.23 suggests the verifier does run.

## Repeat the checks

Set up `tmp/` as in the [original record](../2026-10-14-autoenvscaling-code/README.md#repeat-the-checks), then run from the repository root:

```sh
LITELLM_LOCAL_MODEL_COST_MAP=true tmp/aes-study-venv/bin/python -I docs/records/2026-10-14-claude-review-checks/enum_check.py "$PWD/tmp/autoenvscaling"
LITELLM_LOCAL_MODEL_COST_MAP=true tmp/aes-study-venv/bin/python -I docs/records/2026-10-14-claude-review-checks/solver_status_probe.py "$PWD/tmp/autoenvscaling"
```

Compare the printed output with the saved `.out` files.
