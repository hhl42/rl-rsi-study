# Glossary

Use this as a quick reference, not a prerequisite reading list. The [survey](02-survey.md) explains the ideas with a service-repair example. Source-specific details belong in the linked studies.

## Tasks and learning

| Term | Meaning here |
| --- | --- |
| Agent; harness | An agent uses a model to act through tools. Its harness manages tools, context, execution, retries, and stopping. |
| Task; environment | A task specifies work and success conditions. An environment supplies the starting state and interfaces for doing that work. |
| Policy; weights | The policy chooses actions from the available history. Model weights are the learned numerical parameters that shape those choices. |
| Token | A piece of text or structured output processed by the model; it need not be a whole word. |
| Episode; trajectory; rollout | An episode is one attempt. A trajectory is its recorded actions and observations. Rollout often means either generating or recording that attempt. |
| Reward; verifier | Reward is a numerical training score. A verifier checks the outcome; its result may determine that score. |
| Advantage | An estimate of how much better or worse an action or attempt is than a reference expectation. Group methods use other attempts on the same task as that reference. |
| Training loss; optimizer | The loss is the objective minimized during training. The optimizer adjusts weights using its gradients. A token mask selects which parts of a trace contribute. |
| SFT | Supervised fine-tuning: train weights to imitate supplied examples. |
| DPO | Direct Preference Optimization: train weights from preferred and less-preferred responses. |
| RL; RLHF; RLVR | Reinforcement learning uses rewards to improve a policy. RLHF uses human feedback, often through a learned reward model. RLVR uses checkable rewards such as test outcomes. |
| PPO; GRPO | Policy-gradient methods that limit policy changes during updates. GRPO estimates advantages by comparing attempts within a group. See [the survey](02-survey.md#2-what-can-improve-and-what-training-requires). |
| DPPO | Divergence Proximal Policy Optimization, used by AES for terminal-agent training. Do not assume its update and normalization choices are identical to GRPO; see the [AES study](studies/autoenvscaling.md). |
| RSI | Recursive self-improvement: earlier improvements help the system produce later improvements. Specify whether weights, memory, harness, or task production changes. |
| On-policy; off-policy | Experience collected by the policy being optimized, versus experience from a different or older policy. Real implementations need explicit rules for sample age. |
| Curriculum | Which tasks are selected and in what order during learning. |

## Measurements and names in the studies

| Term | Meaning here |
| --- | --- |
| pass@1 | Estimated probability of success for one sampled attempt under a stated configuration. |
| pass@k | Probability that at least one of k attempts succeeds; it allows multiple chances. |
| avg@k | Average score over k attempts or evaluation runs, following the source's definition. It is not success within k chances. AES reports avg@5. |
| Partial reward; full pass | Partial reward records incomplete progress. A full pass meets the task's completion rule. These support different difficulty measurements. |
| Terminal-Bench; TB2.1; TB4.0 | Benchmarks for tool-using terminal agents; TB abbreviates Terminal-Bench and the suffix identifies a version. Different versions need not contain the same tasks. AES's TB2.1 evaluation has 89 tasks. |
| Tmax | A static terminal-task generation recipe and the main AES baseline. See the [comparison](studies/autoenvscaling.md#4-what-the-results-establish). |
| Harbor | A framework for packaging tasks and running agents in environments with verifiers. |
| verl; SkyRL; Miles | Training software, rather than task datasets. They orchestrate model training and rollout collection; AES uses Miles. |
| Bridge; carry | Two AES integration paths. The bridge waits for complete attempts before passing recorded groups to training. Carry can retain unfinished attempts across weight updates. Their behavior differs; see the [code study](studies/autoenvscaling-code.md). |
| B200 | An NVIDIA GPU model used in AES's reported training setup; the GPU count alone does not specify total compute cost. |
| Qwen3.5-35B-A3B | A model-family/version name plus parameter counts: about 35 billion total parameters and 3 billion active per token. It uses a mixture of experts, selecting part of the model for each token. Active count alone does not specify memory or runtime cost. |

A percentage-point change subtracts two percentages: 40% to 50% is +10 points. The relative improvement is 25%. Keep the baseline, denominator, attempt budget, and cost beside either measure.
