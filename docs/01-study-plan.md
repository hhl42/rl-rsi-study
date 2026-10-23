# Study guide

Reading and viewing for engineering leaders with deep systems experience who already build AI projects. The sequence moves from the overall model to task quality, training, concrete systems, and commercial offerings. Skip familiar material; use implementation references when they bear on current work. The commercial phase can be read alongside the technical phases.

Each step gives a main reading or video, selected sections, and optional depth. Alternatives are substitutes, not additional assignments. [Foundations](studies/foundations.md) provides concept reminders and a question-based paper index. [Research experiments](experiments.md) are separate proposals; [progress](progress.md) records current priorities.

Resource pages and course listings were checked on 2026-10-19–20. Selected text and code were reviewed; videos were not watched end to end and training notebooks were not run. See the [source register](../references/README.md) for review limits.

<a id="reading-sequence"></a>

## Phase 1 — The model and the agent

### 1. Language models and what changes during improvement

- **Watch:** Karpathy's [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g). Focus on learned weights, context, token generation, and training stages. This 2023 overview explains the concepts; it predates current reasoning-model practice.
- **Short alternative:** 3Blue1Brown's [Large Language Models explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs).
- **Optional depth:** Karpathy's [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI), for a fuller account of generation and training. Transformer implementation and pretraining infrastructure can wait until a design question needs them.

### 2. Agent execution and the harness

- **Read:** Hugging Face's [Agents Course, Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction), especially the [action–observation loop](https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure). Focus on model calls, tools, context, and stopping.
- **Video alternative:** Lambert's [lecture 11: Tool Use, Function Calling and The Road to Agents](https://www.youtube.com/watch?v=GMry2DzC304). The [course page](https://rlhfbook.com/course) is the fallback if the direct link fails.
- **Code reference:** The [minimal agent tutorial](https://minimal-agent.com/), from model call through command execution and history update. Useful for locating the task framework's interfaces; its simple shell runner is not an isolation design.

## Phase 2 — Tasks and trustworthy evaluation

### 3. Outcomes, graders, and uncertainty

- **Read closely:** Anthropic's [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). Focus on tasks, trials, graders, repeated-attempt metrics, and interpreting failures.
- **Video alternative:** Lambert's [lecture 12: The Evolution of Frontier Model Evaluation](https://www.youtube.com/watch?v=dFafQmClYq4), also on the [course page](https://rlhfbook.com/course). His [evaluation chapter](https://rlhfbook.com/c/16-evaluation) is a text reference.
- **Read selected cases:** METR's [reward-hacking report](https://metr.org/blog/2025-06-05-recent-reward-hacking/), especially scoring and timing shortcuts. These show how a passing score can fail to represent the intended behavior.
- **Read selected sections:** Anthropic's [statistical evaluation guide](https://www.anthropic.com/research/statistical-approach-to-model-evals), on error bars, sampling assumptions, and paired comparisons. This is the useful depth for judging claims from repeated, related, or small task sets.

### 4. Task contracts and task production

- **Read:** The [HUD task-design study](studies/hud-task-design.md) and [Gottlieb task-factory study](studies/eli-gottlieb-reference.md), then their linked originals for design details. Focus on intended capability, evidence available to the solver, valid alternatives, expert review, and isolation.
- **Read closely:** Harbor's [task format](https://docs.harborframework.com/tasks/overview). Use its [create-a-task tutorial](https://docs.harborframework.com/tutorials/create-a-task) and [Terminal-Bench examples](https://github.com/harbor-framework/terminal-bench-2) as implementation references for packaging, reset, execution, and verification.
- **Local synthesis:** The survey's [task-framework model](02-survey.md#3-what-a-task-framework-must-represent). Task and evaluation contracts deserve the deepest study because they determine whether our deliverable is usable.

## Phase 3 — How tasks become training inputs

### 5. Training stages and data requirements

- **Read:** Lambert's [training overview](https://rlhfbook.com/c/03-training-overview). Focus on the roles of supervised fine-tuning, preference optimization, and online RL, and what each consumes.
- **Supporting reference:** The [instruction-tuning chapter](https://rlhfbook.com/c/04-instruction-tuning), for demonstrations and supervised training.
- **Local explanation:** The survey's [worked training step](02-survey.md#a-worked-training-step), for the path from attempts and rewards to an update. It is a simplified example, not the complete GRPO loss.

### 6. RL updates and the task-to-trainer boundary

- **Read:** Lambert's [reinforcement learning chapter](https://rlhfbook.com/c/06-policy-gradients), focusing on policy-gradient intuition, relative rewards, and grouping attempts in GRPO. The relevant depth is how scoring changes training and which generated tokens contribute to the loss.
- **Video alternative:** [Lecture 3: RL Motivation & Math](https://www.youtube.com/watch?v=K_Sj_-1BUMM). Use [Spinning Up's key concepts](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) for missing RL vocabulary.
- **When integrating training:** Consult the [Unsloth RL guide and notebooks](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide) for concrete small-run code, and the [framework documentation register](../references/README.md#framework-documentation) for verl and SkyRL. Model compatibility and runtime requirements need checking for the chosen version. Detailed optimizer derivations and distributed training internals are conditional references.

## Phase 4 — Concrete improvement systems

### 7. AutoEnvScaling: generating useful environments

- **Read:** Our [AutoEnvScaling study](studies/autoenvscaling.md), starting with the mechanism, results and baselines, and framework implications.
- **Read code through:** The [code walkthrough](studies/autoenvscaling-code.md), following assignment, task validation, calibration, admission, and trajectory export. Its pinned links and observed limitations distinguish the design from what the preview enforces.
- **Paper depth:** The [supplied paper](../references/papers/2610.14163v1-AutoEnvScaling.pdf), sections 3–4 and appendices G–H, when resolving method, comparison, or implementation questions. For static task generation, use the [SWE-smith reference](../references/README.md#f10-task-synthesis); the AES note also identifies the Tmax baseline and its review limits.

### 8. Harness²: improving execution with fixed weights

- **Read:** The [Harness² study](studies/harness2.md), covering runtime edits, the persistent library, reported comparisons, costs, and failure handling.
- **Read code through:** The same note's pinned scheduling, selection, and library links. The [scripted demo record](records/2026-10-19-harness2-demo/README.md) illustrates data flow and persistence; it does not measure model improvement.
- **Paper depth:** Follow the paper links in the note for offline harness tuning, best-of-k retries, library ablations, and combined-token accounting. These comparisons matter when deciding whether adaptation justifies its cost.

### 9. Other mechanisms, selected by the design question

- **Feedback and training data:** [RLTL;DR](studies/rl-tldr.md) and [Recursive Self-Rewrite](studies/recursive-self-rewrite.md), for turning feedback or successful executions into training assets.
- **Memory and improvement across tasks:** [ApprenticeBench](studies/apprentice-bench.md), [Raven](studies/raven.md), and the [Reflexion reference](../references/README.md#f08-learning-through-memory).
- **Further theory:** The [question-based paper index](studies/foundations.md#when-to-open-the-foundational-papers). Read the section relevant to the decision; the foundational source list is not a required sequence.

## Phase 5 — Buyers, offerings, and delivery economics

Read this phase alongside the technical study. It connects framework choices to what a customer might buy.

### 10. The environment market and managed improvement

- **Read:** Epoch AI's [The state of RL environments](https://epoch.ai/gradient-updates/state-of-rl-envs), for reported buyer needs, task economics, and internal construction. Its interview evidence is not an audit of transactions.
- **Read closely:** The [Third Moment Research study](studies/third-moment-research.md) and its linked first-party material. Focus on the public offering, the internal research case, and which commercial claims remain unverified.
- **Read across alternatives:** The [market map](03-opportunities.md#market-map), including its source dates and unverified supplier leads. Compare task supply, quality review, failure-to-task services, managed improvement, and execution infrastructure.

### 11. Adjacent product and integration models

- **Read as relevant:** [TypeSafe and Jev](studies/typesafe-jev.md), for structured decisions and product integration; [MiMo RL](studies/mimo-rl.md), for open environments and training integration.
- **Local synthesis:** [Commercial opportunities](03-opportunities.md), especially buyer selection, candidate task domains, and delivery economics. Public offerings establish possible business models; customer access and demand remain separate evidence.

<details>
<summary>Links from earlier reviews</summary>

<a id="foundations-by-doing"></a>
<a id="h1-inspect-and-run-a-small-task-set"></a>
<a id="h2-observe-one-small-weight-update"></a>

The H1/H2 practice assignments were removed on 2026-10-23 at the user's request. This guide now contains reading and viewing only. The [decision record](progress.md#2026-10-23-use-a-reading-guide-for-engineering-leaders) explains the change.

<a id="proposed-experiments"></a>

Research experiment designs moved to [Research experiments](experiments.md), separately from the study sequence:

<a id="e1-verify-the-verifier"></a>

- [E1: Verify the verifier](experiments.md#e1-verify-the-verifier).

<a id="e2-generate-from-solver-failures"></a>

- [E2: Generate from solver failures](experiments.md#e2-generate-from-solver-failures).

<a id="e3-use-feedback-effectively"></a>

- [E3: Use feedback effectively](experiments.md#e3-use-feedback-effectively).

<a id="e4-test-a-commercial-offer"></a>

- [E4: Test a commercial offer](experiments.md#e4-test-a-commercial-offer).

</details>
