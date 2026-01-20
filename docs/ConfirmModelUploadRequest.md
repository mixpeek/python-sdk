# ConfirmModelUploadRequest

Request to confirm a model upload after S3 upload completes.  Optional fields for integrity verification: - etag: S3 ETag returned from PUT response (recommended) - file_size_bytes: Expected file size for validation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **str** | S3 ETag from upload response for integrity check | [optional] 
**file_size_bytes** | **int** | Expected file size for validation | [optional] 

## Example

```python
from mixpeek.models.confirm_model_upload_request import ConfirmModelUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmModelUploadRequest from a JSON string
confirm_model_upload_request_instance = ConfirmModelUploadRequest.from_json(json)
# print the JSON string representation of the object
print(ConfirmModelUploadRequest.to_json())

# convert the object into a dict
confirm_model_upload_request_dict = confirm_model_upload_request_instance.to_dict()
# create an instance of ConfirmModelUploadRequest from a dict
confirm_model_upload_request_from_dict = ConfirmModelUploadRequest.from_dict(confirm_model_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


