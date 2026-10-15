# Claude review 1: resolution

**Resolved by:** GPT/Codex on 2026-10-14, at the user's request. **Review:** [claude-init-review-1.md](claude-init-review-1.md). The original review and its supporting records are unchanged. This document owns the response; [progress](../progress.md) owns the resulting work order.

Most recommendations are useful and are implemented. The largest changes separate Third Moment's product claims from its internal research, add omitted AES evidence and code findings, and put buyer research alongside practical foundations. We retain the separate source notes, narrow several claims that exceed their evidence, and leave buyer selection and paid execution pending concrete inputs.

## Evidence checked for this resolution

- Re-read the review and relevant repository documents. Compared the AES claims with the supplied v1 paper, including visually inspected Tables 2 and 5. Checked Recursive Self-Rewrite's Table 5 and its explanation of rounded task counts. Verified the two Jev mentions in the supplied Gottlieb PDF.
- Inspected the cited AES code at `2b38259ac0ab5983c7de21df0f50696ab43e8869`. Re-ran the review's [solver-status probe](../records/2026-10-14-claude-review-checks/solver_status_probe.py); output was byte-identical to the [saved output](../records/2026-10-14-claude-review-checks/solver_status_probe.out). The full selected test suite and original probes were not rerun for this resolution; their earlier results remain in their records.
- Checked Third Moment's product and careers pages, OpenAI's case study, METR's investigation, the relevant public research pages, teaching texts, and a bounded set of market sources. Used browser text for ApprenticeBench and Impersona-Env where ordinary retrieval was incomplete. The [source register](../../references/README.md#sources-added-during-review-resolution) records additions and review depth.
- No model API, live sandbox, training job, customer contact, or paper reproduction was performed. The worked update is explicitly illustrative.

## Recommendation-by-recommendation decisions

Rows follow the order of section 6 of the review. “Implemented” means the documentation change is complete, not that a proposed experiment has run.

| # | Recommendation | Decision and change |
| --- | --- | --- |
| 1 | Separate Third Moment sources | **Implemented.** The [business study](../studies/third-moment-research.md) separates the advertised endpoint service, internal trading research, and hiring requirements. None supplies measured customer endpoint outcomes. |
| 2 | Correct code links and add failure handling | **Implemented.** Fixed the four target links and distinguished the `run_chain` entry from its reward assignment. The [code study](../studies/autoenvscaling-code.md#3-confirmed-behavior-and-its-consequences) covers solver export, assignment fallback, classification, pool review, single-attempt admission, proposer-side sampling, and the untested reward-file question. |
| 3 | Expand AES results | **Implemented.** Added the other proposer, evaluation size, uncertainty limits, headline versus controlled gain, generation costs, collection efficiency, and HiL-Bench. [Results](../studies/autoenvscaling.md#4-what-the-results-establish) keep the cost and data-volume limitations beside each claim. |
| 4 | Correct the RL input row | **Implemented with scope clarified.** The [survey](../02-survey.md#2-what-can-improve-and-what-training-requires) names tasks, environments, and rewards as typical external inputs for online RL. It retains the distinction between those assets and the scored attempts consumed by the optimizer; offline RL also exists. |
| 5 | Verify the incident and note Jev | **Implemented.** The [Gottlieb note](../studies/eli-gottlieb-reference.md) links METR, identifies evaluation scope, and records the product mentions. Author affiliation remains unconfirmed. |
| 6 | Build the market map | **Implemented as an initial map.** [Opportunities](../03-opportunities.md#market-map) identifies buyer classes, named alternatives, public prices where found, and missing evidence for all six candidates. Broader unverified market leads remain in the original record. |
| 7 | Put market and foundations before AES repair | **Implemented.** A dated [decision](../progress.md#2026-10-14-resolve-claude-review-1) records the new order. Repair AES only if an experiment selects its code. Public research still consumes staff effort. |
| 8 | Add hands-on tasks and a tiny RL run | **Plan implemented; execution pending.** [H1/H2](../01-study-plan.md#foundations-by-doing) define packages, traces, update inspection, outputs, and resource gates. A budget request should follow an exact model/hardware/run proposal; this review resolution does not start paid work or ask approval for an unspecified amount. |
| 9 | Put teaching texts before papers | **Implemented.** The [reading sequence](../01-study-plan.md#reading-sequence) starts with Spinning Up and the RLHF book. The [worksheet](../studies/foundations.md) ties reading to task artifacts; primary papers remain the checks for consequential claims. |
| 10 | Define E1/E2 measures and pilot limits | **Implemented.** The [plan](../01-study-plan.md#proposed-experiments) defines error categories, denominators, blinded labels, repeats, relevance yield, and failure-class coverage. Small pilots reveal defects and observed costs; correlated cases do not establish precise population rates. |
| 11 | Choose a first buyer class | **Deferred, with a decision procedure.** No customer access or training partner is recorded. The [buyer comparison](../03-opportunities.md#choose-the-first-buyer-to-study) specifies the evidence needed and a reversal rule. Progress makes this the next decision; choosing now would invent team knowledge. |
| 12 | Add execution/security candidates and usage rights | **Implemented.** Both candidates now include buyers, deliverables, alternatives, and uncertainties. The [rights question](../03-opportunities.md#evidence-needed-before-ranking) is specific to provider, model, agreement, date, and intended use. No blanket legal conclusion is asserted. |
| 13 | Add isolation to the task contract | **Implemented.** The [component table](../02-survey.md#3-what-a-task-framework-must-represent) covers network access, credentials, shared services, and trusted logs. E1 includes controlled local negative tests. |
| 14 | Explain Tmax and widen generator comparison | **Implemented at orientation depth.** The [AES study](../studies/autoenvscaling.md#4-what-the-results-establish) explains the static baseline and lists related work as discovery leads. Tmax's full implementation and the other generators remain unreviewed. |
| 15 | Add a glossary | **Implemented.** [Glossary](../glossary.md) defines RSI, benchmark notation, metrics, advantages, training methods, trainer names, GPU/model naming, and bridge/carry. The entry documents link to it. |
| 16 | Merge nine short source notes | **Not adopted.** One source per file preserves stable ownership and links for future deeper review. Several pages are primary research or first-party reports, so a `secondary-sources.md` would misclassify them. Added a takeaway column to the [study index](../studies/README.md) for comparison without opening every note. |
| 17 | Deduplicate status and findings | **Implemented for maintained explanations.** Progress owns status, records own run details, and the code study owns implementation findings. Summaries now link to those owners. Historical reviews and records retain the evidence as originally written; exact single occurrence across all history is not a useful constraint. |
| 18 | Use plain words and reduce caveat repetition | **Implemented selectively.** Rewrote the worklist and major plan passages, simplified the reward explanation, and unified the survey name. Retained limits beside quantitative claims when they affect interpretation; moving all caveats to one remote paragraph would make tables easier to misread. |
| 19 | Add a worked training step | **Implemented.** The [survey example](../02-survey.md#a-worked-training-step) follows four attempts through rewards, mean-centered advantages, generated-token updates, and fresh evaluation. It distinguishes the simplified calculation from original GRPO normalization. |

## Additional source corrections and narrower conclusions

These address details in sections 2–5 of the review beyond its final checklist.

| Source or claim | Evaluation and resulting documentation |
| --- | --- |
| AES uncertainty | Agree that 89 tasks, unspecified interval construction, and missing repeated training runs limit confidence. Appendix H's bootstrap interval belongs to a separate cold-start comparison. It cannot show that Table 3's stated intervals are too narrow or supply uncertainty for its 4.3-point gain. Both sampling and training variation need assessment. |
| AES failure classification | Agree with the broader consistency problem. The classifier uses exception type and phase as well as message patterns; it is not text matching alone. Charging a build or verifier timeout to a task is a policy choice requiring a reason, not automatically an implementation defect. Pool findings are code observations; the reward-file issue is still an untested question. |
| Third Moment interpretation | Hiring evidence makes open-weight training plausible but does not reveal the deployed endpoint architecture. The OpenAI case describes internal trading-system improvement and harness/environment work; it is not customer post-training evidence. Avoid reducing all internal research to harness edits alone. |
| RLTL;DR | Added the practical interpretation of 100 versus 3,500 successful rollouts: nearly equal scores make selection of useful successes worth testing. One setting does not establish that verified successes are always the scarce asset. |
| Recursive Self-Rewrite | Added the 89-task denominator. The paper explicitly says its parenthesized 51 and 66 counts are rounded estimates from percentages, so they must not be presented as observed raw counts. |
| MiMo | Added the announced open environments, task areas, framework, and reported costs for the described RL phase. Artifact licenses and quality remain unchecked. Open availability creates alternatives; it does not establish that all generic environments are interchangeable or costless to use. |
| HUD | Added its work with data vendors and difficulty's dependence on model, harness, and trial count. This is a commercial comparator, not evidence that independent QA has its own budget. |
| AutoBenchmark | Added 10 instances, one attempt per task per iteration, and shared proposer/judge roles. The page includes human initial and iterative direction. It does not report a systematic independent audit of final correctness; “no human validated the outputs” is stronger than the evidence checked here supports. |
| ApprenticeBench | Added 100 tasks, professional validation, a selected model/human cost comparison, and the ablation's limits. Model charges and estimated wages have different cost boundaries. Removing history, feedback, and memory together does not isolate one learning mechanism; reasoning settings also differ among reported variants. |
| Impersona-Env | Added 113 DPO-model comparisons and the author's role as sole voter. These are not independent human participants. |
| Agentic RL III | Added its own experiment and reuse of AIME 2024 for optimization and checkpoint selection. The inspected source did not establish the review's exact 30-question count, so it is not adopted. The `step()` example is an interface lead; current primary-code verification remains pending. |
| Incident and market extrapolations | METR verifies a consequential evaluation incident, not a ranking as the year's “most important” event. Omitted second-hand claims about later training pauses, funding, acquisitions, revenue shares, and service shutdowns from the maintained market map. They can be checked if they change an actual decision. |

## Remaining decisions

Choose a first buyer using access and problem evidence. Then select a permitted task family and prepare concrete resources for H1 and, if useful, H2. Outreach and spending remain pending direction. No reason has yet been established to repair AES or reproduce its full training run.

The original review remains useful evidence even where this resolution differs. New evidence should update the owning study and progress, rather than silently revising what the reviewer originally said.

## Validation

Checked local Markdown links and heading anchors, corrected pinned-code targets, and whitespace. Rechecked the four supplied PDF hashes against the source register. Confirmed the original review, supporting records, and upstream checkout are unchanged. The focused solver-status rerun matched its saved output; no additional live experiment was run.
