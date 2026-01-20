# ApiPluginsModelsPluginListResponse

Response model for listing plugins.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**plugins** | [**List[PluginListItem]**](PluginListItem.md) |  | 
**total** | **int** |  | 
**organization_id** | **str** |  | 

## Example

```python
from mixpeek.models.api_plugins_models_plugin_list_response import ApiPluginsModelsPluginListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPluginsModelsPluginListResponse from a JSON string
api_plugins_models_plugin_list_response_instance = ApiPluginsModelsPluginListResponse.from_json(json)
# print the JSON string representation of the object
print(ApiPluginsModelsPluginListResponse.to_json())

# convert the object into a dict
api_plugins_models_plugin_list_response_dict = api_plugins_models_plugin_list_response_instance.to_dict()
# create an instance of ApiPluginsModelsPluginListResponse from a dict
api_plugins_models_plugin_list_response_from_dict = ApiPluginsModelsPluginListResponse.from_dict(api_plugins_models_plugin_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


