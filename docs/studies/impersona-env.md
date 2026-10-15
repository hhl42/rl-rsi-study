# Impersona-Env: simulated users as feedback

**Question:** Can a model of a user generate useful training feedback for an assistant?

Sources: the author's [Impersona-Env article](https://benshi34.github.io/#/blog/impersona-env) and linked [repository](https://github.com/benshi34/impersona-env). The article was reviewed through the browser on 2026-10-14. Code has not been audited. This is a single-user proof of concept.

## What the source describes

A user model is fine-tuned from message history and context. It simulates conversations and supplies feedback. A judge converts that feedback into guidance; the assistant rewrites responses, producing preferred and less-preferred response pairs for Direct Preference Optimization (DPO). Both the user model and assistant receive weight updates at different stages.

The author identifies a central evaluation problem: the simulator used to create training feedback can also favor the resulting assistant during evaluation. A later blinded arena provides a different check. For the DPO model it reports 113 comparisons: 50 wins, 30 losses, and 33 ties. The author is the sole human voter. These are repeated judgments by one person, not 113 independent users; they do not establish transfer to other users. Reconstructed reasoning in the training data is a generated explanation, not direct observation of the person's thoughts.

## Implication for our exploration

Our hypothesis is that simulated participants could help create tasks where interaction matters and a unit test cannot capture the outcome. Examples might include asking a service owner for missing context or explaining an incident to different audiences.

The difficult part is establishing whether simulated feedback predicts what real participants value. Better performance against a simulator is only an intermediate measurement.

## Next check

Use permitted, purpose-specific example interactions to define one narrow behavior. Assess simulator responses against independent human judgments before using them as training labels. Reserve scenarios and participants for evaluation, and compare against simpler prompting or memory changes. Record consent and reuse rights before collecting personal conversation data. An initial study can use authored examples without copying private message histories into this repository.
