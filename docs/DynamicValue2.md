# DynamicValue2

A value that should be dynamically resolved from the query request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'dynamic']
**var_field** | **str** | The dot-notation path to the value in the runtime query request, e.g., &#39;inputs.user_id&#39; | 

## Example

```python
from mixpeek.models.dynamic_value2 import DynamicValue2

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicValue2 from a JSON string
dynamic_value2_instance = DynamicValue2.from_json(json)
# print the JSON string representation of the object
print(DynamicValue2.to_json())

# convert the object into a dict
dynamic_value2_dict = dynamic_value2_instance.to_dict()
# create an instance of DynamicValue2 from a dict
dynamic_value2_from_dict = DynamicValue2.from_dict(dynamic_value2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


