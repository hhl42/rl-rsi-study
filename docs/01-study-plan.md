# Study and exploration plan

Use the study to choose a commercial opportunity and understand the framework it needs. [Goals and scope](00-goals.md) owns that objective. This plan combines learning, source analysis, customer research, and small experiments. Reading should resolve decisions rather than grow without a stopping point.

## Sequence and outputs

The initial planning estimate is six weeks with regular team participation. It is not a delivery commitment. Record actual availability and budgets in [progress](progress.md) before scheduling experiments. The phases can overlap, particularly public market research and technical reading.

| Phase | Work | Output and completion condition |
| --- | --- | --- |
| 1. Shared foundations, about one week | Learn the agent loop, training methods, rewards, and evaluation. Walk through one concrete task. | Each participant can explain what changes during learning, what a reward means, and how to test improvement on unseen tasks. |
| 2. Focused survey, about two weeks | Study AutoEnvScaling and Third Moment Research. Compare static generation, rubric rewards, and memory or harness improvement. | Survey v1 with source evidence, three opportunity hypotheses, and the unknowns that could change their ranking. |
| 3. Small experiments, about two weeks | Test verification, generation from failures, and one customer-relevant task family. | Reproducible results with full costs and a decision for each hypothesis. |
| 4. Commercial and architecture decision, about one week | Combine experiment evidence with customer evidence. Compare building with using existing tools. | A recommendation to proceed, narrow, change direction, or stop; a bounded next project if proceeding. |

For each study session, answer one question in writing and examine one concrete artifact: a task, reward calculation, trajectory, code path, or customer workflow. A short explanation by a teammate helps expose terms the group does not yet understand. Record useful conclusions in the owning document.

## Reading sequence

The [source register](../references/README.md) gives primary links and review depth. The foundation readings are selected passages, not a requirement to master every derivation.

| Order | Read | Question to answer |
| --- | --- | --- |
| 1 | Survey sections 1–3; Sutton and Barto chapters 1 and 3; ReAct | What are state, observation, action, policy, and reward in a terminal task? |
| 2 | InstructGPT overview; DPO introduction and method; DeepSeek-R1 overview | What different training assets do demonstrations, preferences, and RL require? |
| 3 | PPO sections 1–3; DeepSeekMath section 4; optional Sutton and Barto chapter 13 | How does a reward affect model weights? Why does variation across attempts matter? |
| 4 | SWE-bench and SWE-smith introductions and task construction; Rubrics as Rewards sections 2–3; reward overoptimization | What makes an evaluation or reward trustworthy, and what can go wrong when it is optimized? |
| 5 | AutoEnvScaling sections 3–4 and appendices G–H; POET overview | What must the environment generator know, and what evidence supports adapting tasks to a solver? |
| 6 | RLTL;DR sections 4–6; Recursive Self-Rewrite sections 2 and 3.5–3.6; Reflexion overview | Which improvements need weight updates, and which come from context, feedback, or harness changes? |
| 7 | Third Moment Research's site and case study; ApprenticeBench; Impersona-Env | What would a customer buy? How would we measure improvement in a real workflow? |
| 8 | Harbor task and verifier docs; one of verl or SkyRL | Which interfaces can we reuse, and what would we need to add? |

Keep TypeSafe, Raven, MiMo, and the Agentic RL articles as comparison and discovery material. Follow promising citations when they answer an open question. Do not let the newest source replace the foundations or customer investigation.

## Public research and customer discovery

Start the [opportunity comparison](03-opportunities.md) during phase 2. For each candidate, identify a user, a buyer, the current workaround, and why existing products may be insufficient. Include training teams buying environments and application teams buying more reliable workflows. These may require different products.

Prepare an interview guide using the questions in the opportunity document. Once outreach is authorized, seek concrete recent failures and their costs. Ask how a pilot would be accepted and funded. A public product page can suggest an offering; only customer evidence can establish demand for our version.

## Proposed experiments

These designs are starting points. Select the smallest subset that distinguishes the leading opportunities. A first pilot of roughly 10–20 tasks can estimate cost and reveal defects; it cannot establish broad training value. Include an existing Q&A task family where accessible and one systems task family with executable checks.

### E1 Verify the verifier

**Hypothesis:** We can produce tasks whose graders accept valid alternatives and reject meaningful errors with affordable human review.

Test reference solutions, independently written valid alternatives, plausible wrong solutions, empty submissions, and deliberate shortcuts. Where the grader is an LLM, include paraphrases and irrelevant verbosity. Where it runs tests, include test tampering and solutions that pass only the visible examples. Have a domain expert resolve a blinded sample without seeing the grader's verdict first.

Measure false acceptance, false rejection, repeatability, build and reset failures, review time, and cost per accepted task. Retain all rejected candidates in the accounting. Decide whether the verifier is usable, needs repair, or makes this task family too costly. Passing the reference solution and rejecting an empty solution are useful checks, but insufficient evidence alone.

### E2 Generate from solver failures

**Hypothesis:** Access to real solver failure traces helps a proposer generate more relevant, usable tasks than the same generation system without those traces.

Use the same proposer, tools, task seeds, admission checks, and budget in both arms. Change access to solver traces. Keep a static pool as a comparison. Hold the solver fixed initially so a changing model does not obscure the generator comparison.

Measure valid-task yield, failure-mode coverage, duplication, reward variation, human repair time, and total cost. Count calibration and rejected generation attempts. Evaluate with a solver that did not guide generation when feasible. This tests task production and relevance. Demonstrating training benefit requires a later weight-update experiment.

### E3 Use feedback effectively

**Hypothesis:** Structured feedback helps an agent recover from a specific failure at a useful cost.

Compare independent retries, retries with raw verifier feedback, and retries with a short generated insight. Match total inference and environment budgets, including insight generation. Keep the task, model, and tools fixed. Inspect traces to distinguish useful guidance from leaked answers.

Measure success, total cost, latency, and repeated failure types. Test transfer of reusable feedback to reserved related tasks separately. Improvement with feedback in context is evidence about assisted solving, not proof that model weights learned anything.

### E4 Test a commercial offer

**Hypothesis:** A named buyer values the measured improvement enough to pay for a repeatable deliverable.

Prepare a small offer for the most promising task family: defined input data, output, acceptance criteria, price hypothesis, and delivery cost. Compare it with the customer's current method. Test the offer through authorized interviews or a pilot. Do not treat a task-count target or enthusiastic feedback as willingness to pay.

## Evaluation and resource boundaries

Reserve evaluation repositories or task families before tuning generation. Keep all variants of a parent task in the same split. Keep development feedback separate from final evaluation. Compare model, harness, tools, attempt budget, and compute; report differences that remain.

Choose resource caps after measuring a small pilot. Include API inference, environment execution, grading, calibration, failed attempts, and human work. Full AutoEnvScaling training is not required for the first experiments. A later training partner or bounded open-weight run can test whether the selected assets improve unseen-task performance.

## Decision at the end of the cycle

Choose one opportunity only when we can explain its customer benefit, evidence, delivery cost, and remaining risk. Sketch the minimum reusable interfaces after comparing actual task families. If customer access or data rights are missing, narrow the next phase to resolving that gap. If independent evaluation rejects the technical benefit, change the hypothesis rather than expanding infrastructure.
