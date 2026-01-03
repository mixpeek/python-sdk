# Credentials3

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
from mixpeek.models.credentials3 import Credentials3

# TODO update the JSON string below
json = "{}"
# create an instance of Credentials3 from a JSON string
credentials3_instance = Credentials3.from_json(json)
# print the JSON string representation of the object
print(Credentials3.to_json())

# convert the object into a dict
credentials3_dict = credentials3_instance.to_dict()
# create an instance of Credentials3 from a dict
credentials3_from_dict = Credentials3.from_dict(credentials3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


