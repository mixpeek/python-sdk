# SessionQuotas

Session-level quotas and rate limits.  These limits are enforced per-session to prevent runaway costs. All fields are optional - unset means unlimited.  Attributes:     max_messages: Maximum messages allowed in session (prevents long conversations)     max_tokens_total: Maximum cumulative tokens for session (cost control)     max_tool_calls: Maximum tool calls per session (limits API usage)     max_session_duration_minutes: Maximum session lifetime in minutes     rate_limit_messages_per_minute: Max messages per minute (prevents spam)  Example:     ```python     # Basic quotas for a demo session     quotas = SessionQuotas(         max_messages=50,         max_tokens_total=50000,         max_tool_calls=25     )      # Strict quotas for production     quotas = SessionQuotas(         max_messages=100,         max_tokens_total=100000,         max_tool_calls=50,         max_session_duration_minutes=60,         rate_limit_messages_per_minute=10     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_messages** | **int** | Maximum messages allowed in session. Unset &#x3D; unlimited. | [optional] 
**max_tokens_total** | **int** | Maximum cumulative tokens for session. Unset &#x3D; unlimited. | [optional] 
**max_tool_calls** | **int** | Maximum tool calls per session. Unset &#x3D; unlimited. | [optional] 
**max_session_duration_minutes** | **int** | Maximum session lifetime in minutes. Unset &#x3D; no time limit. | [optional] 
**rate_limit_messages_per_minute** | **int** | Max messages per minute to prevent spam. Unset &#x3D; unlimited. | [optional] 

## Example

```python
from mixpeek.models.session_quotas import SessionQuotas

# TODO update the JSON string below
json = "{}"
# create an instance of SessionQuotas from a JSON string
session_quotas_instance = SessionQuotas.from_json(json)
# print the JSON string representation of the object
print(SessionQuotas.to_json())

# convert the object into a dict
session_quotas_dict = session_quotas_instance.to_dict()
# create an instance of SessionQuotas from a dict
session_quotas_from_dict = SessionQuotas.from_dict(session_quotas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


