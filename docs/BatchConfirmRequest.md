# BatchConfirmRequest

Request to confirm multiple uploads in batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmations** | **List[object]** | List of confirmations with upload_id, etag, file_size_bytes | 

## Example

```python
from mixpeek.models.batch_confirm_request import BatchConfirmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchConfirmRequest from a JSON string
batch_confirm_request_instance = BatchConfirmRequest.from_json(json)
# print the JSON string representation of the object
print(BatchConfirmRequest.to_json())

# convert the object into a dict
batch_confirm_request_dict = batch_confirm_request_instance.to_dict()
# create an instance of BatchConfirmRequest from a dict
batch_confirm_request_from_dict = BatchConfirmRequest.from_dict(batch_confirm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


