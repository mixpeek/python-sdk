# GoogleDriveServiceAccountCredentials

Credentials for Google Drive service account authentication.  Service accounts provide server-to-server authentication for Google Drive without requiring user interaction. They are ideal for automated sync operations.  Prerequisites:     - Create a service account in Google Cloud Console     - Enable Google Drive API for the project     - Download the JSON key file     - Share target Drive files/folders with the service account email  Security:     - private_key field is encrypted at rest using MongoDB client-side field level encryption     - Credentials never appear in logs or API responses     - Use domain-wide delegation for G Suite environments  Use Cases:     - Automated ingestion pipelines from shared drives     - Scheduled sync operations without user interaction     - Service-to-service integration for enterprise deployments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'service_account']
**project_id** | **str** | REQUIRED. Google Cloud project ID where the service account was created. Found in the JSON key file as &#39;project_id&#39;. Format: lowercase alphanumeric with hyphens (e.g., &#39;my-project-123&#39;). | 
**private_key_id** | **str** | REQUIRED. Unique identifier for the private key. Found in the JSON key file as &#39;private_key_id&#39;. Format: 40-character hexadecimal string. | 
**private_key** | **str** | REQUIRED. PEM-encoded RSA private key for authentication. Found in the JSON key file as &#39;private_key&#39;. SECURITY: This field is encrypted at rest. Never log or expose this value. Format: Must include BEGIN/END PRIVATE KEY markers. | 
**client_email** | **str** | REQUIRED. Service account email address. Found in the JSON key file as &#39;client_email&#39;. Share Drive files/folders with this email to grant access. Format: {account-name}@{project-id}.iam.gserviceaccount.com | 
**client_id** | **str** | REQUIRED. Numeric service account identifier. Found in the JSON key file as &#39;client_id&#39;. Format: 21-digit numeric string. | 

## Example

```python
from mixpeek.models.google_drive_service_account_credentials import GoogleDriveServiceAccountCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDriveServiceAccountCredentials from a JSON string
google_drive_service_account_credentials_instance = GoogleDriveServiceAccountCredentials.from_json(json)
# print the JSON string representation of the object
print(GoogleDriveServiceAccountCredentials.to_json())

# convert the object into a dict
google_drive_service_account_credentials_dict = google_drive_service_account_credentials_instance.to_dict()
# create an instance of GoogleDriveServiceAccountCredentials from a dict
google_drive_service_account_credentials_from_dict = GoogleDriveServiceAccountCredentials.from_dict(google_drive_service_account_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


