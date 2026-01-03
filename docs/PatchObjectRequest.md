# PatchObjectRequest

Request model for partially updating a bucket object (PATCH operation).  Task 10: Use extra='allow' to accept any user-defined fields at root level. No nested metadata dict - all fields are flat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_prefix** | **str** | Updated storage key/path prefix of the object | [optional] 
**skip_duplicates** | **bool** | Skip duplicate blobs | [optional] 

## Example

```python
from mixpeek.models.patch_object_request import PatchObjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchObjectRequest from a JSON string
patch_object_request_instance = PatchObjectRequest.from_json(json)
# print the JSON string representation of the object
print(PatchObjectRequest.to_json())

# convert the object into a dict
patch_object_request_dict = patch_object_request_instance.to_dict()
# create an instance of PatchObjectRequest from a dict
patch_object_request_from_dict = PatchObjectRequest.from_dict(patch_object_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


