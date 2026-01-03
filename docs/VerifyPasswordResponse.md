# VerifyPasswordResponse

Response from password verification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | Whether the provided password is valid | 
**public_api_key** | **str** | Public API key for this retriever (only included if password is valid) | [optional] 

## Example

```python
from mixpeek.models.verify_password_response import VerifyPasswordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyPasswordResponse from a JSON string
verify_password_response_instance = VerifyPasswordResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyPasswordResponse.to_json())

# convert the object into a dict
verify_password_response_dict = verify_password_response_instance.to_dict()
# create an instance of VerifyPasswordResponse from a dict
verify_password_response_from_dict = VerifyPasswordResponse.from_dict(verify_password_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


