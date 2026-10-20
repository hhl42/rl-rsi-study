# Progress and decisions

This is the current worklist and decision record. Keep it useful to someone starting without the chat history. [Goals](00-goals.md) owns scope; [the plan](01-study-plan.md) owns the study steps and experiment design.

## Current state

As of 2026-10-19, the repository contains a survey, a study plan, a source register, study notes, and a sourced initial market map. The [guided learning path](studies/foundations.md) now starts with high-level online explanations and videos. Its six steps specify required depth, a small output, and when to move on. Foundational papers are optional references for concrete questions. This documents the learning route; it does not mean the team has completed it.

The first [AutoEnvScaling code study](studies/autoenvscaling-code.md) inspected selected paths at commit `2b38259ac0ab5983c7de21df0f50696ab43e8869`. The [original record](records/2026-10-14-autoenvscaling-code/README.md) owns the offline tests and probes. The [independent review checks](records/2026-10-14-claude-review-checks/README.md) add a solver-side probe. The [review resolution](reviews/claude-init-review-1-resolution.md) records this follow-up's source checks, corrections, and recommendation-by-recommendation response.

The new [Harness² study](studies/harness2.md) covers selected paper results and code at commit `1cfe254e8d25b15f37048c3730134686abe60335`. Its [deterministic demo](records/2026-10-19-harness2-demo/README.md) completed two local task workflows and demonstrated library persistence. Scripted edits and reflection do not establish model improvement.

No live model generation or sandbox integration experiment, model training, customer interview, or paper-result reproduction has been completed. No buyer class, code-reuse path, or paid-run budget has been selected. Public market evidence and offline behavior checks help frame decisions; they do not establish demand or training benefit.

## Next work

| Priority | Work | Output | State |
| --- | --- | --- | --- |
| 1 | Follow learning steps 1–4: whole system, one execution, evaluation, practical training flow | Two-loop diagram, annotated trace, grader counterexamples, and a worked reward calculation | Resource selection complete; team learning outputs pending; no paid resources required |
| Parallel | Compare reachable buyers and their existing alternatives | One accessible problem per buyer class where possible, permitted examples, and a provisional choice with a reason to reverse it | Public map available; team access information needed |
| 2 | Compare mechanisms in learning step 5, then begin H1 with one task | AES/Harness²/manual comparison and one repeatable package; expand H1 to three to five tasks after checking the contract | Source notes and scripted demo available; task not selected |
| 3 | Prepare a concrete resource proposal when model execution is needed | Model/API access, sandbox setup, maximum spend, and stop conditions | Open; no paid runs authorized; H2 only if training depth is needed |
| 4 | Test graders on the chosen task family | E1 defect counts, expert review effort, costs, and a usable/repairable/too-costly decision | Procedures defined; tasks and cases not yet selected |
| 5 | Test the benefit that matters to the first buyer | E2, E3, a Harness² comparison, or bounded training; authorized interviews or pilot evidence | Select after the buyer and task-quality checks |
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

### 2026-10-19 Reorder learning around practical competence

The user found the earlier plan poorly organized and prefers high-level online material and videos before papers. The earlier sequence mixed foundational learning, market decisions, implementation, and long paper lists without clear stopping points.

Replaced that sequence with six learning steps and explicit depth limits. Study task and evaluation contracts closely; learn enough RL to understand the data flow and interpret results. Make a real weight-update exercise conditional on a training question. Keep buyer research alongside learning, so neither customer access nor compute blocks introductory progress. The source register remains a library rather than assigned reading. Goals, shared agent guidance, and entry documents now preserve this preference.

### 2026-10-19 Add Harness² as an implementation comparison

The user added the official repository and requested study notes. Reviewed selected methods, results, and pinned code; ran the provided deterministic local demo without models. Saved its summary and a reproducible record. The study distinguishes current-task harness edits from library changes across tasks, documents execution costs and information boundaries, and proposes controlled comparisons.

Harness² broadens the comparison to improvement with fixed model weights. It does not replace the AES and Third Moment Research priorities or select a commercial offering. The next implementation remains a small task and verifier exercise; the study's proposed experiments are conditional candidates.

### 2026-10-20 Second independent review

The user asked Claude to review the changes since review 1, with emphasis on the learning path and the Harness² study. [Review 2](reviews/claude-init-review-2.md) accepts the resolution's corrections to review 1. It recommends teaching run-to-run variation and reward hacking, building the first Harbor task during the evaluation step, adding a market track, and fixing two learning-path links. It also finds that the Harness² note omits strong alternatives in the paper, such as one-time offline harness tuning and best-of-k retries.

These recommendations have not been adopted. The worklist above is unchanged until the team decides.

Add later decisions with their evidence and effect on the plan. Store completed experiments and interview records under `docs/records/`.
