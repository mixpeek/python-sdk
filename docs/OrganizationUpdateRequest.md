# OrganizationUpdateRequest

Partial update payload for organization metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_name** | **str** | Updated display name for the organization. | [optional] 
**logo_url** | **str** | Updated organization logo URL (e.g., custom logo to override auto-generated logo). | [optional] 
**billing_email** | **str** | Updated billing contact email. | [optional] 
**metadata** | **object** | Replace metadata with provided dictionary when set. | [optional] 
**rate_limits** | [**BaseRateLimits**](BaseRateLimits.md) | Override the computed rate limits for the organization. | [optional] 

## Example

```python
from mixpeek.models.organization_update_request import OrganizationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUpdateRequest from a JSON string
organization_update_request_instance = OrganizationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationUpdateRequest.to_json())

# convert the object into a dict
organization_update_request_dict = organization_update_request_instance.to_dict()
# create an instance of OrganizationUpdateRequest from a dict
organization_update_request_from_dict = OrganizationUpdateRequest.from_dict(organization_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


