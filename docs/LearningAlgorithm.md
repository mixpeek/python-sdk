# LearningAlgorithm

Algorithms for learning feature fusion weights from feedback.  ┌─────────────────────────────────────────────────────────────────────────────┐ │ ALGORITHM COMPARISON                                                         │ ├───────────────────┬─────────────────────────────────────────────────────────┤ │ Algorithm         │ Description                                             │ ├───────────────────┼─────────────────────────────────────────────────────────┤ │ thompson_sampling │ Beta-Bernoulli bandit, natural exploration, no tuning  │ │ epsilon_greedy    │ (Future) Simple ε-greedy exploration                   │ │ ucb               │ (Future) Upper Confidence Bound with guarantees        │ └───────────────────┴─────────────────────────────────────────────────────────┘  THOMPSON_SAMPLING (Recommended):     - Beta-Bernoulli bandit with probabilistic exploration     - Works immediately with uniform priors (α=1, β=1)     - No hyperparameter tuning required     - Natural exploration/exploitation balance via sampling     - Converges to optimal weights as feedback accumulates     - Best for: Binary feedback (click/no-click), most use cases  How it works:     1. Each feature has Beta(α, β) distribution     2. Sample weight from each distribution before search     3. Apply sampled weights to fusion     4. On positive feedback (click): increment α for strong features     5. On no feedback: increment β for features in shown docs     6. Distribution shifts toward effective features over time

## Enum

* `THOMPSON_SAMPLING` (value: `'thompson_sampling'`)

* `EPSILON_GREEDY` (value: `'epsilon_greedy'`)

* `UCB` (value: `'ucb'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


