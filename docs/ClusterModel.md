# ClusterModel

Cluster metadata stored in MongoDB.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_ids** | **List[str]** | Collections to cluster together | 
**cluster_name** | **str** | Optional human-friendly name for the clustering job | [optional] 
**cluster_type** | [**ClusterType**](ClusterType.md) | Vector or attribute clustering | [optional] 
**vector_config** | [**VectorBasedConfig**](VectorBasedConfig.md) | Required when cluster_type is &#39;vector&#39; | [optional] 
**attribute_config** | [**AttributeBasedConfig**](AttributeBasedConfig.md) | Required when cluster_type is &#39;attribute&#39; | [optional] 
**llm_labeling** | [**LLMLabeling**](LLMLabeling.md) | Configuration for LLM-based cluster labeling | [optional] 
**cluster_id** | **str** | Unique cluster identifier | [optional] 
**parquet_path** | **str** | S3 path to parquet files with cluster data | [optional] 
**members_key** | **str** | S3 key to members.parquet (if saved) | [optional] 
**num_clusters** | **int** | Number of clusters found | [optional] 
**cluster_stats** | [**ClusterStats**](ClusterStats.md) | Clustering quality metrics | [optional] 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Clustering job status | [optional] 
**task_id** | **str** | Associated task ID for clustering job | [optional] 
**created_at** | **datetime** | When the cluster was created | [optional] 
**updated_at** | **datetime** | When the cluster was last updated | [optional] 

## Example

```python
from mixpeek.models.cluster_model import ClusterModel

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterModel from a JSON string
cluster_model_instance = ClusterModel.from_json(json)
# print the JSON string representation of the object
print(ClusterModel.to_json())

# convert the object into a dict
cluster_model_dict = cluster_model_instance.to_dict()
# create an instance of ClusterModel from a dict
cluster_model_from_dict = ClusterModel.from_dict(cluster_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


