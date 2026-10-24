# Source register

This register preserves the starting collection and records relevant teaching and research sources. **It is a reference library, not a curriculum. You do not need to read the foundational papers in order or finish them before experimenting.** Use the [study guide](../docs/01-study-plan.md) for readings and videos by phase. Links were checked on 2026-10-14 unless noted. A source being listed does not mean all its experiments have been reviewed.

**Review depth:** *orientation* means the abstract, overview, or selected introductory material was inspected; *selected methods* means relevant methods or results were checked; *page reviewed* means the main page text was read. None of these means reproduced. The [study guide](../docs/01-study-plan.md) owns resource selection, sequence, and depth. The [study index](../docs/studies/README.md) links source analysis; [Foundations](../docs/studies/foundations.md) provides concept reminders and a question-based paper index.

## Foundational sources

F01–F14 are optional primary references for specific questions. F15–F18 record earlier overview and teaching resources; their current role is stated below. The guide now favors the [engineering readings](#engineering-readings). Numbering is an identifier, not a reading order. See [when to open papers](../docs/studies/foundations.md#when-to-open-the-foundational-papers).

### F01 RL foundations

Sutton and Barto, *Reinforcement Learning: An Introduction*, second edition, 2018. [Publisher](https://mitpress.mit.edu/9780262039246/reinforcement-learning/). Consult chapters 1 and 3 for a more formal treatment of interaction and decision processes, or chapter 13 when policy-gradient theory is needed. Publisher metadata checked; chapter study pending. The authors' book site returned an error during retrieval.

### F02 PPO

Schulman et al., *Proximal Policy Optimization Algorithms*, 2017, [paper](https://arxiv.org/abs/1707.06347). Orientation review. Sections 1–3 are relevant when an implementation requires understanding policy updates and constraints on their size. The HTML rendering was incomplete; use the paper PDF for a detailed study.

### F03 InstructGPT

Ouyang et al., *Training language models to follow instructions with human feedback*, 2022, [paper](https://arxiv.org/abs/2203.02155). Orientation review. Establishes the relationship among demonstrations, preference labels, reward models, and reinforcement learning from human feedback.

### F04 DPO

Rafailov et al., *Direct Preference Optimization: Your Language Model is Secretly a Reward Model*, 2023, [paper](https://arxiv.org/abs/2305.18290), v3 methods consulted. Selected methods, sections 3–4. Learn how preference pairs can train a policy without the usual online RL loop.

### F05 GRPO

Shao et al., *DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models*, 2024, [paper](https://arxiv.org/abs/2402.03300), v3 section 4 consulted. Selected methods. Introduces Group Relative Policy Optimization. Focus on grouping attempts and estimating relative rewards.

### F06 Reasoning with RL

DeepSeek-AI et al., *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*, 2025, [paper](https://arxiv.org/abs/2501.12948). Orientation review. Compare R1-Zero, R1, and distillation rather than treating them as one recipe. Detailed result review pending.

### F07 Acting through tools

Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*, 2022, [paper](https://arxiv.org/abs/2210.03629). Orientation review. Explains interleaving model reasoning and actions that obtain new observations.

### F08 Learning through memory

Shinn et al., *Reflexion: Language Agents with Verbal Reinforcement Learning*, 2023, [paper](https://arxiv.org/abs/2303.11366). Orientation review. Its feedback updates episodic text memory rather than model weights. Useful for interpreting broad uses of the word learning.

### F09 Repository evaluation

Jimenez et al., *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?*, 2023, [paper](https://arxiv.org/abs/2310.06770). Orientation review. Introduces repository issue resolution as an executable evaluation. Historical model scores are not a current capability estimate.

### F10 Task synthesis

Yang et al., *SWE-smith: Scaling Data for Software Engineering Agents*, 2025, [paper](https://arxiv.org/abs/2504.21798), [project and artifacts](https://swesmith.com/). Orientation review. A concrete comparison for producing tasks from existing code and tests, including subsequent model training.

### F11 Rubric rewards

Gunjal et al., *Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains*, 2025, [paper](https://arxiv.org/abs/2507.17746), v2 sections 2–3 consulted. Selected methods. Connects prompt-specific grading criteria to training rewards; relevant to the existing Q&A project.

### F12 Generated curricula

Wang et al., *Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions*, 2019, [paper](https://arxiv.org/abs/1901.01753). Orientation review. Earlier work on jointly generating environments and improving their solvers. Its setting differs from terminal agents.

### F13 Reward overoptimization

Gao, Schulman, and Hilton, *Scaling Laws for Reward Model Overoptimization*, 2022, [paper](https://arxiv.org/abs/2210.10760). Orientation review. Studies divergence between optimizing a proxy reward and performance measured by a separate reward model in a synthetic setup.

### F14 Repeated sampling and evaluation

Chen et al., *Evaluating Large Language Models Trained on Code*, 2021, [paper](https://arxiv.org/abs/2107.03374). Orientation review; section 2.1 is relevant when implementing or checking a pass@k estimator. Introduces HumanEval and explains pass@k estimation. This is the historical Codex model paper.

### F15 RLHF teaching book

Nathan Lambert, *Reinforcement Learning from Human Feedback*, [book](https://rlhfbook.com/) and [video course](https://rlhfbook.com/course). On 2026-10-19, checked the course syllabus and selected passages in [training overview](https://rlhfbook.com/c/03-training-overview), [reinforcement learning](https://rlhfbook.com/c/06-policy-gradients), and [evaluation](https://rlhfbook.com/c/16-evaluation). The [instruction-tuning chapter](https://rlhfbook.com/c/04-instruction-tuning) was also consulted in the earlier orientation. No complete book review or end-to-end viewing of the lectures. Selected book passages remain concept lookups; the guide no longer uses the lecture sequence.

### F16 Spinning Up

OpenAI, *Spinning Up in Deep RL*, [key concepts](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html). Introductory page reviewed for foundational orientation. Retained for RL vocabulary lookup, outside the main study sequence; not a current language-model trainer recommendation.

### F17 Language-model overview video

Andrej Karpathy, [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g). The original video and its listing on the [author's site](https://karpathy.ai/) were checked on 2026-10-19. Suggested as a first orientation to the concepts. His longer [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) is an optional expansion. Neither was watched end to end in this study. No timestamp-specific assignments or current capability claims are attributed to them.

### F18 Agent execution introduction

Hugging Face, [Agents Course, Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction). Introductory concepts and [action–observation structure](https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure) reviewed on 2026-10-19. Rechecked the introduction on 2026-10-23: its quizzes, first-agent project, and certification make it a poor default for this team's guide. Removed from the reading sequence; this entry preserves the earlier source record.

## Provided papers

The supplied filenames are retained. Results in our notes refer to these local v1 files, even if a later web version appears. The printed title of the first paper is RLTL;DR; its filename uses RTL-DR.

| Source | Local file | Review depth and location |
| --- | --- | --- |
| RLTL;DR: Self-improvement by Internalizing Self-generated Feedback; Kirchhof et al., 2026 | [2609.37633v1](papers/2609.37633v1-RTL-DR.pdf) | Selected methods and results, sections 4–6, table 2, appendix D; [study](../docs/studies/rl-tldr.md) |
| Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite; Li et al., 2026 | [2610.02826v1](papers/2610.02826v1-Recursive-Self-Rewrite.pdf) | Selected methods and results, section 2 and sections 3.5–3.6, table 5; [study](../docs/studies/recursive-self-rewrite.md) |
| AutoEnvScaling: Automating the Data Flywheel with Terminal Agents; Yu et al., 2026 | [2610.14163v1](papers/2610.14163v1-AutoEnvScaling.pdf) | Selected methods and results, sections 3–4, appendices G–H; [detailed study](../docs/studies/autoenvscaling.md) |

AutoEnvScaling's [official repository](https://github.com/MSR-Orchard/AutoEnvScaling) labels the code a private preview. On 2026-10-14, we inspected selected implementation paths at [commit 2b38259](https://github.com/MSR-Orchard/AutoEnvScaling/tree/2b38259ac0ab5983c7de21df0f50696ab43e8869), dated 2026-10-13. The [code study](../docs/studies/autoenvscaling-code.md) covers assignment, workspace, admission, calibration, pool management, export, and training adapters. The [offline record](../docs/records/2026-10-14-autoenvscaling-code/README.md) owns test counts, outputs, and synthetic probes. No live integrations or paper training results were reproduced. The [author publication list](https://simonucl.github.io/publications/) originally provided the code link.

## Provided pages and related primary material

[links](links.md) is the user-maintained collection of reference leads. The user may add or reformat entries; Git history preserves earlier versions. Preserve supplied entries unless asked to change them, and maintain descriptions, review depth, and agent-discovered additions in this register.

| Source | Role in the study | Review status |
| --- | --- | --- |
| [TypeSafe and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | Structured decisions and calibration; adjacent product direction | Page reviewed; company claims; [study](../docs/studies/typesafe-jev.md) |
| [MiMo RL](https://mimo.xiaomi.com/rl/) | Integrated training system | Dashboard text incomplete; used [official release](https://mimo.mi.com/docs/en-US/news/latest/v2-6) for selected system, artifact, and cost claims; [study](../docs/studies/mimo-rl.md) |
| [ApprenticeBench](https://neocognition.io/blog/apprentice-bench) | Stateful work and learning with memory | Browser setup, selected costs, and learning ablation reviewed; implementation audit pending; [study](../docs/studies/apprentice-bench.md) |
| [Raven](https://github.com/EverMind-AI/Raven) | Harness evolution and orchestration | README orientation; code not audited; [study](../docs/studies/raven.md) |
| [Harness²](https://github.com/google-research/harness2) | Harness editing and experience across tasks | Selected paper and pinned-code review; scripted demo; [details](#harness2) |
| [AutoBenchmark](https://facebookresearch.github.io/RAM/blogs/autobench/) | Benchmark generation and human direction | Main method and setup reviewed; [study](../docs/studies/autobenchmark.md) |
| [Impersona-Env](https://benshi34.github.io/#/blog/impersona-env) | User simulation and preference training | Browser page reviewed; proof of concept; [study](../docs/studies/impersona-env.md) |
| [HUD task design](https://www.hud.ai/research/what-is-a-good-task) | Practical task validity and difficulty | Page reviewed; [study](../docs/studies/hud-task-design.md) |
| [Eli Gottlieb: How to make a good RL task](https://x.com/GottliebEli/status/2110077216260608037) | Task intent, component agreement, and expert feedback in task factories | Supplied [PDF](posts/x-GottliebEli-2110077216260608037.pdf), all eight pages reviewed; practitioner argument; [study](../docs/studies/eli-gottlieb-reference.md) |
| [Third Moment case study](https://openai.com/index/third-moment-research/) | Reported operations and applications | Page reviewed; published 2026-10-14; [study](../docs/studies/third-moment-research.md) |
| [Agentic RL II](https://linpengt.com/blog/agentic-rl-part-ii) | Orientation and further references | Selected passages; secondary technical explanation; [study](../docs/studies/agentic-rl-part-ii.md) |
| [Agentic RL III](https://linpengt.com/blog/agentic-rl-part-iii) | Training systems orientation | Selected passages; check primary docs for implementation claims; [study](../docs/studies/agentic-rl-part-iii.md) |
| [Third Moment product site](https://thirdmomentresearch.com/) | Public offering and delivery process | Page reviewed; added primary source; [study](../docs/studies/third-moment-research.md) |
| [Third Moment careers](https://thirdmomentresearch.com/careers/) | Hiring requirements, distinct from product architecture evidence | Page reviewed; [study](../docs/studies/third-moment-research.md) |

The X URL initially could not be retrieved. The user then supplied a PDF containing the article, which was reviewed on 2026-10-14. Its visible date is October 13; its PDF creation metadata is dated 2026-10-14. References to this article use that saved copy, not a newly retrieved live page.

## Harness2

Added by the user to the link collection; reviewed on 2026-10-19 and rechecked during [review 2 resolution](../docs/reviews/claude-init-review-2-resolution.md) on 2026-10-20. Xu et al., *Harness²: Recursive Agent Harnessing for an Open World*, 2026, [paper v1](https://arxiv.org/html/2610.14224v1), [project](https://harness2.github.io/), [official code](https://github.com/google-research/harness2).

Selected methods and results reviewed: sections 2–4, tables 1–3, figures 5–7, and appendices B–D and F. Rechecked combined-token accounting, offline and retry baselines, library ablations, and judge roles during the second review resolution. Inspected selected code paths at commit `1cfe254e8d25b15f37048c3730134686abe60335`, including recursion, selection, library storage, adapter contracts, context handling, and the demo. The [study](../docs/studies/harness2.md) owns findings; the [offline record](../docs/records/2026-10-19-harness2-demo/README.md) preserves the deterministic demo result. No live model run or benchmark reproduction.

The repository uses Apache 2.0 and says it is not an officially supported Google product. Third-party code and benchmark datasets have their own terms; repository licensing alone does not establish rights to every experiment asset.

## Sources added during review resolution

Checked on 2026-10-14. These are a narrower checked set than the leads in the original market-scan record. Detailed implications belong in the linked owning documents.

| Source | Review depth and use |
| --- | --- |
| Ivison et al., [Tmax](https://arxiv.org/abs/2606.23321), 2026, v1 | Abstract and metadata reviewed; baseline description also checked against AES. Full method and code study pending. See [AES](../docs/studies/autoenvscaling.md). |
| METR, [OpenAI–Hugging Face incident investigation](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), 2026-08-26 | Relevant incident findings and scope reviewed. Primary investigation, not our reproduction. See [Gottlieb and isolation](../docs/studies/eli-gottlieb-reference.md#a-documented-isolation-failure). |
| Epoch AI, [An FAQ on reinforcement learning environments](https://epoch.ai/gradient-updates/state-of-rl-envs), 2026-01-12 | Report reviewed for prices, quality priorities, and internal construction. Rechecked 2026-10-24: evidence remains a January snapshot, from nine calls plus nine text/email contributors. See [market map](../docs/03-opportunities.md#market-map). |
| Scale, [RL environments](https://scale.com/rlenvironments) | Public offer reviewed; vendor claims, no customer-result audit. |
| Applied Compute, [company announcement](https://www.appliedcompute.com/company/fundraise) | Description of enterprise offering reviewed; no funding or customer-performance claims adopted from it. |
| Modal, [pricing](https://modal.com/pricing); Daytona, [pricing](https://www.daytona.io/pricing) | CPU and memory price units checked for the market map. Not a workload-cost benchmark; recheck before a spending decision. |

## Learning resources added in review 2

Checked on 2026-10-20. The study guide selects passages; this list does not add required courses. Videos were not watched and notebooks were not run.

| Source | Review depth and use |
| --- | --- |
| 3Blue1Brown, [Large Language Models explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs) | Original video page identified; short overview alternative. No transcript-level review. |
| SWE-agent team, [minimal agent tutorial](https://minimal-agent.com/) | Model-call, shell-execution, and loop examples read. Earlier introductory resource; replaced in the guide by the control-flow documentation below. No execution-boundary audit. |
| Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), 2026 | Selected grader, repeated-attempt metric, and task-debugging passages reviewed. Primary practitioner guidance, not evidence that every zero-pass task is defective. |
| METR, [Recent frontier models are reward hacking](https://metr.org/blog/2025-06-05-recent-reward-hacking/), 2025 | Concrete scoring/timing shortcuts and detection limits reviewed. Observations from METR's evaluations, not our reproduction or a universal frequency estimate. |
| Anthropic, [A statistical approach to model evaluations](https://www.anthropic.com/research/statistical-approach-to-model-evals), 2024 | Error bars, sampling assumptions, and paired comparisons reviewed. Supports interpreting repeated attempts and comparisons across tasks. |
| Unsloth, [RL guide and notebooks](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide) | Notebook list and hardware discussion reviewed. Earlier setup lead, outside the main study sequence; compatibility and free resource availability not tested. |

Lambert's official [course listing](https://rlhfbook.com/course) confirmed lectures 11 and 12 and their topics in the earlier check. Direct video retrieval failed then; the lectures are no longer part of the guide. Epoch AI's environment-market report remains the commercial context source. The market map labels additional supplier leads as unverified.

## Engineering readings

Selected on 2026-10-23 for engineering readers who already build AI systems. These replace introductory course and tutorial entries in the main guide. The notes below identify the inspected material; no code, SDK call, training run, or benchmark was executed for this selection.

### Agent design

Anthropic, [Building effective agents](https://www.anthropic.com/research/building-effective-agents), 2024-12-19. Reviewed workflow/agent distinctions, autonomy tradeoffs, execution patterns, and tool-interface guidance. A compact architecture account suited to selecting a control flow. The page has changed since publication and warns that its tooling discussion is dated; it is not our current framework comparison.

On 2026-10-24, followed that warning to [Scaling Managed Agents](https://www.anthropic.com/research/managed-agents), published 2026-04-08. Reviewed separation of session history, harness, and sandbox, and the account of model improvements making earlier context-reset logic unnecessary. The linked [product overview](https://platform.claude.com/docs/en/managed-agents/overview) was marked beta. This is a newer architectural account and an advertised service; neither code behavior nor reliability claims were independently tested.

### Agent control flow

SWE-agent team, [Agent control flow](https://mini-swe-agent.com/v2/advanced/control_flow/), v2 documentation. Reviewed the diagram and selected default-agent methods for query, action execution, history, and termination. This directly exposes implementation boundaries. The documentation route identifies the major version but does not pin a code commit; no full implementation or isolation audit was performed.

### Harness state across sessions

Anthropic, [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents), 2025-11-26. Reviewed session initialization, progress artifacts, incremental changes, and testing failures. Useful implementation experience for persistent work and recovery. The linked quickstart and reported performance were not independently tested.

The [2026-03-24 follow-up](https://www.anthropic.com/research/harness-design-long-running-apps), checked 2026-10-24, describes removing context resets with Opus 4.5 and later simplifying orchestration with Opus 4.6. Reviewed those design-change passages; its demos, scores, and costs were not reproduced. Treat the earlier recipe as a model-specific case, not a standing requirement for agents.

### A concrete post-training pipeline

Ai2, [Tülu 3: The next era in open post-training](https://allenai.org/blog/tulu-3-technical), 2024-11-21. Reviewed the article's recipe, data curation, supervised training, preference tuning, verifiable-reward training, and evaluation sections. Connects each stage to its input data and checks. The linked paper, code, and numerical results were not audited; this is a historical pipeline example rather than a current capability ranking.

### Training interfaces

Thinking Machines Lab, [Tinker SDK cheatsheet](https://tinker-docs.thinkingmachines.ai/tinker/sdk-cheatsheet/) and [Loss Functions](https://tinker-docs.thinkingmachines.ai/tinker/losses/). Reviewed the supervised/RL flows, data preparation, sampling, gradient and update calls, and the loss-input explanation. These make token alignment, masks, sampling probabilities, and advantages concrete. They describe one provider's evolving interfaces; no SDK version, provider, or trainer has been selected for our project.

**Documentation conflict found on 2026-10-24:** the cheatsheet's “Create clients” section still recommends `TINKER_SUBPROCESS_SAMPLING=1`. The [changelog](https://tinker-docs.thinkingmachines.ai/changelog/), SDK 0.27.1 dated 2026-09-04, says subprocess sampling was removed and the flag has no effect. This is an observed conflict between pages, not a runtime test. Retain the data-flow reading, but check snippets against the selected release before implementation.

### Environment architecture

Prime Intellect, [verifiers v1: Decomposing Tasksets and Harnesses for Agentic RL & Evaluations](https://www.primeintellect.ai/blog/verifiers-v1), 2026-07-12. Reviewed the architecture and API passages on tasksets, harnesses, runtimes, interception, and traces with branches. It introduced the `verifiers.v1` preview in package `0.2.0`. Keep it for design history; that release state has been superseded.

Checked on 2026-10-24: the [v0.4.0 release notes](https://github.com/PrimeIntellect-ai/verifiers/releases/tag/v0.4.0), dated October 12 on GitHub, remove the legacy v0 implementation. The [release announcement](https://www.primeintellect.ai/blog/prime-rl-0-10-verifiers-0-4) is dated October 19. The [current overview](https://docs.primeintellect.ai/verifiers/v1/overview) describes v1 interfaces. Release notes target Harbor 0.24.0 and reject its multi-step tasks, so compatibility needs checking at the feature level. These are documentation checks; code behavior, isolation, scaling, and commercial claims remain unverified.

## Framework documentation

| Source | Purpose | Review status |
| --- | --- | --- |
| [Harbor task format](https://docs.harborframework.com/tasks/overview), [task tutorial](https://docs.harborframework.com/tutorials/create-a-task), [Terminal-Bench examples](https://github.com/harbor-framework/terminal-bench-2) | Task packaging, execution, and verification | Format, tutorial, and example repository reviewed on 2026-10-20; no task implementation or integration run completed |
| [verl](https://verl.readthedocs.io/en/latest/) | RL training and rollout integration | Overview reviewed; no version selected |
| [SkyRL](https://docs.skyrl.ai/docs) | Alternative training integration | Documentation entry page reviewed; detailed comparison pending |

Harbor's task overview and [release policy](https://docs.harborframework.com/contributing/release-policy) were rechecked on 2026-10-24. The living task page includes multi-step tasks; the policy permits breaking changes in minor releases. Keep the packaging concepts, but match the chosen runner and adapter versions before reuse. No integration run or new review of the example repository was performed.

## Currency check 2026-10-24

This check assessed continued reading value and selected changing claims. It covered Anthropic's agent and evaluation articles and their newer follow-ups; Tülu 3's pipeline explanation; Harbor, Tinker, and verifiers documentation and release information; and Epoch and Third Moment public material. The relevant entries above and the [Third Moment study](../docs/studies/third-moment-research.md) record the findings.

The statistical guide's clustering and paired-comparison reasoning remains useful under its assumptions. METR's June 2025 cases remain evidence of particular grader failures, without establishing current model frequencies. Tülu 3 remains an understandable historical pipeline. Newer harness accounts demonstrate that model-specific workarounds can lose value. Moving documentation can disagree with release notes, as the Tinker check shows.

The check did not rewatch videos, audit newer AES/Harness² commits, reproduce paper results, revalidate the full vendor/pricing map, or test commercial claims. Prior source dates and pinned records still apply. This is not a blanket statement that every document is current.

## Integrity of supplied files

SHA-256 values recorded on 2026-10-14 identify the exact local sources used. These hashes establish file identity, not authenticity or correctness.

```text
399f9134c04149b7a7fe3f360e66b559d4afd3b806bb660c08dbe7a55d135bd7  2609.37633v1-RTL-DR.pdf
24ae4ec47493767e335db1c7d342a90726da3114cb41b461ccc63052a85b9281  2610.02826v1-Recursive-Self-Rewrite.pdf
b59b2abdd375e2c4d299b18401e7e832a1331f7c5cf3b4fba535acf812bd8dd5  2610.14163v1-AutoEnvScaling.pdf
ada540b56b611ba85e1473cc8caab9bb8841ab468d1076c395b25776460ad270  x-GottliebEli-2110077216260608037.pdf
```
