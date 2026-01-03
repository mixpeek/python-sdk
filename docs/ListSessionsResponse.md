# ListSessionsResponse

Response for listing sessions.  Attributes:     results: List of session summaries     total: Total number of sessions matching query     pagination: Pagination information  Example:     ```python     response = ListSessionsResponse(         results=[...],         total=50,         pagination={...}     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GetSessionResponse]**](GetSessionResponse.md) | Session list | 
**total** | **int** | Total matching sessions | 
**pagination** | **Dict[str, object]** | Pagination information | 

## Example

```python
from mixpeek.models.list_sessions_response import ListSessionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListSessionsResponse from a JSON string
list_sessions_response_instance = ListSessionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListSessionsResponse.to_json())

# convert the object into a dict
list_sessions_response_dict = list_sessions_response_instance.to_dict()
# create an instance of ListSessionsResponse from a dict
list_sessions_response_from_dict = ListSessionsResponse.from_dict(list_sessions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


