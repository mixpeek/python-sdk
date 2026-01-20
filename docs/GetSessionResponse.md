# GetSessionResponse

Response for retrieving session metadata.  Attributes:     session_id: Session identifier     namespace_id: Namespace identifier     internal_id: Organization internal ID     user_id: Optional user identifier     session_name: Auto-generated session name (null until first message)     agent_config: Agent configuration     user_memory: User memory/preferences     status: Session status     message_count: Total messages in session     stats: Session statistics     created_at: Creation timestamp     updated_at: Last update timestamp     last_activity_at: Last activity timestamp     expires_at: Expiration timestamp  Example:     ```python     response = GetSessionResponse(         session_id=\"ses_abc123\",         namespace_id=\"ns_xyz789\",         internal_id=\"int_abc123\",         session_name=\"Video search for ML tutorials\",         agent_config=AgentConfig(...),         status=\"active\",         message_count=10,         stats=SessionStats(...)     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session identifier | 
**namespace_id** | **str** | Namespace identifier | 
**internal_id** | **str** | Organization internal ID | 
**user_id** | **str** | User identifier | [optional] 
**session_name** | **str** | Auto-generated session name based on first conversation | [optional] 
**agent_config** | [**AgentConfig**](AgentConfig.md) | Agent configuration | 
**user_memory** | **object** | User memory/preferences | [optional] 
**status** | [**SessionStatus**](SessionStatus.md) | Session status | 
**message_count** | **int** | Total messages in session | 
**stats** | [**SessionStats**](SessionStats.md) | Session statistics | 
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update timestamp | 
**last_activity_at** | **datetime** | Last activity timestamp | 
**expires_at** | **datetime** | Expiration timestamp | 

## Example

```python
from mixpeek.models.get_session_response import GetSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSessionResponse from a JSON string
get_session_response_instance = GetSessionResponse.from_json(json)
# print the JSON string representation of the object
print(GetSessionResponse.to_json())

# convert the object into a dict
get_session_response_dict = get_session_response_instance.to_dict()
# create an instance of GetSessionResponse from a dict
get_session_response_from_dict = GetSessionResponse.from_dict(get_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


