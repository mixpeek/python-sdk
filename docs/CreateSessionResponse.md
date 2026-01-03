# CreateSessionResponse

Response for session creation.  Attributes:     session_id: Unique session identifier     namespace_id: Namespace identifier     internal_id: Organization internal ID     session_name: Auto-generated session name (null until first message)     status: Session status     created_at: Session creation timestamp     expires_at: Session expiration timestamp  Example:     ```python     response = CreateSessionResponse(         session_id=\"ses_abc123\",         namespace_id=\"ns_xyz789\",         internal_id=\"int_abc123\",         session_name=None,  # Will be set after first message         status=\"active\",         created_at=datetime.utcnow(),         expires_at=datetime.utcnow() + timedelta(days=7)     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Unique session identifier | 
**namespace_id** | **str** | Namespace identifier | 
**internal_id** | **str** | Organization internal ID | 
**session_name** | **str** | Auto-generated session name based on first conversation (set after first message) | [optional] 
**status** | [**SessionStatus**](SessionStatus.md) | Session status | 
**created_at** | **datetime** | Session creation timestamp | 
**expires_at** | **datetime** | Session expiration timestamp | 

## Example

```python
from mixpeek.models.create_session_response import CreateSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSessionResponse from a JSON string
create_session_response_instance = CreateSessionResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSessionResponse.to_json())

# convert the object into a dict
create_session_response_dict = create_session_response_instance.to_dict()
# create an instance of CreateSessionResponse from a dict
create_session_response_from_dict = CreateSessionResponse.from_dict(create_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


