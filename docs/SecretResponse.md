# SecretResponse

Response for secret operations (NEVER includes actual decrypted value).  This response is returned after creating, updating, or deleting a secret. For security, the actual secret value is NEVER included in API responses. Only the secret name and operation status are returned.  **Security**: - Decrypted secret values are NEVER included - Only secret name and operation status returned - Actual value only accessible by internal services  **Fields**: - secret_name: Name of the secret that was operated on - created: True if secret was created (null for other operations) - updated: True if secret was updated (null for other operations) - deleted: True if secret was deleted (null for other operations)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_name** | **str** | Name of the secret that was operated on. This is the same name provided in the request. Use this name to reference the secret in api_call stage configuration. | 
**created** | **bool** | True if this secret was created, null otherwise. Only set for POST /secrets operations. | [optional] 
**updated** | **bool** | True if this secret was updated, null otherwise. Only set for PUT /secrets/{name} operations. | [optional] 
**deleted** | **bool** | True if this secret was deleted, null otherwise. Only set for DELETE /secrets/{name} operations. | [optional] 

## Example

```python
from mixpeek.models.secret_response import SecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecretResponse from a JSON string
secret_response_instance = SecretResponse.from_json(json)
# print the JSON string representation of the object
print(SecretResponse.to_json())

# convert the object into a dict
secret_response_dict = secret_response_instance.to_dict()
# create an instance of SecretResponse from a dict
secret_response_from_dict = SecretResponse.from_dict(secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


