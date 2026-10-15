# Raven: harness and orchestration improvement

**Question:** Which improvements can come from the software around a model?

Source: the [EverMind-AI/Raven README](https://github.com/EverMind-AI/Raven), inspected on 2026-10-14. The project describes itself as pre-alpha. No implementation revision has been audited or run here; the observations below concern the README.

## What the source describes

Raven presents an orchestration layer for specialized agent harnesses, shared memory through EverOS, and a process for proposing, evaluating, and adopting harness changes. Its examples emphasize persistent collaboration and extended projects.

The advertised improvement targets include orchestration, memory, and harness behavior. This does not establish that model weights change. Showcases of completed projects also do not isolate the contribution of each component or provide a controlled comparison at equal cost.

## Implication for our exploration

Our hypothesis is that a customer may benefit from better recovery and tool coordination before needing additional model training. The same task suite could compare these interventions. It would have to record both the model version and the harness version, since either can change results.

This is relevant to a managed improvement business: accepting a proposed harness revision requires evidence that it fixes the target failure without causing unacceptable regressions elsewhere.

## Next check

Select and record a code revision, then trace one proposed change from evaluation to adoption or rejection. Check which evidence the proposer sees and which evaluation tasks remain reserved. On a small task set, compare one fixed model under the original and revised harness with equal resource limits. Record regressions and rollback behavior. That test would assess a bounded harness change, not establish general recursive self-improvement.
