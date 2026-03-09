# GrowthMetricsResponse

Document growth trends.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | 
**time_range** | [**ApiAnalyticsCollectionsModelsTimeRange**](ApiAnalyticsCollectionsModelsTimeRange.md) |  | 
**metrics** | [**List[GrowthMetric]**](GrowthMetric.md) |  | 
**summary** | **Dict[str, object]** |  | [optional] 

## Example

```python
from mixpeek.models.growth_metrics_response import GrowthMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GrowthMetricsResponse from a JSON string
growth_metrics_response_instance = GrowthMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(GrowthMetricsResponse.to_json())

# convert the object into a dict
growth_metrics_response_dict = growth_metrics_response_instance.to_dict()
# create an instance of GrowthMetricsResponse from a dict
growth_metrics_response_from_dict = GrowthMetricsResponse.from_dict(growth_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


