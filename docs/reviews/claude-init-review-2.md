# Claude review 2: changes since review 1

**Reviewer:** Claude (Opus 5.5), at the user's request, on 2026-10-20. **Scope:** the two commits after [review 1](claude-init-review-1.md): `4951e68` (GPT's [resolution](claude-init-review-1-resolution.md) of review 1) and `a9e3064` (the revised learning path and the Harness² study). I focused on the study plan, the [learning path](../studies/foundations.md), and the [Harness² note](../studies/harness2.md).

This review recommends; it does not decide. The team decides what to adopt, and [progress](../progress.md) records the decisions.

## Summary

1. **The response to review 1 is good work.** It adopts most recommendations and explains each decision. It also correctly fixes five points where review 1 overstated its evidence (section 2). The remaining disagreements are small.
2. **The new learning path is the right shape.** It starts with videos and plain explanations, sets a depth limit and a stopping point for each step, and treats papers as a library. It also derives what to learn from what the business must do. Section 3 sets out that reasoning from first principles and finds the plan mostly consistent with it.
3. **Five things are still missing from the learning path:**
   - It does not teach why an agent's results vary from run to run.
   - It gives no reading on reward hacking.
   - It builds the first task only at the last step.
   - It has no market track.
   - It assumes a real weight update must cost money.

   Section 3.3 explains each.
4. **Two links are wrong and better resources exist.** Section 4.2 suggests one sequence with a video, a reading, an exercise, and a stopping point for each step. Its new picks include Karpathy's 2025 "Deep Dive", a 60-line agent loop, Anthropic's January 2026 article on evaluating agents, METR on reward hacking, and Epoch AI on the environment market.
5. **The Harness² note is accurate but shows only the best case.** Its mechanism and numbers check out. It omits the paper's weaker results, a one-time offline harness search that nearly matches Harness², a retry baseline, and the share of the gain that comes from the lesson library (section 5).

## 1 What I checked

| Area | Method | Result |
| --- | --- | --- |
| All files changed since review 1 | Read the diffs and the new files in full | Sections 2, 3, and 6 |
| The resolution's corrections to review 1 | Compared each with the paper or the AES code | All five corrections accepted (section 2) |
| Harness² note and demo record | An agent compared every claim with the paper and the pinned code and re-ran the demo; I re-checked Tables 1–3, the Figure 6 text, and the selection fallback | Accurate core; five corrections; important omissions (section 5) |
| Learning-path links | An agent opened every link; I opened the top new recommendations | Two links to fix (section 4.1) |
| New resources | An agent searched and opened candidates; I opened six of them | Suggested sequence (section 4.2) |
| Local links | Script over all Markdown files | Reported in section 7's validation line |

I did not run a model, a notebook, or a training job, and I did not watch the videos.

## 2 The response to review 1

The [resolution](claude-init-review-1-resolution.md) is careful. It implements most recommendations, explains each decision, and corrects review 1 where review 1 went beyond its evidence. The changes I spot-checked are accurate: the separated Third Moment sources, the added AES results, the RL row and worked training step in the survey, the isolation row, the E1 error checklist and measures, and the glossary.

**Corrections to review 1 that I accept:**

| Review 1 said | The resolution's correction | My view |
| --- | --- | --- |
| Appendix H's interval suggests AES's 4.3-point gain is within noise | That interval belongs to a different comparison and cannot bound Table 3 | Correct. The uncertainty is unknown, not shown to be large. |
| AES decides "infrastructure failure" by matching error text | The classifier also uses the execution phase and exception type | Correct. `_is_infra` in `harbor_runner.py` checks phase and type first and uses text patterns as one rule among several. |
| The OpenAI–Hugging Face incident is the year's most important event for environment builders | A ranking is opinion; METR verifies the incident itself | Correct. |
| AutoBenchmark's outputs had no human validation | Too strong for the checked evidence | Correct. Review 1 relayed an agent's claim without checking it. |
| Recursive Self-Rewrite's 51 and 66 are task counts | The paper says they are rounded estimates from percentages | Correct. |

**Remaining points:**

1. **Keeping the nine short notes as separate files.** The resolution's reason is sound: one file per source gives later evidence a stable home. The new takeaway column in the [study index](../studies/README.md) removes most of the navigation cost. I withdraw this recommendation.
2. **The maintained market map is now too narrow.** Keeping only verified sources is good practice. But for task supply, the [market map](../03-opportunities.md#market-map) now names only Scale and MiMo's open release. Mechanize, Prime Intellect, Surge, Mercor, Snorkel, and Turing appear only in the unverified scan record. A reader of the opportunity document would underestimate the competition for task supply. List these names as unverified leads in the map, or check the four or five largest against their own pages.
3. **One new wording error.** The [AES results](../studies/autoenvscaling.md#4-what-the-results-establish) say AES "collects each update's rollouts 42% faster". The paper says 42% *less time*, which is about 1.7 times as fast. Use the paper's wording.

## 3 The study plan, from first principles

### 3.1 Start from what the business must do

Whatever the team eventually sells, the work has four parts:

1. **Build tasks.** Turn a target behavior into tasks that an agent can attempt many times, from a known starting state, inside a safe boundary.
2. **Judge outcomes.** Decide correctly whether an attempt succeeded, and make shortcuts fail.
3. **Show improvement.** Compare an agent before and after a change, fairly, on cases it did not train on, and report the cost.
4. **Deliver to whoever changes the agent.** A training team, a harness-editing loop such as Harness², or an application team uses the result. Someone must pay for it.

The knowledge the team needs, and how deeply, follows from these four parts:

| Part | What to learn | Depth | Reason |
| --- | --- | --- | --- |
| Build tasks | The agent loop; task packages (Harbor); reset; isolation | Expert. Containers, reset, and isolation are existing skills; the agent loop is new. | This is the product's core. |
| Judge outcomes | Test-based and model-based graders; shortcuts; reward hacking; impossible tasks | Expert | Buyers rank robustness against reward hacking first ([Epoch AI](https://epoch.ai/gradient-updates/state-of-rl-envs)). |
| Show improvement | Why agent results vary between runs; success rates; pass@k and avg@k; error bars; held-out splits; contamination | Working to expert | Every claim to a buyer depends on it. |
| Deliver | What SFT, preference training, and RL consume; group advantages; token masks; harness and memory changes | Working: explain it, and run one small example | Needed to specify interfaces and read a buyer's results. |
| Model internals | Transformers, pretraining, optimizer mathematics, distributed training | Awareness only | Needed only if the team itself trains models. |
| Market | Who buys, current alternatives, prices | Working | Needed to choose the first buyer. |

### 3.2 How the revised plan compares

The revised plan is much closer to this, and to what you asked for. Its "Why this order" section reasons from the product question. Its depth table puts the deepest learning at the task boundary and in evaluation. It asks for enough training knowledge to supply inputs and read results, and it makes infrastructure work conditional. Each learning step names one main resource, a video or text alternative, an exercise, a stopping point, and a depth limit. The papers are now a library to consult, not a reading list. These are the right choices, and I would keep them.

### 3.3 What is still missing or in the wrong place

**1. Randomness is never taught directly.** Systems engineers expect a test to give the same result every time. An LLM agent does not: the same task, model, and harness can pass on one run and fail on the next, because the model samples its output. This one fact explains why the field reports success rates, repeated attempts, pass@k, avg@k, calibration bands, and error bars. Step 1 should state it and include a two-minute exercise: send the same prompt five times and compare the answers. Step 3 should add a short resource on error bars (section 4).

**2. Reward hacking has exercises but no reading.** Step 3 asks for a shortcut that passes a health check, which is good. It gives no source showing how often and how inventively real agents find shortcuts. One or two readings (section 4) would show that this is the field's central practical problem, not an edge case.

**3. Building comes too late.** Step 3's exercise (a valid repair, a second valid repair, and a shortcut, with checks that separate them) is the first part of H1 written on paper. Step 6 then builds it in Harbor. Systems engineers learn faster by building, and the built task is reusable. Make H1's first task the step 3 exercise: write the task as a Harbor package with its reference, alternative, and shortcut solutions. No model is needed for this. Step 6 then becomes "run existing agents on three to five tasks."

**4. The market has no learning step.** The plan says buyer research runs alongside learning, but the learning path gives no resource or output for it. Add a parallel market track with two or three readings and one output: a one-page map of who buys environments, from whom, and at what price (section 4).

**5. Observing a real weight update need not cost money.** H2 is gated on a paid budget. Free notebook services can run a small RL fine-tuning example (GRPO on a small open model) in a browser. The team could see real rewards, advantages, and a before-and-after comparison at no cost (section 4). Keep the budget gate for anything larger.

**6. Three numbered sequences share step numbers.** The [plan](../01-study-plan.md) has learning steps 1–6 and decision steps 1–5, and [progress](../progress.md#next-work) has priorities 1–5. "Step 3" means different things in different places. Name them the way H1–H2 and E1–E4 are named, for example L1–L6 for learning and D1–D5 for decisions. Also, the plan's "Reading sequence" table repeats the six learning steps; the [learning path](../studies/foundations.md) should be their only owner.

## 4 Learning resources

### 4.1 Are the current links right?

A research agent opened every link in the [learning path](../studies/foundations.md) on 2026-10-20. All resolve, and the course lecture numbers and titles are correct. Two links point at the wrong material:

| Step | Problem | Fix |
| --- | --- | --- |
| 1 | The text alternative, the RLHF book's ["Training overview"](https://rlhfbook.com/c/03-training-overview), is about RLHF training recipes. It is not a general introduction to language models, so it does not replace the Karpathy video. | Move it to step 4. Use the short video in section 4.2 as step 1's alternative. |
| 6 | The [Harbor link](https://docs.harborframework.com/) goes to a landing page. | Link the [task format](https://docs.harborframework.com/tasks/overview) and the [create-a-task tutorial](https://docs.harborframework.com/tutorials/create-a-task) directly, plus the [terminal-bench-2 repository](https://github.com/harbor-framework/terminal-bench-2) for real examples. |

Two smaller improvements: link Lambert's lectures 11 and 12 as videos ([lecture 11](https://www.youtube.com/watch?v=GMry2DzC304), [lecture 12](https://www.youtube.com/watch?v=dFafQmClYq4)), as is already done for lecture 3. Karpathy's ["Intro to Large Language Models"](https://www.youtube.com/watch?v=zjkBMFhNj_g) dates from November 2023; it still explains the concepts well, but it predates reasoning models and current RL practice.

### 4.2 A suggested learning sequence

The table keeps the learning path's six steps and its rule of one main resource per step. It adds the hands-on work from section 3.3 and a parallel market track. Resources marked "checked" were opened on 2026-10-20 by me or the research agent. None of the videos was watched end to end, and no notebook was run.

| Step | Question | Watch | Read | Do | Stop when |
| --- | --- | --- | --- | --- | --- |
| L1 Whole system | What is a language model, what changes when it learns, and why do its answers vary? | Karpathy, [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) (2025, about 3.5 hours), up to the end of the pretraining and inference sections. Short option: 3Blue1Brown, [LLMs explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs) (about 8 minutes), then Karpathy's 2023 one-hour talk. | None needed | Draw the execution loop and the training loop. Send one prompt five times and compare the answers. | You can say what changes in weights, context, harness, and memory, and why one run proves little. |
| L2 One agent, one task | What is an agent, mechanically? | Lambert, [lecture 11](https://www.youtube.com/watch?v=GMry2DzC304) | Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) (2024). Then the [minimal agent tutorial](https://minimal-agent.com/) from the SWE-agent team: a working agent loop in about 60 lines of Python, also published as [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) (checked). | Read the loop's code. Mark where the model is called, where commands run, where the trajectory is stored, and where an infrastructure failure would appear. | You can explain model, agent, tool, trajectory, and harness by pointing at code. |
| L3 Judging outcomes (go deep) | When is a pass a real pass? | Lambert, [lecture 12](https://www.youtube.com/watch?v=dFafQmClYq4) | Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) (January 2026, checked): graders, pass@k versus pass^k, and why a 0% pass rate usually means a broken task. METR, [Recent frontier models are reward hacking](https://metr.org/blog/2025-06-05-recent-reward-hacking/) (2025): real shortcuts found by agents. Anthropic, [A statistical approach to model evaluations](https://www.anthropic.com/research/statistical-approach-to-model-evals) (2024, checked): error bars and paired comparisons. | Build H1's first task as a Harbor package, with reference, alternative, shortcut, and empty solutions, and tests that separate them. Run each solution several times. | A teammate can run the package. You can put an error bar on a score from 89 tasks. |
| L4 How training uses tasks | How does a score become a weight change? | The post-training and RL sections of Karpathy's Deep Dive, or Lambert's [lecture 3](https://www.youtube.com/watch?v=K_Sj_-1BUMM) | Lambert, [RL chapter](https://rlhfbook.com/c/06-policy-gradients), GRPO part. Hugging Face, [TRL GRPO trainer](https://huggingface.co/docs/trl/main/en/grpo_trainer) for the actual data flow. | The survey's worked example. Optionally, one small GRPO run from the [Unsloth notebooks](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide) on a free notebook GPU. The guide does not say a free GPU is enough; if it is not, this becomes H2 and needs a budget. | As in the current path. |
| L5 Compare improvement loops | What should change for this customer? | Will Brown (Prime Intellect), [RL Environments at Scale](https://www.youtube.com/watch?v=_IzZWeuTx7I): one environment reused for evaluation, SFT data, and RL | The AES and Harness² studies. Anthropic, [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (2025): harness changes made by practitioners. | The one-page comparison, including best-of-k retries and one-time offline harness tuning (section 5.3). | As in the current path. |
| L6 Run agents on tasks | Do our tasks behave under real agents? | Shaw and Marten (Laude Institute), [Everything Is a Rollout](https://www.youtube.com/watch?v=jRCpXUjz4CI) (checked) | The Harbor links in section 4.1 | Expand H1 to three to five tasks; run two agents with repeated attempts, once API access and a spending cap are agreed. | As in the current path. |
| M Market (parallel) | Who buys environments, and what do they pay? | None needed | Epoch AI, [FAQ on RL environments](https://epoch.ai/gradient-updates/state-of-rl-envs) (January 2026, checked). SemiAnalysis, [RL environments and RL for science](https://newsletter.semianalysis.com/p/rl-environments-and-rl-for-science) (January 2026, free except the last section). | One page: buyer classes, named suppliers, reported prices, and the contacts the team can actually reach. | The first-buyer decision has the inputs it needs. |

Useful but optional: Lilian Weng's [Reward hacking in reinforcement learning](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/) (a long survey), [ImpossibleBench](https://arxiv.org/abs/2510.20270) (tasks whose tests contradict their specification, so any pass is cheating; a ready template for E1 negative controls), DeepLearning.AI's short video course [Post-training of LLMs](https://www.deeplearning.ai/short-courses/post-training-of-llms/) (SFT, DPO, and online RL in about 1.5 hours), and Karpathy's [Pong from Pixels](https://karpathy.github.io/2016/05/31/rl/) (policy gradients in plain code).

Not recommended for this team now: full university courses such as Stanford CS336 (too deep unless H2 is approved), Sutton and Barto read in order, and broad agent lecture series.

## 5 The Harness² study

A separate agent checked the [note](../studies/harness2.md) against the paper (arXiv 2610.14224v1) and the pinned code, and re-ran the demo. I re-checked the paper's Tables 1–3 and the Figure 6 text myself.

### 5.1 What is accurate

The mechanism description is accurate and well suited to this team. It explains the executor and editor roles, the two loops (edits within a task, a lesson library across tasks), and the fact that each new task starts from the common initial harness. The two reported results match Tables 1 and 2, including the setup (OpenCode, `k=1`, Claude Opus 4.8 as editor) and the meaning of "±" (standard deviation over three runs). The ledger arithmetic (`4k` executor runs and `3k` editing stages), the selection pool, the library rules, the adapter boundary, and the unrestricted network and disabled Codex sandbox are all confirmed in the code.

The demo re-ran at the same commit with a byte-identical summary and wrote nothing into the checkout. The record correctly says that the editor is scripted and shows data flow, not model reasoning.

### 5.2 Corrections

- **"Figure 6 separately counts executor and improvement tokens."** It does not. Figure 6 plots one combined token total per task; the paper says the comparison "includes both execution and improvement costs." There is no split.
- **"The recursion code implements this basic step"** (steps 1–6). The linked function, `run_parallel`, covers steps 2–4. The initial run is in `schedule.run_task`; selection and reflection are in `schedule._run_one_mode`. Point each step at its own function.
- **Library admission.** The "additional content checks" are a scan for seven fixed grader-verdict strings. Say so; it is a weak check.
- **One missing behavior that matters.** At `k=1`, if the composed run fails, nothing is delivered, even when the initial run produced a deliverable. A production system would need a fallback.
- **Link format.** `EXPERIMENTS.md#L93` does not jump to a line, because GitHub renders Markdown files. Use `?plain=1#L93`.

### 5.3 What the note leaves out

The note reports the two largest gains. The paper's tables contain more that bears directly on a choice between improving harnesses and training weights:

1. **The gains vary widely.** Across three benchmarks and four executor–harness pairs, one improvement step adds 3.0 to 11.5 points on WorkBuddy-Bench, 1.2 to 4.5 on JobBench, and 2.0 to 11.8 on LAB (a legal benchmark the note does not mention). The two JobBench gains under Codex (+1.4 and +1.2) are within the run-to-run standard deviations.
2. **A one-time offline search nearly matches it.** The paper compares Meta-Harness, which tunes a harness once on separate training tasks and then deploys it unchanged. Meta-Harness comes close in several settings, for example 35.8 versus 36.0 on JobBench (Gemini 3.5 Flash, OpenCode). It wins on LAB for Gemini 3.5 Flash under Codex. Harness² instead spends about four executor runs per task at deployment. For a product, "tune once offline" versus "improve every task online" is a central cost decision.
3. **The paper already has a retry baseline.** Figure 5 includes "best-of-k": the unchanged harness run `k` times, with the same selector. That partly answers the note's first open question (is editing better than more attempts?). Read Figure 5 before designing that experiment.
4. **The library explains much of the gain.** In Table 3 (Gemini 3.5 Flash, OpenCode), removing the library lowers WorkBuddy-Bench from 77.5 to 74.4 and JobBench from 36.0 to 34.2. So the library accounts for about 3 of the 5.1-point WorkBuddy-Bench gain and about 2 of the 4.5-point JobBench gain. A library built on JobBench adds only 0.5 to 2.9 points when used on WorkBuddy-Bench.
5. **The judges overlap with the system.** JobBench is graded by Claude Opus 4.8, the same model that edits, selects, and reflects. The paper names this shared-bias risk as a limitation. This is the same independence problem the E1 plan is designed to catch.
6. **The editor guidance is written per benchmark.** Each benchmark has hand-written lists of things to try and selection checks. Part of the improvement therefore comes from human-written, benchmark-specific guidance, which a customer deployment would also need.

My reading: Harness² is a strong comparison for the "managed improvement" candidate. It shows gains of several points from improving the software around a fixed model, with no GPUs. But the costs move to every task at deployment, and an offline search gets much of the benefit. The note's open questions are the right ones. Its first experiment should include best-of-k and an offline harness-search arm at equal token budgets.

## 6 Smaller findings

- **The source register contradicts the new link list.** The [register](../../references/README.md#provided-pages-and-related-primary-material) says `links.md` is "the original list. Keep it unchanged as provenance." The latest commit added the Harness² link to `links.md` and reformatted every line. Either rule is fine, but the register should say that the user adds new links there.
- **Harness² sits outside the provided-pages table.** It is a user-provided link like the others, but the register gives it a separate section. Add a row to the table that links to that section, so that all user-provided sources appear in one list.
- **The glossary lacks the newest terms.** Add executor and editor (Harness²), best-of-k, and pass^k if step L3 adopts the Anthropic evaluation article.
- **The plan's evidence wording is good.** The H1 and H2 resource gates, the rule that no paid run is authorized, and the honest "videos were not watched end to end" notes are the right practice. Keep them.

## 7 Recommended changes

Priority 1 items fix errors or cost little. Priority 2 items change the learning path and need the team's agreement. Priority 3 items are tidying.

| Priority | Change | Owning document | Done when |
| --- | --- | --- | --- |
| 1 | Fix the step 1 text alternative and the Harbor links; link lectures 11 and 12 as videos | [Learning path](../studies/foundations.md) | Each link opens the material the step describes |
| 1 | Correct the Figure 6 description, the recursion-step links, the library-check wording, and the `EXPERIMENTS.md` link; add the missing fallback at `k=1` | [Harness² study](../studies/harness2.md) | Each claim matches the paper and the code |
| 1 | Add the full range of gains, Meta-Harness, best-of-k, the library ablation, judge overlap, and per-benchmark guidance | [Harness² study](../studies/harness2.md) | A reader sees the strongest alternatives beside the headline results |
| 1 | Change "42% faster" to "42% less time" | [AES study](../studies/autoenvscaling.md#4-what-the-results-establish) | The wording matches the paper |
| 2 | Teach randomness in step 1 and add error bars to step 3 | [Learning path](../studies/foundations.md) | Steps 1 and 3 each have a resource and an exercise for it |
| 2 | Add reward-hacking and agent-evaluation readings to step 3 | [Learning path](../studies/foundations.md) | Step 3 has at least one source showing real agent shortcuts |
| 2 | Make H1's first task the step 3 exercise; turn step 6 into running agents on three to five tasks | [Learning path](../studies/foundations.md), [study plan](../01-study-plan.md#h1-inspect-and-run-a-small-task-set) | The team builds a Harbor task before it studies training |
| 2 | Add the minimal agent loop to step 2 | [Learning path](../studies/foundations.md) | Step 2's exercise points at real code |
| 2 | Add a market track with its readings and one-page output | [Learning path](../studies/foundations.md), [opportunities](../03-opportunities.md) | The first-buyer decision has a named input |
| 2 | Offer a free notebook run as an option before H2's paid run | [Study plan](../01-study-plan.md#h2-observe-one-small-weight-update) | The plan says when the free option is enough and when H2's budget gate applies |
| 2 | Add a best-of-k arm and an offline harness-tuning arm to the Harness² experiments | [Harness² study](../studies/harness2.md#implications-and-next-tests) | The first comparison has equal token budgets across all arms |
| 3 | Rename the sequences (for example L1–L6 and D1–D5) and keep the six learning steps only in the learning path | [Study plan](../01-study-plan.md), [progress](../progress.md) | No two sequences share step numbers |
| 3 | List the main environment suppliers as unverified leads in the market map | [Opportunities](../03-opportunities.md#market-map) | Task supply shows more than one commercial alternative |
| 3 | Resolve the `links.md` rule; add Harness² to the provided-pages table; add the new glossary terms | [Source register](../../references/README.md), [glossary](../glossary.md) | The register and the link list agree |

**Validation of this review:** every local link and heading anchor in the repository resolves, checked by script after writing.
