# EngineStageBreakdownResponse

Response for engine stage breakdown.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_range** | [**ApiAnalyticsModelsTimeRange**](ApiAnalyticsModelsTimeRange.md) | Time range of the analysis | 
**stages** | [**List[StagePerformanceOutput]**](StagePerformanceOutput.md) | Performance breakdown by stage | 
**total_time_ms** | **float** | Total time across all stages (sum) | 

## Example

```python
from mixpeek.models.engine_stage_breakdown_response import EngineStageBreakdownResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EngineStageBreakdownResponse from a JSON string
engine_stage_breakdown_response_instance = EngineStageBreakdownResponse.from_json(json)
# print the JSON string representation of the object
print(EngineStageBreakdownResponse.to_json())

# convert the object into a dict
engine_stage_breakdown_response_dict = engine_stage_breakdown_response_instance.to_dict()
# create an instance of EngineStageBreakdownResponse from a dict
engine_stage_breakdown_response_from_dict = EngineStageBreakdownResponse.from_dict(engine_stage_breakdown_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


