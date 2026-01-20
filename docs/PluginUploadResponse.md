# PluginUploadResponse

Response model for plugin upload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether upload succeeded | 
**plugin_id** | **str** | Unique plugin identifier | 
**validation_status** | **str** | Validation status | 
**validation_errors** | **List[str]** | Validation error messages if failed | [optional] 
**deployment_status** | **str** | Deployment status | 
**feature_uri** | **str** | Feature URI for the plugin | 
**s3_archive_url** | **str** | S3 URL where archive is stored | 

## Example

```python
from mixpeek.models.plugin_upload_response import PluginUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PluginUploadResponse from a JSON string
plugin_upload_response_instance = PluginUploadResponse.from_json(json)
# print the JSON string representation of the object
print(PluginUploadResponse.to_json())

# convert the object into a dict
plugin_upload_response_dict = plugin_upload_response_instance.to_dict()
# create an instance of PluginUploadResponse from a dict
plugin_upload_response_from_dict = PluginUploadResponse.from_dict(plugin_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


