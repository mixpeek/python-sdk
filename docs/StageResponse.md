# StageResponse

Standard response format for a single stage in a retriever pipeline.  Each stage execution returns an object of this type, containing the execution time, results, and any additional metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage_name** | **str** |  | 
**version** | **str** |  | 
**execution_time** | **float** |  | 
**results** | [**List[RetrieverResponseFinalResultsInner]**](RetrieverResponseFinalResultsInner.md) |  | 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from mixpeek.models.stage_response import StageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StageResponse from a JSON string
stage_response_instance = StageResponse.from_json(json)
# print the JSON string representation of the object
print(StageResponse.to_json())

# convert the object into a dict
stage_response_dict = stage_response_instance.to_dict()
# create an instance of StageResponse from a dict
stage_response_from_dict = StageResponse.from_dict(stage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


