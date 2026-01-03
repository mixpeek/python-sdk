# UpdateSecretRequest

Request to update an existing secret in the organization vault.  Updates the encrypted value of an existing secret. The old value is permanently overwritten with no history or rollback capability.  **Use Cases**: - Rotate API keys periodically for security - Update expired tokens - Change credentials after security incident - Switch from test to production keys  **Security**: - Old value is permanently overwritten (no history) - New value is encrypted before storage - No rollback or undo capability - Update is logged for audit trail  **Requirements**: - secret_value: REQUIRED, new plaintext value - Secret must already exist (use POST to create)  **Permissions**: Requires ADMIN permission to update secrets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_value** | **str** | REQUIRED. New plaintext value for the secret. This will replace the existing encrypted value. The old value is permanently overwritten with no history. The new value will be encrypted at rest using Fernet encryption. Use this to rotate keys, update expired tokens, or change credentials. Format: any string (will be encrypted as-is). | 

## Example

```python
from mixpeek.models.update_secret_request import UpdateSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSecretRequest from a JSON string
update_secret_request_instance = UpdateSecretRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSecretRequest.to_json())

# convert the object into a dict
update_secret_request_dict = update_secret_request_instance.to_dict()
# create an instance of UpdateSecretRequest from a dict
update_secret_request_from_dict = UpdateSecretRequest.from_dict(update_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


