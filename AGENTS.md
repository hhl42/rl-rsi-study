# Shared agent guidance

These instructions apply to GPT/Codex, Claude, and other agents working in this repository. `CLAUDE.md` imports this file. Keep shared rules here so the two entry points cannot diverge.

## Start each task

Read [goals](docs/00-goals.md), the [document map](docs/README.md), and [progress](docs/progress.md). Then read the files relevant to the request. Inspect the working tree before editing and preserve changes made by others.

The current phase is study and exploration toward a commercial product. Help the team choose an opportunity and understand the task framework it would require. AutoEnvScaling and Third Moment Research have priority, but compare alternatives. A paper result, a compelling demo, and a customer willing to pay are different kinds of evidence.

Write for engineering leaders with deep systems experience who already build AI projects. Organize the study guide as readings and videos by phase and step, with selected sections and optional depth. Prefer standalone engineering articles, design reports, implementation documentation, and focused talks. Judge the material's audience and substance, not just the guide's formatting; beginner courses and build-your-first-agent tutorials are poor default choices. Keep book chapters and papers as references for specific questions. Do not add teaching exercises, quizzes, completion artifacts, or course-style gates. Practical work follows project needs.

Do not infer a decision to build a general platform, operate training infrastructure, or sell a particular product from interest in a paper. Routine reading, documentation, and reversible checks should proceed within the user's request. Research does not itself authorize customer outreach, publication, paid runs, or deployment.

## Keep the repository useful to the next reader

- Use the owning file in the document map. Update its explanation instead of appending a conflicting rule elsewhere.
- Save valuable findings, sources, limitations, decisions, and next actions. Do not keep required context only in chat, private memory, or temporary files.
- Update progress when work changes its state. Distinguish planned, completed, and blocked work.
- Record material scope changes with the reason in progress, then update goals and affected documents. Goals can change with evidence or user direction.
- Use relative links inside repository documents. Do not require a local username, absolute path, or sibling checkout.
- Keep the stack small. Create a new document only when it owns a distinct question or a durable research record.
- Keep the study guide limited to reading and viewing. Keep research experiment proposals separate, with hypotheses, measures, and decision criteria. Do not assign calendar durations unless the user asks for a schedule.

## Use evidence carefully

Follow [the research method](docs/research-method.md). Prefer papers, official implementations, and first-party product material. Use secondary explanations for orientation, then check the primary source for consequential technical claims.

Distinguish reported results, our observations, inferences, and open hypotheses. Give quantitative claims their metric, baseline, model, evaluation setting, and source location. Do not call something reproduced because its code is available. Do not call a revenue claim verified because it appears in a launch announcement.

For every self-improvement claim, identify what changes: weights, memory, prompt, tools, harness, task pool, or some combination. Keep benchmark quality, training usefulness, and commercial value separate. Log inaccessible sources without guessing their contents.

Keep source files unchanged. Record versions for results that depend on them. Do not put credentials, customer traffic, or private source material into the shared repository. Record data permissions when they affect an experiment or product decision.

## Write plain English

These rules adapt the writing guidance from the related `ai-data-research` repository. They are self-contained here and apply to docs, code comments, commit messages, and error text.

1. Prefer common words. Say what the system or person does.
2. Put one main idea in each sentence. Split sentences that need rereading.
3. Avoid metaphors and compressed labels. Explain the actual relationship.
4. State the evidence before its interpretation.
5. Use one name for one thing. Define an unfamiliar AI term before relying on it.
6. Use normal word order and connected paragraphs. Use tables for compact comparisons and lists for steps or parallel items. Keep tables narrow, usually two or three columns. Use short sections when prose would create tall, cramped cells on GitHub.
7. Keep new findings in proportion. Rewrite an affected passage so it reads coherently.
8. Keep numbers only when they help a decision. Place the relevant limitation beside the claim.
9. Use dates for changing sources, measurements, and decisions. Avoid decorative dates and attribution in enduring rules.
10. Document why and when to use a command. Let its help text own flags and defaults.

Explain technical ideas with concrete systems examples. Avoid assuming the reader understands training, reward models, or benchmark conventions. Be concise without removing the reasoning a new reader needs.

## Finish a change

Check local links and heading anchors, source attribution, terminology, and agreement with goals. Read the changed passages as a new teammate would. For documentation-only work, focused checks are enough; do not invent a large test process. Report what changed and any material gap. Do not claim unrun experiments or checks passed.

Commit completed changes after the relevant checks pass, unless the user explicitly asks otherwise. Stage only files relevant to the task, preserve unrelated changes, and report the commit hash in the final response.
