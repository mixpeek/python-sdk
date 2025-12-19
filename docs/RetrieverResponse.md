# RetrieverResponse

Response from a retriever execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** | Unique identifier for the retriever execution | [optional] 
**execution_time** | **float** | Total execution time of the retriever pipeline. | [optional] [default to 0.0]
**stage_results** | [**List[StageResponse]**](StageResponse.md) | Results from each stage of the retriever pipeline. | [optional] 
**final_results** | [**List[RetrieverResponseFinalResultsInner]**](RetrieverResponseFinalResultsInner.md) | Final sorted and paginated results of the retriever execution. | [optional] 

## Example

```python
from mixpeek.models.retriever_response import RetrieverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverResponse from a JSON string
retriever_response_instance = RetrieverResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieverResponse.to_json())

# convert the object into a dict
retriever_response_dict = retriever_response_instance.to_dict()
# create an instance of RetrieverResponse from a dict
retriever_response_from_dict = RetrieverResponse.from_dict(retriever_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


