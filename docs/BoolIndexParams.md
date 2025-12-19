# BoolIndexParams

Configuration for boolean index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'bool']

## Example

```python
from mixpeek.models.bool_index_params import BoolIndexParams

# TODO update the JSON string below
json = "{}"
# create an instance of BoolIndexParams from a JSON string
bool_index_params_instance = BoolIndexParams.from_json(json)
# print the JSON string representation of the object
print(BoolIndexParams.to_json())

# convert the object into a dict
bool_index_params_dict = bool_index_params_instance.to_dict()
# create an instance of BoolIndexParams from a dict
bool_index_params_from_dict = BoolIndexParams.from_dict(bool_index_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


