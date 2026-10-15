# Market scan for RL environments and managed improvement: 2026-10-14

**Question:** Who sells RL environments, task data, managed training, and sandbox infrastructure today? Who buys, at what price, and what risks do commentators name?

**Method:** a research agent searched public web sources on 2026-10-14 for the [Claude review](../../reviews/claude-init-review-1.md#41-a-market-map). Claude re-checked the Epoch AI survey, the MiMo release, OpenAI's fine-tuning notice, and the Third Moment Research pages. Everything else is as reported by press, analysts, or the companies. Some pages blocked automated access (OpenAI's blog, finsmes), and The Information is paywalled; claims that depend on them rest on secondary coverage.

**Status:** an unverified starting list for the [opportunity comparison](../../03-opportunities.md). It is not a market census. Funding and revenue figures are company claims or press reports. Marketplace revenue is often gross, including contractor pay.

## Price and buyer evidence

- **Epoch AI** ([2026-01-12](https://epoch.ai/gradient-updates/state-of-rl-envs), 18 interviewees, re-checked): most per-task prices US$200–2,000, US$20k rare; contracts often six to seven figures per quarter; exclusivity costs about four to five times more; "substantially more in-housing" by labs; robustness against reward hacking ranked as the top quality criterion.
- **SemiAnalysis** ([2026-01-06](https://newsletter.semianalysis.com/p/rl-environments-and-rl-for-science)): more than 35 vendors, almost all seed stage, under 20 staff, with one to three customers; a website replica costs about US$20k.
- **TechCrunch** ([2025-09-21](https://techcrunch.com/2025/09/21/silicon-valley-bets-big-on-environments-to-train-ai-agents/)), citing The Information: Anthropic leaders discussed spending more than US$1B on RL environments over a year. Not confirmed by Anthropic. The AES paper cites this article.
- **Mechanize** ([2025-08-18](https://www.mechanize.work/blog/cheap-rl-tasks-will-waste-compute/)): argues that tasks under about US$500 waste compute. A vendor's argument, not a measurement.

## Environment and task vendors

| Company | Sells | Reported buyer | Reported funding or event |
| --- | --- | --- | --- |
| Mechanize | High-fidelity coding and office environments | Labs | Google DeepMind license-and-hire, 2026-09 |
| Fleet | Enterprise-app replicas and SDK | Labs | Seed; talks at about US$750M valuation (unconfirmed) |
| Deeptune | Workplace-software replicas | Labs | Acquired by Mercor, 2026-07-09 |
| Halluminate | Computer-use environments, finance focus | Labs (company claim) | US$30M Series A, 2026-10 |
| HUD | SDK, hosted platform, environment marketplace | 50+ businesses (company claim) | US$16M, 2026-06 |
| Bespoke Labs | Enterprise simulations; open-source Curator | Labs, enterprises | US$40M seed and Series A, 2026-07 |
| Veris AI | Enterprise sandboxes with mock SaaS and simulated users | Enterprises | US$8.5M seed, 2025-06 |
| Prime Intellect | Environments Hub (2,500+), `verifiers`, prime-rl, compute | Startups, enterprises | US$130M Series A, 2026-07 |
| Scale, Surge, Mercor, Snorkel, Turing, Invisible, Handshake | Expert data, now also RL environments | Labs | Large data-labelling firms entering the market |

Acquisitions and license-and-hire deals in about 15 months: Rubrik–Predibase, CoreWeave–OpenPipe, Datadog–Adaptive ML, Mercor–Deeptune, Google DeepMind–Mechanize.

## Managed training and improvement

| Offering | What it is | Reported status |
| --- | --- | --- |
| OpenAI reinforcement fine-tuning | RL fine-tuning on an OpenAI model | Self-serve fine-tuning is being wound down; closed to new users since 2026-05 ([OpenAI guide](https://developers.openai.com/api/docs/guides/rft-use-cases)) |
| Applied Compute | Engineers placed with the customer plus its own RL stack | Raised US$80M, 2026-04 |
| Thinking Machines Tinker | Training API for open-weight models | Generally available 2025-12 |
| CoreWeave (OpenPipe ART, serverless RL) | Open-source agent RL and managed RL | OpenPipe acquired 2025-09 |
| Fireworks, Together | RL training APIs on open models | Fireworks moved managed RFT to a training API |
| AWS Bedrock RFT, Nova Forge | Managed RFT that can train on stored Bedrock request logs | Launched 2025-12 |
| Mistral Forge | Full model lifecycle with engineers placed with the customer | Launched 2026-03 |
| Third Moment Research | Managed OpenAI-compatible endpoint with RL post-training | No pricing, customers, or funding found; see the [study](../../studies/third-moment-research.md) |

## Formats and trainers

Harbor (Laude Institute; used by AES and Terminal-Bench), Prime Intellect `verifiers`, OpenEnv (Meta, Hugging Face, and a governing committee), and NVIDIA NeMo Gym all define environments. Trainers include verl, slime, Miles, SkyRL, prime-rl, rLLM, AReaL, TorchForge, and NeMo RL. Several trainers ship adapters for more than one format.

## Sandbox and rollout infrastructure

Modal (reports that sandboxes are more than a third of revenue), Daytona, E2B, Runloop, Morph Cloud, CoreWeave Sandboxes, Docker Cloud Sandboxes, and AWS Strands Box sell isolated execution for agents. The agent found no funded startup focused only on RL-environment containment; that is a gap in the search, not proof that none exists.

## Named risks

- **Few buyers and in-housing:** SemiAnalysis and Epoch, above.
- **Commoditization:** [Wing VC](https://www.wing.vc/content/who-will-win-the-rl-environment-market--and-why) (2026-01) and [B. Anderson](https://benanderson.work/blog/dont-build-rl-env-startup/) (2025-09); Wing and others also argue that real workflows stay custom.
- **Quality:** N. Lambert ([Interconnects, 2026-10-09](https://www.interconnects.ai/p/i-expect-rapid-progress-but-not-towards)) says much purchased environment work is poor, yet labs still see a return.
- **Reward hacking spreading to other behavior:** Anthropic and Redwood, [arXiv 2511.18397](https://arxiv.org/abs/2511.18397).
- **Sandbox escape:** the 2026 OpenAI–Hugging Face incident; see the review's [section 4.2](../../reviews/claude-init-review-1.md#42-environment-security-and-the-2026-openaihugging-face-incident).

## Further sources from the scan (not reviewed)

[Mercor–Deeptune](https://www.mercor.com/blog/mercor-to-acquire-deeptune/), [HUD funding](https://www.hud.ai/blog/announcing-16m-series-a), [Prime Intellect funding](https://www.intelcapital.com/prime-intellect-raises-130m-series-a-to-build-the-open-superintelligence-stack/), [Scale RL environments](https://scale.com/rlenvironments), [Applied Compute](https://www.appliedcompute.com/company/the-advantage-you-own), [Mistral Forge](https://mistral.ai/products/forge/), [AWS Bedrock RFT](https://aws.amazon.com/about-aws/whats-new/2025/12/bedrock-reinforcement-fine-tuning-66-base-models), [CoreWeave–OpenPipe](https://coreweave.com/news/coreweave-to-acquire-openpipe-leader-in-reinforcement-learning), [Modal Series C](https://modal.com/blog/modal-series-c), [Daytona Series A](https://www.daytona.io/dotfiles/daytona-raises-24m-series-a-to-give-every-agent-a-computer), [CoreWeave Sandboxes](https://www.coreweave.com/news/coreweave-sandboxes-launches-to-accelerate-reinforcement-learning-agent-tool-use-and-model-evaluation), [OpenEnv](https://huggingface.co/blog/openenv), [NeMo Gym](https://github.com/NVIDIA-NeMo/Gym/releases), [Miles v0.1](https://www.lmsys.org/blog/2026-08-18-miles-v0-1/), [Marin trainer comparison](https://github.com/marin-community/marin/issues/6162), [Cloud Security Alliance note](https://labs.cloudsecurityalliance.org/research/csa-research-note-openai-artifactory-sandbox-escape-20260730/), [Fortune on a second pause](https://fortune.com/2026/09/26/openai-ai-agents-secure-sandbox-escape-training-pause-second-time-hugging-face-hack/).
