# CreateRetrieverResponse

Response after creating a retriever.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever** | [**RetrieverConfig**](RetrieverConfig.md) | Created retriever configuration. | 

## Example

```python
from mixpeek.models.create_retriever_response import CreateRetrieverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRetrieverResponse from a JSON string
create_retriever_response_instance = CreateRetrieverResponse.from_json(json)
# print the JSON string representation of the object
print(CreateRetrieverResponse.to_json())

# convert the object into a dict
create_retriever_response_dict = create_retriever_response_instance.to_dict()
# create an instance of CreateRetrieverResponse from a dict
create_retriever_response_from_dict = CreateRetrieverResponse.from_dict(create_retriever_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


