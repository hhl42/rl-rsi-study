# Commercial opportunities

The eventual product must solve a customer problem at a sustainable delivery cost. These are hypotheses, not selected products. [Goals](00-goals.md) defines the scope; [progress](progress.md) records decisions.

## Initial candidates

| Candidate | Potential buyer and problem | Deliverable to test | Main uncertainty |
| --- | --- | --- | --- |
| Specialized training tasks and environments | Model or post-training teams need useful practice in a domain | Versioned task packages, reliable rewards, provenance, and a training evaluation | Will they pay for capability beyond available data? |
| Verification and task-quality service | Training teams or environment suppliers cannot cheaply trust generated tasks | Independent checks, defect reports, and repaired packages | Is validation a separate budgeted need or an internal feature? |
| Workflow failure to task generation | Agent teams struggle to turn traces into repeatable tasks | Reproducible environments for a defined failure class | Can real workflows be reconstructed with acceptable effort and permissions? |
| Managed improvement for one workflow | Application owners need fewer agent failures | Improved agent configuration or model with independent acceptance results | Can integration, improvement, and support be profitable? |
| Environment execution infrastructure | Training and evaluation teams need many resettable, isolated runs | Measured improvement in startup, throughput, isolation, or cost within an existing runner | Which unmet requirement survives comparison with established sandbox providers? |
| Environment security and reward-hacking audit | Labs, environment vendors, or application teams need evidence that agents cannot bypass boundaries or grading | A scoped audit, reproducible failure cases, and verification of repairs | Will buyers fund an outside audit, and can we establish the necessary trust and expertise? |

The [Third Moment study](studies/third-moment-research.md) informs managed improvement; the [AES study](studies/autoenvscaling.md) informs task supply and execution efficiency. Their technical results and public offers do not establish demand for our version.

## Market map

Vendor and pricing entries below retain their 2026-10-14 check date. This is an initial comparison, not a live supplier ranking or market census. Company pages establish advertised offers; the entries do not verify customer outcomes. “No public price found” refers to the inspected source at that date. Refresh the relevant offer, price, and terms before a product or spending decision.

| Candidate and buyer | Named alternatives and possible workaround | Price evidence and implication |
| --- | --- | --- |
| Task supply → model/post-training teams | [Scale](https://scale.com/rlenvironments) advertises expert-built environments. [MiMo](studies/mimo-rl.md) releases environments. Internal task construction is another option. | No public Scale task price found. Open artifacts raise the question of what a buyer needs beyond generic supply; inspect licenses and quality before treating them as reusable. |
| Independent quality → training teams or suppliers | [HUD](https://www.hud.ai/research/what-is-a-good-task) describes task design and work with data vendors. Internal expert review and Harbor verifier tests can supply parts of the same function. | No standalone HUD audit price found. First establish whether buyers want a separate reviewer or expect QA within task supply. |
| Failures to tasks → agent/application teams | HUD's conversion of enterprise material is a direct comparator; customers can also build regression tasks themselves. | No public conversion price found. Compare reconstruction effort, permissions, and acceptance quality, rather than generated prompt count. |
| Managed improvement → application owners | [Third Moment Research](studies/third-moment-research.md), [Applied Compute](https://www.appliedcompute.com/company/fundraise), and an internal agent-engineering team. Applied Compute describes company-specific agents trained for enterprise workflows. | No public project price found on these pages. Compare onboarding, access to data, responsibility for regressions, and continuing support. |
| Execution → training/evaluation infrastructure teams | [Modal](https://modal.com/pricing), [Daytona](https://www.daytona.io/pricing), and a customer's own container workers. | Modal lists US$0.0000131 per physical CPU core-second and US$0.00000222 per GiB-second. Daytona lists US$0.0504 per vCPU-hour and US$0.0162 per GiB-hour. Physical cores and vCPUs are different units; storage, GPU, and other charges are additional. Benchmark a full workload before comparing cost. |
| Security audit → labs and environment suppliers | Internal security teams plus Harbor-based negative tests; Modal and Daytona supply infrastructure controls that may cover part of the need. These are substitutes, not verified independent audit offerings. | No comparable third-party audit price verified. First determine which checks customers already perform and whether independent evidence changes a purchase or release decision. |

[Epoch AI's January 2026 report](https://epoch.ai/gradient-updates/state-of-rl-envs), based on input from 18 people through nine calls and nine text/email exchanges, reports typical task prices of US$200–2,000, higher prices for exclusivity, and increased internal construction by labs. Respondents emphasize robustness against reward hacking. Rechecking the page on 2026-10-24 did not update that January evidence. Use it for buyer and quality questions; it supplies neither current quotes for our task family nor audited transactions.

### Additional supplier leads

Added on 2026-10-20 from the [earlier market scan](records/2026-10-14-market-scan/README.md): **Mechanize, Prime Intellect, Surge, Mercor, Snorkel, and Turing**. Their current task/environment offerings, prices, and fit are **unverified leads** in this map. Inclusion is not a supplier ranking or confirmation that they offer equivalent products.

Before ranking task supply, check relevant first-party product pages for the actual deliverable, target buyer, acceptance terms, and public pricing. The earlier scan's funding and acquisition claims remain unverified too. The narrower checked table above should not be mistaken for the full competitive set.

<a id="buyer-brief-for-m1"></a>

### Buyer evidence

Use a short, sourced brief to support a provisional buyer choice. Add it here for each serious candidate, using these fields:

- Buyer role, recurring failure, current workaround, and named alternatives.
- Proposed deliverable and measurable acceptance criteria.
- Reported prices, source dates, and what the prices cover; unknowns remain explicit.
- Permitted examples and reachable roles. Keep private contact details in an approved location.
- Largest evidence gap, next check, and a condition that would reverse a provisional choice.

No buyer brief with confirmed team access is complete yet. Use public research to prepare it; customer contact requires separate direction.

## Choose the first buyer to study

| Buyer class | What they can buy | Evidence needed before choosing |
| --- | --- | --- |
| Model/post-training team | Tasks, rewards, trajectories, execution, or quality assurance | A reachable evaluator, a real capability gap, ingestion requirements, and access to downstream training evaluation |
| Application owner | Fewer failures in a recurring workflow | A reachable owner, permitted examples, measurable failure cost, and an acceptance test for improved behavior |

No team contacts, customer commitments, or training partner have been recorded. We should not pick a class from public vendor pages alone. First compare one accessible case from each class where possible. Prefer the class with a reachable buyer, permitted data, and a credible acceptance test. Record the choice and a reversal condition in progress; for example, switch if access or permissions fail while the other class provides a concrete pilot opportunity. Security and execution buyers may sit within either class.

## Candidate task domains

Codebase Q&A is the closest existing asset. Systems debugging and performance work fit the team's experience and may allow executable checks. Stateful business workflows require domain access and reliable simulation. Personalization adds data and evaluation requirements.

Compare domains by real examples, ability to judge outcomes, and reachable buyers. Quantitative finance should not become our domain merely because it appears in a company case study.

## Evidence needed before ranking

For each serious candidate, collect the current alternative, recurring failure costs, data access, acceptance criteria, integration effort, and budget process. Ask which parts customers build internally and which they would buy.

Check rights for each proposed input and output: customer data, source repositories, generated environments, model outputs, and derived trajectories. Record the provider, model, applicable agreement and date, intended downstream training or resale, and the buyer's intended use. Public research use does not establish commercial permission. Review the actual agreement and obtain legal advice when a concrete restriction or ambiguity affects a proposed product; do not assume one rule applies to every provider or contract.

Potential advantages include domain knowledge, authorized access to difficult cases, independent verification, and repeatable delivery. Each needs evidence. Producing many prompts or adopting a task format is a capability, not yet a reason customers will choose us.

## Questions for customer discovery

1. Describe the last agent failure that someone had to repair. How often does it happen, and who bears its cost?
2. What detects and fixes it today? Which internal tools or suppliers have you tried?
3. What traces, initial state, and outcome data could a pilot use, with what permissions?
4. What measurable improvement and regression limits would make the pilot acceptable?
5. Who approves and funds it? What purchase or deployment decision follows a successful pilot?

Ask about actual work before pitching our solution. Use the [research method](research-method.md#commercial-evidence) to record responses. Outreach and commitments require user direction.

## Cost model

Separate four cost layers:

| Layer | Include |
| --- | --- |
| Generation | Authoring inference, environment construction, and rejected candidates |
| Acceptance | Execution, calibration, independent review, verifier repair, and permission checks |
| Learning and evaluation | Solver rollouts, training updates, failed runs, and reserved-task evaluation |
| Delivery | Integration, hosting, monitoring, support, and recurring updates |

For task supply:

`cost per accepted task = total generation and acceptance cost / independently accepted tasks`

State the acceptance standard and report diversity and buyer relevance. Cheap duplicates can lower this ratio without adding value. AES's [generation-cost results](studies/autoenvscaling.md#4-what-the-results-establish) cover basic technical validity; they are not directly comparable to Epoch's reported customer prices. No margin estimate follows from subtracting one from the other.

For a managed service, subtract all four layers from customer revenue. Separate onboarding from recurring delivery and keep labor, volume, and price assumptions explicit. Execution products need cost per completed useful rollout, including startup, retries, and idle capacity; raw CPU prices alone cannot establish an advantage.

## Decision criteria

Proceed toward a bounded prototype when a specific problem, permitted data, independent acceptance test, plausible cost, and customer evidence justify it. Target the largest remaining uncertainty.

Narrow or reject a candidate when outcomes cannot be measured, access fails, existing tools meet the need, or support and review cost overwhelm the benefit. Build framework components that the selected experiments reuse. Decide later whether customers need the framework itself or only its outputs.
