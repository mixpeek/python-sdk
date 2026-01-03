# AuditSettingsUpdateRequest

Payload for updating audit settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_auditing_enabled** | **bool** | Enable or disable read operation auditing. | [optional] 

## Example

```python
from mixpeek.models.audit_settings_update_request import AuditSettingsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuditSettingsUpdateRequest from a JSON string
audit_settings_update_request_instance = AuditSettingsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AuditSettingsUpdateRequest.to_json())

# convert the object into a dict
audit_settings_update_request_dict = audit_settings_update_request_instance.to_dict()
# create an instance of AuditSettingsUpdateRequest from a dict
audit_settings_update_request_from_dict = AuditSettingsUpdateRequest.from_dict(audit_settings_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


