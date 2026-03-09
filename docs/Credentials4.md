# Credentials4

REQUIRED. Authentication credentials for Snowflake. Choose key_pair for production (recommended) or username_password for simpler setup. The 'type' field determines which credential mechanism is used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'key_pair']
**username** | **str** | REQUIRED. Snowflake username (case-insensitive). | 
**private_key** | **str** | REQUIRED. PEM-encoded RSA private key for authentication. SECURITY: This field is encrypted at rest via CSFLE. Never log or expose. Format: -----BEGIN PRIVATE KEY-----...-----END PRIVATE KEY-----  | 
**private_key_passphrase** | **str** | NOT REQUIRED. Passphrase for encrypted private key. SECURITY: Encrypted at rest if provided. Use only if private key is passphrase-protected. | [optional] 
**password** | **str** | REQUIRED. Snowflake password for authentication. SECURITY: This field is encrypted at rest via CSFLE. Never log or expose. | 

## Example

```python
from mixpeek.models.credentials4 import Credentials4

# TODO update the JSON string below
json = "{}"
# create an instance of Credentials4 from a JSON string
credentials4_instance = Credentials4.from_json(json)
# print the JSON string representation of the object
print(Credentials4.to_json())

# convert the object into a dict
credentials4_dict = credentials4_instance.to_dict()
# create an instance of Credentials4 from a dict
credentials4_from_dict = Credentials4.from_dict(credentials4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


