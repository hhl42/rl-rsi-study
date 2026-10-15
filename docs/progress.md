# Progress and decisions

This is the current worklist and decision record. Keep it useful to someone starting without the chat history. [Goals](00-goals.md) owns scope; [the plan](01-study-plan.md) owns the study steps and experiment design.

## Current state

As of 2026-10-14, the repository contains an initial survey, a study plan, a source register, and commercial hypotheses. The [study index](studies/README.md) covers all 14 original references with study notes. A shared worksheet guides reading of the 14 added foundational sources. The three supplied paper PDFs were inspected in selected methods and results sections. The X article, subsequently supplied as a PDF, was reviewed in full. The source register distinguishes those reads from lighter orientation reviews and incomplete page retrievals.

The first [AutoEnvScaling code study](studies/autoenvscaling-code.md) is complete at commit `2b38259ac0ab5983c7de21df0f50696ab43e8869`. We traced selected generation, admission, calibration, pool, export, and training paths; 198 selected offline tests passed, and synthetic probes exposed several important contract gaps. The [research record](records/2026-10-14-autoenvscaling-code/README.md) preserves the code, outputs, environment, and repeat commands.

No live generation or sandbox experiment, model training, customer interview, or paper-result reproduction has been completed. The survey and opportunity matrix remain drafts. Offline behavior checks establish facts about the inspected release, not historical training results or commercial demand.

## Next work

| Priority | Work | Output | State |
| --- | --- | --- | --- |
| 1 | Team walkthrough of the AES task lifecycle and foundation concepts | Corrections to the [systems explanation](studies/autoenvscaling.md) and a shared task example | Study ready; team walkthrough planned |
| 2 | Define and check the task data contract before a live E1/E2 pilot | Outcome status through export, minimum scored attempts, reset behavior, and memory-selection rules; follow the [test sequence](studies/autoenvscaling.md#7-what-to-test-next) | Initial code audit and offline probes completed; contract checks next |
| 3 | Compare suppliers and managed improvement services beyond Third Moment Research | Alternatives, buyer hypotheses, public offer and pricing evidence where available | Planned |
| 4 | Identify accessible workflows and potential interview participants | Candidate cases and interview plan; outreach only when directed | Planned |
| 5 | Resolve study time, experiment budget, compute access, and training partners | Resource assumptions for the first pilot | Open |
| 6 | Select and run the smallest useful experiments from the plan | Reproducible records and updates to the opportunity comparison | Planned after pilot scope and resources are known |

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

The checks confirmed that a validation infrastructure failure can become a negative training reward during export, and that calibration can admit only two scored attempts after failed retries. They also clarified rubric exclusions, retained aggregate feedback in the no-trace condition, memory replacement, and differences between bridge and carry training. These are observations about the preview; their effects on the original research runs are unknown.

Prioritize explicit data contracts, independent verifier checks, and calibration stability before training. Refined E2 to hold aggregate performance information constant when measuring trace value. No product choice, live-run budget, or training reproduction has been approved by this study.

### 2026-10-14 Independent review of the initial repository

The user asked Claude to review every document for accuracy, plan quality, and organization. The [review](reviews/claude-init-review-1.md) found the cited numbers accurate and confirmed the AES code findings, with a correction needed to the Third Moment Research note. It recommends putting market research and hands-on foundations before further AES work, adding environment security and a market map, and simplifying the document stack. Two supporting records were added: [review checks of the AES code study](records/2026-10-14-claude-review-checks/README.md) and an unverified [market scan](records/2026-10-14-market-scan/README.md).

The recommendations have not been adopted. The worklist above is unchanged until the team decides.

## Findings that affect the next step

- AutoEnvScaling's paper distinguishes matched solver updates from matched total compute and documents supervised proposer initialization. Its preview adds concrete data-integrity and reproduction gaps. Use the [systems study](studies/autoenvscaling.md) for experiment choices and the [code findings](studies/autoenvscaling-code.md) before reusing an implementation path.
- Third Moment Research's own product site makes its managed offering explicit. Use the [business note](studies/third-moment-research.md) when comparing buyers and deliverables.
- Gottlieb's [task-factory study](studies/eli-gottlieb-reference.md) distinguishes repairing one task from improving the process that produces later tasks. Its proposed use of expert feedback informs an extension of E1; it does not establish training benefit or commercial demand.

Add later decisions with their evidence and effect on the plan. Move detailed experiments and interview records into linked files under `docs/records/` when they exist.
