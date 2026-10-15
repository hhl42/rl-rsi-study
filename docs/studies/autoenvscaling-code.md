# AutoEnvScaling code study

This document owns the implementation evidence behind the [systems explanation](autoenvscaling.md). We inspected selected paths at commit `2b38259ac0ab5983c7de21df0f50696ab43e8869`, dated 2026-10-13, and ran offline checks on 2026-10-14. All source links below pin that commit. This is a focused review, not a full security audit or reproduction of the research runs.

The [original research record](../records/2026-10-14-autoenvscaling-code/README.md) owns test counts, dependencies, commands, and probe outputs. The [independent review checks](../records/2026-10-14-claude-review-checks/README.md) extend the failure analysis below. Evidence here is from code reading and synthetic inputs; live execution and training remain untested. Upstream code is unchanged.

## 1. Code map

Read these in order to follow a task from authoring to training. Paths below are in the upstream repository.

| Component | Entry point | Responsibility |
| --- | --- | --- |
| Task artifact | [tasks.py](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/tasks.py) | Required Harbor files, metadata, artifact digest. |
| Assignment | [assignment.py: build_assignment](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/proposer/assignment.py#L139) | Summarize solver rewards and failure text; choose difficulty direction. |
| Workspace and episode | [workspace.py](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/proposer/workspace.py), [episode.py](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/proposer/episode.py#L279) | Stage inputs, start the authoring harness, retrieve output and persistent files. |
| Host orchestration | [pipeline.py: run_chain](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/pipeline.py#L260) | Score each submitted task, record its trajectory, and request revisions. |
| Admission | [admission.py: validate](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/validation/admission.py#L57) | Structural, execution, contamination, and rubric checks. |
| Calibration | [band.py: calibrate](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/calibration/band.py#L49) | Sample the current solver, expand near a boundary, and return a difficulty verdict. |
| Pool | [pool.py](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/pool.py#L202) | Admission, exact duplicate rejection, active/reserve membership, and review. |
| Training groups | [export.py](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/trajectories/export.py#L397), [rewards.py](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/rewards.py) | Convert trajectories to messages, rewards, and group-relative advantages. |
| Training orchestration | [selfplay/loop.py](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/selfplay/loop.py) | Collect solver groups, invoke the trainer, refresh the pool, and schedule proposer work. |
| Trainer integration | [Miles bridge](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/training/miles/rollout.py), [carry rollout](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/training/carry/rollout.py) | Two different ways to collect and deliver training data. See section 4. |

## 2. Admission is several different judgments

The [validation path](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/validation/admission.py#L57) rejects malformed packages before running trials. Reference-agent execution supplies the build evidence; it must earn reward at least 1. The empty agent must earn less than 0.5. Failed build/reference checks skip later expensive work. Local contamination checks still run. An unavailable reviewer or trial infrastructure can mark a check as an infrastructure error.

The [contamination index](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/validation/contamination.py) compares normalized instruction word sequences against held-out instructions. It catches literal overlap, not semantic similarity, related source repositories, or copied test logic. The artifact digest similarly catches identical content, not equivalent tasks. Our split policy still needs parent/source provenance.

The [rubric runner](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/validation/rubric.py#L126) applies configured exclusions before requesting Harbor review. Missing required verdicts count as errors. This is useful defensive behavior, but passing a model review is not independent evidence that the author's tests are correct.

[_run_one](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/validation/admission.py#L167) requests one reference and one empty-agent attempt, without a repeated-reset check. Harbor may retry execution errors; that is different from testing repeatability. The proposer can also call [solver_model](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/docker/proposer/tools/solver_model) before submitting. Record this extra sampling cost and use fresh calibration attempts when checking whether repeated tuning has exploited noisy estimates.

The paper defines solver reward as the fraction of tests passed. The Harbor path reads the verifier's numeric reward file; it does not enforce that formula. The release-status page leaves consistent injection of a fraction-of-tests template open. Thus a task's reward semantics must be checked, not inferred from the experiment's name.

## 3. Confirmed behavior and its consequences

The probe results are observations about this commit. They do not establish that these behaviors occurred in the original research runs.

### Infrastructure errors can become training rewards

**Observed defect.** [run_chain](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/pipeline.py#L298) deliberately records `reward=None` when validation has an infrastructure error. The error flag survives inside the serialized check data. But [scored_proposer_reward](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/trajectories/export.py#L397) derives a missing reward from `validation.passed` without checking that flag.

Our probe injected an infrastructure failure through the real pipeline with fake execution dependencies. The pipeline produced `None`; the exporter produced `-1`. With a successful sample from the same assignment, both entered an RL group with rewards `[-1, 1]`. This can teach the proposer to avoid an output because infrastructure failed, even though its task quality is unknown.

The solver path has the same kind of defect. [scored_solver_reward](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/trajectories/export.py#L407) and [attempt_reward](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/proposer/assignment.py#L46) reconstruct a missing reward from test counts. The review's synthetic trial had an infrastructure error, no reward, and one of four tests passed. Export and assignment summaries treated it as 0.25, while calibration and pool review excluded it. The [solver-status probe](../records/2026-10-14-claude-review-checks/solver_status_probe.py) reproduced this during resolution of the review. It assumes a failed agent still leaves a verifier report; this was not exercised live.

**Before reuse:** preserve an explicit unscored status through serialization, assignment summaries, and training export. Test the same outcome through every consumer, rather than fixing only one fallback function.

### Failure classification and pool review need one shared policy

[parse_trial and its failure classifier](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/validation/harbor_runner.py#L317) use exception types, execution phase, and message patterns. The review probe classified a rate-limit message as infrastructure failure, but scored a different endpoint-error message when a verifier reward existed. Build-budget and verifier timeouts normally count against the task. These are policy choices that need recorded reasons; a timeout alone does not identify its cause.

In [pool.review](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/pool.py#L340), three unavailable attempts and one scored attempt leave a one-element sample. Its standard deviation is zero, so the default review retires the task. With no scored attempts it instead keeps the task unchanged. An exception from a review worker propagates through `asyncio.gather` and the self-play call. These findings are from code reading, not a live outage experiment.

For our framework, use one outcome record with execution state, phase, reason, evidence, and an optional reward. Keep scoring eligibility explicit: `scored` or `unscored`. An `agent_failed` outcome can still be scored if the verifier completed reliably; a `task_broken` or `infrastructure_failed` outcome may be unscored. Define these rules once and apply them in calibration, pool review, assignment, and export.

### Calibration can admit fewer scored attempts than requested

[calibrate and _draw_scored](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/calibration/band.py#L66) retry missing outcomes once. [CalibrationReport](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/results.py#L54) checks the mean and standard deviation but has no minimum sample count.

Our fake runner returned `[0.25, 0.75, unavailable, unavailable]`, then two more unavailable outcomes. Only two attempts had scores. Their mean was 0.5 and standard deviation 0.25, so the task was admitted. The nominal four-attempt setting is not a guarantee of four valid observations.

Even with no infrastructure failures, small samples give uncertain decisions. We exactly enumerated the default rule under a simplified model: each attempt has an independent binary outcome with fixed success probability. A task with true success probability 0.5 is admitted about 84.4% of the time; one with probability 0.1 is admitted about 15.2% of the time. These are mathematical model results, not measured LLM performance. Real tasks also have partial credit and correlated failures.

**Before reuse:** distinguish requested, executed, and scored attempts. Allow insufficient-evidence outcomes. Measure admission stability on fresh samples before choosing thresholds.

### The preview skips more rubric checks than the paper specifies

Paper appendix G.4 names the binary-reward criterion as the exception. [ValidationSettings](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/config.py#L30) skips ten criteria: binary reward plus README, time estimate, category/tags, task name, three explanation-quality checks, CTRF reporting, and separate verifier configuration. The [release-status document](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/docs/release-status.md) says this matches author decisions for the paper runs. The written accounts therefore differ; we cannot resolve that from this release.

**Implication:** persist the actual checklist and reviewer version with every decision. Some exclusions concern packaging rather than correctness, but their effect on acceptance must be explicit.

### Removing solver feedback does not remove all solver information

[plan_assignments](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/pipeline.py#L112) clears failure text in the no-feedback condition, and workspace construction omits past solver trajectories. However, assignments still retain full success rate, mean reward, reward variation, attempt count, and a difficulty direction derived from them. The probe confirmed this.

The default assignment rule requests a harder variant at full pass rate ≥ 0.5. A [replacement request](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/pool.py#L88) overrides this direction when mean-reward review classified the parent as too easy or too hard. Under the intended [0, 1] reward range, partial credit can give a high mean without any full successes.

This is consistent with an ablation described as removing past trajectories. It should not be interpreted as removing every solver-derived signal. For our E2 experiment, hold aggregate statistics constant and vary trace access; use a separate condition if studying all feedback.

### Persistent memory is copied, not selected for quality

[save_persistent](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/proposer/workspace.py#L246) replaces each shared `memory/` or `tools/` directory with the episode's copy. The pipeline calls it before scoring. Parallel chains begin from the round's workspace snapshot; later completed episodes can overwrite earlier changes. Our sequential copy probe confirmed replacement rather than merging. It did not measure concurrency behavior or memory quality.

There is no reward-based acceptance rule for these changes in this path. A failed task can still supply the memory used later. Preserve candidate memory versions and define selection or merging if we want to attribute improvement to persistent learning.

The [workspace sealing code](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/proposer/episode.py#L215) explicitly treats permissions as advisory because the agent runs as root. Host restaging prevents modifications from becoming future fixed inputs. It does not prove that malicious task code cannot interfere within an episode. No adversarial isolation test was performed.

## 4. Pool and training boundaries

The [pool](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/pool.py#L202) copies admitted tasks and rejects exact content duplicates. `seed` only checks required files; it does not validate or calibrate them. `review` rechecks active and reserve tasks and retires unsuitable ones. The [self-play reviewer](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/selfplay/loop.py#L161) uses four attempts. Admission and later review therefore have different sampling policies.

The [exporter](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/trajectories/export.py#L451) groups proposer revisions with initial attempts by assignment unless configured otherwise. A setting of 128 proposer chains need not mean exactly 128 exported trajectories. Groups with constant rewards are discarded. Count actual training samples and all attempted episodes separately.

The release has two trainer paths:

| Concern | Bridge path | Carry path |
| --- | --- | --- |
| Episode lifetime | Self-play waits for episodes to finish. | Unfinished episodes can remain alive across weight updates. |
| Batch filling | Up to three sampling waves; can return fewer than 16 useful groups. | Continues until the required number of valid groups is collected, or fails. |
| Training representation | Re-tokenizes recorded conversations; does not preserve the original engine's sampling log-probabilities. | Recording proxy retains sampled token IDs, log-probabilities, and loss masks. |
| Policy update | Finished groups pass through a shared-directory bridge. | Proxy gates requests, drains engine calls, then resumes episodes under the updated policy. |
| Recovery | Completed trajectory exchange. | In-memory episode registry; missing state after restart causes an episode restart, not durable continuation. |

Sources: [bridge encoding](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/training/miles/rollout.py#L46), [self-play collection](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/selfplay/loop.py#L184), [carry collection and configuration](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/training/carry/rollout.py#L254), and the authors' [partial-rollout account](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/docs/partial-rollout.md).

Why retain token probabilities? Training needs to know how the policy that produced an output differs from the policy being updated. Reconstructing a readable conversation is not sufficient to reconstruct the original sampled tokens and their probabilities. A **loss mask** identifies which tokens contribute to learning; tool outputs should not be treated as model-authored answers.

The carry design is a useful systems study: it defines group-level failure, capacity, staleness, and quiescence rules. Its configuration rejects recomputed sampling probabilities. But our checks used fakes, and the authors also mark the port as needing live validation. Their historical-run account does not establish that this release reproduces the paper's shared-model self-play end to end.

## 5. What the release does not establish

The authors' [experiment map](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/docs/experiments.md) records material gaps:

- Original assignment suites, generated environments, trajectories, and checkpoints behind reported numbers are not released. Rendering figures from supplied aggregates or transcribed tables is not reproduction.
- The paper's static Tmax baseline is regenerated using the same proposer. The release uses existing TMax-15K tasks instead. That changes the comparison.
- The paper's Table 2 validity metric uses build, reference, and empty-agent checks and excludes specified infrastructure/provider failures. The preview's validation metric includes contamination and rubric review and also runs calibration for valid tasks. Those reported rates need separate definitions.
- The cross-domain launcher implements terminal generation, not all seven domains. The appendix's reset checks and stricter empty-agent rule are not implemented there.
- HiL-Bench task generation and its RL episode runner are incomplete. Do not infer a general multi-domain task framework from the paper's scope alone.

The [release-status page](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/docs/release-status.md) lists sandbox, Harbor review, and Miles integrations as requiring live runs. Dependencies were resolved locally for our offline review; that does not pin the environment used for the paper.

One security question remains open: the [carry verifier](https://github.com/MSR-Orchard/AutoEnvScaling/blob/2b38259ac0ab5983c7de21df0f50696ab43e8869/autoenvscaling/training/carry/driver.py#L762) clears its reward directory before grading. Whether the Harbor path provides equivalent protection against a solver-planted reward file has not been tested. This is a test candidate, not a confirmed vulnerability.

Use the preview as a concrete design reference and a source of testable contracts. The [next-test sequence](autoenvscaling.md#7-what-to-test-next) prioritizes task correctness and data integrity before a training reproduction.
