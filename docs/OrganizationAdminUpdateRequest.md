# OrganizationAdminUpdateRequest

Admin-only update request for organizations.  Allows changing the account tier and overriding rate limits.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | [**AccountTier**](AccountTier.md) |  | [optional] 
**rate_limits** | [**BaseRateLimits**](BaseRateLimits.md) |  | [optional] 

## Example

```python
from mixpeek.models.organization_admin_update_request import OrganizationAdminUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAdminUpdateRequest from a JSON string
organization_admin_update_request_instance = OrganizationAdminUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationAdminUpdateRequest.to_json())

# convert the object into a dict
organization_admin_update_request_dict = organization_admin_update_request_instance.to_dict()
# create an instance of OrganizationAdminUpdateRequest from a dict
organization_admin_update_request_from_dict = OrganizationAdminUpdateRequest.from_dict(organization_admin_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


