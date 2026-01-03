# PatchRetrieverResponse

Response after updating a retriever.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever** | [**RetrieverConfig**](RetrieverConfig.md) | Updated retriever configuration. | 

## Example

```python
from mixpeek.models.patch_retriever_response import PatchRetrieverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatchRetrieverResponse from a JSON string
patch_retriever_response_instance = PatchRetrieverResponse.from_json(json)
# print the JSON string representation of the object
print(PatchRetrieverResponse.to_json())

# convert the object into a dict
patch_retriever_response_dict = patch_retriever_response_instance.to_dict()
# create an instance of PatchRetrieverResponse from a dict
patch_retriever_response_from_dict = PatchRetrieverResponse.from_dict(patch_retriever_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


