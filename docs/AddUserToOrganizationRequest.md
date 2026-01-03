# AddUserToOrganizationRequest

Payload for adding users to an organization (private/admin endpoint).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_identifier** | **str** | Organization ID or name to add users to. | 
**logo_url** | **str** | Organization logo URL (e.g., from Google Favicon service). If provided and organization doesn&#39;t have a logo, this will be set. | [optional] 
**users** | [**List[UserCreateRequest]**](UserCreateRequest.md) | List of users to add to the organization. | 

## Example

```python
from mixpeek.models.add_user_to_organization_request import AddUserToOrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserToOrganizationRequest from a JSON string
add_user_to_organization_request_instance = AddUserToOrganizationRequest.from_json(json)
# print the JSON string representation of the object
print(AddUserToOrganizationRequest.to_json())

# convert the object into a dict
add_user_to_organization_request_dict = add_user_to_organization_request_instance.to_dict()
# create an instance of AddUserToOrganizationRequest from a dict
add_user_to_organization_request_from_dict = AddUserToOrganizationRequest.from_dict(add_user_to_organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


