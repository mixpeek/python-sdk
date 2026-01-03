# SlowQueriesResponse

Response for slow queries endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_id** | **str** | Namespace ID analyzed | 
**time_range_days** | **int** | Number of days analyzed | 
**latency_threshold_ms** | **float** | Latency threshold used | 
**slow_queries** | [**List[SlowQueryDetails]**](SlowQueryDetails.md) | Slow query details | 
**total_slow_queries** | **int** | Total slow queries found | 

## Example

```python
from mixpeek.models.slow_queries_response import SlowQueriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SlowQueriesResponse from a JSON string
slow_queries_response_instance = SlowQueriesResponse.from_json(json)
# print the JSON string representation of the object
print(SlowQueriesResponse.to_json())

# convert the object into a dict
slow_queries_response_dict = slow_queries_response_instance.to_dict()
# create an instance of SlowQueriesResponse from a dict
slow_queries_response_from_dict = SlowQueriesResponse.from_dict(slow_queries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


