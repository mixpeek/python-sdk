# CreateClusterRequest

Create a clustering job for one or more collections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_ids** | **List[str]** | Collections to cluster together | 
**cluster_name** | **str** | Optional human-friendly name for the clustering job | [optional] 
**cluster_type** | [**ClusterType**](ClusterType.md) | Vector or attribute clustering | [optional] 
**vector_config** | [**VectorBasedConfig**](VectorBasedConfig.md) | Required when cluster_type is &#39;vector&#39; | [optional] 
**attribute_config** | [**AttributeBasedConfig**](AttributeBasedConfig.md) | Required when cluster_type is &#39;attribute&#39; | [optional] 
**llm_labeling** | [**LLMLabeling**](LLMLabeling.md) | Configuration for LLM-based cluster labeling | [optional] 

## Example

```python
from mixpeek.models.create_cluster_request import CreateClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterRequest from a JSON string
create_cluster_request_instance = CreateClusterRequest.from_json(json)
# print the JSON string representation of the object
print(CreateClusterRequest.to_json())

# convert the object into a dict
create_cluster_request_dict = create_cluster_request_instance.to_dict()
# create an instance of CreateClusterRequest from a dict
create_cluster_request_from_dict = CreateClusterRequest.from_dict(create_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


