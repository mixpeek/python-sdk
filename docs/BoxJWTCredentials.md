# BoxJWTCredentials

Credentials for Box JWT (JSON Web Token) authentication.  JWT provides server-to-server authentication using a public/private key pair. Recommended for enterprise integrations requiring high security.  Prerequisites:     - Create a Box application with Server Authentication (with JWT)     - Generate a public/private key pair in the Developer Console     - Authorize the application in the Box Admin Console     - Download the JSON configuration file  Security:     - private_key encrypted at rest via CSFLE     - RSA key pair used for signing JWT assertions     - No user interaction required

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'jwt']
**client_id** | **str** | REQUIRED. Box application client ID. | 
**client_secret** | **str** | REQUIRED. Box application client secret. SECURITY: Encrypted at rest via CSFLE. | 
**enterprise_id** | **str** | REQUIRED. Box enterprise ID for JWT authentication. Find in: Box Admin Console &gt; Enterprise Settings. | 
**jwt_key_id** | **str** | REQUIRED. Public key ID registered with Box. Found in the JSON config file as &#39;publicKeyID&#39;. | 
**private_key** | **str** | REQUIRED. PEM-encoded RSA private key for JWT signing. SECURITY: Encrypted at rest via CSFLE. Never log or expose. Found in the JSON config file as &#39;privateKey&#39;. | 
**private_key_passphrase** | **str** | Passphrase for the private key if it is encrypted. SECURITY: Encrypted at rest via CSFLE. | [optional] 

## Example

```python
from mixpeek.models.box_jwt_credentials import BoxJWTCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of BoxJWTCredentials from a JSON string
box_jwt_credentials_instance = BoxJWTCredentials.from_json(json)
# print the JSON string representation of the object
print(BoxJWTCredentials.to_json())

# convert the object into a dict
box_jwt_credentials_dict = box_jwt_credentials_instance.to_dict()
# create an instance of BoxJWTCredentials from a dict
box_jwt_credentials_from_dict = BoxJWTCredentials.from_dict(box_jwt_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


