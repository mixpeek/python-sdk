# CreateBenchmarkRequest

Request to create a new benchmark run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark_name** | **str** | Human-readable name for this benchmark. | 
**baseline_retriever_id** | **str** | ID of the baseline retriever pipeline to compare against. | 
**candidate_retriever_ids** | **List[str]** | IDs of candidate retriever pipelines to evaluate. | 
**session_filter** | [**SessionFilterInput**](SessionFilterInput.md) | Optional filter criteria for selecting sessions to replay. | [optional] 
**session_count** | **int** | Number of sessions to include in the benchmark. | [optional] [default to 1000]

## Example

```python
from mixpeek.models.create_benchmark_request import CreateBenchmarkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBenchmarkRequest from a JSON string
create_benchmark_request_instance = CreateBenchmarkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBenchmarkRequest.to_json())

# convert the object into a dict
create_benchmark_request_dict = create_benchmark_request_instance.to_dict()
# create an instance of CreateBenchmarkRequest from a dict
create_benchmark_request_from_dict = CreateBenchmarkRequest.from_dict(create_benchmark_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


