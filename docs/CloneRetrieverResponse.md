# CloneRetrieverResponse

Response after cloning a retriever.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever** | [**RetrieverConfig**](RetrieverConfig.md) | Cloned retriever configuration with new retriever_id. | 
**source_retriever_id** | **str** | ID of the source retriever that was cloned. | 

## Example

```python
from mixpeek.models.clone_retriever_response import CloneRetrieverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloneRetrieverResponse from a JSON string
clone_retriever_response_instance = CloneRetrieverResponse.from_json(json)
# print the JSON string representation of the object
print(CloneRetrieverResponse.to_json())

# convert the object into a dict
clone_retriever_response_dict = clone_retriever_response_instance.to_dict()
# create an instance of CloneRetrieverResponse from a dict
clone_retriever_response_from_dict = CloneRetrieverResponse.from_dict(clone_retriever_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


