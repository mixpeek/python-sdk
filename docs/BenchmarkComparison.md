# BenchmarkComparison

Comparison of all candidates against the baseline.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline_retriever_id** | **str** | ID of the baseline pipeline. | 
**comparisons** | [**List[PipelineComparison]**](PipelineComparison.md) | Comparison results for each candidate. | 
**recommendation** | **str** | System-generated recommendation based on results. | [optional] 

## Example

```python
from mixpeek.models.benchmark_comparison import BenchmarkComparison

# TODO update the JSON string below
json = "{}"
# create an instance of BenchmarkComparison from a JSON string
benchmark_comparison_instance = BenchmarkComparison.from_json(json)
# print the JSON string representation of the object
print(BenchmarkComparison.to_json())

# convert the object into a dict
benchmark_comparison_dict = benchmark_comparison_instance.to_dict()
# create an instance of BenchmarkComparison from a dict
benchmark_comparison_from_dict = BenchmarkComparison.from_dict(benchmark_comparison_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


