# DynamicValue6

A value that should be dynamically resolved from the query request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'dynamic']
**var_field** | **str** | The dot-notation path to the value in the runtime query request, e.g., &#39;inputs.user_id&#39; | 

## Example

```python
from mixpeek.models.dynamic_value6 import DynamicValue6

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicValue6 from a JSON string
dynamic_value6_instance = DynamicValue6.from_json(json)
# print the JSON string representation of the object
print(DynamicValue6.to_json())

# convert the object into a dict
dynamic_value6_dict = dynamic_value6_instance.to_dict()
# create an instance of DynamicValue6 from a dict
dynamic_value6_from_dict = DynamicValue6.from_dict(dynamic_value6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


