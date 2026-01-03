# Credentials

REQUIRED. Authentication credentials for Google Drive API access. Choose service_account for production (recommended) or oauth for personal access. The 'type' field determines which credential type is used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'service_account']
**project_id** | **str** | REQUIRED. Google Cloud project ID where the service account was created. Found in the JSON key file as &#39;project_id&#39;. Format: lowercase alphanumeric with hyphens (e.g., &#39;my-project-123&#39;). | 
**private_key_id** | **str** | REQUIRED. Unique identifier for the private key. Found in the JSON key file as &#39;private_key_id&#39;. Format: 40-character hexadecimal string. | 
**private_key** | **str** | REQUIRED. PEM-encoded RSA private key for authentication. Found in the JSON key file as &#39;private_key&#39;. SECURITY: This field is encrypted at rest. Never log or expose this value. Format: Must include BEGIN/END PRIVATE KEY markers. | 
**client_email** | **str** | REQUIRED. Service account email address. Found in the JSON key file as &#39;client_email&#39;. Share Drive files/folders with this email to grant access. Format: {account-name}@{project-id}.iam.gserviceaccount.com | 
**client_id** | **str** | REQUIRED. OAuth 2.0 client ID from Google Cloud Console. Found in the API credentials section. Format: {id}.apps.googleusercontent.com | 
**client_secret** | **str** | REQUIRED. OAuth 2.0 client secret from Google Cloud Console. SECURITY: This field is encrypted at rest. Never log or expose this value. Format: Alphanumeric string from Google Cloud Console. | 
**refresh_token** | **str** | REQUIRED. Long-lived refresh token obtained during OAuth consent flow. Used to automatically obtain new access tokens without user interaction. SECURITY: Encrypted at rest. Can be revoked by user at any time. Obtain via: Complete OAuth flow with drive.readonly or drive scope. | 

## Example

```python
from mixpeek.models.credentials import Credentials

# TODO update the JSON string below
json = "{}"
# create an instance of Credentials from a JSON string
credentials_instance = Credentials.from_json(json)
# print the JSON string representation of the object
print(Credentials.to_json())

# convert the object into a dict
credentials_dict = credentials_instance.to_dict()
# create an instance of Credentials from a dict
credentials_from_dict = Credentials.from_dict(credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


