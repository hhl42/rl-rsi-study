# Research method

Collect evidence that changes a technical or commercial decision. Write enough detail for another teammate to check the claim or repeat the work. Use the [source register](../references/README.md) to find the original material.

## Types of evidence

Use wording that makes the status clear. Short labels are useful in result tables, but every sentence does not need a label.

| Status | Meaning |
| --- | --- |
| Reported | A named source makes the claim; we have not reproduced it. |
| Observed | We directly inspected an artifact or measured a result. State what was inspected or run. |
| Inference | Our interpretation of evidence. Explain the reasoning. |
| Hypothesis | A proposition we plan to test. State what would count against it. |
| Unknown | A material question for which the available evidence is insufficient. |

An official product page establishes what a company offers or claims. It does not establish revenue, customer outcomes, or implementation details that it does not disclose. Code availability is not reproduction. An abstract review is not a methods audit.

## Source notes

For a source that changes our view, record:

- The question it answers and its title, URL or local file, version, and relevant section or table.
- Its mechanism in plain English, including which component learns or changes.
- The important result, with the model, baseline, metric, sample or evaluation set, and resource assumptions.
- What limits the interpretation, and which artifacts are available.
- The implication for us and the next check needed.

Use a detailed study file only when the source merits one. Short notes can stay in the source register. Preserve provided PDFs. Link to additional papers rather than copying full articles into the repository. Track retrieval dates for changing web sources. Record exact revisions when inspecting implementation behavior.

## Currency and applicability

Separate the source's publication date, our check date, and the version or period its evidence describes. A page reopened today can still report an old experiment or market. A living documentation URL can change without changing its title.

For each consequential reading, identify what remains useful: a concept, a result in a specified setting, or an implementation or offer that needs checking before use. Explain concrete limits beside the recommendation. Newer publication is not stronger validation, and an older source is not automatically obsolete.

When an author flags outdated advice, follow the replacement or correction. For code reuse, compare the selected release's documentation, changelog, and implementation. If they conflict, record the conflict and avoid treating the snippet as verified. Reassess harness workarounds when the model, task, or execution setting changes. Refresh prices and commercial terms for the actual decision.

The guide owns reader-facing context; the source register owns dated check details. Keep historical results and records intact. State the scope of each refresh rather than giving the whole repository a new freshness date. This is a rule for future edits, not a scheduled monitoring commitment.

## Experiment records

Before running an experiment, state the hypothesis, intervention, baseline, budget, evaluation split, and decision it should inform. Name the primary metric and the tradeoffs that could reverse the conclusion. Choose decision thresholds after a small pilot if cost or variance is unknown; do not choose them after inspecting the final comparison.

Keep reproducible configuration, task and source versions, model and harness identifiers, seeds where supported, commands, outputs or permitted artifact locations, costs, failures, and the analysis. Count attempted and rejected tasks as well as accepted ones. Separate infrastructure failures from agent failures.

Use repeated runs and uncertainty estimates when randomness matters. Keep related task variants together when splitting training and evaluation data. A hundred variants from one parent task do not provide a hundred independent tests of generalization.

When records become necessary, save them under `docs/records/` with descriptive filenames and link them from progress. Large or sensitive artifacts can live in an approved shared store; record a durable location and retrieval instructions. A local temporary path is not sufficient evidence for the team.

## Commercial evidence

For a customer conversation, record the role, workflow, current alternative, failure frequency and cost, budget owner, data access, buying process, and agreed next action. Keep confidential details in an approved location and put a suitable summary here. Distinguish an expressed interest from a paid commitment and a contract from collected revenue.

Draft interview questions freely. Contacting people or making commitments requires user direction. Public research can proceed while customer access is unresolved.

## Review before sharing

Check that the claim matches the source and that a teammate can follow the links. Explain unexplained terms. Check that limitations change the interpretation rather than repeating generic cautions. Update the owning document and progress when a finding changes the plan.
