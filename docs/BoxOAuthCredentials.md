# BoxOAuthCredentials

Credentials for Box OAuth 2.0 authentication.  Box supports OAuth 2.0 with access and refresh tokens. The refresh token is used to automatically obtain new access tokens without user interaction.  Prerequisites:     - Create a Box application at https://developer.box.com     - Configure OAuth 2.0 with the appropriate scopes     - Complete the OAuth consent flow to obtain tokens  Security:     - client_secret, access_token, and refresh_token encrypted at rest via CSFLE     - Access tokens expire in ~60 minutes; refresh tokens used for renewal     - Token refresh happens automatically during sync execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'oauth']
**client_id** | **str** | REQUIRED. Box application client ID. Found in: Box Developer Console &gt; Your App &gt; Configuration &gt; OAuth 2.0 Credentials. | 
**client_secret** | **str** | REQUIRED. Box application client secret. SECURITY: Encrypted at rest via CSFLE. Never log or expose. Found in: Box Developer Console &gt; Your App &gt; Configuration. | 
**access_token** | **str** | REQUIRED. Box OAuth 2.0 access token. SECURITY: Encrypted at rest. Expires in ~60 minutes. | 
**refresh_token** | **str** | REQUIRED. Box OAuth 2.0 refresh token for automatic token renewal. SECURITY: Encrypted at rest. Single-use; new one issued on each refresh. | 

## Example

```python
from mixpeek.models.box_o_auth_credentials import BoxOAuthCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of BoxOAuthCredentials from a JSON string
box_o_auth_credentials_instance = BoxOAuthCredentials.from_json(json)
# print the JSON string representation of the object
print(BoxOAuthCredentials.to_json())

# convert the object into a dict
box_o_auth_credentials_dict = box_o_auth_credentials_instance.to_dict()
# create an instance of BoxOAuthCredentials from a dict
box_o_auth_credentials_from_dict = BoxOAuthCredentials.from_dict(box_o_auth_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


