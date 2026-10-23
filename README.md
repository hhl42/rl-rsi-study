# RL and RSI study

RL means reinforcement learning. RSI means recursive self-improvement: earlier improvements help produce later ones.

We are studying how to create tasks, environments, and feedback that improve AI agents. The team has deep systems experience and already builds AI projects. Our ultimate goal is a commercial product. Our current work is study and exploration: understand the field, identify a customer problem, and test a small number of opportunities before committing to a product.

**Start with [Goals and scope](docs/00-goals.md).** It owns the project's direction. AutoEnvScaling and Third Moment Research are the first detailed studies, but they do not define the limits of the search.

## Start here

Read [Goals and scope](docs/00-goals.md) and [Progress and decisions](docs/progress.md) for direction and current state. The [study guide](docs/01-study-plan.md) organizes readings and videos into phases: models and agents, task quality, training, concrete improvement systems, and commercial offerings. It identifies useful sections and optional depth for engineering leaders.

Consult [Foundations](docs/studies/foundations.md) for concept reminders and optional papers, the [survey](docs/02-survey.md) for explanations, and the [opportunity comparison](docs/03-opportunities.md) for candidate buyers. [Research experiments](docs/experiments.md) preserves proposals to select when project questions warrant them.

Use the [document map](docs/README.md) to find the file that owns a question. The [source register](references/README.md) is a library with review depth, not a mandatory reading list.

## Priority studies

- [AutoEnvScaling](docs/studies/autoenvscaling.md): how an agent generates and calibrates training environments.
- [Third Moment Research](docs/studies/third-moment-research.md): its public offering and what we need to understand about the business.

The [study index](docs/studies/README.md) also covers the other references, including [Harness²](docs/studies/harness2.md), a comparison that improves execution software and stored lessons with fixed model weights. Notes distinguish source findings, our interpretations, and checks still needed.

## Working in this repository

GPT/Codex and Claude use the shared rules in [AGENTS.md](AGENTS.md). [CLAUDE.md](CLAUDE.md) imports that file. Humans can use the same rules for evidence and writing.

Useful findings, decisions, experiment designs, and unresolved questions belong in the repository. Chat history and agent memory are not the project record. Follow the [research method](docs/research-method.md) when adding evidence.

This repository is readable without a sibling checkout, an AI subscription, or a GPU. The related `ai-data-research` project develops codebase Q&A tasks. Its reusable ideas are summarized here; its private files and task packages are not copied here.

Use the [glossary](docs/glossary.md) for unfamiliar terms and [progress](docs/progress.md) for completed work and next actions.
