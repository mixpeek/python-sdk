# ParametersValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ParameterType**](ParameterType.md) | The type of the parameter (e.g., &#39;fixed&#39;). | 
**value** | **object** |  | 

## Example

```python
from mixpeek.models.parameters_value import ParametersValue

# TODO update the JSON string below
json = "{}"
# create an instance of ParametersValue from a JSON string
parameters_value_instance = ParametersValue.from_json(json)
# print the JSON string representation of the object
print(ParametersValue.to_json())

# convert the object into a dict
parameters_value_dict = parameters_value_instance.to_dict()
# create an instance of ParametersValue from a dict
parameters_value_from_dict = ParametersValue.from_dict(parameters_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


