# PatchNamespaceRequest

Request schema for partially updating a namespace (PATCH operation).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_name** | **str** | Updated name for the namespace | [optional] 
**description** | **str** | Updated description for the namespace | [optional] 
**payload_indexes** | [**List[PayloadIndexConfigInput]**](PayloadIndexConfigInput.md) | Updated list of custom payload indexes for this namespace. | [optional] 
**auto_create_indexes** | **bool** | Enable automatic creation of Qdrant payload indexes based on filter usage patterns. When enabled, the system tracks which fields are most frequently filtered (&gt;100 queries/24h) and automatically creates indexes to improve query performance. Background task runs every 6 hours. Expected performance improvement: 50-90% latency reduction for filtered queries. Default: False. | [optional] 

## Example

```python
from mixpeek.models.patch_namespace_request import PatchNamespaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchNamespaceRequest from a JSON string
patch_namespace_request_instance = PatchNamespaceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchNamespaceRequest.to_json())

# convert the object into a dict
patch_namespace_request_dict = patch_namespace_request_instance.to_dict()
# create an instance of PatchNamespaceRequest from a dict
patch_namespace_request_from_dict = PatchNamespaceRequest.from_dict(patch_namespace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


