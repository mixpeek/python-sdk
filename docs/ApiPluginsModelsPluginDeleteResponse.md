# ApiPluginsModelsPluginDeleteResponse

Response model for plugin deletion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**plugin_id** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from mixpeek.models.api_plugins_models_plugin_delete_response import ApiPluginsModelsPluginDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPluginsModelsPluginDeleteResponse from a JSON string
api_plugins_models_plugin_delete_response_instance = ApiPluginsModelsPluginDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(ApiPluginsModelsPluginDeleteResponse.to_json())

# convert the object into a dict
api_plugins_models_plugin_delete_response_dict = api_plugins_models_plugin_delete_response_instance.to_dict()
# create an instance of ApiPluginsModelsPluginDeleteResponse from a dict
api_plugins_models_plugin_delete_response_from_dict = ApiPluginsModelsPluginDeleteResponse.from_dict(api_plugins_models_plugin_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


