# MessageHistoryItem

Single message in conversation history.  Attributes:     message_id: Message identifier     role: Message role (user, assistant, tool)     content: Message text content     content_type: Content type (text, tool_call, tool_result)     tool_name: Tool name (if tool message)     tool_inputs: Tool inputs (if tool call)     tool_outputs: Tool outputs (if tool result)     tool_status: Tool execution status (if tool message)     timestamp: Message timestamp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Message identifier | 
**role** | **str** | Message role | 
**content** | **str** | Message content | 
**content_type** | **str** | Content type | 
**tool_name** | **str** | Tool name (if tool message) | [optional] 
**tool_inputs** | **str** | Tool inputs (if tool call) | [optional] 
**tool_outputs** | **str** | Tool outputs (if tool result) | [optional] 
**tool_status** | **str** | Tool status (if tool message) | [optional] 
**timestamp** | **datetime** | Message timestamp | 

## Example

```python
from mixpeek.models.message_history_item import MessageHistoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of MessageHistoryItem from a JSON string
message_history_item_instance = MessageHistoryItem.from_json(json)
# print the JSON string representation of the object
print(MessageHistoryItem.to_json())

# convert the object into a dict
message_history_item_dict = message_history_item_instance.to_dict()
# create an instance of MessageHistoryItem from a dict
message_history_item_from_dict = MessageHistoryItem.from_dict(message_history_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


