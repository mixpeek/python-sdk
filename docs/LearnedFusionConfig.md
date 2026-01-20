# LearnedFusionConfig

Configuration for learned fusion with bandit-based weight optimization.  Enables personalized feature weighting by learning from user interactions. The system learns which features (text, image, audio, etc.) matter most for different users or contexts.  ┌─────────────────────────────────────────────────────────────────────────────┐ │ HOW LEARNED FUSION WORKS                                                     │ ├─────────────────────────────────────────────────────────────────────────────┤ │ 1. Query arrives with context (user_id, segment, etc.)                      │ │ 2. Look up bandit state for this context                                    │ │ 3. Sample feature weights from Beta distributions                           │ │ 4. Execute separate queries per feature with learned weights                │ │ 5. Fuse results using sampled weights                                       │ │ 6. On feedback (click), update bandit for relevant features                 │ └─────────────────────────────────────────────────────────────────────────────┘  Cold Start Handling:     - NEW users: Uses demographic context (user_segment, device_type)     - Returning users: Uses personal context after min_interactions     - Fallback: Global context as ultimate fallback  Requirements:     - Interactions API must be called with feedback (clicks, etc.)     - Context features should be passed in query inputs  Example:     ```python     LearnedFusionConfig(         algorithm=LearningAlgorithm.THOMPSON_SAMPLING,         context_features=[\"INPUT.user_id\"],         demographic_features=[\"INPUT.user_segment\", \"INPUT.device_type\"],         reward_signal=\"click\",         min_interactions=5,     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | [**LearningAlgorithm**](LearningAlgorithm.md) | Learning algorithm for weight optimization. THOMPSON_SAMPLING (default): Beta-Bernoulli bandit with natural exploration. Works immediately, no tuning needed, best for most use cases. | [optional] 
**context_features** | **List[str]** | Template variables for personal context (e.g., [&#39;INPUT.user_id&#39;]). Empty list &#x3D; global learning (same weights for all users). Personal context is used after user has min_interactions. Supports: INPUT.*, CONTEXT.*, etc. | [optional] 
**demographic_features** | **List[str]** | Template variables for demographic fallback context. Used for NEW users with &lt; min_interactions. Enables cold start by learning from similar user segments. Examples: INPUT.user_segment, INPUT.device_type, INPUT.country. | [optional] 
**fallback_strategy** | **str** | Strategy when user lacks sufficient history. &#39;hierarchical&#39;: Try personal → demographic → global (recommended). &#39;global&#39;: Skip demographic, fall back directly to global. | [optional] [default to 'hierarchical']
**min_interactions** | **int** | Minimum interactions before using personal context. Below this threshold, uses demographic or global context. Prevents overfitting to small samples. Typical range: 3-10. | [optional] [default to 5]
**reward_signal** | **str** | Interaction type(s) that count as positive reward. Single: &#39;click&#39;, &#39;purchase&#39;, &#39;positive_feedback&#39;. Multiple: &#39;click,purchase&#39; (comma-separated). Determines when to strengthen feature weights. | [optional] [default to 'click']
**exploration_bonus** | **float** | Controls exploration vs exploitation balance. 1.0 &#x3D; balanced (default). Higher &#x3D; more exploration (try diverse weights). Lower &#x3D; more exploitation (use known winners). Typical range: 0.5-2.0. | [optional] [default to 1.0]
**prior_alpha** | **float** | Beta distribution prior for positive feedback (α). 1.0 &#x3D; uniform prior (no initial bias). Higher &#x3D; initial belief that features are effective. | [optional] [default to 1.0]
**prior_beta** | **float** | Beta distribution prior for negative feedback (β). 1.0 &#x3D; uniform prior (no initial bias). Higher &#x3D; initial belief that features are ineffective. | [optional] [default to 1.0]

## Example

```python
from mixpeek.models.learned_fusion_config import LearnedFusionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LearnedFusionConfig from a JSON string
learned_fusion_config_instance = LearnedFusionConfig.from_json(json)
# print the JSON string representation of the object
print(LearnedFusionConfig.to_json())

# convert the object into a dict
learned_fusion_config_dict = learned_fusion_config_instance.to_dict()
# create an instance of LearnedFusionConfig from a dict
learned_fusion_config_from_dict = LearnedFusionConfig.from_dict(learned_fusion_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


