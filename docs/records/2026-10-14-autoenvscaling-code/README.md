# AutoEnvScaling offline code study: 2026-10-14

**Question:** What does the released implementation teach us about task generation, admission, calibration, and training interfaces? Which assumptions need checking before a live pilot?

**Source:** [MSR-Orchard/AutoEnvScaling](https://github.com/MSR-Orchard/AutoEnvScaling/tree/2b38259ac0ab5983c7de21df0f50696ab43e8869), commit `2b38259ac0ab5983c7de21df0f50696ab43e8869` (2026-10-13). Tracked upstream files were unchanged. The paper is the supplied [v1 PDF](../../../references/papers/2610.14163v1-AutoEnvScaling.pdf); its identity is recorded in the [source register](../../../references/README.md#integrity-of-supplied-files).

## What ran

- Selected upstream tests: **198 passed**, zero failures/errors/skips, one Starlette deprecation warning. Nineteen modules covered rewards, calibration, validation, assignment, workspace, episodes, pipeline, pool, export, self-play, and Miles/carry adapters. [Machine-readable summary](test-summary.json).
- [Our probe](probe.py): synthetic inputs passed through real upstream functions, with fake model and execution dependencies. [Complete outputs](probe-results.json).
- Exact enumeration of binary outcomes under the calibration rule: all 256 length-eight sequences, weighted by each assumed success probability. No Monte Carlo sampling error.

There were no model requests, container trials, cloud sandboxes, or GPU training. Tests use fakes and do not verify live API compatibility, isolation, generated task validity, or training improvement. Dependencies and source code were downloaded to an isolated environment under the ignored `tmp/` directory. No upstream changes were made.

Python was 3.12.14 on Darwin arm64. [environment.json](environment.json) records all 106 installed package versions, including Harbor 0.23.0 and Modal 1.6.1. This is an observed environment manifest, not a portable lockfile or the paper's training environment.

## Findings and interpretation

| Probe | Observed output | Interpretation |
| --- | --- | --- |
| Infrastructure failure through pipeline and export | Pipeline reward `null`; export reward `-1`; failed sample included beside a successful sample | Confirmed status-loss defect at the export boundary. |
| Calibration with repeated infrastructure failures | Requested batches of 4 and 2; two valid rewards `[0.25, 0.75]`; admitted | Minimum scored count is not enforced. |
| No-feedback assignment | Failure text cleared; aggregate statistics and direction retained | This removes trajectories, not all solver-derived information. |
| Four partial successes | Mean reward 0.75; full pass rate 0; direction `simpler` | Assignment direction and calibration use different measures. |
| Two memory writes | Only the later copied text retained | Directory replacement, without merging or quality selection. |
| Default rubric | Ten skipped criteria | Compare the effective checklist with the paper's stated binary-only exception. |
| Binary calibration model | Admission probabilities about 15.2%, 54.6%, 84.4%, 54.6%, 15.2% for success probabilities 0.1, 0.25, 0.5, 0.75, 0.9 | Small-sample selection is noisy even under independent, stationary outcomes. This is not an empirical LLM estimate. |

The [code study](../../studies/autoenvscaling-code.md) owns detailed source analysis. The [main study](../../studies/autoenvscaling.md#7-what-to-test-next) owns the next tests. These findings justify contract checks and verifier auditing before training on generated output; they do not establish effects on the paper's historical runs.

## Repeat the checks

Run from this repository root with Git, uv, and Python 3.12 available. Use a fresh checkout destination if `tmp/autoenvscaling` already exists. Setup downloads public code and dependencies; the test/probe commands do not need model credentials.

```sh
mkdir -p tmp
GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1 git clone --no-checkout https://github.com/MSR-Orchard/AutoEnvScaling.git tmp/autoenvscaling
git -C tmp/autoenvscaling checkout --detach 2b38259ac0ab5983c7de21df0f50696ab43e8869
UV_CACHE_DIR=tmp/uv-cache uv venv --python 3.12 tmp/aes-study-venv
UV_CACHE_DIR=tmp/uv-cache uv pip install --python tmp/aes-study-venv/bin/python -e 'tmp/autoenvscaling[dev]'
```

The Git environment overrides avoid local URL rewrite rules. Installation above repeats the original dependency resolution procedure; later package resolution may differ. Compare the resulting versions with `environment.json` when interpreting differences.

Run exactly the recorded test modules, using the summary as the selection list:

```sh
tmp/aes-study-venv/bin/python - <<'PY'
import json
import os
from pathlib import Path
import subprocess
import sys

root = Path.cwd()
record = root / 'docs/records/2026-10-14-autoenvscaling-code'
summary = json.loads((record / 'test-summary.json').read_text())
modules = [name.replace('.', '/') + '.py' for name in summary['modules']]
env = dict(os.environ, AES_LIVE_TESTS='0', LITELLM_LOCAL_MODEL_COST_MAP='true')
subprocess.run([sys.executable, '-m', 'pytest', '-q', *modules],
               cwd=root / 'tmp/autoenvscaling', env=env, check=True)
PY
```

Run the synthetic probes and compare output without replacing the committed observation:

```sh
tmp/aes-study-venv/bin/python docs/records/2026-10-14-autoenvscaling-code/probe.py tmp/autoenvscaling > tmp/aes-probe-results.json
diff -u docs/records/2026-10-14-autoenvscaling-code/probe-results.json tmp/aes-probe-results.json
```

The probe rejects a different commit or modified tracked upstream files. Its placeholder endpoint is never contacted because execution dependencies are injected. Temporary task files are discarded automatically. If dependencies, source, or assumptions change, create a new dated record rather than overwriting these observations.
