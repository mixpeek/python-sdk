# SendMessageRequest

Request payload for sending a message to the agent.  Attributes:     content: Message text content     metadata: Optional message metadata     stream: Whether to stream response as SSE (default: True)  Note:     When stream=True, the response will be Server-Sent Events (SSE).     When stream=False, the response will be a MessageResponse object.  Example:     ```python     # Streaming request (SSE)     request = SendMessageRequest(         content=\"Find videos about machine learning\",         stream=True     )      # Non-streaming request     request = SendMessageRequest(         content=\"Find videos about machine learning\",         stream=False     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Message text content (REQUIRED) | 
**metadata** | **Dict[str, object]** | Message metadata (OPTIONAL) | [optional] 
**stream** | **bool** | Stream response as SSE (default: True) | [optional] [default to True]

## Example

```python
from mixpeek.models.send_message_request import SendMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessageRequest from a JSON string
send_message_request_instance = SendMessageRequest.from_json(json)
# print the JSON string representation of the object
print(SendMessageRequest.to_json())

# convert the object into a dict
send_message_request_dict = send_message_request_instance.to_dict()
# create an instance of SendMessageRequest from a dict
send_message_request_from_dict = SendMessageRequest.from_dict(send_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


