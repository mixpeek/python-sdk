# ListSessionsRequest

Request payload for listing sessions.  Attributes:     status: Optional status filter     filters: Optional additional filters     sort: Optional sort configuration  Example:     ```python     request = ListSessionsRequest(         status=\"active\",         filters={\"user_id\": \"user_123\"}     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**SessionStatus**](SessionStatus.md) | Filter by session status | [optional] 
**filters** | **Dict[str, object]** | Additional filters | [optional] 
**sort** | **Dict[str, object]** | Sort configuration | [optional] 

## Example

```python
from mixpeek.models.list_sessions_request import ListSessionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListSessionsRequest from a JSON string
list_sessions_request_instance = ListSessionsRequest.from_json(json)
# print the JSON string representation of the object
print(ListSessionsRequest.to_json())

# convert the object into a dict
list_sessions_request_dict = list_sessions_request_instance.to_dict()
# create an instance of ListSessionsRequest from a dict
list_sessions_request_from_dict = ListSessionsRequest.from_dict(list_sessions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


