# Credentials

REQUIRED. Box authentication credentials. Choose 'oauth' for user-level access, 'ccg' for server-to-server (recommended), or 'jwt' for high-security enterprise. The 'type' field determines which authentication flow is used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'oauth']
**client_id** | **str** | REQUIRED. Box application client ID. | 
**client_secret** | **str** | REQUIRED. Box application client secret. SECURITY: Encrypted at rest via CSFLE. | 
**access_token** | **str** | REQUIRED. Box OAuth 2.0 access token. SECURITY: Encrypted at rest. Expires in ~60 minutes. | 
**refresh_token** | **str** | REQUIRED. Box OAuth 2.0 refresh token for automatic token renewal. SECURITY: Encrypted at rest. Single-use; new one issued on each refresh. | 
**enterprise_id** | **str** | REQUIRED. Box enterprise ID for JWT authentication. Find in: Box Admin Console &gt; Enterprise Settings. | 
**user_id** | **str** | User ID to authenticate as. Used when the app needs to act as a specific managed user. Mutually exclusive with enterprise_id for token acquisition. | [optional] 
**jwt_key_id** | **str** | REQUIRED. Public key ID registered with Box. Found in the JSON config file as &#39;publicKeyID&#39;. | 
**private_key** | **str** | REQUIRED. PEM-encoded RSA private key for JWT signing. SECURITY: Encrypted at rest via CSFLE. Never log or expose. Found in the JSON config file as &#39;privateKey&#39;. | 
**private_key_passphrase** | **str** | Passphrase for the private key if it is encrypted. SECURITY: Encrypted at rest via CSFLE. | [optional] 

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


