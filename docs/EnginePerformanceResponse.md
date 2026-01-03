# EnginePerformanceResponse

Response for engine performance query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_range** | [**ApiAnalyticsModelsTimeRange**](ApiAnalyticsModelsTimeRange.md) | Time range of the query | 
**metrics** | [**List[PerformanceMetric]**](PerformanceMetric.md) | Time-series performance metrics | 
**summary** | [**PerformanceSummary**](PerformanceSummary.md) | Overall summary statistics | [optional] 

## Example

```python
from mixpeek.models.engine_performance_response import EnginePerformanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnginePerformanceResponse from a JSON string
engine_performance_response_instance = EnginePerformanceResponse.from_json(json)
# print the JSON string representation of the object
print(EnginePerformanceResponse.to_json())

# convert the object into a dict
engine_performance_response_dict = engine_performance_response_instance.to_dict()
# create an instance of EnginePerformanceResponse from a dict
engine_performance_response_from_dict = EnginePerformanceResponse.from_dict(engine_performance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


