# ApiNamespacesPluginsModelsPluginDeleteResponse

Response model for plugin deletion.  Includes information about Ray Serve deployment removal if the plugin was deployed for realtime inference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**plugin_id** | **str** |  | 
**message** | **str** |  | 
**deployment_removed** | **bool** | True if a Ray Serve deployment was queued for removal via blue-green deployment | [optional] [default to False]

## Example

```python
from mixpeek.models.api_namespaces_plugins_models_plugin_delete_response import ApiNamespacesPluginsModelsPluginDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNamespacesPluginsModelsPluginDeleteResponse from a JSON string
api_namespaces_plugins_models_plugin_delete_response_instance = ApiNamespacesPluginsModelsPluginDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(ApiNamespacesPluginsModelsPluginDeleteResponse.to_json())

# convert the object into a dict
api_namespaces_plugins_models_plugin_delete_response_dict = api_namespaces_plugins_models_plugin_delete_response_instance.to_dict()
# create an instance of ApiNamespacesPluginsModelsPluginDeleteResponse from a dict
api_namespaces_plugins_models_plugin_delete_response_from_dict = ApiNamespacesPluginsModelsPluginDeleteResponse.from_dict(api_namespaces_plugins_models_plugin_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


