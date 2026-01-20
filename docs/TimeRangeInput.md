# TimeRangeInput

Time range filter for session queries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** | Start of time range (inclusive). | [optional] 
**end** | **datetime** | End of time range (inclusive). | [optional] 

## Example

```python
from mixpeek.models.time_range_input import TimeRangeInput

# TODO update the JSON string below
json = "{}"
# create an instance of TimeRangeInput from a JSON string
time_range_input_instance = TimeRangeInput.from_json(json)
# print the JSON string representation of the object
print(TimeRangeInput.to_json())

# convert the object into a dict
time_range_input_dict = time_range_input_instance.to_dict()
# create an instance of TimeRangeInput from a dict
time_range_input_from_dict = TimeRangeInput.from_dict(time_range_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


