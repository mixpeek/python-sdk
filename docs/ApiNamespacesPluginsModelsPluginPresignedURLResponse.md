# ApiNamespacesPluginsModelsPluginPresignedURLResponse

Response containing presigned URL for plugin upload.  After receiving this response: 1. PUT the plugin archive to `presigned_url` with Content-Type: application/gzip 2. Call POST /namespaces/{id}/plugins/uploads/{upload_id}/confirm to finalize

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **str** | Upload ID to use when confirming | 
**presigned_url** | **str** | S3 presigned URL for PUT upload | 
**s3_key** | **str** | S3 object key where file will be stored | 
**expires_at** | **datetime** | When the presigned URL expires | 
**namespace_id** | **str** | Target namespace | 
**name** | **str** | Plugin name | 
**version** | **str** | Plugin version | 

## Example

```python
from mixpeek.models.api_namespaces_plugins_models_plugin_presigned_url_response import ApiNamespacesPluginsModelsPluginPresignedURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNamespacesPluginsModelsPluginPresignedURLResponse from a JSON string
api_namespaces_plugins_models_plugin_presigned_url_response_instance = ApiNamespacesPluginsModelsPluginPresignedURLResponse.from_json(json)
# print the JSON string representation of the object
print(ApiNamespacesPluginsModelsPluginPresignedURLResponse.to_json())

# convert the object into a dict
api_namespaces_plugins_models_plugin_presigned_url_response_dict = api_namespaces_plugins_models_plugin_presigned_url_response_instance.to_dict()
# create an instance of ApiNamespacesPluginsModelsPluginPresignedURLResponse from a dict
api_namespaces_plugins_models_plugin_presigned_url_response_from_dict = ApiNamespacesPluginsModelsPluginPresignedURLResponse.from_dict(api_namespaces_plugins_models_plugin_presigned_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


