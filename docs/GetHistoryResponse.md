# GetHistoryResponse

Response for retrieving conversation history.  Attributes:     session_id: Session identifier     messages: List of messages in chronological order     total_messages: Total number of messages in session     returned_messages: Number of messages returned (may be limited)     has_more: Whether there are more messages available  Example:     ```python     response = GetHistoryResponse(         session_id=\"ses_abc123\",         messages=[...],         total_messages=50,         returned_messages=20,         has_more=True     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session identifier | 
**messages** | [**List[MessageHistoryItem]**](MessageHistoryItem.md) | Message history | 
**total_messages** | **int** | Total messages in session | 
**returned_messages** | **int** | Messages returned | 
**has_more** | **bool** | Whether more messages available | 

## Example

```python
from mixpeek.models.get_history_response import GetHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHistoryResponse from a JSON string
get_history_response_instance = GetHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(GetHistoryResponse.to_json())

# convert the object into a dict
get_history_response_dict = get_history_response_instance.to_dict()
# create an instance of GetHistoryResponse from a dict
get_history_response_from_dict = GetHistoryResponse.from_dict(get_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


