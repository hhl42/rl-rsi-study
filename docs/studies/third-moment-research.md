# Third Moment Research business study

Third Moment Research is a useful case for comparing a task supplier with a managed improvement service. Our aim is to understand the customer problem and delivery requirements, then test whether a narrower opportunity fits this team.

Sources checked on 2026-10-14 describe three different things. Keep their evidence separate.

## Public offering

The [company product site](https://thirdmomentresearch.com/) advertises managed, OpenAI API-compatible endpoints tailored to a customer's workflow. It describes collecting trajectories, diagnosing failures, having the customer choose issues to fix, and returning an improved endpoint with evaluation results. Serving, RL post-training, harness changes, and versioning are advertised parts of the service. This establishes an offer, not measured customer outcomes.

## Internal research described by OpenAI

The [OpenAI case study](https://openai.com/index/third-moment-research/) describes agents improving a baseline trading system built by Third Moment's own engineers. It reports 10,000 concurrent agents and research sessions of 36–48 hours, using OpenAI models and Codex. Its concrete examples concern faster backtesting, changes to the surrounding harness, and environment security testing. It does not document customer endpoint results or a customer model-weight update. Its scale claims concern internal research, not adoption or revenue for the advertised service.

## Hiring evidence and remaining gaps

The [careers page](https://thirdmomentresearch.com/careers/) asks for experience post-training open-weight models of at least 8B parameters and names SkyRL and Miles. This supports an interest in operating a training stack. An open-weight implementation of the endpoint service is a plausible inference, but the page does not identify the deployed models or connect them to the OpenAI case study.

The reviewed pages do not establish prices, named endpoint customers, contract economics, data ownership terms, or independently measured improvement. OpenAI API compatibility describes an interface; it does not identify the model provider or training method.

## Business interpretation

Our inference is that a managed offering sells responsibility for an improvement process as well as software. A potential customer wants a recurring failure reduced without staffing every part of diagnosis, evaluation, training, and operation. The amount of expert work required per customer would strongly affect the economics.

This suggests two different opportunities to compare. A task supplier serves a team that already has a training or evaluation system. A managed improvement provider serves a team that wants a better application outcome. The second has more delivery obligations. Neither is established as the better fit for us.

## Questions that could change our decision

| Question | Why it matters | Evidence to seek |
| --- | --- | --- |
| Who owns the problem and budget? | Users, application owners, and model teams can have different priorities. | Buyer interviews and existing spending |
| Which failures are expensive and frequent? | Rare impressive examples may not justify ongoing cost. | Representative workflow records and failure accounting |
| Can the work be replayed? | Missing external state can make tasks costly to reconstruct. | A permitted sample and a replay prototype |
| Can success be checked independently? | Training and acceptance against the same weak judge can conceal defects. | Expert labels, business outcomes, or separate checks |
| What can be reused across customers? | One-off integration work can dominate delivery. | Time spent on a second workflow or customer |
| What data can be retained and reused? | Access and usage rights affect both product feasibility and lasting advantage. | Actual customer requirements and contractual terms |
| Who operates the improved system? | Hosting, support, latency, and rollback affect cost and liability. | A bounded service specification |

These are questions for our market study, not claims about deficiencies in Third Moment Research.

## A narrow offer to investigate

One hypothesis is a service that turns a customer's recurring engineering-agent failures into reproducible tasks with independently checked outcomes. An initial deliverable could include a small task set, failure analysis, and a measured comparison of the current agent with one bounded improvement.

Its value would depend on the customer: a training team might pay for usable environments, while an application team might require a reduction in escalation or rework. The acceptance metric must be chosen with that buyer. Do not assume that selling more tasks is the right unit.

Before proposing production operation or training at scale, establish data access, replay cost, grader reliability, and willingness to pay. Compare the offer with the customer's internal tools and other suppliers. The [commercial opportunity matrix](../03-opportunities.md) owns the broader comparison.
