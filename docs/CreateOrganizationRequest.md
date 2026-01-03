# CreateOrganizationRequest

Payload for creating a new organization (private/admin endpoint).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_name** | **str** | Display name for the organization. | 
**logo_url** | **str** | Organization logo URL (e.g., from Google Favicon service). If not provided, will be auto-generated from first user&#39;s email domain. | [optional] 
**users** | [**List[UserCreateRequest]**](UserCreateRequest.md) | Initial users to create with the organization. | [optional] 
**metadata** | **Dict[str, object]** | Custom metadata for the organization. | [optional] 
**credit_count** | **int** | Initial credit count for the organization. Defaults to 1000 if not provided. | [optional] 
**account_type** | **str** | Account type for the organization (free, pro, team, enterprise). Defaults to &#39;free&#39;. | [optional] 

## Example

```python
from mixpeek.models.create_organization_request import CreateOrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationRequest from a JSON string
create_organization_request_instance = CreateOrganizationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationRequest.to_json())

# convert the object into a dict
create_organization_request_dict = create_organization_request_instance.to_dict()
# create an instance of CreateOrganizationRequest from a dict
create_organization_request_from_dict = CreateOrganizationRequest.from_dict(create_organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


