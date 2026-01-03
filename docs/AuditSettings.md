# AuditSettings

Organization audit configuration.  Controls audit logging behavior for the organization. Allows enabling read access auditing for compliance requirements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_auditing_enabled** | **bool** | When enabled, read operations (GET requests) are logged to the audit trail. This includes resource access like NAMESPACE_ACCESSED, BUCKET_ACCESSED, etc. Disabled by default to reduce audit log volume. Enable for compliance requirements that mandate tracking all resource access. | [optional] [default to False]

## Example

```python
from mixpeek.models.audit_settings import AuditSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuditSettings from a JSON string
audit_settings_instance = AuditSettings.from_json(json)
# print the JSON string representation of the object
print(AuditSettings.to_json())

# convert the object into a dict
audit_settings_dict = audit_settings_instance.to_dict()
# create an instance of AuditSettings from a dict
audit_settings_from_dict = AuditSettings.from_dict(audit_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


