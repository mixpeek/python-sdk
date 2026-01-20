# BenchmarkResponse

Response containing benchmark details and results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark_id** | **str** | Unique benchmark identifier. | 
**benchmark_name** | **str** | Human-readable name. | 
**baseline_retriever_id** | **str** | Baseline retriever ID. | 
**candidate_retriever_ids** | **List[str]** | Candidate retriever IDs. | 
**session_filter** | [**SessionFilterOutput**](SessionFilterOutput.md) | Filter criteria used. | [optional] 
**session_count** | **int** | Number of sessions in benchmark. | 
**status** | [**BenchmarkStatus**](BenchmarkStatus.md) | Current benchmark status. | 
**results** | [**List[BenchmarkResult]**](BenchmarkResult.md) | Results per pipeline (available when completed). | [optional] 
**comparison** | [**BenchmarkComparison**](BenchmarkComparison.md) | Statistical comparison (available when completed). | [optional] 
**created_at** | **datetime** | Creation timestamp. | 
**started_at** | **datetime** | Execution start time. | [optional] 
**completed_at** | **datetime** | Completion time. | [optional] 
**error_message** | **str** | Error message if failed. | [optional] 

## Example

```python
from mixpeek.models.benchmark_response import BenchmarkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BenchmarkResponse from a JSON string
benchmark_response_instance = BenchmarkResponse.from_json(json)
# print the JSON string representation of the object
print(BenchmarkResponse.to_json())

# convert the object into a dict
benchmark_response_dict = benchmark_response_instance.to_dict()
# create an instance of BenchmarkResponse from a dict
benchmark_response_from_dict = BenchmarkResponse.from_dict(benchmark_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


