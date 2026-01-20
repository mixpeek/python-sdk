# PatchClusterRequest

Request model for partially updating a cluster (PATCH operation).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | Updated name for the cluster | [optional] 
**description** | **str** | Updated description for the cluster | [optional] 
**metadata** | **object** | Updated metadata for the cluster | [optional] 

## Example

```python
from mixpeek.models.patch_cluster_request import PatchClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchClusterRequest from a JSON string
patch_cluster_request_instance = PatchClusterRequest.from_json(json)
# print the JSON string representation of the object
print(PatchClusterRequest.to_json())

# convert the object into a dict
patch_cluster_request_dict = patch_cluster_request_instance.to_dict()
# create an instance of PatchClusterRequest from a dict
patch_cluster_request_from_dict = PatchClusterRequest.from_dict(patch_cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


