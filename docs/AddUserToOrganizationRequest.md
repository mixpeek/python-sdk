# AddUserToOrganizationRequest

Add User to Organization Request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_identifier** | **str** |  | 
**users** | [**List[UserModelInput]**](UserModelInput.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

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


