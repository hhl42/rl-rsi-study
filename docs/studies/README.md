# Study notes

These notes explain what each reference contributes, what it does not establish, and what we should check next. Start with the [guided learning path](foundations.md), use the [survey](../02-survey.md) for shared concepts, and follow the [study plan](../01-study-plan.md) toward experiments. Reading a note does not complete a paper review or reproduce a result.

The [source register](../../references/README.md) owns bibliographic details and review depth. Keep one note per source so later reviews have a stable home. Page format does not determine evidence quality: several pages below are original research or first-party product reports.

## Foundations and priority studies

| Note | Main question | Main takeaway |
| --- | --- | --- |
| [Guided learning path](foundations.md) | What should a systems team learn, how deeply, and in what order? | Start with online explanations and videos; use observable outputs to decide when to move on. |
| [AutoEnvScaling](autoenvscaling.md), with [code walkthrough](autoenvscaling-code.md) | How does adaptive task generation work, and which contracts does the preview actually enforce? | Adaptation can improve useful rollout yield; validate quality independently. |
| [Third Moment Research](third-moment-research.md) | What does a managed agent-improvement business offer? | The managed product and internal research case provide different evidence. |

## Other supplied papers

| Note | Main question | Main takeaway |
| --- | --- | --- |
| [RLTL;DR](rl-tldr.md) | Can feedback become a compact training asset? | Useful feedback and selected successes can both become training assets. |
| [Recursive Self-Rewrite](recursive-self-rewrite.md) | Can successes under different harnesses become reusable demonstrations? | Fresh replay turns private guidance into public demonstrations, with leakage checks. |

## Other supplied pages

| Note | Main question | Main takeaway |
| --- | --- | --- |
| [TypeSafe and Jev](typesafe-jev.md) | What changes when the product makes structured decisions? | A valid output format does not ensure a correct decision. |
| [MiMo RL](mimo-rl.md) | What does integrating tasks, rewards, and large-scale training require? | Open environments provide reuse candidates; integration and training remain substantial work. |
| [ApprenticeBench](apprentice-bench.md) | How should we evaluate an agent learning a job across tasks? | Persistent knowledge changes what an evaluation must reset and retain. |
| [Raven](raven.md) | How does harness improvement differ from weight training? | Harness changes and model-weight changes need separate evaluation. |
| [Harness²](harness2.md) | How can execution evidence guide harness edits and reusable lessons? | Fixed model weights can support an improvement loop; selection and stored lessons still need independent evaluation. |
| [AutoBenchmark](autobenchmark.md) | What can automated benchmark construction do, and where does human direction help? | Harder generated tests still need independent correctness checks. |
| [Impersona-Env](impersona-env.md) | Can a simulated user supply useful preference feedback? | One simulated user and one human voter give limited transfer evidence. |
| [HUD task design](hud-task-design.md) | What makes a task meaningful, reproducible, and fairly graded? | Judge real outcomes; measure difficulty for a specified agent setup. |
| [Agentic RL Part II](agentic-rl-part-ii.md) | Which task and feedback patterns should we investigate? | Use as a map of ideas to verify in primary sources. |
| [Agentic RL Part III](agentic-rl-part-iii.md) | How do rollouts, rewards, and distributed training connect? | Inspect the task-to-trainer boundary before selecting a distributed system. |
| [Eli Gottlieb on task factories](eli-gottlieb-reference.md) | How can expert feedback improve tasks and the process that produces them? | Expert reasons can improve task production; isolation needs its own checks. |

The notes' proposed checks are candidates. [Progress](../progress.md) owns the active worklist; adding a note does not commit the team to running every proposed experiment.
