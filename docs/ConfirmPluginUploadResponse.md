# ConfirmPluginUploadResponse

Response from confirming a plugin upload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether upload and validation succeeded | 
**upload_id** | **str** | The upload ID | 
**plugin_id** | **str** | Created plugin ID if successful | [optional] 
**validation_status** | **str** | Validation status | 
**validation_errors** | **List[str]** | Validation errors if any | [optional] 
**deployment_status** | **str** | Deployment status | 
**feature_uri** | **str** | Feature URI for using the plugin | [optional] 
**s3_archive_url** | **str** | S3 URL of the archive | [optional] 
**message** | **str** | Additional status message | [optional] 

## Example

```python
from mixpeek.models.confirm_plugin_upload_response import ConfirmPluginUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmPluginUploadResponse from a JSON string
confirm_plugin_upload_response_instance = ConfirmPluginUploadResponse.from_json(json)
# print the JSON string representation of the object
print(ConfirmPluginUploadResponse.to_json())

# convert the object into a dict
confirm_plugin_upload_response_dict = confirm_plugin_upload_response_instance.to_dict()
# create an instance of ConfirmPluginUploadResponse from a dict
confirm_plugin_upload_response_from_dict = ConfirmPluginUploadResponse.from_dict(confirm_plugin_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


