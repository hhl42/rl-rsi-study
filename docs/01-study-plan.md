# Study guide

Reading and viewing for engineering leaders with deep systems experience who already build AI projects. The sequence moves from the overall model to task quality, training, concrete systems, and commercial offerings. Skip familiar material; use implementation references when they bear on current work. The commercial phase can be read alongside the technical phases.

Each step gives focused readings and optional depth. Prefer standalone engineering articles, design reports, and implementation documentation. Use a video for orientation and a book section when a specific concept needs more explanation. [Foundations](studies/foundations.md) provides concept reminders and a question-based paper index. [Research experiments](experiments.md) are separate proposals; [progress](progress.md) records current priorities.

The engineering replacements were checked on 2026-10-23; earlier sources retain their recorded review dates. Videos were not watched end to end, and listing implementation documentation does not mean its code was run. The [source register](../references/README.md#engineering-readings) records what was reviewed.

<a id="reading-sequence"></a>

## Phase 1 — The model and the agent

### 1. Language models and what changes during improvement

- **Optional overview:** Karpathy's [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g). Focus on learned weights, context, token generation, and training stages. This standalone 2023 talk explains the concepts; it predates current reasoning-model practice. Skip it if those distinctions are familiar.
- **Short alternative:** 3Blue1Brown's [Large Language Models explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs). Choose one overview rather than watching both.

### 2. Agent execution and the harness

- **Read:** Anthropic's [Building effective agents](https://www.anthropic.com/research/building-effective-agents). Focus on workflows versus agents, when added autonomy is useful, the execution loop, and tool-interface design in appendix 2. This is an architecture discussion; its 2024 publication date limits its value as a current tooling guide.
- **Implementation reference:** mini-SWE-agent's [Agent control flow](https://mini-swe-agent.com/v2/advanced/control_flow/). Read the diagram and accompanying default-agent code for model calls, environment execution, message history, and termination. This exposes the interfaces without a build-your-first-agent tutorial.
- **For work across sessions:** Anthropic's [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents). Focus on environment initialization, persisted progress, recovery, and end-to-end checks. It is one team's implementation account, useful for separating harness responsibilities from model capability.

## Phase 2 — Tasks and trustworthy evaluation

### 3. Outcomes, graders, and uncertainty

- **Read closely:** Anthropic's [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). Focus on tasks, trials, graders, repeated-attempt metrics, and interpreting failures.
- **Read selected cases:** METR's [reward-hacking report](https://metr.org/blog/2025-06-05-recent-reward-hacking/), especially scoring and timing shortcuts. These show how a passing score can fail to represent the intended behavior.
- **Read selected sections:** Anthropic's [statistical evaluation guide](https://www.anthropic.com/research/statistical-approach-to-model-evals), on error bars, sampling assumptions, and paired comparisons. This is the useful depth for judging claims from repeated, related, or small task sets.

### 4. Task contracts and task production

- **Read:** The [HUD task-design study](studies/hud-task-design.md) and [Gottlieb task-factory study](studies/eli-gottlieb-reference.md), then their linked originals for design details. Focus on intended capability, evidence available to the solver, valid alternatives, expert review, and isolation.
- **Read closely:** Harbor's [task format](https://docs.harborframework.com/tasks/overview), with [Terminal-Bench examples](https://github.com/harbor-framework/terminal-bench-2) for concrete packaging and verifier code.
- **Architecture comparison:** Prime Intellect's [verifiers v1 design](https://www.primeintellect.ai/blog/verifiers-v1). Read the separation of taskset, harness, and runtime, then the architecture sections on interception and traces. Useful when deciding which interfaces belong in our framework, including traces through compaction and subagents. The article describes a preview; its implementation has not been audited here.
- **Local synthesis:** The survey's [task-framework model](02-survey.md#3-what-a-task-framework-must-represent). Task and evaluation contracts deserve the deepest study because they determine whether our deliverable is usable.

## Phase 3 — How tasks become training inputs

### 5. Training stages and data requirements

- **Read:** Ai2's [Tülu 3 engineering report](https://allenai.org/blog/tulu-3-technical). Read the recipe and data sections, then supervised fine-tuning, preference tuning, verifiable rewards, and evaluation. It shows why different training stages need different data and checks. Use this 2024 recipe as a concrete pipeline example, not a current model ranking or a universal sequence.
- **Concept lookup:** Lambert's [training overview](https://rlhfbook.com/c/03-training-overview), only for distinctions that remain unclear. It is a supporting reference rather than another assigned chapter.

### 6. RL updates and the task-to-trainer boundary

- **Mechanism:** The survey's [worked training step](02-survey.md#a-worked-training-step), for attempts, rewards, relative advantages, and a weight update. It is a simplified explanation, not the complete GRPO loss.
- **Implementation reference:** Thinking Machines' [Tinker SDK cheatsheet](https://tinker-docs.thinkingmachines.ai/tinker/sdk-cheatsheet/). Read the SFT/RL flow diagrams and the data preparation, sampling, gradient, and optimizer sections. Follow how collected samples become updates and how updated weights return to sampling.
- **Data-contract detail:** Tinker's [Loss Functions](https://tinker-docs.thinkingmachines.ai/tinker/losses/), specifically “How it works,” for token alignment, sampling log-probabilities, advantages, and excluded tokens. These pages illustrate one provider's interfaces; they do not select our trainer.
- **When the update math matters:** Lambert's [reinforcement learning chapter](https://rlhfbook.com/c/06-policy-gradients), limited to policy-gradient intuition and relative rewards in GRPO. Detailed optimizer derivations and distributed training internals remain conditional references.

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
