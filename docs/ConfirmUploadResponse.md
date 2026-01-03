# ConfirmUploadResponse

Response from upload confirmation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **str** | Upload ID that was confirmed | 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Updated upload status (COMPLETED or PROCESSING) | 
**etag** | **str** | S3 ETag from uploaded object | [optional] 
**file_size_bytes** | **int** | Actual file size from S3 | [optional] 
**file_hash** | **str** | File content hash (from ETag) | [optional] 
**verified_at** | **datetime** | When verification completed | [optional] 
**completed_at** | **datetime** | When upload completed | [optional] 
**object_id** | **str** | Created bucket object ID (if create_object_on_confirm was true) | [optional] 
**task_id** | **str** | Task ID for async processing (if async&#x3D;true) | [optional] 
**message** | **str** | Confirmation message | [optional] 

## Example

```python
from mixpeek.models.confirm_upload_response import ConfirmUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmUploadResponse from a JSON string
confirm_upload_response_instance = ConfirmUploadResponse.from_json(json)
# print the JSON string representation of the object
print(ConfirmUploadResponse.to_json())

# convert the object into a dict
confirm_upload_response_dict = confirm_upload_response_instance.to_dict()
# create an instance of ConfirmUploadResponse from a dict
confirm_upload_response_from_dict = ConfirmUploadResponse.from_dict(confirm_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


