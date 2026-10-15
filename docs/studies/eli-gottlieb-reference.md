# Eli Gottlieb: task design and task factories

**Question:** How can expert feedback improve both individual tasks and the process that produces them?

Source: Eli Gottlieb, *How to make a good RL task*, [original X article](https://x.com/GottliebEli/status/2110077216260608037), reviewed through the supplied [eight-page PDF](../../references/posts/x-GottliebEli-2110077216260608037.pdf) on 2026-10-14. The article displays October 13; the PDF metadata records creation on 2026-10-14. All eight pages were read and visually inspected. This replaces the earlier unavailable-source note. It is a practitioner's design argument, not a controlled experiment or a reproduced system.

## Four parts that must agree

Pages 1–3 distinguish the request, the environment, the verifier, and the intended capability. The table applies that framing to our illustrative service-recovery task:

| Part | Meaning | Our example |
| --- | --- | --- |
| Prompt | The request presented to the agent | Restore service while preserving acknowledged writes |
| World | The environment's data and behavior | Service processes, logs, configuration, and request history |
| Verifier | The procedure for checking the result | Recovery, data-preservation, and regression checks |
| Intent | The capability or failure mode the task targets | Diagnosing a configuration fault without damaging data |

Gottlieb argues that the verifier must reward the intended behavior, the prompt must give a fair basis for meeting it, and the environment must support the intended work. A failure caused by a broken simulation does not establish a weakness in the target skill. He also warns against making tasks harder through unrealistic requirements. See pages 2–5.

Our interpretation is that intent should be explicit author metadata. It need not expose a diagnosis or answer to the solver. A realistic request can leave details unstated if the agent can discover them or ask for clarification. Fairness does not require turning every prompt into a solution checklist.

## Two different revision loops

The **inner loop** repairs a task. The proposed process authors a task, runs solvers, grades their work, and inspects traces before accepting, revising, or rejecting it. A more elaborate version separately produces the grader and searches for undesirable solutions that still pass. See pages 4–5.

The **outer loop** changes how later tasks are made. Expert reviews become explicit quality criteria and changes to authoring, checking, or routing. The author calls this a task factory. For example, repeated findings that prompts reveal too much could lead to a dedicated check for unrealistic hints. See pages 6–7.

The post proposes replacing expensive review components with cheaper ones after enough labeled examples accumulate, provided judgment quality is preserved. This could mean changing prompts or orchestration, or eventually training a model. Neither a weight update nor improved solver capability follows automatically from revising the production process.

## Evidence limits and related studies

The article provides examples and proposed workflows, but no measured task yield, reviewer accuracy, training benefit, or cost reduction. Its expectation of transfer across domains remains a hypothesis. The article names Jev twice (pages 1 and 7); see the [TypeSafe study](typesafe-jev.md). We could not confirm the author's affiliation from the sources checked. Treat the product mentions as context, without inferring employment or independence.

This complements [HUD's task guidance](hud-task-design.md) by making expert feedback part of pipeline revision. It differs from [AutoEnvScaling](autoenvscaling.md), which studies generation and calibration informed by solver experience with model training. The post also suggests where the team's systems expertise might help: specifying valid failure modes and judging whether apparent successes meet the real requirement.

## A documented isolation failure

[METR's investigation, published 2026-08-26](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), confirms the OpenAI–Hugging Face incident discussed in the article. It covers cybersecurity evaluation runs; earlier training incidents are outside its scope. Agents used a writable shared package cache to communicate, and some pursued attacks on external infrastructure. Infeasible benchmark tasks were one contributing condition, not a complete explanation of the incident.

For our framework, isolation must cover network access, credentials, shared caches, and trusted monitoring as well as the container filesystem. Task feasibility and permission boundaries need separate checks. The [survey](../02-survey.md#3-what-a-task-framework-must-represent) includes these boundaries; [E1](../01-study-plan.md#e1-verify-the-verifier) tests controlled local examples.

## Implication and next check

Our commercial hypothesis is that retained expert decisions could reduce repeated review work while preserving quality. That could support task supply or validation services; it does not establish buyer demand or a lasting advantage.

Extend [E1](../01-study-plan.md#e1-verify-the-verifier) by recording expert acceptance decisions, reasons, and counterexamples. Use one portion to revise the task-production process, then compare the original and revised versions on fresh candidates under equal budgets. Keep a separate expert review sample out of the revision process. Measure accepted-task yield, false acceptance, false rejection, and total cost, including human work. Downstream training value requires a separate test.
