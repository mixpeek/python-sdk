# RetrieverPerformanceResponse

Retriever performance metrics response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_id** | **str** | Retriever identifier | 
**time_range** | [**ApiAnalyticsModelsTimeRange**](ApiAnalyticsModelsTimeRange.md) | Time range of the data | 
**metrics** | **List[object]** | Time-series performance metrics | 
**summary** | **object** | Aggregated summary statistics | [optional] 

## Example

```python
from mixpeek.models.retriever_performance_response import RetrieverPerformanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverPerformanceResponse from a JSON string
retriever_performance_response_instance = RetrieverPerformanceResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieverPerformanceResponse.to_json())

# convert the object into a dict
retriever_performance_response_dict = retriever_performance_response_instance.to_dict()
# create an instance of RetrieverPerformanceResponse from a dict
retriever_performance_response_from_dict = RetrieverPerformanceResponse.from_dict(retriever_performance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


