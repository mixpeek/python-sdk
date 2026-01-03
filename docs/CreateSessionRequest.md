# CreateSessionRequest

Request payload for creating a new agent session.  Attributes:     agent_config: Agent configuration (model, temperature, tools, etc.)     quotas: Optional session quotas and rate limits     user_id: Optional user identifier     user_memory: Optional initial user memory/preferences     metadata: Optional session metadata  Example:     ```python     request = CreateSessionRequest(         agent_config=AgentConfig(             model=\"claude-3-5-sonnet-20241022\",             temperature=0.7,             available_tools=[\"search_retrievers\", \"execute_retriever\"]         ),         quotas=SessionQuotas(             max_messages=100,             max_tokens_total=100000         ),         user_id=\"user_123\",         user_memory={\"preferences\": {\"language\": \"en\"}}     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_config** | [**AgentConfig**](AgentConfig.md) | Agent configuration (REQUIRED) | 
**quotas** | [**SessionQuotas**](SessionQuotas.md) | Session quotas and rate limits (OPTIONAL) | [optional] 
**user_id** | **str** | User identifier (OPTIONAL) | [optional] 
**user_memory** | **Dict[str, object]** | Initial user memory/preferences (OPTIONAL) | [optional] 
**metadata** | **Dict[str, object]** | Session metadata (OPTIONAL) | [optional] 
**enable_memory** | **bool** | Enable semantic memory for conversation context (OPTIONAL, default: True) | [optional] [default to True]

## Example

```python
from mixpeek.models.create_session_request import CreateSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSessionRequest from a JSON string
create_session_request_instance = CreateSessionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSessionRequest.to_json())

# convert the object into a dict
create_session_request_dict = create_session_request_instance.to_dict()
# create an instance of CreateSessionRequest from a dict
create_session_request_from_dict = CreateSessionRequest.from_dict(create_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


