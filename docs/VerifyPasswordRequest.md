# VerifyPasswordRequest

Request to verify password for a password-protected retriever.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The password to verify against the retriever&#39;s password | 

## Example

```python
from mixpeek.models.verify_password_request import VerifyPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyPasswordRequest from a JSON string
verify_password_request_instance = VerifyPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyPasswordRequest.to_json())

# convert the object into a dict
verify_password_request_dict = verify_password_request_instance.to_dict()
# create an instance of VerifyPasswordRequest from a dict
verify_password_request_from_dict = VerifyPasswordRequest.from_dict(verify_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


