# IntegerIndexParams

Configuration for integer index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'integer']
**lookup** | **bool** |  | [optional] [default to True]
**range** | **bool** |  | [optional] [default to True]

## Example

```python
from mixpeek.models.integer_index_params import IntegerIndexParams

# TODO update the JSON string below
json = "{}"
# create an instance of IntegerIndexParams from a JSON string
integer_index_params_instance = IntegerIndexParams.from_json(json)
# print the JSON string representation of the object
print(IntegerIndexParams.to_json())

# convert the object into a dict
integer_index_params_dict = integer_index_params_instance.to_dict()
# create an instance of IntegerIndexParams from a dict
integer_index_params_from_dict = IntegerIndexParams.from_dict(integer_index_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


