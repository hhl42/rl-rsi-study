# Recursive Self-Rewrite: turning successes into demonstrations

**Question:** Can successes discovered under different agent harnesses become better training examples for one general harness?

Source: Li et al., *Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite*, supplied [v1 PDF](../../references/papers/2610.02826v1-Recursive-Self-Rewrite.pdf). Selected methods and results reviewed on 2026-10-14: section 2, sections 3.5–3.6, and table 5. No implementation or result has been reproduced here.

## Mechanism

The same base model collects successful trajectories under several harnesses. A planner turns a success into a runbook: procedural guidance for solving the task. Deterministic checks and a model critic screen the runbook for unavailable information and answer leakage. An executor then solves the task again in a fresh environment under the general harness.

The runbook privately guides generation but is removed from the public training trajectory. Another filtering step looks for unexplained values that may reveal hidden answer transfer. Verified trajectories train the model through supervised fine-tuning (SFT). At evaluation, the model uses the general harness without the private runbooks. This is a data-construction and SFT method, not a new RL optimizer. See section 2.

## Evidence and limits

The paper uses Qwen-3.8-27B. Across its approximately 3,000-task discovery pool, the three harnesses collectively solve 759 tasks. Rewriting expands 2,001 successful source trajectories to 11,094 passing rewrites. The final RSR training mixture also includes 766 direct successes from the general harness. Data volume and composition change along with the rewriting method, so the main comparison does not isolate rewriting alone.

Table 5 reports these Terminal-Bench 2 results:

| Metric | Base model | Direct SFT | RSR |
| --- | --- | --- | --- |
| Success within three attempts, pass@3 | 57.0% | 53.4% | 74.2% |
| Mean success rate across three individual runs | 51.7% | 43.8% | 70.1% |

These metrics answer different questions. The first allows several chances; the second averages individual attempts. Neither should be presented without its attempt budget. On the paper's own long-horizon benchmark, process reward rises from 0.21 to 0.29, while all three methods complete zero of 46 tasks. Better partial progress does not establish task completion.

Several evaluation sets are curated by the authors. Dataset independence and leakage filtering need closer review. A model critic is a screening mechanism, not proof that private guidance cannot influence a supposedly public trajectory.

## Implication and next check

Our hypothesis is that task replay and trajectory repair could be useful services even before building an online RL loop. A framework would need separate records for author evidence, private guidance, solver-visible observations, and the final training trace.

For a small permitted task set, compare direct successful traces with fresh re-executions. Match the number of training examples or report the mismatch. Inspect whether each action can be justified from the public history, and count unsuccessful rewrites in the cost. Test downstream benefit on reserved task families before calling cleaner traces better training data.
