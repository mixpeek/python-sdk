# StageStatistics

Execution metrics for a single stage in a retriever execution run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_count** | **int** | Number of documents received by the stage (REQUIRED). | 
**output_count** | **int** | Number of documents emitted by the stage (REQUIRED). | 
**duration_ms** | **float** | Wall-clock duration in milliseconds (REQUIRED). | 
**efficiency** | **float** | Output/Input ratio. 0 when input_count is 0 (REQUIRED). | 
**cache_hit** | **bool** | Indicates whether the result originated from stage cache (OPTIONAL). | [optional] 
**error** | **str** | Stage-specific error message if execution failed but retriever execution continued (OPTIONAL). | [optional] 
**llm_calls** | **int** | Number of LLM invocations performed by the stage (OPTIONAL). | [optional] 
**tokens_used** | **int** | Total tokens consumed by the stage (OPTIONAL, only for LLM stages). | [optional] 
**metadata** | **object** | Stage-specific metadata containing additional execution details (OPTIONAL). For example, join stages include: join_strategy, join_type, matched_count, match_rate, etc. LLM stages may include: model_name, temperature, max_tokens, etc. | [optional] 

## Example

```python
from mixpeek.models.stage_statistics import StageStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of StageStatistics from a JSON string
stage_statistics_instance = StageStatistics.from_json(json)
# print the JSON string representation of the object
print(StageStatistics.to_json())

# convert the object into a dict
stage_statistics_dict = stage_statistics_instance.to_dict()
# create an instance of StageStatistics from a dict
stage_statistics_from_dict = StageStatistics.from_dict(stage_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


