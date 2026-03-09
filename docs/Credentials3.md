# Credentials3

REQUIRED. Azure AD authentication credentials. Choose client_credentials for production (app-only) or delegated for user-level access. The 'type' field determines which authentication flow is used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'client_credentials']
**tenant_id** | **str** | REQUIRED. Azure AD tenant ID. Use &#39;common&#39; for multi-tenant apps, or specific tenant ID for single-tenant. | 
**client_id** | **str** | REQUIRED. Azure AD application (client) ID. | 
**client_secret** | **str** | REQUIRED. Azure AD client secret. SECURITY: Encrypted at rest via CSFLE. | 
**refresh_token** | **str** | REQUIRED. OAuth2 refresh token obtained from consent flow. SECURITY: Encrypted at rest. Can be revoked by user. Obtain via: Complete OAuth flow with Files.Read.All scope. | 

## Example

```python
from mixpeek.models.credentials3 import Credentials3

# TODO update the JSON string below
json = "{}"
# create an instance of Credentials3 from a JSON string
credentials3_instance = Credentials3.from_json(json)
# print the JSON string representation of the object
print(Credentials3.to_json())

# convert the object into a dict
credentials3_dict = credentials3_instance.to_dict()
# create an instance of Credentials3 from a dict
credentials3_from_dict = Credentials3.from_dict(credentials3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


