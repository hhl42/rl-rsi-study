# Research experiments

These proposals test technical and commercial hypotheses. Select an experiment when it answers a concrete project question. The [study guide](01-study-plan.md) owns reading and viewing; [progress](progress.md) owns the active worklist. None of the experiments below has been completed.

## How to choose an experiment

Use the [buyer evidence](03-opportunities.md#buyer-evidence) to select a provisional problem, with a reason to reconsider it. Check task quality with E1 before interpreting an improvement score. Then choose E2, E3, a [Harness² comparison](studies/harness2.md#implications-and-next-tests), or a bounded training comparison according to the proposed customer benefit. E4 tests whether that benefit supports a commercial offer.

Keep model, harness, environment, and task versions explicit. Reuse the team's existing projects where they provide suitable cases and permissions. AES repair or trainer integration is justified only when the selected comparison needs it. Public research and experiment preparation do not authorize customer outreach or spending.

## Proposed experiments

A first pilot of roughly 10–20 tasks can expose defect types and give observed costs for those examples. It cannot establish a precise population failure rate or broad training value. Even zero errors in 15 independent checks leaves an approximate 95% upper bound near 20% under the rule of three. Related variants are correlated, so task or submission counts alone do not supply independent evidence.

### E1 Verify the verifier

**Hypothesis:** Graders can accept valid alternatives and reject meaningful errors with affordable review.

Before running, write an error checklist: impossible or underspecified task; missing evidence or dependencies; incorrect reference; false acceptance; false rejection; inconsistent grading; reset contamination; leaked answers; test or reward-file tampering; and unintended access to networks, shared services, or credentials. Test isolation only in environments we control, with synthetic credentials and local stand-ins for external services.

Define the grader's pass threshold before measuring errors. Prepare reference solutions, independent valid alternatives, plausible wrong solutions, empty submissions, and shortcuts. For model judges, include paraphrases and irrelevant verbosity. For executable tests, include visible-example overfitting and tampering. Have a domain expert label the prepared cases without seeing the grader's verdict; retain reasons and resolve disputed labels before scoring them.

| Measure | Procedure |
| --- | --- |
| False acceptance | Grader accepts an expert-labeled invalid submission; divide by all labeled invalid submissions. Report counts and affected tasks. |
| False rejection | Grader rejects an expert-labeled valid submission; divide by all labeled valid submissions. |
| Repeatability | Repeat a fixed submission from a fresh reset under the same configuration; report verdict disagreements and reward spread. |
| Execution reliability | Count build, reset, verifier, and infrastructure failures separately, with attempted executions as the denominator. Do not silently turn unscored attempts into wrong answers. |
| Review effort and cost | Record authoring, execution, expert review, repair, and rejected candidates. Divide total cost by independently accepted tasks; state what acceptance checks cover. |

Decide whether the task family is usable, repairable, or too costly. Reference success and empty failure alone are insufficient. An optional extension uses retained expert reasons to revise task production, then compares old and new processes on fresh candidates under equal budgets with a separate expert review sample. This tests the [task-factory hypothesis](studies/eli-gottlieb-reference.md), not downstream training benefit.

### E2 Generate from solver failures

**Hypothesis:** Solver traces help a proposer produce more relevant, usable tasks than the same system without those traces.

Use the same proposer, tools, seeds, admission checks, fixed solver, and total budget. Keep aggregate success statistics and assignment direction identical; vary access to raw trajectories and their failure summaries. Removing all solver-derived information is a separate comparison. Include a static pool as a baseline. The [AES code finding](studies/autoenvscaling-code.md#removing-solver-feedback-does-not-remove-all-solver-information) explains why the distinction matters.

Before generation, have an expert label observed failures by cause, such as missing pagination or unsafe restart order. Freeze the labels and a relevance rubric. A candidate is relevant only if independently solving and reviewing it shows that it exercises the intended failure, is feasible, and offers enough evidence to act. Reviewers should not know which generation arm produced it.

Report **relevance yield** as relevant, valid, nonduplicate tasks divided by all generated candidates. Report **coverage** as predefined failure classes with at least one independently accepted task divided by all predefined classes. Also show counts per class: one task in every class can hide poor depth. Reserve source cases for a transfer check and keep related variants together.

Measure duplication, reward variation, repair effort, and total cost, including calibration and rejected attempts. Use a solver that did not guide generation when feasible. These measures test production and relevance; a separate weight-update experiment must test training benefit. If AES code is selected, first follow its [conditional checks](studies/autoenvscaling.md#7-what-to-test-next).

### E3 Use feedback effectively

**Hypothesis:** Structured feedback helps an agent recover from a specific failure at a useful cost.

Compare independent retries, retries with raw verifier feedback, and retries with a short generated insight. Match total inference and environment budgets, including insight generation. Keep task, model, and tools fixed. Inspect traces for leaked answers.

Measure success, total cost, latency, and repeated failure types. Test transfer of reusable feedback to reserved related tasks separately. Improvement while feedback remains in context is evidence about assisted solving; evaluate without that feedback to study what weight training retained.

### E4 Test a commercial offer

**Hypothesis:** A named buyer values the improvement enough to pay for a repeatable deliverable.

Prepare a small offer: defined input, output, acceptance criteria, price hypothesis, and delivery cost. Compare it with the customer's current method through authorized interviews or a pilot. Record budget authority and a concrete purchase or pilot decision; task counts and enthusiastic comments do not establish willingness to pay.

## Evaluation and resource boundaries

Reserve repositories or task families before tuning generation. Keep variants of a parent task in one split. Separate development feedback from final evaluation. Match model, harness, tools, attempts, and compute, or report differences.

Set a cap before each paid pilot, then use its observed costs to propose the next cap. Count API inference, environment execution, grading, calibration, failures, and human work. Full AES training is unnecessary for the first experiments. A training partner or bounded open-weight run can later test unseen-task improvement.

## Decision at the end of the cycle

Choose one opportunity when its customer benefit, evidence, delivery cost, and remaining risk are clear. Define reusable interfaces from the actual task families. If customer access or data rights are missing, resolve that gap. If independent evaluation rejects the benefit, revise the hypothesis before expanding infrastructure.
