# Foundations: guided learning path

Start here to learn the AI concepts needed for this project. **The foundational papers in the source register are a reference library, not an assigned reading list.** Use online explanations and selected videos first. Open a paper when you have a specific claim or implementation question to check.

This guide owns learning steps **L1–L6** and the parallel **M1** market exercise, including resources and stopping points. The [plan](../01-study-plan.md) owns implementation exercises H1/H2 and commercial decision stages D1–D5. Consult the [survey](../02-survey.md) and [glossary](../glossary.md) when needed.

## How to use this guide

Choose each step's main resource or its alternative; they are not cumulative assignments. Short supporting passages in L3 address separate evaluation skills. Skip a step if you can already produce its output. Use one familiar example throughout: repair a service configuration without losing acknowledged writes.

Keep each output small and explain it to another teammate. Save useful conclusions and unresolved questions in the owning study note. Watching an entire course is not the completion criterion. Begin M1 whenever useful; it need not wait for the technical steps.

Resource pages and course listings were checked on 2026-10-19–20. Selected text and code examples were reviewed. Videos were not watched end to end, and no training notebook was run. Direct retrieval of Lambert's lecture videos failed; the official course page remains a fallback. The [source register](../../references/README.md#learning-resources-added-in-review-2) records review depth.

## L1 See the whole system

**Question:** What is a language model, what changes during learning, and why can answers vary?

**Start with:** Karpathy's [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g). Use this 2023 introduction for the concepts; it predates current reasoning-model practice.

**Short alternative:** 3Blue1Brown's [Large Language Models explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs). Use Karpathy's longer [Deep Dive](https://www.youtube.com/watch?v=7xTGNNLPyMI) only if the basic model and generation process remain unclear.

Distinguish four things: weights are learned numerical parameters; context contains the current messages and tool results; the harness controls execution and context; persistent memory stores information for later retrieval. Training changes weights. A saved incident runbook can improve an agent through context without training it.

A model produces probabilities for possible next tokens. Sampling can produce different actions from the same weights and context. Tool timing and environment changes can add variation too. Repeated success therefore needs measurement even when the software version is fixed; a deterministic-looking example does not establish universal repeatability.

**Exercise and stopping point:** Draw execution and weight-training loops. Then draw five actions from one fixed toy distribution: inspect logs with probability 0.6, restart with 0.3, or edit configuration with 0.1. Explain why different draws are not learning. If already authorized model access is available, compare five independent runs of one prompt and record the model and sampling settings. Five runs illustrate variation; they do not establish a reliable success rate.

**Depth limit:** Explain inputs, outputs, randomness, and what changes. Transformer implementation, backpropagation, and pretraining infrastructure can wait.

## L2 Follow one agent through one task

**Question:** What does our framework supply during execution?

**Start with:** Hugging Face's [Agents Course, Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction), focusing on messages, tools, and the [action–observation loop](https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure).

**Video alternative:** Lambert's [lecture 11: Tool Use, Function Calling and The Road to Agents](https://www.youtube.com/watch?v=GMry2DzC304), also linked from his [course](https://rlhfbook.com/course).

**Exercise:** Inspect the [minimal agent tutorial](https://minimal-agent.com/). Point to the model call, action parsing, command execution, observation appended to history, and stopping condition. Identify where a trajectory could be saved and where execution errors appear. This is a code-reading exercise: its simple shell runner is not our isolation design.

Write a service-repair trace: inspect logs → observe error → edit configuration → restart → check writes → submit. Label generated actions separately from tool observations. The [scripted Harness² demo](../records/2026-10-19-harness2-demo/README.md) supplies a small runnable data-flow example if useful.

**Stopping point:** Explain model, agent, task, environment, trajectory, and verifier by pointing to code or the trace. Specify what resets between attempts.

**Depth limit:** Follow one execution path. Installing several agent frameworks or publishing an agent is unnecessary.

## L3 Judge outcomes and build the first task

**Question:** When does a passing score reflect the intended outcome?

**Start with:** Anthropic's [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), focusing on tasks, trials, graders, and repeated-attempt metrics.

**Video alternative:** Lambert's [lecture 12: The Evolution of Frontier Model Evaluation](https://www.youtube.com/watch?v=dFafQmClYq4), linked from his [course](https://rlhfbook.com/course). His [evaluation chapter](https://rlhfbook.com/c/16-evaluation) remains an optional text reference.

Two supporting passages matter here. Read one concrete case from METR's [reward-hacking report](https://metr.org/blog/2025-06-05-recent-reward-hacking/), such as a kernel that accesses the grader's reference result and bypasses timing. Then read the error-bar and paired-comparison recommendations in Anthropic's [statistical evaluation guide](https://www.anthropic.com/research/statistical-approach-to-model-evals). These are selected passages, not three complete reading assignments.

**Build exercise:** Start [H1](../01-study-plan.md#h1-inspect-and-run-a-small-task-set) now. Use Harbor's [task format](https://docs.harborframework.com/tasks/overview) and [create-a-task tutorial](https://docs.harborframework.com/tutorials/create-a-task) to package one service-repair task. Include a reference repair, a different valid repair, an empty submission, and a shortcut that restores health checks while losing writes. Repeat deterministic checks from fresh resets. Another teammate should be able to run them. No model is needed for this part.

**Measurement exercise:** For an illustrative 60 successes out of 100 independent tasks, estimate the success rate and an approximate 95% interval using the statistical guide. State the sampling assumptions. Explain why 100 related variants, or repeated attempts on one task, do not establish the same generalization claim. For a before/after comparison, explain why pairing results by task helps. Separate variation across attempts from uncertainty about which tasks were sampled.

**Stopping point:** The task accepts valid alternatives and rejects the shortcut. You can distinguish pass@k, success of the output selected from k attempts, and pass^k reliability; see the [glossary](../glossary.md#measurements-and-names-in-the-studies). Explain why zero passes should prompt investigation of the task and grader but does not prove either is broken.

**Depth limit:** Go deep on grading, leakage, splits, uncertainty, and costs. This first package teaches the contract; [E1](../01-study-plan.md#e1-verify-the-verifier) later evaluates a task family more systematically.

## L4 Understand how training consumes our tasks

**Question:** How can an outcome score change future model behavior?

**Start with:** Lambert's [reinforcement learning chapter](https://rlhfbook.com/c/06-policy-gradients). Focus on RL's role, policy-gradient intuition, and grouping attempts in GRPO. Consult the [training overview](https://rlhfbook.com/c/03-training-overview) here if the relationships among training stages are unclear.

**Video alternative:** [Lecture 3: RL Motivation & Math](https://www.youtube.com/watch?v=K_Sj_-1BUMM). Use [Spinning Up](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) only for missing vocabulary.

**Exercise:** Follow the [survey's worked update](../02-survey.md#a-worked-training-step): sample → score → compare rewards → update weights → evaluate on reserved tasks. Mean-centering rewards `0, 0, 0, 1` gives advantages `−0.25, −0.25, −0.25, +0.75`. Explain the update direction and why identical rewards give no preference in this calculation. This is not the complete GRPO loss.

**Stopping point:** Explain the assets consumed by SFT, preference optimization, and online RL. Identify generated tokens versus tool observations, and explain why a wrong reward can reinforce the wrong behavior.

**Depth limit:** Understand probabilities, log probabilities, gradients, and the data flow. A real update is optional [H2](../01-study-plan.md#h2-observe-one-small-weight-update), which can use suitable existing or free compute. Deriving PPO or operating a distributed trainer is not required.

## L5 Compare concrete improvement loops

**Question:** What should change to solve our candidate customer's problem?

**Start with:** The mechanism and comparison sections of our [AES](autoenvscaling.md) and [Harness²](harness2.md) studies. Consult the [Third Moment note](third-moment-research.md) separately for the commercial offering.

**Exercise and stopping point:** Write short comparisons of manual task construction, AES, and Harness². Include unchanged-harness retries with a selector and a harness tuned once offline as alternatives. For each, identify what changes, acceptance evidence, transfer, and costs before and during deployment. Describe one possible customer deliverable and its acceptance test.

**Depth limit:** Understand control flow and one relevant code path. Open paper sections to answer concrete questions; the other study notes are optional comparisons.

## L6 Run agents on the small task set

**Question:** Do our tasks behave reliably under actual agents?

**Start with:** H1's package from L3. Use the [Harbor tutorial](https://docs.harborframework.com/tutorials/create-a-task) for execution and [Terminal-Bench task examples](https://github.com/harbor-framework/terminal-bench-2) for packaging details. Public examples are teaching material, not an independent final evaluation set.

**Exercise:** Expand to three to five tasks and complete [H1](../01-study-plan.md#h1-inspect-and-run-a-small-task-set) with two existing agents and repeated attempts after access and resource limits are agreed. Record task, model, and harness versions; annotate a trace; separate agent, task, grader, and infrastructure failures.

**Stopping point:** A teammate can repeat the run. We can explain observed variation, account for failed starts and retries, and name the uncertainty that E1 or a subsequent comparison will test.

**Depth limit:** Reuse execution infrastructure. This is integration practice, not proof of training benefit or a commitment to a general platform.

## M1 Investigate buyers alongside learning

**Start with:** Epoch AI's [FAQ on RL environments](https://epoch.ai/gradient-updates/state-of-rl-envs), then our [market map](../03-opportunities.md#market-map) and [Third Moment study](third-moment-research.md). This supplies a training-buyer view and an application-owner comparison.

**Output:** Prepare the [buyer brief](../03-opportunities.md#buyer-brief-for-m1): buyer classes, named alternatives, reported prices and their limits, permitted examples, reachable roles, and an acceptance test. Put unknowns in the brief rather than guessing. Customer contact requires separate direction.

**Stopping point:** D2 has evidence to make a provisional buyer choice or can identify exactly what is missing. Public vendor claims alone cannot establish demand.

## When to open the foundational papers

| A concrete question has arisen | Relevant reference |
| --- | --- |
| How should repository tasks be constructed and evaluated? | [SWE-bench and SWE-smith, F09–F10](../../references/README.md#f09-repository-evaluation) |
| Can we trust a rubric reward under optimization? | [Rubrics as Rewards, F11](../../references/README.md#f11-rubric-rewards), and [reward overoptimization, F13](../../references/README.md#f13-reward-overoptimization) |
| Which update or training interface are we implementing? | [PPO, F02](../../references/README.md#f02-ppo), [GRPO, F05](../../references/README.md#f05-grpo); Sutton and Barto for missing theory |
| Is preference data the right deliverable? | [InstructGPT and DPO, F03–F04](../../references/README.md#f03-instructgpt) |
| Does an adaptive curriculum justify its cost? | AES methods and ablations, its Tmax baseline, then [POET, F12](../../references/README.md#f12-generated-curricula) if useful |
| Does improvement persist through memory or weights? | [Reflexion, F08](../../references/README.md#f08-learning-through-memory), or the RLTL;DR and Recursive Self-Rewrite notes |

Read the relevant section, identify the claim and comparison, and record the answer. A full paper review is warranted when a consequential design choice depends on it.
