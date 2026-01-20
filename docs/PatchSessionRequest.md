# PatchSessionRequest

Request payload for updating session metadata.  Only user_memory can be updated after session creation. To change agent_config or quotas, create a new session.  Attributes:     user_memory: Updated user memory/preferences  Example:     ```python     request = PatchSessionRequest(         user_memory={             \"preferences\": {\"language\": \"es\", \"domain\": \"science\"},             \"learned_context\": {\"favorite_topics\": [\"AI\", \"robotics\"]}         }     )     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_memory** | **object** | Updated user memory (REQUIRED) | 

## Example

```python
from mixpeek.models.patch_session_request import PatchSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSessionRequest from a JSON string
patch_session_request_instance = PatchSessionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchSessionRequest.to_json())

# convert the object into a dict
patch_session_request_dict = patch_session_request_instance.to_dict()
# create an instance of PatchSessionRequest from a dict
patch_session_request_from_dict = PatchSessionRequest.from_dict(patch_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


