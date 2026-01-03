# AuditEventResponse

Single audit event in list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_id** | **str** | Unique audit event identifier | 
**timestamp** | **object** |  | 
**resource_type** | **str** | Type of resource affected | 
**resource_id** | **str** | ID of the affected resource | 
**action** | **str** | Action performed | 
**actor_id** | **str** | Who performed the action | 
**actor_type** | **str** | Type of actor | [optional] [default to 'user']
**status** | **str** | Status of the action | [optional] [default to 'success']
**changes** | **object** |  | [optional] 
**ip_address** | **str** | Request IP address | [optional] 
**user_agent** | **str** | Request user agent | [optional] 

## Example

```python
from mixpeek.models.audit_event_response import AuditEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEventResponse from a JSON string
audit_event_response_instance = AuditEventResponse.from_json(json)
# print the JSON string representation of the object
print(AuditEventResponse.to_json())

# convert the object into a dict
audit_event_response_dict = audit_event_response_instance.to_dict()
# create an instance of AuditEventResponse from a dict
audit_event_response_from_dict = AuditEventResponse.from_dict(audit_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


