# Study and exploration plan

Use the study to choose a commercial opportunity and understand the framework it needs. [Goals and scope](00-goals.md) owns that objective. Reading, practical exercises, and customer research should resolve decisions. The steps have outputs rather than calendar estimates; [progress](progress.md) owns the active worklist.

## Sequence and outputs

| Step | Work | Output and completion condition |
| --- | --- | --- |
| 1. Market and practical foundations | Compare public offerings while learning the agent loop and inspecting small tasks. Use the exercises below. | A sourced market map and one annotated trajectory. The team can explain task, environment, reward, and what changes during learning. |
| 2. First buyer and problem | Compare accessible model-training teams and application owners. Identify permitted examples and a route to customer evidence. | A provisional buyer choice in progress, with evidence, the largest gap, and a condition that would reverse it. Prepare authorized interviews as soon as access allows. |
| 3. Task quality | Run E1 on a small task family relevant to that buyer. | Defects, review effort, costs, and a decision: usable, repairable, or too costly. |
| 4. Test the claimed benefit | Choose E2, E3, or a bounded training experiment according to the buyer's need. | A reproducible comparison that changes or confirms the opportunity ranking. |
| 5. Commercial and architecture decision | Test E4; compare reuse with building. | Proceed, narrow, change direction, or stop. If proceeding, define the smallest project and its acceptance test. |

Steps can overlap. Customer evidence need not wait for all reading or technical experiments. Public research needs staff effort but no customer contact; it cannot establish demand by itself. Outreach, paid runs, and commitments require direction beyond this documentation work. AES repair work enters the plan only if a selected experiment will reuse its implementation.

## Foundations by doing

The [worksheet](studies/foundations.md) connects these exercises to reading. The [glossary](glossary.md) explains terms as needed.

### H1 Inspect and run a small task set

Write three to five Harbor-compatible tasks by hand in a familiar systems domain, such as configuration repair. Pin their dependencies and define initial state, reset, instructions, reference solution, and verifier. Start with reference and empty solutions; record a deliberate wrong solution and a different valid repair.

Once API access, sandbox resources, and a spend cap are agreed, run two existing agents with documented model and harness versions. Keep task resources and attempt budgets comparable. Repeat attempts to look for inconsistent outcomes, rather than interpreting one run as a reliable success rate. Annotate one trajectory: observations, generated actions, stopping reason, reward, elapsed time, and cost. Include failed starts and retries in accounting.

**Output:** the task packages, run configuration, an annotated trace, and a short account of surprising failures. Each participant should explain whether a failure came from the agent, task, grader, or infrastructure. This is an integration exercise, not evidence of training benefit or a representative benchmark.

### H2 Observe one small weight update

Prepare a tiny open-weight RL exercise with a checkable toy answer. Choose a supported small model and trainer, a training set, and a separate evaluation set. Inspect groups with mixed rewards and groups where every attempt fails. Save the rewards, advantages, which tokens contribute to the training loss, and before/after results at the same sampling budget.

**Before any paid run:** write down the exact model, hardware, expected run size, API and compute charges, maximum spend, and stop conditions. Request approval for that concrete proposal. This plan authorizes preparation, not spending. Until resources are agreed, use the [worked example](02-survey.md#a-worked-training-step) and an offline calculation. A toy run teaches the update mechanism; it does not validate a commercial task family.

## Reading sequence

Use teaching material for vocabulary, then primary papers to check the claims that matter. Select passages; understanding every derivation is not a prerequisite. The [source register](../references/README.md) records review depth.

| Order | Start here; then check | Question to answer |
| --- | --- | --- |
| 1 | [Spinning Up: key concepts](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html); survey sections 1–3; then Sutton and Barto chapters 1 and 3 and ReAct | What are state, observation, action, policy, and reward in H1? |
| 2 | [RLHF book: training overview](https://rlhfbook.com/c/03-training-overview) and [instruction tuning](https://rlhfbook.com/c/04-instruction-tuning); then InstructGPT, DPO, and DeepSeek-R1 overviews | Which assets do SFT, preferences, and online RL require? |
| 3 | [RLHF book: reinforcement learning](https://rlhfbook.com/c/06-policy-gradients) and the worked example; then PPO sections 1–3 and DeepSeekMath section 4 | How do rewards affect weights? Why does variation among attempts matter? |
| 4 | SWE-bench and SWE-smith task construction; Rubrics as Rewards sections 2–3; reward overoptimization; [HUD](studies/hud-task-design.md) and [Gottlieb](studies/eli-gottlieb-reference.md) | Which E1 errors could make optimization reward the wrong behavior? |
| 5 | [Tmax](https://arxiv.org/abs/2606.23321) before [AES](studies/autoenvscaling.md); AES sections 3–4 and appendices G–H; POET overview | What does adaptation add over static generation, and at what total cost? |
| 6 | [RLTL;DR](studies/rl-tldr.md) sections 4–6; [Recursive Self-Rewrite](studies/recursive-self-rewrite.md) sections 2 and 3.5–3.6; Reflexion | Which improvements come from weights, feedback, or context? |
| 7 | [Third Moment Research](studies/third-moment-research.md), [ApprenticeBench](studies/apprentice-bench.md), and [Impersona-Env](studies/impersona-env.md) | What would the chosen buyer purchase, and how would they accept it? |
| 8 | Harbor task and verifier docs; one of verl or SkyRL; AES code only if reuse is proposed | What must our task package supply, and which interfaces can we reuse? |

Use the other [study notes](studies/README.md) as targeted comparisons. For each session, answer one question in writing using one artifact: a trajectory, reward calculation, code path, or customer workflow. Record conclusions in the owning document.

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
