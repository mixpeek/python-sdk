# RetrieverAPIKeyListResponse

Response for listing retriever API keys.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[APIKeyModel]**](APIKeyModel.md) | List of API keys for the retriever (plaintext key never included). | [optional] 
**total** | **int** | Total number of keys (including revoked if requested). | [optional] [default to 0]

## Example

```python
from mixpeek.models.retriever_api_key_list_response import RetrieverAPIKeyListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverAPIKeyListResponse from a JSON string
retriever_api_key_list_response_instance = RetrieverAPIKeyListResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieverAPIKeyListResponse.to_json())

# convert the object into a dict
retriever_api_key_list_response_dict = retriever_api_key_list_response_instance.to_dict()
# create an instance of RetrieverAPIKeyListResponse from a dict
retriever_api_key_list_response_from_dict = RetrieverAPIKeyListResponse.from_dict(retriever_api_key_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


