# GoogleDriveConfig

Google Drive and Google Workspace shared drive configuration.  This configuration enables Mixpeek to connect to Google Drive for automated file ingestion and synchronization. Supports both personal Drive and Google Workspace shared drives (formerly Team Drives).  Authentication Options:     - Service Account: Recommended for production. No user interaction required.     - OAuth2: Suitable for personal Drive access or development.  Requirements:     - Google Drive API enabled in Google Cloud Console     - Appropriate authentication credentials configured     - Files/folders shared with the service account or OAuth user     - Network connectivity to drive.googleapis.com  Use Cases:     - Sync marketing materials from shared drives     - Ingest documents from team collaboration folders     - Monitor and process uploaded media files     - Archive and search historical documents

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] [default to 'google_drive']
**credentials** | [**Credentials**](Credentials.md) |  | 
**shared_drive_id** | **str** | NOT REQUIRED. Google Workspace shared drive (Team Drive) identifier. When provided, sync operations are scoped to this shared drive only. When omitted, syncs from &#39;My Drive&#39; of the authenticated account. Find ID: Open shared drive in browser, copy ID from URL. Format: 0A{alphanumeric-string} | [optional] 
**impersonate_user** | **str** | NOT REQUIRED. Email address to impersonate when using service account credentials. Requires domain-wide delegation to be enabled for the service account. Used in G Suite environments to access files as a specific user. When omitted, uses the service account&#39;s own access. Format: Valid email address in the G Suite domain. | [optional] 

## Example

```python
from mixpeek.models.google_drive_config import GoogleDriveConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDriveConfig from a JSON string
google_drive_config_instance = GoogleDriveConfig.from_json(json)
# print the JSON string representation of the object
print(GoogleDriveConfig.to_json())

# convert the object into a dict
google_drive_config_dict = google_drive_config_instance.to_dict()
# create an instance of GoogleDriveConfig from a dict
google_drive_config_from_dict = GoogleDriveConfig.from_dict(google_drive_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


