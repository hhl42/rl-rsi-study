# RLTL;DR: learning from short feedback

**Question:** Can a short explanation of a failure become useful training data, including when successful solutions are rare?

Source: Kirchhof et al., *RLTL;DR: Self-improvement by Internalizing Self-generated Feedback*, supplied [v1 PDF](../../references/papers/2609.37633v1-RTL-DR.pdf). Selected methods and results reviewed on 2026-10-14: sections 4–6, table 2, and appendix D. We have not reproduced the experiments.

## Mechanism

The model attempts a task, receives verifier feedback, and writes a short insight about what to do differently. Later attempts receive accumulated insights. This can help the model solve the task while its weights remain unchanged.

RLTL;DR also updates weights. It combines GRPO, an RL method that compares rewards across attempts, with a supervised objective that trains the model to predict the insights from the task. The intention is to make the guidance useful even when the insight is absent at evaluation. Section 5 tests simpler alternatives, including supervised fine-tuning (SFT) on task–insight pairs alone.

For a systems example, an insight might say to check all pages of an API response. Giving that reminder to an agent and training a model to handle pagination without the reminder are different interventions. This example illustrates the distinction; it is not a result from our repository.

## Evidence and limits

The main setup uses Qwen 3.5 9B with thinking. It selects tasks on which that model had no success in 128 attempts. This is an observed difficulty filter, not proof that the tasks are unsolvable. The Appworld preparation combines train, development, and test-normal tasks before filtering, while leaving test-challenge unseen. Its results must be interpreted with that split, rather than treated as a standard leaderboard run. See section 4.1.

Table 2 reports the following on the Synthetic-API (SAPI) frontier-difficulty split. Evaluation uses unseen tasks without insights in context or sequential retries:

| Training method | Evaluation pass@1 | Forward / backward tokens during policy updates |
| --- | --- | --- |
| RLTL;DR | 18.9% | 720M / 12M |
| SFT on 3.5k successful full rollouts | 20.9% | 400M / 6.6M |
| SFT on 100 successful rollouts | 20.8% | 9.5M / 217k |
| SFT on deduplicated task–insight pairs | 16.9% | 4.6M / 68k |

The table reports standard deviation of 0.6 percentage points. Short insights reduce policy-update work, but they do not match the best listed score. The same table explicitly excludes roughly one billion tokens of rollout collection from these update counts. It therefore does not establish an equally large reduction in end-to-end cost.

Transfer is uneven: section 4 reports improvements in API tasks but overfitting on Leetcode. SAPI is proprietary, which limits independent access to that part of the evidence.

## Implication and next check

Our hypothesis is that a task framework may need to retain structured feedback and the evidence behind it, alongside successful trajectories. Feedback could be a deliverable, but usefulness must be tested on new tasks.

Start with [E3](../01-study-plan.md#e3-use-feedback-effectively): compare retries with no feedback, raw feedback, and a short insight under the same total budget. Inspect whether an insight explains a reusable mistake or merely reveals the answer. A later training experiment should compare full trajectories with insight targets and evaluate without supplying the training hints. That later step is needed to test weight learning.
