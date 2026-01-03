# SecretsListResponse

Response for listing secrets in the organization vault.  Returns ONLY secret names, never decrypted values. Use this endpoint to discover which secrets are configured in your organization.  **Security**: - Returns ONLY secret names, never values - Decrypted values never exposed via API - Use for auditing which secrets are configured  **Use Cases**: - Discover which secrets are configured - Audit secret inventory - Check if a secret exists before using it - Verify secret name spelling before referencing in api_call  **Permissions**: Requires READ permission to list secrets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | **List[str]** | List of secret names in the organization vault. Only names are returned, never decrypted values. Use these names as references in api_call stage configuration. Names are unique within the organization. Empty list if no secrets are configured. | 
**count** | **int** | Total number of secrets in the organization vault. This is the length of the secrets array. Useful for monitoring and auditing secret inventory. | 

## Example

```python
from mixpeek.models.secrets_list_response import SecretsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecretsListResponse from a JSON string
secrets_list_response_instance = SecretsListResponse.from_json(json)
# print the JSON string representation of the object
print(SecretsListResponse.to_json())

# convert the object into a dict
secrets_list_response_dict = secrets_list_response_instance.to_dict()
# create an instance of SecretsListResponse from a dict
secrets_list_response_from_dict = SecretsListResponse.from_dict(secrets_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


