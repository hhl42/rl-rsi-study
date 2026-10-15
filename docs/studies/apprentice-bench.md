# ApprenticeBench: learning a job across tasks

**Question:** How should evaluation change when an agent retains experience from earlier work?

Sources: NeoCognition's [ApprenticeBench article](https://neocognition.io/blog/apprentice-bench) and [benchmark site](https://apprenticebench.com/). Browser overview and setup reviewed on 2026-10-14. Full results, scoring, and implementation remain unaudited.

## What the source describes

The benchmark simulates accounts-payable work for a construction company using Odoo. An agent receives historical records, handles a sequence of bills, and receives feedback that becomes less detailed after the initial tasks. It must use company conventions and adapt as policies change.

Persistent memory allows information from earlier work to affect later decisions. The setup therefore evaluates learning through experience and context; that alone does not demonstrate model-weight updates. Its simulated business workflow should not be described as a measured customer deployment.

## Implication for our exploration

Our hypothesis is that some systems tasks should form a sequence. An on-call assistant may need to remember a prior incident, a temporary workaround, or a change in service ownership. Resetting everything after each task could remove the behavior we want to measure.

A framework would need to distinguish state that resets per attempt from state that persists across tasks. Evaluation would also need to separate useful transfer from repetition of the same answer. Task order becomes part of the experiment configuration.

## Next check

Inspect one complete task sequence and its scoring rules. Design a small incident sequence with an explicit policy change. Compare the same agent with no persistent notes, its own notes, and expert-written notes. Reserve different incidents for the later evaluation. Measure recurring errors and the cost of maintaining memory, alongside success. This would test memory usefulness; a separate experiment would be needed to test weight learning.
