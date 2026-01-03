# StageBreakdownResponse

Stage breakdown response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_id** | **str** | Retriever identifier | 
**stages** | [**List[StagePerformanceMetrics]**](StagePerformanceMetrics.md) | Stage metrics | 
**total_latency_ms** | **float** | Total pipeline latency | 

## Example

```python
from mixpeek.models.stage_breakdown_response import StageBreakdownResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StageBreakdownResponse from a JSON string
stage_breakdown_response_instance = StageBreakdownResponse.from_json(json)
# print the JSON string representation of the object
print(StageBreakdownResponse.to_json())

# convert the object into a dict
stage_breakdown_response_dict = stage_breakdown_response_instance.to_dict()
# create an instance of StageBreakdownResponse from a dict
stage_breakdown_response_from_dict = StageBreakdownResponse.from_dict(stage_breakdown_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


