# AutoEnvScaling study

AutoEnvScaling is our first detailed study of an adaptive task-generation system. It connects environment construction to solver feedback and then to training. Its value for this project is the complete experimental loop, including the checks and resource costs around generation.

**Evidence:** selected methods and results from the supplied [v1 paper](../../references/papers/2610.14163v1-AutoEnvScaling.pdf), especially sections 3–4 and appendices G–H. Results below are author-reported. The [official repository](https://github.com/MSR-Orchard/AutoEnvScaling) README was inspected on 2026-10-14; code behavior has not been audited or reproduced. The [source register](../../references/README.md#provided-papers) records file identity.

## How the system works

There are two roles. The **solver** attempts tasks. The **proposer** builds tasks for the solver. A host process controls admission to the training pool.

1. The proposer receives an assignment based on a parent environment, solver performance, and a recurring failure.
2. It inspects trajectories and existing environments. It writes an instruction, runtime environment, reference solution, and tests as a Harbor task.
3. It builds and tests the task inside a sandbox and can revise it.
4. Host validation checks execution, the reference solution, an empty solution, contamination, and task quality.
5. Calibration measures whether the current solver produces a useful range of rewards on the task.
6. Accepted tasks enter the pool. Solver training and later pool reviews produce new assignments.

This is a concrete systems distinction from asking a model to emit a task description. The proposer can execute the artifact, observe errors, and repair it. The admission checks remain outside the parts of the workspace that it can change. Source: section 3.

## Validation and calibration

The paper's appendix G.4 specifies the following admission policy:

| Check | Paper setting | What it establishes |
| --- | --- | --- |
| Build and files | Valid package and successful environment build | The package can execute under this setup |
| Reference solution | Reward equals 1 | At least the supplied solution passes |
| Empty solution | Reward below 0.5 | Doing nothing does not receive high reward |
| Contamination | Flag instruction overlap of 13 consecutive words with held-out tasks | Detects a particular form of textual overlap |
| Task review | Proposer's model applies the Harbor task rubric; binary-only reward criterion excluded | Additional model-based review |
| Calibration | Mean reward in [0.25, 0.75], standard deviation at least 0.1 | Attempts provide differing rewards at moderate average difficulty |

Calibration starts with four solver rollouts and expands to eight near a mean-reward boundary. Failed assignments allow up to two revisions. These are the paper's choices, not universal requirements for our framework.

The distinction between mean reward and reward variation matters. Attempts that all score 0.5 meet the mean band but give no within-group ranking. Attempts that differ because tests are flaky also give variation, but it is not useful evidence about solver actions. Our audit should examine the cause of variation.

The authors acknowledge that reference solutions and tests can share a mistake. A model review using the proposer's own model is not independent confirmation. Our interpretation is that independent alternatives, negative controls, and expert sampling remain valuable even after admission passes.

## What learns

The paper studies two settings. With an external closed-weight proposer, the proposer's weights stay fixed while its harness, tools, and memory can improve. RL updates the solver. In the shared-model setting, one open-weight policy trains on both proposer and solver trajectories.

The solver reward is the fraction of tests passed. The proposer receives -1 for failed validation, -0.25 for passing validation but failing calibration, and 1 for admission. The method uses Divergence Proximal Policy Optimization, or DPPO, with advantages computed separately for the two roles. Its advantages are mean-centered without GRPO's standard-deviation normalization. Source: section 3.3 and appendix G.1.

The shared-model experiment starts with supervised fine-tuning on 600 proposer trajectories from external models. Thus, its later self-training does not establish independence from external demonstrations at initialization. Source: appendix H.

## Results that matter for our decisions

The paper reports avg@5 for these Terminal-Bench evaluations. This averages performance over five attempts; it is different from pass@5, which asks whether any attempt succeeds. All compared methods use the paper's Pi harness and evaluation resources. Avoid comparing these figures directly with a different harness's leaderboard score.

| Comparison | Reported result | Interpretation and limit |
| --- | --- | --- |
| Qwen3.5-35B-A3B, GPT-5.6-sol proposer, Terminal-Bench 2.1 | Static Tmax: 34.6 ± 1.9; AutoEnvScaling: 38.9 ± 2.4 | Table 3 reports a 4.3-point gain under matched training steps; the table labels ± as confidence intervals. |
| Same setting, remove solver feedback | Score falls to 35.3 ± 2.3 | Supports examining failure traces as an input to generation. The remaining difference from static generation is small. |
| Shared Qwen3.6-35B-A3B after cold start, Terminal-Bench 2.1 | 41.1 to 53.3; static Tmax ends at 47.2 | A 12.2-point gain over the starting checkpoint and 6.1 over the static comparison. Figure 6 and section 4.3. |
| Shared model, Terminal-Bench 4.0 | 1.6 to 3.2; static Tmax ends at 1.4 | Improvement transfers to a harder evaluation, but absolute performance remains low. |

The training comparisons match solver updates, **not total compute or elapsed time**. The full and static runs reach 288 updates. The no-proposer-training ablation ends at 160; at that common endpoint the full, static, and ablation scores are 48.9, 44.9, and 40.1. Comparing the full final result with an earlier ablation endpoint would overstate the isolated effect. Source: appendix G.1.

The reported shared-model training uses 4–8 B200 GPUs. Each solver batch retains 16 environment groups with 16 trajectories per group. Groups with no reward variation are discarded and replaced. The active pool has 256 tasks and is reviewed every 16 solver updates. These settings explain why a faithful training reproduction is a separate resource decision. A small generation experiment does not require reproducing the full run.

## What to inspect in the implementation

The repository README describes a preview release. Before relying on it, record a commit and trace one task through assignment, sandbox execution, validation, calibration, pool update, and result recording. Inspect how retries and failed calls affect cost and how benchmark material is excluded. Check the behavior against the paper rather than treating the README as an execution trace.

Pay particular attention to resumable trajectories. The paper carries unfinished terminal episodes across policy updates. A reproduction needs the recorded policy version and sampling probabilities, along with environment state. Restoring files alone may not restore the experiment.

## Questions for our experiments

- Does solver feedback improve diversity and relevance after accounting for its collection cost?
- How often do admitted tasks fail an independent verifier audit?
- Does difficulty estimated from four or eight attempts remain stable on later attempts?
- Does selecting tasks for one solver produce useful tasks for another?
- Do training gains persist under a total-budget comparison that includes task generation and calibration?
- Which parts can be reused from Harbor and the released system, and which need domain expertise?

The first practical adaptation is [E2 in the study plan](../01-study-plan.md#e2-generate-from-solver-failures): hold the solver fixed and isolate the value of failure traces. Combine it with verifier auditing before attempting joint training. This tests an important component without claiming to reproduce the paper.
