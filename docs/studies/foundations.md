# Foundations: guided learning path

Start here to learn the AI concepts needed for this project. **The foundational papers in the source register are a reference library, not an assigned reading list.** Use online explanations and selected videos first. Open a paper when you have a specific claim or implementation question to check.

The [plan](../01-study-plan.md) explains why these steps matter and how they lead to experiments. This guide owns learning resources, exercises, and stopping points. The [survey](../02-survey.md) is a reference to consult along the way, not another prerequisite.

## How to use this guide

Follow the six steps below. Choose each step's main resource **or** its alternative; they are not cumulative assignments. Skip a step if you can already produce its output. Use one familiar example throughout: an agent must repair a service configuration without losing acknowledged writes.

Keep each output small: a diagram, annotated trace, calculation, or comparison. Explain it to another teammate, then move on. Record useful conclusions and unresolved questions in the owning study note. Watching a whole course or recognizing its vocabulary is not the completion criterion.

Resource pages and course listings were checked on 2026-10-19. Selected text was reviewed; the videos have not been watched end to end. Topic scopes below are our recommendations, not verified timestamps. The [source register](../../references/README.md#f15-rlhf-teaching-book) records review depth.

## Step 1 See the whole system

**Question:** What is a language model, and where can improvement happen?

**Start with:** Andrej Karpathy's video [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g). Focus on what a model contains, generation, training, and the software around it. Use it for the concepts, not as a current model-capability survey.

**Text alternative:** Nathan Lambert's [training overview](https://rlhfbook.com/c/03-training-overview). Use relevant parts of Lecture 0 in the [accompanying course](https://rlhfbook.com/course) only if unfamiliar ML concepts block understanding.

For our purpose, distinguish:

- **Weights:** learned numerical parameters, changed by training.
- **Context:** information supplied for the current generation, including messages and tool results.
- **Harness:** software that assembles context, executes tools, and controls the agent loop.
- **Persistent memory:** stored information that the harness may retrieve on later tasks.

**Exercise and stopping point:** Draw two loops. One executes a task with fixed weights; the other uses collected data to update weights and evaluate the updated model. Place tasks, rewards, traces, and memory on the diagram. Explain why saving an incident runbook can improve an agent without training it.

**Depth limit:** Understand inputs, outputs, and what changes. Do not implement a transformer, study pretraining infrastructure, or derive backpropagation yet.

## Step 2 Follow one agent through one task

**Question:** What does our framework supply during execution?

**Start with:** Hugging Face's [Agents Course, Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction). Read the concepts covering agents, messages, tools, and the [action–observation loop](https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure). The framework installation and agent-publication exercises are optional.

**Video alternative:** Lambert's [course](https://rlhfbook.com/course), Lecture 11, “Tool Use, Function Calling and The Road to Agents.”

**Exercise:** Write a short service-repair trace: instruction → inspect logs → observe error → change configuration → restart → inspect result → submit. Label model-generated actions separately from tool observations. Specify initial state, permitted actions, reset, completion, and the independently checked outcome.

The saved [Harness² demo record](../records/2026-10-19-harness2-demo/README.md) offers a smaller executable example. Its editor is scripted, so use it to inspect data flow, not model reasoning.

**Stopping point:** Explain model, agent, task, environment, trajectory, and verifier using this trace. Identify where an infrastructure failure would be recorded.

**Depth limit:** Trace one execution path. Do not learn several agent SDKs or design a general orchestration platform.

## Step 3 Decide whether the result is actually better

**Question:** What evidence would justify accepting a task or an improvement?

**Start with:** Lambert's [evaluation chapter](https://rlhfbook.com/c/16-evaluation), especially “The Complexity of Agentic Evaluations,” “Why Many External Evaluation Comparisons Are Unreliable,” and the discussion of contamination.

**Video alternative:** The [course](https://rlhfbook.com/course), Lecture 12, “The Evolution of Frontier Model Evaluation.”

**Exercise:** Write a valid repair, a different valid repair, and a shortcut that passes a health check while losing writes. Define checks that accept both repairs and reject the shortcut. Explain how an agent could see development feedback while final evaluation remains independent.

**Stopping point:** Produce a small evaluation table covering correctness, repeatability, generalization to reserved cases, cost, and latency. Distinguish one successful attempt from a reliable success rate, and a better task score from customer value. Consult the [survey](../02-survey.md#7-reading-results-without-misleading-ourselves) for pass@1 and pass@k.

**Depth limit:** Go deep here. Task validity, grader errors, leakage, splits, and fair comparisons directly affect our product. The larger [E1](../01-study-plan.md#e1-verify-the-verifier) study comes later; designing a few negative controls is enough for this learning step.

## Step 4 Understand how training consumes our tasks

**Question:** How can an outcome score change future model behavior?

**Start with:** Lambert's [reinforcement learning chapter](https://rlhfbook.com/c/06-policy-gradients). Focus on the role of RL, the policy-gradient intuition, and grouping attempts in GRPO. Follow the data path: sample attempts → score → compare rewards → update weights → evaluate on reserved tasks.

**Video alternative:** [Lecture 3, “RL Motivation & Math”](https://www.youtube.com/watch?v=K_Sj_-1BUMM). Use the [Spinning Up introduction](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) only to fill gaps in policy, observation, action, return, or trajectory.

**Exercise:** Work through the [survey's numerical example](../02-survey.md#a-worked-training-step). With rewards `0, 0, 0, 1`, subtract the mean to obtain `−0.25, −0.25, −0.25, +0.75`. Explain which generated behavior receives positive pressure and why identical rewards give no preference under this calculation. This illustrates mean-centered advantages; it is not the complete GRPO loss.

**Stopping point:** Explain which assets three methods consume: SFT uses example outputs or trajectories to imitate; preference optimization uses comparisons; online RL samples new attempts and scores their outcomes. Explain why a wrong reward can teach the wrong behavior and why training-set gains do not establish transfer.

**Depth limit:** Understand probabilities, log probabilities, gradient direction, and the task-to-update data flow. Deriving PPO, implementing an optimizer, and running GPUs are not prerequisites. [H2](../01-study-plan.md#h2-observe-one-small-weight-update) becomes useful if we need to inspect real training behavior or integrate with a trainer.

## Step 5 Compare concrete improvement loops

**Question:** What should change to solve our candidate customer's problem?

**Start with:** Our [AutoEnvScaling study](autoenvscaling.md) and [Harness² study](harness2.md). Read their mechanism explanations first. Consult the [Third Moment Research note](third-moment-research.md) separately for the commercial offering.

**Exercise and stopping point:** Make a one-page comparison of manual task construction, AES, and Harness². Identify what changes, what evidence accepts the change, what stays fixed, how transfer is measured, and what costs grow. Then describe one possible customer deliverable and its acceptance test.

AES motivates adaptive task production and training. Harness² motivates editing execution software and retaining lessons with fixed model weights. A business offering is a separate kind of evidence; it does not establish which algorithm caused an improvement.

**Depth limit:** Understand the control flow and one relevant code path. Open paper methods, results, or ablations only to resolve a question raised by the comparison. The other study notes are alternatives to consult, not another required reading sequence.

## Step 6 Build the smallest useful task experiment

**Question:** Can another person execute and judge our task reliably?

**Start with:** [Harbor's task documentation](https://docs.harborframework.com/), alongside [survey section 3](../02-survey.md#3-what-a-task-framework-must-represent). Inspect an existing task before designing a format.

**Exercise:** Begin [H1](../01-study-plan.md#h1-inspect-and-run-a-small-task-set) with one hand-written task and reference, wrong, and alternative valid solutions. Expand to three to five tasks after that contract is clear. Model runs follow when access and resource limits are agreed; initial authoring and deterministic checks need no model API.

**Stopping point:** Another teammate can reset, solve, and grade the task from its package. We can explain which uncertainty the next experiment will test. Choose E1 before trying to optimize against an untrusted grader.

**Depth limit:** Implement the task boundary and reuse execution infrastructure. Training integration is conditional on the opportunity; a general platform is not this step's output.

## When to open the foundational papers

| A concrete question has arisen | Relevant reference |
| --- | --- |
| How should repository tasks be constructed and evaluated? | [SWE-bench and SWE-smith, F09–F10](../../references/README.md#f09-repository-evaluation) |
| Can we trust a rubric reward under optimization? | [Rubrics as Rewards, F11](../../references/README.md#f11-rubric-rewards), and [reward overoptimization, F13](../../references/README.md#f13-reward-overoptimization) |
| Which exact update or training interface are we implementing? | [PPO, F02](../../references/README.md#f02-ppo), [GRPO, F05](../../references/README.md#f05-grpo); Sutton and Barto for missing theory |
| Is preference data the right deliverable? | [InstructGPT and DPO, F03–F04](../../references/README.md#f03-instructgpt) |
| Does an adaptive curriculum justify its cost? | AES methods and ablations, its Tmax baseline, then [POET, F12](../../references/README.md#f12-generated-curricula) if the older formulation helps |
| Does improvement persist through memory or weights? | [Reflexion, F08](../../references/README.md#f08-learning-through-memory), or the RLTL;DR and Recursive Self-Rewrite notes |

Read the relevant section, identify the claim and comparison, and record the answer. A full paper review is warranted when a consequential design choice depends on it.
