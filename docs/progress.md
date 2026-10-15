# Progress and decisions

This is the current worklist and decision record. Keep it useful to someone starting without the chat history. [Goals](00-goals.md) owns scope; [the plan](01-study-plan.md) owns the study steps and experiment design.

## Current state

As of 2026-10-14, the repository contains a survey, a study plan, a source register, study notes for the original references, and a sourced initial market map. The [glossary](glossary.md) and [foundation worksheet](studies/foundations.md) support readers new to AI. The source register distinguishes selected paper sections, reviewed pages, orientation reads, and unaudited artifacts.

The first [AutoEnvScaling code study](studies/autoenvscaling-code.md) inspected selected paths at commit `2b38259ac0ab5983c7de21df0f50696ab43e8869`. The [original record](records/2026-10-14-autoenvscaling-code/README.md) owns the offline tests and probes. The [independent review checks](records/2026-10-14-claude-review-checks/README.md) add a solver-side probe. The [review resolution](reviews/claude-init-review-1-resolution.md) records this follow-up's source checks, corrections, and recommendation-by-recommendation response.

No live generation or sandbox experiment, model training, customer interview, or paper-result reproduction has been completed. No buyer class, code-reuse path, or paid-run budget has been selected. Public market evidence and offline behavior checks help frame decisions; they do not establish demand or training benefit.

## Next work

| Priority | Work | Output | State |
| --- | --- | --- | --- |
| 1 | Compare reachable buyers and their existing alternatives | One accessible problem per buyer class where possible, permitted examples, and a provisional choice with a reason to reverse it | Public map added; team access information needed |
| 2 | Learn through small tasks and traces alongside the buyer research | H1's three to five tasks, one annotated trace, and the team's explanation of a reward and update | Exercise and teaching material ready; execution resources not agreed |
| 3 | Prepare concrete resource proposals | Model/API access, sandbox setup, maximum spend, stop conditions, and any training partner for H1/H2 | Open; no paid runs authorized |
| 4 | Test graders on the chosen task family | E1 defect counts, expert review effort, costs, and a usable/repairable/too-costly decision | Procedures defined; tasks and cases not yet selected |
| 5 | Test the benefit that matters to the first buyer | E2, E3, or bounded training comparison; authorized interviews or pilot evidence | Select after the buyer and task-quality checks |
| Conditional | If reusing AES, check how results reach training | A sandbox failure stays unscored; too little valid evidence remains inconclusive; reset and isolation checks pass | Audit findings documented; no repair project selected |

## Decisions

### 2026-10-14 Establish the exploration scope

The team chose opportunity selection and reusable task-framework design as the immediate objectives. The ultimate objective is commercial. Study and exploration are the current phase; a particular product and a large training effort have not been selected.

AutoEnvScaling and Third Moment Research receive early attention. Foundational reading, alternative approaches, and customer problems remain in scope so the study does not depend only on the team's initial references.

Durable context belongs in repository documents. Shared agent rules live in AGENTS.md, with CLAUDE.md importing them. The writing rules adapt the related project's plain-English guidance and are reproduced here so readers do not need that checkout.

### 2026-10-14 Plan by completed steps and document the remaining references

The user asked for steps without week-based estimates because capacity and other variables determine the pace. The plan now uses outputs and completion criteria. Shared agent guidance preserves this preference for later edits.

Added notes for the remaining original references under `docs/studies/`, with source links, review limits, implications, and proposed checks. Added a foundation reading worksheet and linked the notes from the document map and source register. These are study aids; they do not change the status of unrun experiments or unaudited implementations.

### 2026-10-14 Review the supplied X article

The user supplied Eli Gottlieb's *How to make a good RL task* as a PDF. Replaced its unavailable-source note with a study and recorded the saved source and hash. Added task intent and expert-guided revision of the production process to the survey and reading plan. These are design ideas to test; the article provides no measured training gains or cost reductions. The project's scope and opportunity ranking remain unchanged.

### 2026-10-14 Study AutoEnvScaling's implementation

The user requested a deeper systems explanation, code study, framework lessons, open questions, and next tests. Inspected the official preview at a pinned commit and completed selected offline tests and synthetic probes without running models or cloud infrastructure. Expanded the main study and added a code companion and reproducible record.

The [code study](studies/autoenvscaling-code.md#3-confirmed-behavior-and-its-consequences) owns the findings and their limits. They concern the inspected preview; effects on the historical paper runs remain unknown.

Prioritize explicit data contracts, independent verifier checks, and calibration stability before training. Refined E2 to hold aggregate performance information constant when measuring trace value. No product choice, live-run budget, or training reproduction has been approved by this study.

### 2026-10-14 Independent review of the initial repository

The user asked Claude to review every document for accuracy, plan quality, and organization. The [review](reviews/claude-init-review-1.md) found the cited numbers accurate and confirmed the AES code findings, with a correction needed to the Third Moment Research note. It recommends putting market research and hands-on foundations before further AES work, adding environment security and a market map, and simplifying the document stack. Two supporting records were added: [review checks of the AES code study](records/2026-10-14-claude-review-checks/README.md) and an unverified [market scan](records/2026-10-14-market-scan/README.md).

At the time of that review, its recommendations were pending. The following resolution records the changes now adopted for this study.

### 2026-10-14 Resolve Claude review 1

The user requested careful evaluation and documentation updates on points we agree with. The [resolution](reviews/claude-init-review-1-resolution.md) records each recommendation, checked evidence, and narrower interpretations where needed.

Adopt market and buyer research alongside practical foundations as the next work. Further AES repair depends on selecting its code for an experiment. This keeps the technical study tied to a commercial decision. Added beginner teaching material, H1/H2 exercises, operational E1/E2 measures, an initial market map, security boundaries, and a glossary. Corrected source attribution and expanded important result context.

Keep the short per-source notes and improve their index instead of merging them. They provide stable owners for later evidence, and several are primary reports rather than secondary material. Keep dated reviews and experiment records unchanged; remove duplication from current summaries.

The first buyer remains undecided because customer access, permitted data, and a downstream evaluator are unknown. Compare model-training teams with application owners using the [access criteria](03-opportunities.md#choose-the-first-buyer-to-study), then record a provisional choice and reversal condition. The documentation changes do not authorize outreach, spending, or a training run.

Add later decisions with their evidence and effect on the plan. Store completed experiments and interview records under `docs/records/`.
