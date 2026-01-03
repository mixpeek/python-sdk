# ListRetrieversResponse

Response from listing retrievers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[RetrieverModelOutput]**](RetrieverModelOutput.md) | List of retrievers in the namespace. | [optional] 
**total** | **int** | Total number of retrievers. | [optional] [default to 0]

## Example

```python
from mixpeek.models.list_retrievers_response import ListRetrieversResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListRetrieversResponse from a JSON string
list_retrievers_response_instance = ListRetrieversResponse.from_json(json)
# print the JSON string representation of the object
print(ListRetrieversResponse.to_json())

# convert the object into a dict
list_retrievers_response_dict = list_retrievers_response_instance.to_dict()
# create an instance of ListRetrieversResponse from a dict
list_retrievers_response_from_dict = ListRetrieversResponse.from_dict(list_retrievers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


