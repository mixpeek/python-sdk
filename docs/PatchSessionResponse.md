# PatchSessionResponse

Response for session update.  Attributes:     session_id: Session identifier     updated_at: Update timestamp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session identifier | 
**updated_at** | **datetime** | Update timestamp | 

## Example

```python
from mixpeek.models.patch_session_response import PatchSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSessionResponse from a JSON string
patch_session_response_instance = PatchSessionResponse.from_json(json)
# print the JSON string representation of the object
print(PatchSessionResponse.to_json())

# convert the object into a dict
patch_session_response_dict = patch_session_response_instance.to_dict()
# create an instance of PatchSessionResponse from a dict
patch_session_response_from_dict = PatchSessionResponse.from_dict(patch_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


