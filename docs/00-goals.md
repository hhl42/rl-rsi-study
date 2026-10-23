# Goals and scope

We want to build a commercial product that helps AI agents improve through better tasks, environments, or feedback. We first need to understand the technical choices and find a customer problem worth solving. This document owns that direction. It can change as we learn.

## Current objectives

1. Build enough shared AI knowledge to assess research and implementation claims without depending on terminology or headline scores.
2. Identify a small number of commercial opportunities that fit our systems experience, access to data, and ability to reach customers.
3. Understand the reusable task framework each opportunity needs. Test the difficult assumptions before building a general framework.

The immediate output is a survey supported by source notes, an opportunity comparison, and small experiment designs. Completing a survey is progress toward a decision. It is not the ultimate measure of success.

The team brings deep systems expertise and hands-on AI project experience. Use a focused reading and viewing guide to fill AI-specific gaps, beginning with high-level online explanations and videos. Study task and evaluation contracts deeply and training mechanisms enough to assess data requirements and results. Optimizer theory and training infrastructure become priorities when a project needs them. The [study guide](01-study-plan.md) owns the sequence and optional depth; practical work follows research and product questions.

## What success would mean

At the end of the first exploration cycle, we should be able to name:

- A target user and buyer, a recurring problem, and the alternative they use today.
- A proposed deliverable and a measurable benefit to that customer.
- The task and data pipeline needed to deliver it, including how outcomes are checked.
- The evidence supporting the proposal, its largest remaining uncertainty, and an affordable test of that uncertainty.
- A reason to build, narrow the scope, pursue a different opportunity, or stop.

We should understand both technical feasibility and whether delivery could be repeatable and profitable. A publication or benchmark improvement alone does not establish either customer demand or sustainable economics.

## Scope of this exploration

Study task generation, environment construction, reward and feedback design, trajectory collection, evaluation, and curricula. A trajectory is the sequence of an agent's actions and the environment's responses. A curriculum is the selection and ordering of tasks used during learning.

Study enough supervised fine-tuning and reinforcement learning to understand how these assets are consumed. Include improvements to memory and agent harnesses, since these may provide customer value without changing model weights. A harness is the software that controls the agent's tools, context, execution, and recovery.

Investigate commercial forms such as task datasets, executable environments, validation services, and managed agent improvement. These are candidates, not selected products. The framework may become an internal production system, a customer-facing product, or a component of a service.

Large training runs, a production platform, and a sales launch are later decisions. Small prototypes belong here when they answer a specific research or commercial question.

## Initial priorities and breadth

AutoEnvScaling is our first detailed systems study. Third Moment Research is our first detailed business study. Their mechanisms and claims should guide questions, not become assumptions about what we must build.

Compare them with earlier RL methods, static task generation, rubric rewards, memory-based learning, and alternative commercial offerings. Explore at least one opportunity outside repository Q&A. Systems debugging and performance work are an initial hypothesis because the team understands that work; access to real customer problems must still be established.

## Relationship to the existing project

The related `ai-data-research` repository develops codebase Q&A tasks with private author evidence and rubric-based grading. Its documentation separates task quality, grading reliability, and training usefulness. It currently treats model training as a downstream activity.

We can learn from its task packaging, author and solver separation, negative controls, and operational experience. The team also identifies `taskgen-codebase-qa` as current hands-on AI work. This repository owns the broader exploration and should be understandable without access to sibling projects. Do not assume an existing task family is the best commercial direction, or that its assets may be redistributed.

## Constraints and assumptions to resolve

Systems expertise and hands-on AI engineering do not imply equal familiarity with every RL method. Use optional depth to address the relevant gaps. Compute budget, customer access, data permissions, and potential training partners still need to be recorded in [progress](progress.md) as they become known. The reading guide requires no GPUs.

Revisit the scope when customer evidence changes the problem, an experiment rejects a key hypothesis, or the user changes priorities. Record the reason in [progress](progress.md), then update this document and affected plans. Preserve the reasoning so a fresh reader can understand the choice.
