# VectorBasedConfig

Configuration for vector-based clustering.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_extractor_name** | **str** | Name of the feature extractor to use for vectors | 
**clustering_method** | [**ClusteringAlgorithm**](ClusteringAlgorithm.md) | Clustering algorithm to use | 
**sample_size** | **int** | Number of samples to use for clustering | [optional] 
**kmeans_parameters** | [**KmeansParameters**](KmeansParameters.md) |  | [optional] 
**dbscan_parameters** | [**DbscanParameters**](DbscanParameters.md) |  | [optional] 
**hdbscan_parameters** | [**HdbscanParameters**](HdbscanParameters.md) |  | [optional] 
**algorithm_params** | [**AlgorithmParams**](AlgorithmParams.md) |  | [optional] 

## Example

```python
from mixpeek.models.vector_based_config import VectorBasedConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VectorBasedConfig from a JSON string
vector_based_config_instance = VectorBasedConfig.from_json(json)
# print the JSON string representation of the object
print(VectorBasedConfig.to_json())

# convert the object into a dict
vector_based_config_dict = vector_based_config_instance.to_dict()
# create an instance of VectorBasedConfig from a dict
vector_based_config_from_dict = VectorBasedConfig.from_dict(vector_based_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


