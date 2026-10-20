# Claude review 2: resolution

Resolved by GPT/Codex on 2026-10-20 at the user's request. This document responds to [review 2](claude-init-review-2.md); the original review and earlier records are unchanged. [Progress](../progress.md) owns the active worklist.

Most recommendations are adopted. The main changes correct Harness²'s cost and failure-handling descriptions, show its alternatives and weaker results, and make the learning path more practical. We retain short learning sections instead of the review's six-column table, as the user requested. Shared writing guidance now favors narrow tables and sections for prose-heavy comparisons.

## Evidence checked

Read the complete review and affected documents. Rechecked Harness² v1's tables 1–3, figures 5–7, and appendices B–D and F using the saved paper text. Compared its claims with code at `1cfe254e8d25b15f37048c3730134686abe60335`: scheduler, recursion, selection, library, context checks, and benchmark prompts. Source and function links are in the [study](../studies/harness2.md).

The review's saved demo summary is byte-identical to our [committed result](../records/2026-10-19-harness2-demo/result.json), with SHA-256 `ce38ca6c1104b6b8c80981dab8b3d4b949e15b72e5cd026807518d510a4c1f5d`. This checks the saved artifact; we did not rerun the demo for this resolution. The absent fallback is confirmed by reading `selection_pool`, `trivial_selection`, and their scheduler call path, not a newly executed failure probe.

Checked AES's collection metric against Figure 7/appendix G.1 and the pinned release's `fig_training_metrics_summary.json`. The matched interval uses 42.3% less collection time, rounded to 42% in the study. This is not a new measurement.

Opened selected primary teaching pages, Harbor documentation, the minimal agent tutorial, METR's examples, the statistical guide, the Unsloth guide, and Epoch AI's report. The [source register](../../references/README.md#learning-resources-added-in-review-2) records review depth and video-access limits. No model, notebook, training job, customer contact, or benchmark reproduction was run.

## Priority 1: corrections and comparisons

1. **Resource destinations — adopted.** The [learning path](../studies/foundations.md) moves Lambert's training overview to L4. L1 retains Karpathy's concise introduction with a short 3Blue1Brown alternative. Harbor links now target the task format, tutorial, and example repository. Lectures 11 and 12 have direct links and course-page fallbacks. The course listing confirms the topics; direct video retrieval failed here, so playback was not independently verified.

2. **Harness² implementation descriptions — adopted.** The [study](../studies/harness2.md) states that Figure 6 reports combined tokens, maps the workflow to its actual functions, identifies the seven-string content scan, and fixes the Markdown line link with `?plain=1`. It documents the absent initial-output fallback at `k=1`. “Add the missing fallback” is interpreted as documenting the behavior and a proposed comparison; we did not modify upstream code. A deployment must choose an explicit failure policy, not automatically return an unchecked earlier answer.

3. **Broader Harness² evidence — adopted with limits.** Added the range across all four executor/harness configurations for each benchmark, smaller Codex/JobBench gains, Meta-Harness, best-of-k, the library ablation and transfer result, judge overlap, and benchmark-specific guidance. The comparison now shows alternatives beside the strongest results. Statistical, causal, and cost qualifications appear below.

4. **AES time wording — adopted.** The [AES study](../studies/autoenvscaling.md#4-what-the-results-establish) now says “42% less time.” A time reduction and a throughput increase use different denominators. The existing scope limit remains: collection time is not total training cost.

## Priority 2: learning and experiments

5. **Randomness and uncertainty — adopted.** L1 distinguishes sampled outputs from weight changes and adds a toy sampling exercise that needs no model account. Five real prompt runs are optional with existing authorized access. L3 adds an interval calculation, task-sampling assumptions, and paired comparisons. The [survey](../02-survey.md#7-reading-results-without-misleading-ourselves) and [glossary](../glossary.md) explain the shared terms.

6. **Agent evaluation and reward hacking — adopted.** L3 uses Anthropic's agent-evaluation guide and selected METR examples. It asks learners to identify grader shortcuts and build negative controls. The article's zero-pass warning concerns many trials with frontier models. We retain it as a reason to inspect the task and grader, not a general conclusion from any zero-pass result; model capability can also be the cause.

7. **Build earlier — adopted.** L3 now produces H1's first Harbor package and deterministic checks. L6 expands to three to five tasks and runs existing agents. [H1](../01-study-plan.md#h1-inspect-and-run-a-small-task-set) owns the implementation details. These are planned outputs; no task package was built during this documentation change.

8. **Read a real agent loop — adopted.** L2 points to the minimal agent tutorial and asks learners to locate calls, actions, observations, state, and errors. It does not require running the tutorial's unrestricted shell loop.

9. **Market learning — adopted.** M1 uses Epoch's report, the maintained map, and the Third Moment study. [Opportunities](../03-opportunities.md#buyer-brief-for-m1) owns the buyer-brief fields and remaining access gaps. This covers training and application buyers without adding another mandatory reading list.

10. **Free-compute H2 — adopted with a correction to the premise.** The previous H2 gated paid execution, not every real weight update. It nevertheless lacked an explicit free option. [H2](../01-study-plan.md#h2-observe-one-small-weight-update) now permits suitable existing or free resources after checking model, memory, notebook revision, and required outputs. The guide's examples are leads, not a guarantee of a free GPU or a successful run. Paid execution retains its concrete approval gate.

11. **Stronger experiment baselines — adopted.** The [Harness² comparison](../studies/harness2.md#implications-and-next-tests) includes unchanged-harness best-of-k, manual tuning, offline harness search, and online editing. It uses common token caps and reports actual spend, human effort, dollars, latency, and offline cost amortization. Equal `k` is not equal compute; equal tokens from differently priced models are not equal dollars.

## Priority 3: ownership and navigation

12. **Distinct labels and one sequence owner — adopted.** L1–L6 and M1 live in the foundation guide. The plan links there instead of repeating the six rows; its commercial stages use D1–D5. Progress uses a work queue rather than another competing numbered sequence.

13. **Supplier coverage — adopted as leads.** The [market map](../03-opportunities.md#additional-supplier-leads) names Mechanize, Prime Intellect, Surge, Mercor, Snorkel, and Turing as unverified leads from the earlier scan. It does not rank them, assert equivalent offerings, or adopt unverified funding claims. Checking relevant offerings remains work before opportunity ranking.

14. **Source register and glossary — adopted.** The register now describes `links.md` as user-maintained, with history preserved in Git. Harness² appears in the provided-pages table and links to its detailed entry. The glossary adds executor/editor, sampling, best-of-k, pass^k, and uncertainty terms. User-supplied reference entries remain unchanged.

## Where we keep narrower conclusions

**Library contribution.** Table 3 supports a conditional benefit from enabling the library in Gemini/OpenCode at `k=1`. A component-removal experiment does not partition total gains into independent shares. We retain the observed score drops and avoid assigning a fixed fraction of all improvement to memory.

**Offline economics.** Similar scores make offline tuning a serious alternative. They do not establish that it is cheaper: Figure 6 includes search/improvement costs and reports greater total compute for Meta-Harness in that comparison. Deployment volume, amortization, inference prices, and latency can change the commercial answer.

**Human guidance and model overlap.** The code contains benchmark-specific instructions and the JobBench judge shares the editor's model. These are concrete setup and evaluation concerns. The cited evidence does not isolate the instructions' causal contribution or prove that shared bias caused any particular gain. Fixed-weight improvement still consumes inference compute; “no weight training” is more precise than “no GPUs.”

**Learning load.** Retain the short default L1 route rather than require the long Deep Dive. Do not add every suggested talk, survey, course, trainer manual, or market article. The selected resources fill concrete gaps; additional resources remain discovery leads in the original review. Statistical depth and a small training demonstration do not require completing a university ML curriculum.

## Validation and remaining work

Checked local Markdown links and heading anchors, whitespace, pinned-code targets, and the supplied source-file hashes. Confirmed that the original review, prior records, reference link collection, and inspected Harness² checkout remain unchanged. Video playback and notebook execution remain unverified.

The next work is the team's learning outputs, H1's first task package, and M1's buyer brief. No buyer, paid run, repair project, or production framework has been selected by this resolution.
