# Study and exploration plan

Use the study to choose a commercial opportunity and understand the framework it needs. [Goals and scope](00-goals.md) owns that objective. Reading, practical exercises, and customer research should resolve decisions. The steps have outputs rather than calendar estimates; [progress](progress.md) owns the active worklist.

## Why this order

Our first job is to decide which agent behavior a customer needs improved and whether we can measure that improvement. Then we can choose the tasks, feedback, and improvement method. Choosing a trainer or reproducing a large paper before answering those questions would leave the product question unresolved.

The learning path therefore starts with a whole-system explanation, follows one execution, and studies evaluation before optimization. We need the deepest knowledge at the task boundary: what the agent sees, what it can do, how execution resets, and how outcomes are judged. We need enough training knowledge to supply useful inputs and interpret results. Operating a training system is a later, conditional choice.

## Reading sequence

Follow the [guided learning path](studies/foundations.md). It supplies one main resource per step, video or text alternatives, exercises, and stopping points. **Do not read the foundational source list in order.** Papers are consulted when an experiment or design choice raises a specific question.

| Step | Learn | Output that shows enough understanding |
| --- | --- | --- |
| 1. Whole system | Language models, training versus inference, weights versus context and harness | Draw execution and training loops; identify what each improvement method changes. |
| 2. One execution | Agent, tools, task, environment, trajectory, reset | Annotate a trace and explain the task's inputs, actions, and outcome. |
| 3. Trustworthy measurement | Task validity, grader errors, held-out evaluation, repeated attempts, cost | Design checks for a valid repair, an alternative repair, and a misleading shortcut. |
| 4. Task-to-training flow | SFT, preference data, RL sampling, rewards, advantages, weight updates | Work through one numerical update and explain the assets each method consumes. |
| 5. Competing mechanisms | Manual task construction, AES, Harness²; commercial offering separately | Compare what changes, the acceptance evidence, transfer, and total cost. |
| 6. Small implementation | Package, reset, solve, and grade a familiar task | Complete H1 progressively; another teammate can execute the package. |

Skip a step when its output is already clear. Use the survey as a reference and the glossary on demand. The first five steps can use existing explanations, traces, and offline calculations; they do not depend on a GPU, customer access, or a paid API.

## How much depth we need

| Area | Required in this exploration | Go deeper when |
| --- | --- | --- |
| Language models | Explain tokens, context, learned weights, generation, and the purpose of training stages | A model architecture or adaptation choice affects our task or product. |
| Tasks, environments, traces | Inspect and implement the execution contract, reset, versioning, and failure recording | The first task family exposes a missing interface or reliability problem. |
| Rewards and evaluation | Design and challenge graders; detect leakage; compare transfer and cost fairly | An experiment requires a more precise statistical estimate or specialized domain judgment. |
| RL and other training methods | Trace samples through scoring and an update; interpret simple advantages and token masks | We integrate with a trainer or must explain a training failure. Then inspect the actual loss and run H2. |
| Training infrastructure | Recognize rollout, scoring, and optimization stages and their version boundaries | A selected opportunity requires owning throughput, scheduling, or model updates. |
| Commercial evidence | Identify a buyer, current alternative, acceptance test, and delivery cost | Access supports an authorized interview or concrete pilot. |

A full ML curriculum, every foundational paper, transformer implementation, and PPO derivation are not entry requirements. Fill a missing concept when it blocks an output above.

## From learning to an opportunity decision

| Step | Work | Output and completion condition |
| --- | --- | --- |
| 1. Learn and investigate | Follow the learning path while comparing public offerings and reachable buyer classes. | Shared execution and improvement diagrams, a sourced market map, and candidate customer problems. |
| 2. Select a provisional problem | Compare permitted examples, buyer access, and measurable outcomes. | A provisional choice in progress, with evidence, the largest gap, and a condition that would reverse it. |
| 3. Establish task quality | Use H1's integration experience and run E1 on a relevant small task family. | Defects, review effort, costs, and a decision: usable, repairable, or too costly. |
| 4. Test the claimed benefit | Choose E2, E3, a Harness² comparison, or a bounded training experiment according to the buyer's need. | A reproducible comparison that changes or confirms the opportunity ranking. |
| 5. Make a commercial and architecture decision | Test E4; compare reuse with building. | Proceed, narrow, change direction, or stop. If proceeding, define the smallest project and its acceptance test. |

Customer research runs alongside learning. It need not wait for all six steps, and lack of customer access should not block foundational learning. Public research cannot establish demand by itself. Outreach, paid runs, and commitments require direction beyond this documentation work. AES repair work enters the plan only if a selected experiment will reuse its implementation.

## Foundations by doing

These are implementation exercises after the introductory learning steps. H1 applies the task and evaluation concepts; H2 is conditional on a need to inspect weight training. Neither is a prerequisite for starting the study.

### H1 Inspect and run a small task set

Start with one hand-written task in a familiar systems domain, such as configuration repair. Use Harbor as the first packaging candidate. Pin dependencies and define initial state, reset, instructions, reference solution, and verifier. Check reference and empty solutions, a deliberate wrong solution, and a different valid repair. Another teammate should be able to repeat these checks. Then expand to three to five tasks.

Once API access, sandbox resources, and a spend cap are agreed, run two existing agents with documented model and harness versions. Keep task resources and attempt budgets comparable. Repeat attempts to look for inconsistent outcomes, rather than interpreting one run as a reliable success rate. Annotate one trajectory: observations, generated actions, stopping reason, reward, elapsed time, and cost. Include failed starts and retries in accounting.

**Output:** the task packages, run configuration, an annotated trace, and a short account of surprising failures. Each participant should explain whether a failure came from the agent, task, grader, or infrastructure. This is an integration exercise, not evidence of training benefit or a representative benchmark.

### H2 Observe one small weight update

**Optional depth step:** use this when training integration or a training-related uncertainty justifies it. It is not required before H1, E1, or harness-improvement studies. Prepare a tiny open-weight RL exercise with a checkable toy answer. Choose a supported small model and trainer, a training set, and a separate evaluation set. Inspect groups with mixed rewards and groups where every attempt fails. Save the rewards, advantages, which tokens contribute to the training loss, and before/after results at the same sampling budget.

**Before any paid run:** write down the exact model, hardware, expected run size, API and compute charges, maximum spend, and stop conditions. Request approval for that concrete proposal. This plan authorizes preparation, not spending. Until resources are agreed, use the [worked example](02-survey.md#a-worked-training-step) and an offline calculation. A toy run teaches the update mechanism; it does not validate a commercial task family.

## Public research and customer discovery

Maintain the [market map](03-opportunities.md#market-map) from public sources. Compare the buyer's current workaround and named alternatives, including internal construction. Keep vendor claims, interview evidence, and our hypotheses distinct.

Before choosing the first buyer, list contacts the team can legitimately reach, available problem examples, data permissions, and acceptance criteria. Use the opportunity document's interview questions when outreach is authorized. An accessible buyer with a measurable problem is a stronger starting point than a fashionable architecture.

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
