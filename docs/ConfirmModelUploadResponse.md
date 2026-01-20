# ConfirmModelUploadResponse

Response from confirming a model upload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether upload and validation succeeded | 
**upload_id** | **str** | The upload ID | 
**model_id** | **str** | Created model ID if successful | [optional] 
**validation_status** | **str** | Validation status | 
**validation_errors** | **List[str]** | Validation errors if any | [optional] 
**s3_archive_url** | **str** | S3 URL of the archive | [optional] 
**message** | **str** | Additional status message | [optional] 

## Example

```python
from mixpeek.models.confirm_model_upload_response import ConfirmModelUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmModelUploadResponse from a JSON string
confirm_model_upload_response_instance = ConfirmModelUploadResponse.from_json(json)
# print the JSON string representation of the object
print(ConfirmModelUploadResponse.to_json())

# convert the object into a dict
confirm_model_upload_response_dict = confirm_model_upload_response_instance.to_dict()
# create an instance of ConfirmModelUploadResponse from a dict
confirm_model_upload_response_from_dict = ConfirmModelUploadResponse.from_dict(confirm_model_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


