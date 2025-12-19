# ListRetrieversRequest

List of retriever requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**LogicalOperatorInput**](LogicalOperatorInput.md) | Filters to apply when listing retrievers | [optional] 
**sorts** | [**List[SortOption]**](SortOption.md) | Sorting options for the retriever list | [optional] 
**search** | **str** | Search term for wildcard search across all text fields | [optional] 
**case_sensitive** | **bool** | If True, filters and search will be case-sensitive | [optional] [default to False]
**limit** | **int** | Pagination limit | [optional] [default to 10]
**offset** | **int** | Pagination offset | [optional] [default to 0]

## Example

```python
from mixpeek.models.list_retrievers_request import ListRetrieversRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListRetrieversRequest from a JSON string
list_retrievers_request_instance = ListRetrieversRequest.from_json(json)
# print the JSON string representation of the object
print(ListRetrieversRequest.to_json())

# convert the object into a dict
list_retrievers_request_dict = list_retrievers_request_instance.to_dict()
# create an instance of ListRetrieversRequest from a dict
list_retrievers_request_from_dict = ListRetrieversRequest.from_dict(list_retrievers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


