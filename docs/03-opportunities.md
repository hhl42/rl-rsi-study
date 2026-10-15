# Commercial opportunities

The eventual product must solve a customer problem with a delivery cost the business can sustain. This document compares hypotheses; no opportunity or business model has been selected. The [goals](00-goals.md) define the scope, and [progress](progress.md) records decisions.

## Initial candidates

| Candidate | Potential buyer and problem | Deliverable to test | Main uncertainty |
| --- | --- | --- | --- |
| Specialized training tasks and environments | Model or post-training teams need additional useful practice in a domain | Versioned task packages, reliable rewards, provenance, and a training evaluation | Will they pay for incremental capability beyond available data? |
| Verification and task-quality service | Teams cannot trust or cheaply audit their generated tasks | Independent checks, defect reports, and repaired task packages | Is validation a separate budgeted need or an internal feature? |
| Workflow failure to task generation | Agent teams have traces but struggle to turn failures into repeatable tests or training tasks | Reproducible environments built from a defined failure class | Can real workflows be reconstructed with acceptable effort and permissions? |
| Managed improvement for one workflow | Application owners need fewer agent failures without building a training team | An improved agent configuration or model with independent acceptance results | Can improvement and support be delivered repeatedly at a profit? |

The [Third Moment Research study](studies/third-moment-research.md) provides one public comparison for managed improvement. The [AutoEnvScaling study](studies/autoenvscaling.md) provides a mechanism relevant to environment supply. Neither establishes demand for our proposed offerings.

## Candidate task domains

Codebase Q&A is the closest existing asset. Systems debugging and performance work fit the team's expertise and may allow executable checks. Stateful business workflows broaden the search but require domain access and reliable simulation. Personalization introduces another set of data and evaluation requirements.

Compare these domains by available evidence and access, not apparent technical novelty. A promising domain needs real examples, a way to judge success, and a reachable buyer. We should not select quantitative finance merely because it appears in a company case study.

## Evidence needed before ranking

For each serious candidate, collect the buyer's current alternative, recurring failure costs, data access, acceptance criteria, integration effort, and budget process. Include internal construction, open-source tools, specialist providers, and broader platforms in the alternatives. The competitor and pricing review is still pending; the current matrix is not a market census.

Evaluate potential advantage in concrete terms. Domain expertise, authorized access to difficult cases, independent verification, and repeatable low-cost delivery are hypotheses worth testing. A generic agent wrapper or an ability to generate many prompts is not evidence of a lasting advantage.

## Questions for customer discovery

1. Describe the last case where the agent failed and someone had to repair the outcome.
2. How often does that class of failure occur, and who pays its cost?
3. What do you use to detect and fix it today? Where does that process fail?
4. What traces, initial state, and outcome data could a pilot use?
5. What would demonstrate a useful improvement, and what regressions would make it unacceptable?
6. Who would approve and fund a pilot? What happens if it succeeds?

Ask about actual work before describing our proposed solution. Record evidence using the [research method](research-method.md#commercial-evidence). Outreach and customer commitments require user direction.

## Cost model

For a task offering, estimate:

`cost per accepted task = total generation, execution, grading, calibration, review, and repair cost / accepted tasks`

Include rejected candidates. Also report diversity and downstream usefulness, since cheap duplicates can make the cost figure look good without creating value.

For a managed service, estimate customer revenue less inference, environment compute, training, expert labor, integration, support, and recurring evaluation costs. Separate one-time onboarding from recurring delivery. Keep pricing, volume, and labor assumptions explicit. Public token prices alone cannot establish service margins.

## Decision criteria

Proceed toward a bounded prototype when we have a specific customer problem, evidence of willingness to pay, permitted data access, a credible independent acceptance test, and a plausible delivery-cost estimate. The prototype should target the largest remaining uncertainty.

Narrow or reject a candidate when the outcome cannot be measured, data cannot be obtained, existing tools meet the need adequately, or review and support costs overwhelm the expected value. A technically interesting result can still fail these tests.

The task framework should contain components reused by the selected experiments. Decide later whether customers need direct access to that framework or only its outputs.
