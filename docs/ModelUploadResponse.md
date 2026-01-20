# ModelUploadResponse

Response model for model upload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether upload succeeded | 
**model_id** | **str** | Unique model identifier | 
**deployment_status** | **str** | Deployment status | 
**endpoint** | **str** | Model inference endpoint | 
**model_archive_url** | **str** | S3 URL where archive is stored | 

## Example

```python
from mixpeek.models.model_upload_response import ModelUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelUploadResponse from a JSON string
model_upload_response_instance = ModelUploadResponse.from_json(json)
# print the JSON string representation of the object
print(ModelUploadResponse.to_json())

# convert the object into a dict
model_upload_response_dict = model_upload_response_instance.to_dict()
# create an instance of ModelUploadResponse from a dict
model_upload_response_from_dict = ModelUploadResponse.from_dict(model_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


