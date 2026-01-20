# ConfirmationRequest

Request to approve or deny a pending confirmation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **bool** | True to approve, False to deny the action | 

## Example

```python
from mixpeek.models.confirmation_request import ConfirmationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmationRequest from a JSON string
confirmation_request_instance = ConfirmationRequest.from_json(json)
# print the JSON string representation of the object
print(ConfirmationRequest.to_json())

# convert the object into a dict
confirmation_request_dict = confirmation_request_instance.to_dict()
# create an instance of ConfirmationRequest from a dict
confirmation_request_from_dict = ConfirmationRequest.from_dict(confirmation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


