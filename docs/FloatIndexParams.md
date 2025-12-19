# FloatIndexParams

Configuration for float index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'float']

## Example

```python
from mixpeek.models.float_index_params import FloatIndexParams

# TODO update the JSON string below
json = "{}"
# create an instance of FloatIndexParams from a JSON string
float_index_params_instance = FloatIndexParams.from_json(json)
# print the JSON string representation of the object
print(FloatIndexParams.to_json())

# convert the object into a dict
float_index_params_dict = float_index_params_instance.to_dict()
# create an instance of FloatIndexParams from a dict
float_index_params_from_dict = FloatIndexParams.from_dict(float_index_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


