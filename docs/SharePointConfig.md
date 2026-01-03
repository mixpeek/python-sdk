# SharePointConfig

Microsoft SharePoint and OneDrive for Business configuration.  Enables Mixpeek to connect to SharePoint sites, document libraries, and OneDrive for Business for automated file ingestion and synchronization.  Architecture:     SharePoint hierarchy: Tenant → Sites → Drives (Document Libraries) → Items     - site_id: Identifies the SharePoint site     - drive_id: Identifies a specific document library within the site     - folder_path: Path within the document library  Authentication Methods:     1. Client Credentials (RECOMMENDED for production):         - App-only access without user interaction         - Requires admin consent for Graph API permissions         - Access level determined by app permissions      2. Delegated:         - User-level access via OAuth consent         - Access limited to user's permissions         - Requires refresh token management  Requirements:     - Azure AD application registration     - Microsoft Graph API permissions (Sites.Read.All, Files.Read.All)     - Network connectivity to graph.microsoft.com  Use Cases:     - Sync SharePoint document libraries     - Ingest enterprise collaboration files     - Monitor and process uploaded documents     - Archive compliance-sensitive materials  Example:     ```python     config = {         \"provider_type\": \"sharepoint\",         \"credentials\": {             \"type\": \"client_credentials\",             \"tenant_id\": \"12345678-...\",             \"client_id\": \"87654321-...\",             \"client_secret\": \"your-secret\",         },         \"site_id\": \"contoso.sharepoint.com,guid1,guid2\",         \"drive_id\": \"b!abc123...\",         \"folder_path\": \"/Shared Documents/Marketing\",     }     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] [default to 'sharepoint']
**credentials** | [**Credentials2**](Credentials2.md) |  | 
**site_id** | **str** | NOT REQUIRED if using personal OneDrive. SharePoint site identifier for targeting a specific site. Format: &#39;{hostname},{site-collection-id},{web-id}&#39; or site URL. Find via: Microsoft Graph API GET /sites?search&#x3D;{keyword} Example: &#39;contoso.sharepoint.com,12345678-...,87654321-...&#39; | [optional] 
**drive_id** | **str** | NOT REQUIRED if you want to use the default document library. Specific drive (document library) ID within the site. Find via: GET /sites/{site-id}/drives Format: Base64-encoded ID starting with &#39;b!&#39; | [optional] 
**folder_path** | **str** | NOT REQUIRED. Path within the drive to sync from. If omitted, syncs from the root of the drive. Format: Forward-slash separated path (e.g., &#39;/Documents/Marketing&#39;). Note: Leading slash is optional. | [optional] 

## Example

```python
from mixpeek.models.share_point_config import SharePointConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SharePointConfig from a JSON string
share_point_config_instance = SharePointConfig.from_json(json)
# print the JSON string representation of the object
print(SharePointConfig.to_json())

# convert the object into a dict
share_point_config_dict = share_point_config_instance.to_dict()
# create an instance of SharePointConfig from a dict
share_point_config_from_dict = SharePointConfig.from_dict(share_point_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


