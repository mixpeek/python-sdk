# BenchmarkResult

Results for a single pipeline in a benchmark run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_id** | **str** | ID of the retriever/pipeline tested. | 
**retriever_name** | **str** | Human-readable name of the retriever. | 
**pipeline_hash** | **str** | Hash of the pipeline configuration. | 
**metrics** | [**AlignmentMetrics**](AlignmentMetrics.md) | Alignment metrics for this pipeline. | 
**taxonomy_deltas** | [**Dict[str, AlignmentMetrics]**](AlignmentMetrics.md) | Metrics broken down by taxonomy node (for understanding category-level performance). | [optional] 
**latency** | [**LatencyMetrics**](LatencyMetrics.md) | Performance timing statistics. | 
**failed_sessions** | **int** | Number of sessions that failed during replay. | 
**error_summary** | **Dict[str, int]** | Count of errors by type (error_type -&gt; count). | [optional] 

## Example

```python
from mixpeek.models.benchmark_result import BenchmarkResult

# TODO update the JSON string below
json = "{}"
# create an instance of BenchmarkResult from a JSON string
benchmark_result_instance = BenchmarkResult.from_json(json)
# print the JSON string representation of the object
print(BenchmarkResult.to_json())

# convert the object into a dict
benchmark_result_dict = benchmark_result_instance.to_dict()
# create an instance of BenchmarkResult from a dict
benchmark_result_from_dict = BenchmarkResult.from_dict(benchmark_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


