# RetrieverExecutionStatistics

Aggregated execution statistics for an entire retriever execution run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stages** | [**Dict[str, StageStatistics]**](StageStatistics.md) | Per-stage statistics keyed by stage instance name (REQUIRED). | [optional] 
**total_time_ms** | **float** | Total retriever execution time in milliseconds (REQUIRED). | [optional] [default to 0.0]
**credits_used** | **float** | Total credits consumed across all stages (OPTIONAL in MVP). | [optional] [default to 0.0]

## Example

```python
from mixpeek.models.retriever_execution_statistics import RetrieverExecutionStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverExecutionStatistics from a JSON string
retriever_execution_statistics_instance = RetrieverExecutionStatistics.from_json(json)
# print the JSON string representation of the object
print(RetrieverExecutionStatistics.to_json())

# convert the object into a dict
retriever_execution_statistics_dict = retriever_execution_statistics_instance.to_dict()
# create an instance of RetrieverExecutionStatistics from a dict
retriever_execution_statistics_from_dict = RetrieverExecutionStatistics.from_dict(retriever_execution_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


