# ListRetrieversRequest

Request to list retrievers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | **str** | Search term for wildcard search across retriever_id, retriever_name, description, and other text fields | [optional] 
**filters** | **Dict[str, object]** | Filters to apply to the retriever list. Supports filtering by retriever_id or retriever_name. | [optional] 
**sorts** | **List[Dict[str, object]]** | Sort options for the retriever list | [optional] 
**case_sensitive** | **bool** | If True, filters and search will be case-sensitive | [optional] [default to False]

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


