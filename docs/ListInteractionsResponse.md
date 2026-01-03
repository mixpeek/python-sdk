# ListInteractionsResponse

Response for listing interactions with pagination.  Returns a paginated list of interaction records matching the query filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[InteractionResponse]**](InteractionResponse.md) | List of interactions matching the query filters | 
**pagination** | [**PaginationResponse**](PaginationResponse.md) | Pagination information for navigating result pages | 

## Example

```python
from mixpeek.models.list_interactions_response import ListInteractionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListInteractionsResponse from a JSON string
list_interactions_response_instance = ListInteractionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListInteractionsResponse.to_json())

# convert the object into a dict
list_interactions_response_dict = list_interactions_response_instance.to_dict()
# create an instance of ListInteractionsResponse from a dict
list_interactions_response_from_dict = ListInteractionsResponse.from_dict(list_interactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


