# CustomPluginParams

Parameters for custom plugin extractors.  This model accepts any extractor_type that doesn't match the builtin extractors, allowing custom plugins to define their own parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extractor_type** | **str** | Custom plugin extractor type (plugin name) | 

## Example

```python
from mixpeek.models.custom_plugin_params import CustomPluginParams

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPluginParams from a JSON string
custom_plugin_params_instance = CustomPluginParams.from_json(json)
# print the JSON string representation of the object
print(CustomPluginParams.to_json())

# convert the object into a dict
custom_plugin_params_dict = custom_plugin_params_instance.to_dict()
# create an instance of CustomPluginParams from a dict
custom_plugin_params_from_dict = CustomPluginParams.from_dict(custom_plugin_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


