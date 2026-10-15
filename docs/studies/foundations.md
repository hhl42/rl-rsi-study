# Foundation reading worksheet

Build understanding around [H1's small Harbor task set](../01-study-plan.md#h1-inspect-and-run-a-small-task-set) and [H2's training example](../01-study-plan.md#h2-observe-one-small-weight-update). The plan owns execution steps and resource approvals. This worksheet owns the questions to answer while reading and inspecting those artifacts. Until H1 runs, use the survey's illustrative service-repair task.

Use the [glossary](../glossary.md) as needed. The [source register](../../references/README.md) records review depth; the assigned papers are not all fully reviewed.

## 1 Describe the interaction

Start with [Spinning Up's key concepts](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html), then check Sutton and Barto chapters 1 and 3 and [ReAct](../../references/README.md#f07-acting-through-tools).

Annotate an H1 trajectory: initial state, observation, generated action, tool response, stopping reason, and reward. Explain how a missing log differs from a bad decision. Mark which state resets between attempts and which evidence the solver can see. Keep the annotation with the exercise record.

## 2 Separate the training methods

Read the RLHF book's [training overview](https://rlhfbook.com/c/03-training-overview) and [instruction tuning](https://rlhfbook.com/c/04-instruction-tuning). Then compare the pipeline in [InstructGPT](../../references/README.md#f03-instructgpt), the [DPO method](../../references/README.md#f04-dpo), and the [DeepSeek-R1 overview](../../references/README.md#f06-reasoning-with-rl).

For one H1 task, identify a successful demonstration, a preference pair, and a runnable environment with a reward function. Which buyer would consume each? Which component changes: weights, memory, or harness? Separate R1-Zero, R1, and distillation when explaining that paper.

## 3 Connect rewards to updates

Read the RLHF book's [reinforcement learning chapter](https://rlhfbook.com/c/06-policy-gradients) and the survey's [worked step](../02-survey.md#a-worked-training-step). Then check [PPO sections 1–3](../../references/README.md#f02-ppo) and [DeepSeekMath section 4](../../references/README.md#f05-grpo).

Calculate advantages for `[0, 0, 0, 1]` and `[0, 0, 0, 0]`. Mark generated tokens and tool observations in the trace. Explain why a final reward cannot identify the exact faulty command. If H2 runs, compare its actual normalization and token mask with the teaching example; record any differences.

## 4 Challenge the verifier

Read task construction in [SWE-bench](../../references/README.md#f09-repository-evaluation) and [SWE-smith](../../references/README.md#f10-task-synthesis), [Rubrics as Rewards](../../references/README.md#f11-rubric-rewards), [reward overoptimization](../../references/README.md#f13-reward-overoptimization), and [HumanEval section 2.1](../../references/README.md#f14-repeated-sampling-and-evaluation).

Use H1's alternate valid repair and deliberate wrong solution to challenge the grader. Explain a false acceptance and a false rejection. State whether a reported score is pass@k or an average across attempts. Choose an unseen failure family for evaluation. Feed observed defects into E1's checklist.

## 5 Locate the improvement

Read [Reflexion](../../references/README.md#f08-learning-through-memory) and [POET](../../references/README.md#f12-generated-curricula), then compare the newer study notes.

Draw separate boxes for weights, memory, harness, and task pool. Mark which changes in Reflexion, AES, and Recursive Self-Rewrite. Propose a comparison that changes only one component. Explain how its result could affect the first buyer's acceptance test.

The foundation step is complete when the team can explain these artifacts and their limits in plain English. Let unresolved questions select the next reading.
