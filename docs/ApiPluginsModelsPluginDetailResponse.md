# ApiPluginsModelsPluginDetailResponse

Response model for plugin details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [default to True]
**plugin** | [**ApiPluginsModelsPluginDocument**](ApiPluginsModelsPluginDocument.md) |  | 

## Example

```python
from mixpeek.models.api_plugins_models_plugin_detail_response import ApiPluginsModelsPluginDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPluginsModelsPluginDetailResponse from a JSON string
api_plugins_models_plugin_detail_response_instance = ApiPluginsModelsPluginDetailResponse.from_json(json)
# print the JSON string representation of the object
print(ApiPluginsModelsPluginDetailResponse.to_json())

# convert the object into a dict
api_plugins_models_plugin_detail_response_dict = api_plugins_models_plugin_detail_response_instance.to_dict()
# create an instance of ApiPluginsModelsPluginDetailResponse from a dict
api_plugins_models_plugin_detail_response_from_dict = ApiPluginsModelsPluginDetailResponse.from_dict(api_plugins_models_plugin_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


