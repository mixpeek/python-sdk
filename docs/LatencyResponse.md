# LatencyResponse

Processing latency distribution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | 
**time_range** | [**ApiAnalyticsCollectionsModelsTimeRange**](ApiAnalyticsCollectionsModelsTimeRange.md) |  | 
**metrics** | [**List[LatencyMetric]**](LatencyMetric.md) |  | 
**slowest_documents** | **List[object]** |  | [optional] 

## Example

```python
from mixpeek.models.latency_response import LatencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LatencyResponse from a JSON string
latency_response_instance = LatencyResponse.from_json(json)
# print the JSON string representation of the object
print(LatencyResponse.to_json())

# convert the object into a dict
latency_response_dict = latency_response_instance.to_dict()
# create an instance of LatencyResponse from a dict
latency_response_from_dict = LatencyResponse.from_dict(latency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


