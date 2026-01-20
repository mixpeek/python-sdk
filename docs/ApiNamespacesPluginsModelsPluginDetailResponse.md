# ApiNamespacesPluginsModelsPluginDetailResponse

Response model for plugin details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**plugin** | [**ApiNamespacesPluginsModelsPluginDocument**](ApiNamespacesPluginsModelsPluginDocument.md) |  | 
**presigned_download_url** | **str** | Presigned URL for downloading the plugin archive (valid for 1 hour) | [optional] 

## Example

```python
from mixpeek.models.api_namespaces_plugins_models_plugin_detail_response import ApiNamespacesPluginsModelsPluginDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNamespacesPluginsModelsPluginDetailResponse from a JSON string
api_namespaces_plugins_models_plugin_detail_response_instance = ApiNamespacesPluginsModelsPluginDetailResponse.from_json(json)
# print the JSON string representation of the object
print(ApiNamespacesPluginsModelsPluginDetailResponse.to_json())

# convert the object into a dict
api_namespaces_plugins_models_plugin_detail_response_dict = api_namespaces_plugins_models_plugin_detail_response_instance.to_dict()
# create an instance of ApiNamespacesPluginsModelsPluginDetailResponse from a dict
api_namespaces_plugins_models_plugin_detail_response_from_dict = ApiNamespacesPluginsModelsPluginDetailResponse.from_dict(api_namespaces_plugins_models_plugin_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


