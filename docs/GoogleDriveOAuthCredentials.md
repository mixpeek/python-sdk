# GoogleDriveOAuthCredentials

Credentials for Google Drive OAuth2 user authentication.  OAuth2 credentials provide access to Google Drive on behalf of a specific user. This authentication method is suitable when accessing personal Drive files or when service account delegation is not available.  Prerequisites:     - Create OAuth 2.0 credentials in Google Cloud Console     - Configure authorized redirect URIs     - Complete OAuth consent flow to obtain refresh token     - Ensure appropriate OAuth scopes are granted (drive.readonly or drive)  Security:     - client_secret and refresh_token are encrypted at rest     - Access tokens are automatically refreshed and cached temporarily     - Credentials are scoped to the user who granted consent  Use Cases:     - Personal Drive file access for individual users     - Prototyping and development without service account setup     - Environments where service account delegation is not feasible  Limitations:     - Requires user interaction during initial setup     - Access is limited to files the consenting user can access     - Refresh tokens can be revoked by the user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'oauth']
**client_id** | **str** | REQUIRED. OAuth 2.0 client ID from Google Cloud Console. Found in the API credentials section. Format: {id}.apps.googleusercontent.com | 
**client_secret** | **str** | REQUIRED. OAuth 2.0 client secret from Google Cloud Console. SECURITY: This field is encrypted at rest. Never log or expose this value. Format: Alphanumeric string from Google Cloud Console. | 
**refresh_token** | **str** | REQUIRED. Long-lived refresh token obtained during OAuth consent flow. Used to automatically obtain new access tokens without user interaction. SECURITY: Encrypted at rest. Can be revoked by user at any time. Obtain via: Complete OAuth flow with drive.readonly or drive scope. | 

## Example

```python
from mixpeek.models.google_drive_o_auth_credentials import GoogleDriveOAuthCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDriveOAuthCredentials from a JSON string
google_drive_o_auth_credentials_instance = GoogleDriveOAuthCredentials.from_json(json)
# print the JSON string representation of the object
print(GoogleDriveOAuthCredentials.to_json())

# convert the object into a dict
google_drive_o_auth_credentials_dict = google_drive_o_auth_credentials_instance.to_dict()
# create an instance of GoogleDriveOAuthCredentials from a dict
google_drive_o_auth_credentials_from_dict = GoogleDriveOAuthCredentials.from_dict(google_drive_o_auth_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


