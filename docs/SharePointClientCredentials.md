# SharePointClientCredentials

SharePoint/OneDrive client credentials (app-only) authentication.  Client credentials flow provides application-level access without user interaction. Recommended for automated sync operations in enterprise environments.  Prerequisites:     1. Register an application in Azure AD (portal.azure.com)     2. Grant Microsoft Graph API permissions:        - Sites.Read.All (Application) - for SharePoint site access        - Files.Read.All (Application) - for file access     3. Admin consent granted for the permissions     4. Generate client secret  Security:     - client_secret encrypted at rest via CSFLE     - Provides application-level access to all sites (based on permissions)     - No user context - accesses files as the application itself     - Consider using certificate-based auth for production  Use Cases:     - Automated enterprise-wide document ingestion     - Background sync without user interaction     - Multi-tenant applications with admin consent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'client_credentials']
**tenant_id** | **str** | REQUIRED. Azure AD tenant ID (directory ID). Find in: Azure Portal &gt; Azure Active Directory &gt; Overview. Format: UUID (e.g., &#39;12345678-1234-1234-1234-123456789abc&#39;) | 
**client_id** | **str** | REQUIRED. Azure AD application (client) ID. Find in: Azure Portal &gt; App Registrations &gt; Your App &gt; Overview. Format: UUID | 
**client_secret** | **str** | REQUIRED. Azure AD client secret for authentication. SECURITY: This field is encrypted at rest via CSFLE. Never log or expose. Generate in: Azure Portal &gt; App Registrations &gt; Your App &gt; Certificates &amp; secrets. Note: Secrets expire; consider using certificates for production. | 

## Example

```python
from mixpeek.models.share_point_client_credentials import SharePointClientCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SharePointClientCredentials from a JSON string
share_point_client_credentials_instance = SharePointClientCredentials.from_json(json)
# print the JSON string representation of the object
print(SharePointClientCredentials.to_json())

# convert the object into a dict
share_point_client_credentials_dict = share_point_client_credentials_instance.to_dict()
# create an instance of SharePointClientCredentials from a dict
share_point_client_credentials_from_dict = SharePointClientCredentials.from_dict(share_point_client_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


