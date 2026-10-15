# Foundation reading worksheet

Use one concrete example throughout: an agent repairs a service after a configuration change. It can inspect logs, edit files, and run checks. This is an illustrative task, not an implemented environment.

The [survey](../02-survey.md) explains the concepts. This worksheet turns the added foundation readings into questions and small written exercises. Links below lead to the [source register](../../references/README.md), which records versions, primary sources, and review depth. Most readings have only an orientation review so far; the worksheet is a study aid, not a completed literature audit.

## 1 Describe the interaction

Read [Sutton and Barto, chapters 1 and 3](../../references/README.md#f01-rl-foundations), and the overview of [ReAct](../../references/README.md#f07-acting-through-tools).

Draw one attempt from the initial service failure to its final check. Identify the full environment state, what the agent can observe, its allowed actions, and the stopping condition. Explain how a missing log differs from a bad decision. Produce one example trajectory with a failed action and a useful response from the environment.

## 2 Separate the training methods

Read the pipeline overview in [InstructGPT](../../references/README.md#f03-instructgpt), the introduction and method in [DPO](../../references/README.md#f04-dpo), and the overview of [DeepSeek-R1](../../references/README.md#f06-reasoning-with-rl).

For the service task, write three possible training assets: a successful demonstration, a pair of answers with a preference label, and an agent attempt with a reward. Identify what creates each label and which method consumes it. Explain the difference between training a model and giving an unchanged model better context. Separate R1-Zero, R1, and distillation when discussing the paper.

## 3 Connect rewards to updates

Read [PPO, sections 1–3](../../references/README.md#f02-ppo), and [DeepSeekMath, section 4](../../references/README.md#f05-grpo). Sutton and Barto chapter 13 is a deeper follow-up.

Work through the survey's groups of rewards, `[0, 0, 0, 1]` and `[0, 0, 0, 0]`. Explain what the group comparison can distinguish. Then list three reasons for all-zero rewards: a task beyond the solver's ability, a broken environment, and an incorrect verifier. Describe a check that separates them. The output should explain why task difficulty alone cannot tell us whether training will help.

## 4 Design trustworthy evaluation

Read the task construction sections of [SWE-bench](../../references/README.md#f09-repository-evaluation) and [SWE-smith](../../references/README.md#f10-task-synthesis), [Rubrics as Rewards, sections 2–3](../../references/README.md#f11-rubric-rewards), [reward overoptimization](../../references/README.md#f13-reward-overoptimization), and [HumanEval, section 2.1](../../references/README.md#f14-repeated-sampling-and-evaluation).

Specify a service-repair check that accepts two different valid fixes. Add a wrong fix that passes a superficial check. Explain which criteria can be executed and which need judgment. Reserve an unseen failure family for evaluation. State whether the score means success on one attempt, success within several attempts, or average success across attempts, and account for the extra cost.

## 5 Locate the improvement

Read the overviews of [Reflexion](../../references/README.md#f08-learning-through-memory) and [POET](../../references/README.md#f12-generated-curricula), then compare the newer study notes.

Draw separate boxes for model weights, memory, harness, and task pool. Mark what changes in Reflexion, AutoEnvScaling, and Recursive Self-Rewrite. Propose a comparison that changes just one component. Explain why improvement while a helpful note remains in context does not establish improvement after the note is removed.

The foundation step is complete when the team can explain these artifacts and their limitations in plain English. Open questions should guide the next reading, rather than expanding the prerequisite list without a purpose.
