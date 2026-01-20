# ApiNamespacesPluginsModelsCreatePluginUploadRequest

Request to generate a presigned URL for plugin archive upload.  This is step 1 of the presigned URL workflow: 1. POST /namespaces/{id}/plugins/uploads → Returns presigned_url + upload_id 2. PUT presigned_url with plugin archive (client uploads directly to S3) 3. POST /namespaces/{id}/plugins/uploads/{upload_id}/confirm → Validates and deploys  Requirements:     - name: Plugin name (e.g., 'my_custom_extractor')     - version: Semantic version (e.g., '1.0.0')     - file_size_bytes: Expected archive size for quota validation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Plugin name (alphanumeric with underscores, no spaces) | 
**version** | **str** | Semantic version string | 
**description** | **str** | Optional description of the plugin | [optional] 
**file_size_bytes** | **int** | Expected file size in bytes for quota validation | [optional] 
**presigned_url_expiration** | **int** | Presigned URL expiration time in seconds (1-24 hours) | [optional] [default to 3600]

## Example

```python
from mixpeek.models.api_namespaces_plugins_models_create_plugin_upload_request import ApiNamespacesPluginsModelsCreatePluginUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNamespacesPluginsModelsCreatePluginUploadRequest from a JSON string
api_namespaces_plugins_models_create_plugin_upload_request_instance = ApiNamespacesPluginsModelsCreatePluginUploadRequest.from_json(json)
# print the JSON string representation of the object
print(ApiNamespacesPluginsModelsCreatePluginUploadRequest.to_json())

# convert the object into a dict
api_namespaces_plugins_models_create_plugin_upload_request_dict = api_namespaces_plugins_models_create_plugin_upload_request_instance.to_dict()
# create an instance of ApiNamespacesPluginsModelsCreatePluginUploadRequest from a dict
api_namespaces_plugins_models_create_plugin_upload_request_from_dict = ApiNamespacesPluginsModelsCreatePluginUploadRequest.from_dict(api_namespaces_plugins_models_create_plugin_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


