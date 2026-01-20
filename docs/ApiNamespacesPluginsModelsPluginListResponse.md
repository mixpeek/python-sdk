# ApiNamespacesPluginsModelsPluginListResponse

Response model for listing plugins.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**plugins** | [**List[PluginListItem]**](PluginListItem.md) |  | 
**total** | **int** |  | 
**namespace_id** | **str** |  | 

## Example

```python
from mixpeek.models.api_namespaces_plugins_models_plugin_list_response import ApiNamespacesPluginsModelsPluginListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNamespacesPluginsModelsPluginListResponse from a JSON string
api_namespaces_plugins_models_plugin_list_response_instance = ApiNamespacesPluginsModelsPluginListResponse.from_json(json)
# print the JSON string representation of the object
print(ApiNamespacesPluginsModelsPluginListResponse.to_json())

# convert the object into a dict
api_namespaces_plugins_models_plugin_list_response_dict = api_namespaces_plugins_models_plugin_list_response_instance.to_dict()
# create an instance of ApiNamespacesPluginsModelsPluginListResponse from a dict
api_namespaces_plugins_models_plugin_list_response_from_dict = ApiNamespacesPluginsModelsPluginListResponse.from_dict(api_namespaces_plugins_models_plugin_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


