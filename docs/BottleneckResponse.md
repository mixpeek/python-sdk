# BottleneckResponse

Response for bottleneck analysis.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_range** | [**ApiAnalyticsModelsTimeRange**](ApiAnalyticsModelsTimeRange.md) | Time range of the analysis | 
**bottlenecks** | [**List[BottleneckAnalysis]**](BottleneckAnalysis.md) | Ranked list of bottlenecks | 
**total_time_ms** | **float** | Total execution time across all components | 

## Example

```python
from mixpeek.models.bottleneck_response import BottleneckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BottleneckResponse from a JSON string
bottleneck_response_instance = BottleneckResponse.from_json(json)
# print the JSON string representation of the object
print(BottleneckResponse.to_json())

# convert the object into a dict
bottleneck_response_dict = bottleneck_response_instance.to_dict()
# create an instance of BottleneckResponse from a dict
bottleneck_response_from_dict = BottleneckResponse.from_dict(bottleneck_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


