# PatchBatchRequest

Request model for partially updating a batch (PATCH operation).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, object]** | Additional user-defined metadata for the batch. | [optional] 

## Example

```python
from mixpeek.models.patch_batch_request import PatchBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchBatchRequest from a JSON string
patch_batch_request_instance = PatchBatchRequest.from_json(json)
# print the JSON string representation of the object
print(PatchBatchRequest.to_json())

# convert the object into a dict
patch_batch_request_dict = patch_batch_request_instance.to_dict()
# create an instance of PatchBatchRequest from a dict
patch_batch_request_from_dict = PatchBatchRequest.from_dict(patch_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


