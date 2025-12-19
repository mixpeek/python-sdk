# ClusteringConfig

Complete configuration for clustering operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | [**ClusteringAlgorithm**](ClusteringAlgorithm.md) | Clustering algorithm to use | 
**algorithm_params** | [**AlgorithmParams**](AlgorithmParams.md) |  | [optional] 
**feature_vector** | [**FeatureVectorRef**](FeatureVectorRef.md) | Reference to the vector to use for clustering | 
**additional_features** | **List[str]** | Additional features for multi-modal clustering | [optional] 
**normalize_features** | **bool** | Whether to normalize features before clustering | [optional] [default to True]
**dimensionality_reduction** | [**DimensionalityReduction**](DimensionalityReduction.md) |  | [optional] 
**hierarchical** | **bool** | Whether to create hierarchical clusters | [optional] [default to False]
**max_hierarchy_depth** | **int** | Maximum depth for hierarchical clustering | [optional] [default to 3]
**llm_labeling** | [**LLMLabeling**](LLMLabeling.md) | Configuration for LLM-based labeling | [optional] 
**batch_size** | **int** | Batch size for processing | [optional] [default to 1000]
**parallelism** | **int** | Number of parallel workers | [optional] [default to 4]
**sample_size** | **int** | Sample size for large collections | [optional] 

## Example

```python
from mixpeek.models.clustering_config import ClusteringConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClusteringConfig from a JSON string
clustering_config_instance = ClusteringConfig.from_json(json)
# print the JSON string representation of the object
print(ClusteringConfig.to_json())

# convert the object into a dict
clustering_config_dict = clustering_config_instance.to_dict()
# create an instance of ClusteringConfig from a dict
clustering_config_from_dict = ClusteringConfig.from_dict(clustering_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


