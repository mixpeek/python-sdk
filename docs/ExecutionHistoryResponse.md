# ExecutionHistoryResponse

Cluster execution history response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** |  | 
**time_range** | [**ApiAnalyticsClustersModelsTimeRange**](ApiAnalyticsClustersModelsTimeRange.md) |  | 
**results** | [**List[ClusterExecutionMetric]**](ClusterExecutionMetric.md) |  | 
**summary** | **Dict[str, object]** |  | [optional] 

## Example

```python
from mixpeek.models.execution_history_response import ExecutionHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionHistoryResponse from a JSON string
execution_history_response_instance = ExecutionHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(ExecutionHistoryResponse.to_json())

# convert the object into a dict
execution_history_response_dict = execution_history_response_instance.to_dict()
# create an instance of ExecutionHistoryResponse from a dict
execution_history_response_from_dict = ExecutionHistoryResponse.from_dict(execution_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


