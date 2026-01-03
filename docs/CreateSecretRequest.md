# CreateSecretRequest

Request to create a new secret in the organization vault.  Secrets are encrypted at rest using Fernet encryption and stored in the organization document. Use secrets to securely store API keys, tokens, and credentials for external services.  **Use Cases**: - Store API keys for Stripe, GitHub, OpenAI, etc. - Manage authentication tokens for api_call retriever stage - Store credentials for third-party integrations  **Security**: - Secret values are encrypted using ENCRYPTION_KEY from environment - Decrypted values are NEVER returned in API responses - Only secret names are exposed in list operations - Access is logged for audit trail  **Requirements**: - secret_name: REQUIRED, must be unique within organization - secret_value: REQUIRED, plaintext value to encrypt  **Permissions**: Requires ADMIN permission to create secrets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_name** | **str** | REQUIRED. Name/key for the secret. Use descriptive names that indicate the service and purpose. Must be unique within the organization. Format: lowercase with underscores (e.g., &#39;stripe_api_key&#39;). Common patterns: &#39;{service}_{type}_{environment}&#39; like &#39;stripe_api_key_prod&#39;. This name is used to reference the secret in api_call stage configuration. Examples: &#39;stripe_api_key&#39;, &#39;github_token&#39;, &#39;openai_api_key&#39;, &#39;weather_api_key&#39;. | 
**secret_value** | **str** | REQUIRED. Plaintext secret value to encrypt and store. This value will be encrypted at rest using Fernet encryption. The encrypted value is stored in MongoDB with the organization document. The plaintext value is NEVER logged or exposed in API responses. Only the secret name is visible when listing secrets. Use this field to store: API keys, tokens, passwords, credentials. Format: any string (will be encrypted as-is). For Basic auth, use format &#39;username:password&#39;. | 

## Example

```python
from mixpeek.models.create_secret_request import CreateSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSecretRequest from a JSON string
create_secret_request_instance = CreateSecretRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSecretRequest.to_json())

# convert the object into a dict
create_secret_request_dict = create_secret_request_instance.to_dict()
# create an instance of CreateSecretRequest from a dict
create_secret_request_from_dict = CreateSecretRequest.from_dict(create_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


