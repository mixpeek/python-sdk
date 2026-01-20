# DynamicValue3

A value that should be dynamically resolved from the query request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'dynamic']
**var_field** | **str** | The dot-notation path to the value in the runtime query request, e.g., &#39;inputs.user_id&#39; | 

## Example

```python
from mixpeek.models.dynamic_value3 import DynamicValue3

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicValue3 from a JSON string
dynamic_value3_instance = DynamicValue3.from_json(json)
# print the JSON string representation of the object
print(DynamicValue3.to_json())

# convert the object into a dict
dynamic_value3_dict = dynamic_value3_instance.to_dict()
# create an instance of DynamicValue3 from a dict
dynamic_value3_from_dict = DynamicValue3.from_dict(dynamic_value3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


