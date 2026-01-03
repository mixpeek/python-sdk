# SnowflakeKeyPairCredentials

Snowflake key pair authentication (RECOMMENDED for production).  Key pair authentication provides secure, password-less access to Snowflake. The private key is encrypted at rest using MongoDB CSFLE.  Prerequisites:     1. Generate RSA key pair (2048-bit minimum)     2. Extract public key and assign to Snowflake user     3. Store private key securely (encrypted)  Security:     - Private key encrypted at rest via CSFLE     - No password exposure     - Key rotation supported     - Recommended for production  Example:     Generate key pair:     ```bash     openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -nocrypt     openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub     ```      Assign public key to Snowflake user:     ```sql     ALTER USER mixpeek_sync SET RSA_PUBLIC_KEY='MIIBIjANBg...';     ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'key_pair']
**username** | **str** | Snowflake username for authentication | 
**private_key** | **str** | REQUIRED. PEM-encoded RSA private key for authentication. SECURITY: This field is encrypted at rest via CSFLE. Never log or expose. Format: -----BEGIN PRIVATE KEY-----...-----END PRIVATE KEY-----  | 
**private_key_passphrase** | **str** | NOT REQUIRED. Passphrase for encrypted private key. SECURITY: Encrypted at rest if provided. Use only if private key is passphrase-protected. | [optional] 

## Example

```python
from mixpeek.models.snowflake_key_pair_credentials import SnowflakeKeyPairCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeKeyPairCredentials from a JSON string
snowflake_key_pair_credentials_instance = SnowflakeKeyPairCredentials.from_json(json)
# print the JSON string representation of the object
print(SnowflakeKeyPairCredentials.to_json())

# convert the object into a dict
snowflake_key_pair_credentials_dict = snowflake_key_pair_credentials_instance.to_dict()
# create an instance of SnowflakeKeyPairCredentials from a dict
snowflake_key_pair_credentials_from_dict = SnowflakeKeyPairCredentials.from_dict(snowflake_key_pair_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


