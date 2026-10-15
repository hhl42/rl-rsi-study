# AutoBenchmark: generating evaluations with human direction

**Question:** Can an agent construct a difficult, valid benchmark, and what does human expertise contribute?

Source: Meta RAM's [AutoBenchmark: benchmark creation & the role of humans](https://facebookresearch.github.io/RAM/blogs/autobench/), method and setup reviewed on 2026-10-14. No generated package or result has been reproduced here.

## What the source describes

A research agent chooses a capability to measure and constructs a runnable Harbor-compatible benchmark. Solvers attempt it, while separate review steps assess benchmark quality. Among accepted revisions, the loop retains the one with the lowest solver score. External solvers are evaluated without feeding their results back to the generator.

The study varies human direction from none to detailed initial and iterative feedback. It reports that detailed direction helps produce harder benchmarks. The same model serves several proposing and judging roles, leaving correlated mistakes as a concern. External solver scores check a different aspect than independent validation of task correctness.

The artifact being improved is the benchmark. The page does not establish that training on its tasks improves a solver's weights.

## Implication for our exploration

Our inference is that domain expertise may be useful in specifying what a task should measure and supplying reliable evidence. This is a plausible advantage for a systems team, but its value needs measurement.

Compare this with [AutoEnvScaling](autoenvscaling.md): selecting a difficult evaluation and selecting a useful training task are different objectives. A task that every solver fails may reveal a capability gap, yet provide little information to a particular training method.

## Next check

For one systems capability, compare a broad request with an expert-written specification under the same generation budget. Review correctness and relevance before comparing difficulty. Test with a solver whose traces did not guide construction. Count expert effort and rejected tasks. Only a later learning experiment can establish whether the accepted tasks are useful for training.
