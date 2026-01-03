# TerminateSessionResponse

Response for session termination.  Attributes:     session_id: Session identifier     status: New session status (terminated)     terminated_at: Termination timestamp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session identifier | 
**status** | [**SessionStatus**](SessionStatus.md) | Session status (terminated) | 
**terminated_at** | **datetime** | Termination timestamp | 

## Example

```python
from mixpeek.models.terminate_session_response import TerminateSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateSessionResponse from a JSON string
terminate_session_response_instance = TerminateSessionResponse.from_json(json)
# print the JSON string representation of the object
print(TerminateSessionResponse.to_json())

# convert the object into a dict
terminate_session_response_dict = terminate_session_response_instance.to_dict()
# create an instance of TerminateSessionResponse from a dict
terminate_session_response_from_dict = TerminateSessionResponse.from_dict(terminate_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


