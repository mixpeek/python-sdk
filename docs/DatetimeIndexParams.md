# DatetimeIndexParams

Configuration for datetime index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'datetime']

## Example

```python
from mixpeek.models.datetime_index_params import DatetimeIndexParams

# TODO update the JSON string below
json = "{}"
# create an instance of DatetimeIndexParams from a JSON string
datetime_index_params_instance = DatetimeIndexParams.from_json(json)
# print the JSON string representation of the object
print(DatetimeIndexParams.to_json())

# convert the object into a dict
datetime_index_params_dict = datetime_index_params_instance.to_dict()
# create an instance of DatetimeIndexParams from a dict
datetime_index_params_from_dict = DatetimeIndexParams.from_dict(datetime_index_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


