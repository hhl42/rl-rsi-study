# Progress and decisions

This is the current worklist and decision record. Keep it useful to someone starting without the chat history. [Goals](00-goals.md) owns scope; the [study guide](01-study-plan.md) owns reading and viewing; [research experiments](experiments.md) owns proposed comparisons.

## Current state

As of 2026-10-23, the repository contains a survey, a reading and viewing guide, a source register, study notes, research experiment proposals, and a sourced initial market map. The [study guide](01-study-plan.md) serves engineering leaders with deep systems expertise and existing hands-on AI work. It now favors engineering articles, design reports, and implementation documentation, with selected sections and optional depth. Practice assignments and completion gates have been removed. Book chapters and foundational papers are references for concrete questions.

The first [AutoEnvScaling code study](studies/autoenvscaling-code.md) inspected selected paths at commit `2b38259ac0ab5983c7de21df0f50696ab43e8869`. The [original record](records/2026-10-14-autoenvscaling-code/README.md) owns the offline tests and probes. The [independent review checks](records/2026-10-14-claude-review-checks/README.md) add a solver-side probe. The [review resolution](reviews/claude-init-review-1-resolution.md) records this follow-up's source checks, corrections, and recommendation-by-recommendation response.

The new [Harness² study](studies/harness2.md) covers selected paper results and code at commit `1cfe254e8d25b15f37048c3730134686abe60335`. Its [deterministic demo](records/2026-10-19-harness2-demo/README.md) completed two local task workflows and demonstrated library persistence. Scripted edits and reflection do not establish model improvement. The [review 2 resolution](reviews/claude-init-review-2-resolution.md) adds weaker results, competing baselines, and corrected cost and failure-handling descriptions.

No live model generation or sandbox integration experiment, model training, customer interview, or paper-result reproduction has been recorded in this repository. This does not describe the team's work in other projects. No buyer class, code-reuse path, or paid-run budget has been selected here. Public market evidence and offline behavior checks help frame decisions; they do not establish demand or training benefit.

## Next work

- **Reading:** Use the study guide selectively, starting with the overview where useful and giving task quality and evaluation the most attention. AES, Harness², and Third Moment notes already provide detailed comparisons. The guide does not track individual reading completion.
- **Commercial investigation:** Resolve the gaps in [buyer evidence](03-opportunities.md#buyer-evidence), including permitted examples, reachable roles, and alternatives. The map includes unverified supplier leads; a provisional buyer choice remains open.
- **Research when a project question is selected:** Use [E1](experiments.md#e1-verify-the-verifier) to check grader errors and delivery costs before interpreting a claimed benefit. Choose E2, E3, a Harness² comparison, or a bounded training comparison according to that question. These remain proposals, with the task family and acceptance criteria undecided.
- **Conditional reuse work.** Repair AES or integrate Harness² only if an experiment selects it. No paid-run budget, customer outreach, or implementation-repair project has been authorized by these documentation changes.

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

At the time of this review, its recommendations were pending. The following resolution records the decisions now adopted.

### 2026-10-20 Resolve Claude review 2

The user requested source-checked responses and rejected the proposed six-column learning table as hard to read on GitHub. The [resolution](reviews/claude-init-review-2-resolution.md) records each recommendation and narrower conclusions where the review exceeds its evidence. The original review remains unchanged.

Corrected AES's collection-time wording and Harness²'s combined-token description, function links, marker checks, and missing initial-output fallback. Expanded the comparison with weaker gains, offline tuning, retries, library ablations, judge overlap, and human setup work. These are documentation corrections, not implementation repairs or new benchmark results.

Moved the first task package into L3, added randomness and statistical interpretation, supplied real agent code and reward-hacking examples, and made M1's buyer brief explicit. Learning steps live only in the foundation guide; decision stages use D1–D5. H2 can use suitable existing or free compute. Retained a short introductory route instead of assigning every suggested resource.

Added narrow-table guidance, unverified supplier leads, source-list ownership, and glossary terms. No scope change to the commercial objective or initial AES/Third Moment priorities. Validation and source-access limits are recorded in the resolution.

### 2026-10-23 Use a reading guide for engineering leaders

The user wants readings and videos by phase and step, without exercises. The team has deep systems expertise and already builds AI projects, including `taskgen-codebase-qa`. The earlier plan's teaching assignments and completion gates did not fit that audience.

Made the study plan the single reading and viewing sequence, with focused sections, alternatives, and optional depth. Foundations now holds concept reminders and a question-based paper index. Removed H1/H2 practice assignments and the L/M/D course and decision sequences. Kept E1–E4 as separate research proposals, with their measures and resource boundaries. Actual work follows project questions and the active worklist.

Updated goals, shared agent guidance, entry documents, and current links. Earlier reviews and dated records remain unchanged; compatibility links explain where proposals moved or assignments were retired. The commercial objective and AES/Third Moment priorities are unchanged. This is a documentation reorganization, not a new experiment or source revalidation.

### 2026-10-23 Select engineering materials, not just a different format

The user pointed out that the Hugging Face Agents Course still uses a course format. Removing exercises from our guide had left much of its beginner-oriented source selection intact.

Replaced that course and the minimal-agent tutorial with architecture and control-flow readings. Removed course lectures, the long introductory-video expansion, Spinning Up, and notebook setup from the main sequence. Retained a choice of standalone overview videos and the evaluation articles, which address concrete engineering questions. Harbor's format and examples remain; its tutorial is no longer in the sequence.

Training now starts from Ai2's Tülu 3 pipeline report and uses Tinker's interfaces to connect samples to updates. Selected Lambert passages remain optional concept lookups. Added the verifiers architecture article as a conditional comparison for task and trace contracts. These sources illustrate different implementations without selecting a provider or changing the AES/Third Moment priorities.

The [source register](../references/README.md#engineering-readings) records the new source checks and their limits. Earlier sources and reviews remain available. No new implementation, training experiment, or commercial validation was performed.

Add later decisions with their evidence and effect on the plan. Store completed experiments and interview records under `docs/records/`.
