# InstantiateClusterTemplateRequest

Request to instantiate a cluster from a template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | Name for the new cluster | 
**collection_ids** | **List[str]** | Collection IDs to use for the cluster | 
**description** | **str** | Optional description override for the cluster | [optional] 

## Example

```python
from mixpeek.models.instantiate_cluster_template_request import InstantiateClusterTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstantiateClusterTemplateRequest from a JSON string
instantiate_cluster_template_request_instance = InstantiateClusterTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(InstantiateClusterTemplateRequest.to_json())

# convert the object into a dict
instantiate_cluster_template_request_dict = instantiate_cluster_template_request_instance.to_dict()
# create an instance of InstantiateClusterTemplateRequest from a dict
instantiate_cluster_template_request_from_dict = InstantiateClusterTemplateRequest.from_dict(instantiate_cluster_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


