# BenchmarkListResponse

Response for listing benchmarks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmarks** | [**List[BenchmarkResponse]**](BenchmarkResponse.md) | List of benchmarks. | 
**total** | **int** | Total count matching filter. | 
**page** | **int** | Current page. | [optional] [default to 1]
**page_size** | **int** | Items per page. | [optional] [default to 20]

## Example

```python
from mixpeek.models.benchmark_list_response import BenchmarkListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BenchmarkListResponse from a JSON string
benchmark_list_response_instance = BenchmarkListResponse.from_json(json)
# print the JSON string representation of the object
print(BenchmarkListResponse.to_json())

# convert the object into a dict
benchmark_list_response_dict = benchmark_list_response_instance.to_dict()
# create an instance of BenchmarkListResponse from a dict
benchmark_list_response_from_dict = BenchmarkListResponse.from_dict(benchmark_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


