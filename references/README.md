# Source register

This register preserves the starting collection and records relevant teaching and research sources. **It is a reference library, not a curriculum. You do not need to read the foundational papers in order or finish them before experimenting.** Start with the [guided learning path](../docs/studies/foundations.md). Links were checked on 2026-10-14 unless noted. A source being listed does not mean all its experiments have been reviewed.

**Review depth:** *orientation* means the abstract, overview, or selected introductory material was inspected; *selected methods* means relevant methods or results were checked; *page reviewed* means the main page text was read. None of these means reproduced. The [study plan](../docs/01-study-plan.md) connects learning to decisions. The [study index](../docs/studies/README.md) links source analysis; the foundation guide owns resource selection and depth.

## Foundational sources

F01–F14 are optional primary references for specific questions. F15–F18 provide the online teaching resources used in the learning path. Their numbering is an identifier, not a reading order. See [when to open papers](../docs/studies/foundations.md#when-to-open-the-foundational-papers).

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

Nathan Lambert, *Reinforcement Learning from Human Feedback*, [book](https://rlhfbook.com/) and [video course](https://rlhfbook.com/course). On 2026-10-19, checked the course syllabus and selected passages in [training overview](https://rlhfbook.com/c/03-training-overview), [reinforcement learning](https://rlhfbook.com/c/06-policy-gradients), and [evaluation](https://rlhfbook.com/c/16-evaluation). The [instruction-tuning chapter](https://rlhfbook.com/c/04-instruction-tuning) was also consulted in the earlier orientation. No complete book review or end-to-end viewing of the lectures. The foundation guide selects topics; the full course is optional.

### F16 Spinning Up

OpenAI, *Spinning Up in Deep RL*, [key concepts](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html). Introductory page reviewed for the foundation sequence. Teaching material for agent/environment interaction, policies, and trajectories; not a current language-model trainer recommendation.

### F17 Language-model overview video

Andrej Karpathy, [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g). The original video and its listing on the [author's site](https://karpathy.ai/) were checked on 2026-10-19. Suggested as a first orientation to the concepts. His longer [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) is an optional expansion. Neither was watched end to end in this study. No timestamp-specific assignments or current capability claims are attributed to them.

### F18 Agent execution introduction

Hugging Face, [Agents Course, Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction). Introductory concepts and [action–observation structure](https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure) reviewed on 2026-10-19. Use the conceptual sections; completing framework tutorials or certification is not part of our required path.

## Provided papers

The supplied filenames are retained. Results in our notes refer to these local v1 files, even if a later web version appears. The printed title of the first paper is RLTL;DR; its filename uses RTL-DR.

| Source | Local file | Review depth and location |
| --- | --- | --- |
| RLTL;DR: Self-improvement by Internalizing Self-generated Feedback; Kirchhof et al., 2026 | [2609.37633v1](papers/2609.37633v1-RTL-DR.pdf) | Selected methods and results, sections 4–6, table 2, appendix D; [study](../docs/studies/rl-tldr.md) |
| Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite; Li et al., 2026 | [2610.02826v1](papers/2610.02826v1-Recursive-Self-Rewrite.pdf) | Selected methods and results, section 2 and sections 3.5–3.6, table 5; [study](../docs/studies/recursive-self-rewrite.md) |
| AutoEnvScaling: Automating the Data Flywheel with Terminal Agents; Yu et al., 2026 | [2610.14163v1](papers/2610.14163v1-AutoEnvScaling.pdf) | Selected methods and results, sections 3–4, appendices G–H; [detailed study](../docs/studies/autoenvscaling.md) |

AutoEnvScaling's [official repository](https://github.com/MSR-Orchard/AutoEnvScaling) labels the code a private preview. On 2026-10-14, we inspected selected implementation paths at [commit 2b38259](https://github.com/MSR-Orchard/AutoEnvScaling/tree/2b38259ac0ab5983c7de21df0f50696ab43e8869), dated 2026-10-13. The [code study](../docs/studies/autoenvscaling-code.md) covers assignment, workspace, admission, calibration, pool management, export, and training adapters. The [offline record](../docs/records/2026-10-14-autoenvscaling-code/README.md) owns test counts, outputs, and synthetic probes. No live integrations or paper training results were reproduced. The [author publication list](https://simonucl.github.io/publications/) originally provided the code link.

## Provided pages and related primary material

[links](links.md) is the original list. Keep it unchanged as provenance; maintain descriptions and additions here.

| Source | Role in the study | Review status |
| --- | --- | --- |
| [TypeSafe and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | Structured decisions and calibration; adjacent product direction | Page reviewed; company claims; [study](../docs/studies/typesafe-jev.md) |
| [MiMo RL](https://mimo.xiaomi.com/rl/) | Integrated training system | Dashboard text incomplete; used [official release](https://mimo.mi.com/docs/en-US/news/latest/v2-6) for selected system, artifact, and cost claims; [study](../docs/studies/mimo-rl.md) |
| [ApprenticeBench](https://neocognition.io/blog/apprentice-bench) | Stateful work and learning with memory | Browser setup, selected costs, and learning ablation reviewed; implementation audit pending; [study](../docs/studies/apprentice-bench.md) |
| [Raven](https://github.com/EverMind-AI/Raven) | Harness evolution and orchestration | README orientation; code not audited; [study](../docs/studies/raven.md) |
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

Added by the user to the link collection; reviewed on 2026-10-19. Xu et al., *Harness²: Recursive Agent Harnessing for an Open World*, 2026, [paper v1](https://arxiv.org/html/2610.14224v1), [project](https://harness2.github.io/), [official code](https://github.com/google-research/harness2).

Selected methods and results reviewed: sections 2–4, tables 1–3, figure 6, and relevant appendix details. Inspected selected code paths at commit `1cfe254e8d25b15f37048c3730134686abe60335`, including recursion, selection, library storage, adapter contracts, context handling, and the demo. The [study](../docs/studies/harness2.md) owns findings; the [offline record](../docs/records/2026-10-19-harness2-demo/README.md) preserves the deterministic demo result. No live model run or benchmark reproduction.

The repository uses Apache 2.0 and says it is not an officially supported Google product. Third-party code and benchmark datasets have their own terms; repository licensing alone does not establish rights to every experiment asset.

## Sources added during review resolution

Checked on 2026-10-14. These are a narrower checked set than the leads in the original market-scan record. Detailed implications belong in the linked owning documents.

| Source | Review depth and use |
| --- | --- |
| Ivison et al., [Tmax](https://arxiv.org/abs/2606.23321), 2026, v1 | Abstract and metadata reviewed; baseline description also checked against AES. Full method and code study pending. See [AES](../docs/studies/autoenvscaling.md). |
| METR, [OpenAI–Hugging Face incident investigation](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), 2026-08-26 | Relevant incident findings and scope reviewed. Primary investigation, not our reproduction. See [Gottlieb and isolation](../docs/studies/eli-gottlieb-reference.md#a-documented-isolation-failure). |
| Epoch AI, [The state of RL environments](https://epoch.ai/gradient-updates/state-of-rl-envs), 2026-01-12 | Interview report reviewed for prices, quality priorities, and internal construction. Reported observations, not transaction audits. See [market map](../docs/03-opportunities.md#market-map). |
| Scale, [RL environments](https://scale.com/rlenvironments) | Public offer reviewed; vendor claims, no customer-result audit. |
| Applied Compute, [company announcement](https://www.appliedcompute.com/company/fundraise) | Description of enterprise offering reviewed; no funding or customer-performance claims adopted from it. |
| Modal, [pricing](https://modal.com/pricing); Daytona, [pricing](https://www.daytona.io/pricing) | CPU and memory price units checked for the market map. Not a workload-cost benchmark; recheck before a spending decision. |

## Framework documentation

| Source | Purpose | Review status |
| --- | --- | --- |
| [Harbor](https://docs.harborframework.com/) | Task packaging, execution, and verification | Documentation index reviewed; interface walkthrough pending |
| [verl](https://verl.readthedocs.io/en/latest/) | RL training and rollout integration | Overview reviewed; no version selected |
| [SkyRL](https://docs.skyrl.ai/docs) | Alternative training integration | Documentation entry page reviewed; detailed comparison pending |

## Integrity of supplied files

SHA-256 values recorded on 2026-10-14 identify the exact local sources used. These hashes establish file identity, not authenticity or correctness.

```text
399f9134c04149b7a7fe3f360e66b559d4afd3b806bb660c08dbe7a55d135bd7  2609.37633v1-RTL-DR.pdf
24ae4ec47493767e335db1c7d342a90726da3114cb41b461ccc63052a85b9281  2610.02826v1-Recursive-Self-Rewrite.pdf
b59b2abdd375e2c4d299b18401e7e832a1331f7c5cf3b4fba535acf812bd8dd5  2610.14163v1-AutoEnvScaling.pdf
ada540b56b611ba85e1473cc8caab9bb8841ab468d1076c395b25776460ad270  x-GottliebEli-2110077216260608037.pdf
```
