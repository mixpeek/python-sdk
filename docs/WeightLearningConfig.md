# WeightLearningConfig

Configuration for automatic feature weight learning in multi-feature clustering.  When multi_feature_strategy='weighted' and feature_weights is not provided, this configuration controls how optimal weights are automatically learned.  The system tries different weight combinations and picks the one that produces the best clustering quality (measured by silhouette score, etc.).  Examples:     Bayesian optimization (recommended):     {         \"method\": \"bayesian\",         \"max_iterations\": 20,         \"metric\": \"silhouette\",         \"sample_size\": 5000     }      Grid search (exhaustive, limited to 2-3 features):     {         \"method\": \"grid_search\",         \"max_iterations\": 5,         \"metric\": \"silhouette\"     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | Weight learning method: - bayesian: Gaussian process optimization (recommended, scales to 5+ features) - grid_search: Exhaustive search (limited to 2-3 features, simpler but slower) | [optional] [default to 'bayesian']
**max_iterations** | **int** | Maximum optimization iterations: - grid_search: Number of values to try per feature (total: max_iterations^n_features) - bayesian: Number of weight combinations to evaluate Recommended: 20 for bayesian, 5 for grid_search | [optional] [default to 20]
**metric** | **str** | Clustering quality metric to optimize: - silhouette: Measures how similar points are to their cluster vs other clusters (range: [-1, 1], higher is better) - davies_bouldin: Ratio of within-cluster to between-cluster distances (range: [0, ∞], lower is better) - calinski_harabasz: Ratio of between-cluster to within-cluster variance (range: [0, ∞], higher is better) Recommended: silhouette (most general-purpose) | [optional] [default to 'silhouette']
**sample_size** | **int** | Optional: Learn weights on a random sample (speeds up large datasets). If provided and dataset has more documents, weights are learned on sample_size random documents, then applied to full dataset. Recommended: 5000 for datasets &gt;10k documents | [optional] 
**random_state** | **int** | Random seed for reproducibility of weight learning | [optional] [default to 42]

## Example

```python
from mixpeek.models.weight_learning_config import WeightLearningConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WeightLearningConfig from a JSON string
weight_learning_config_instance = WeightLearningConfig.from_json(json)
# print the JSON string representation of the object
print(WeightLearningConfig.to_json())

# convert the object into a dict
weight_learning_config_dict = weight_learning_config_instance.to_dict()
# create an instance of WeightLearningConfig from a dict
weight_learning_config_from_dict = WeightLearningConfig.from_dict(weight_learning_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


