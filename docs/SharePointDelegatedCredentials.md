# SharePointDelegatedCredentials

SharePoint/OneDrive delegated (user) authentication via OAuth2.  Delegated flow provides access on behalf of a specific user. Useful when you need to access files with user-level permissions.  Prerequisites:     1. Register an application in Azure AD     2. Grant Microsoft Graph API permissions:        - Sites.Read.All (Delegated) or Sites.Selected        - Files.Read.All (Delegated) or Files.Read     3. Configure redirect URI for OAuth flow     4. Complete OAuth consent to obtain refresh token  Security:     - client_secret and refresh_token encrypted at rest     - Access scoped to what the consenting user can access     - Refresh tokens can be revoked by user or admin  Use Cases:     - Personal OneDrive access     - User-specific SharePoint sites     - Respecting per-user permissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'delegated']
**tenant_id** | **str** | REQUIRED. Azure AD tenant ID. Use &#39;common&#39; for multi-tenant apps, or specific tenant ID for single-tenant. | 
**client_id** | **str** | REQUIRED. Azure AD application (client) ID. | 
**client_secret** | **str** | REQUIRED. Azure AD client secret. SECURITY: Encrypted at rest via CSFLE. | 
**refresh_token** | **str** | REQUIRED. OAuth2 refresh token obtained from consent flow. SECURITY: Encrypted at rest. Can be revoked by user. Obtain via: Complete OAuth flow with Files.Read.All scope. | 

## Example

```python
from mixpeek.models.share_point_delegated_credentials import SharePointDelegatedCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SharePointDelegatedCredentials from a JSON string
share_point_delegated_credentials_instance = SharePointDelegatedCredentials.from_json(json)
# print the JSON string representation of the object
print(SharePointDelegatedCredentials.to_json())

# convert the object into a dict
share_point_delegated_credentials_dict = share_point_delegated_credentials_instance.to_dict()
# create an instance of SharePointDelegatedCredentials from a dict
share_point_delegated_credentials_from_dict = SharePointDelegatedCredentials.from_dict(share_point_delegated_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


