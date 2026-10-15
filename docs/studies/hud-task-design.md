# HUD: designing a useful task

**Question:** How do we turn real work into a task with a clear, fair outcome check?

Source: HUD's [What is a good task?](https://www.hud.ai/research/what-is-a-good-task), page reviewed on 2026-10-14. This is practical guidance from an environment vendor, not a controlled study of training benefit.

## What the source contributes

HUD recommends starting from a real request, specifying the desired outcome, and supplying the files and tools needed to do the work. It emphasizes reproducibility and inspecting agent traces, including perfect scores that might hide shortcuts.

Difficulty should come from the work itself. Ambiguous instructions, irrelevant obstacles, or stricter grading added merely to lower scores can make a task less valid. The agent may take a different path from the reference solution and still meet the actual requirement. The article is guidance for task authors; it does not itself describe a model update or establish a training gain.

## Applying it to our team

Consider a proposed task to restore a service after a configuration error. We should state the required behavior and constraints: requests succeed, configuration survives a restart, and unrelated services still work. A check that merely looks for one expected command would reject other valid repairs and might accept an ineffective replay.

This example suggests a useful commercial question: can we convert a customer's failure into an executable acceptance test that the customer trusts? That may require more expert effort than generating the prompt.

## Next check

Apply [E1, verify the verifier](../01-study-plan.md#e1-verify-the-verifier), to one permitted workflow. Prepare a reference solution, a different valid solution, plausible failures, and a shortcut that exploits a superficial check. Have an expert inspect disagreements. Record what needed repair and the total authoring cost. Keep the result separate from any later claim that the task improves training.
