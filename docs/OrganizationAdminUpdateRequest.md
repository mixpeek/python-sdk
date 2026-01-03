# OrganizationAdminUpdateRequest

Admin-only update payload for organization.  Security: This model is ONLY used by private admin endpoints that require MIXPEEK_PRIVATE_TOKEN authentication. Regular users cannot access or modify these fields, especially infrastructure configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | [**AccountTier**](AccountTier.md) | Update organization billing tier. | [optional] 
**rate_limits** | [**BaseRateLimits**](BaseRateLimits.md) | Override rate limits for the organization. | [optional] 
**infrastructure** | [**OrganizationInfrastructure**](OrganizationInfrastructure.md) | 🔒 ADMIN ONLY: Configure dedicated infrastructure (Qdrant/Ray). This field is ONLY accessible via private admin endpoints with MIXPEEK_PRIVATE_TOKEN. NOT exposed in public API responses. NOT modifiable by organization users. Used for ENTERPRISE customers with dedicated infrastructure. | [optional] 

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


