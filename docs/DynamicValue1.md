# DynamicValue1

A value that should be dynamically resolved from the query request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'dynamic']
**var_field** | **str** | The dot-notation path to the value in the runtime query request, e.g., &#39;inputs.user_id&#39; | 

## Example

```python
from mixpeek.models.dynamic_value1 import DynamicValue1

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicValue1 from a JSON string
dynamic_value1_instance = DynamicValue1.from_json(json)
# print the JSON string representation of the object
print(DynamicValue1.to_json())

# convert the object into a dict
dynamic_value1_dict = dynamic_value1_instance.to_dict()
# create an instance of DynamicValue1 from a dict
dynamic_value1_from_dict = DynamicValue1.from_dict(dynamic_value1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


