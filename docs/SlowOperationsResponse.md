# SlowOperationsResponse

Response for slowest operations query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_range** | [**ApiAnalyticsModelsTimeRange**](ApiAnalyticsModelsTimeRange.md) | Time range of the query | 
**operations** | [**List[SlowOperation]**](SlowOperation.md) | List of slowest operations | 
**threshold_ms** | **float** | Latency threshold used for filtering | 

## Example

```python
from mixpeek.models.slow_operations_response import SlowOperationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SlowOperationsResponse from a JSON string
slow_operations_response_instance = SlowOperationsResponse.from_json(json)
# print the JSON string representation of the object
print(SlowOperationsResponse.to_json())

# convert the object into a dict
slow_operations_response_dict = slow_operations_response_instance.to_dict()
# create an instance of SlowOperationsResponse from a dict
slow_operations_response_from_dict = SlowOperationsResponse.from_dict(slow_operations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


