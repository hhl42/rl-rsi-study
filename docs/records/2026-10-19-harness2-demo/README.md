# Harness² deterministic demo record

Completed on 2026-10-19. This check exercises the provided local workflow without model services. Its purpose is to make harness edits, execution traces, and library state inspectable for the foundation study. The [study note](../../studies/harness2.md) owns interpretation and proposed next tests.

## Source and command

Repository: [google-research/harness2](https://github.com/google-research/harness2), commit `1cfe254e8d25b15f37048c3730134686abe60335`. The demo is implemented in [demo.py](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/demo.py) and its [CLI](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/cli/demo.py).

From the pinned checkout at `tmp/harness2`, using the existing Python 3.12 study environment, we ran:

```sh
../aes-study-venv/bin/python -B -m harness2.cli.demo --output ../harness2-study-demo --k 1
```

To repeat in another checkout, use a Python version supported by its `pyproject.toml`, substitute the interpreter path, and choose a fresh output directory. The demo uses the standard library and local subprocesses. Both parallel and sequential modes ran; no dependency installation, model API, or benchmark download was needed for this invocation. The upstream checkout was downloaded separately.

## Observed outputs

Exit code: `0`. The saved [result.json](result.json) is the generated summary, copied unchanged.

| Observation | Value |
| --- | --- |
| Completed task workflows | 2 |
| Failed task workflows | 0 |
| Executor invocations across both modes | 14 |
| Scripted editor calls, including reflection | 16 |
| Library entries before first task | 0 per mode |
| Library entries before second task | 1 per mode |

Each task uses seven executor invocations across both modes: one shared initial run and three additional runs per mode. This explains why the combined count is 14 rather than 16. For a comparison of either mode with another method, charge that mode for its own initial run.

The first task's ledger contains `100.25`, `−20.10`, and `5.00`. We inspected these parallel-mode trace files under the demo output:

| Artifact | Observed result |
| --- | --- |
| `executions/demo-oc-agg1/ledger-1/base1/trajectory.md` | Runs `scripts/summarize.py`; prints `Total: 105.25`. |
| `executions/demo-oc-agg1/ledger-1/agg1/trajectory.md` | Runs the edited script; prints `Total: 85.15`. |
| `library/k1/agg/accounting/harnesses/ledger-1/EXPERIENCE.md` | Records removal of the positive-only filter and a lesson to include signed amounts. |

The sum can be checked directly from those three amounts. The difference is caused by a literal scripted edit in `DemoProposer`, not an inferred repair by a model. The summary's completed/failed fields concern workflow completion, not an independently measured benchmark success rate.

## Limits

This confirms that the local demo connects editing, actual Python execution, and library persistence at the pinned revision. At `k=1` there is no selector session. The demo does not test stochastic models, semantic lesson quality, whether later editors use the library, benchmark adapters, isolation, or training. The complete generated tree remains disposable under ignored `tmp/`; this record preserves the command, key evidence, and limits needed by future readers.
