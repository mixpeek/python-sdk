# ParameterConfig

A typed value for a feature extractor parameter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ParameterType**](ParameterType.md) | The type of the parameter (e.g., &#39;fixed&#39;). | 
**value** | **object** |  | 

## Example

```python
from mixpeek.models.parameter_config import ParameterConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterConfig from a JSON string
parameter_config_instance = ParameterConfig.from_json(json)
# print the JSON string representation of the object
print(ParameterConfig.to_json())

# convert the object into a dict
parameter_config_dict = parameter_config_instance.to_dict()
# create an instance of ParameterConfig from a dict
parameter_config_from_dict = ParameterConfig.from_dict(parameter_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


