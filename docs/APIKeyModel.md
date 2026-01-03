# APIKeyModel

API key document stored in MongoDB.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Public identifier for the API key. | [optional] 
**key_hash** | **str** | SHA-256 hash of the plaintext key. | 
**key_prefix** | **str** | Visible prefix of the API key for user identification (e.g., &#39;sk_abc123...&#39;). Shows the first 10 characters of the plaintext key to help users identify which key is which in lists, without exposing the full secret. This follows industry best practices from GitHub, Stripe, and AWS. Generated automatically for new keys. Older keys may not have this field. | [optional] 
**internal_id** | **str** | Organization internal identifier. | 
**organization_id** | **str** | Organization public identifier (denormalized). | [optional] 
**user_id** | **str** | Identifier of the user who owns the key. | 
**name** | **str** | Human-friendly key label. | 
**description** | **str** | Optional description explaining the key usage. | [optional] [default to '']
**permissions** | [**List[Permission]**](Permission.md) | Permissions granted to the key (least privilege recommended). | [optional] 
**scopes** | [**List[ResourceScopeOutput]**](ResourceScopeOutput.md) | Resource-level scopes restricting the key. | [optional] 
**rate_limit_override** | **int** | Optional per-key rate limit override in requests per minute. | [optional] 
**status** | [**KeyStatus**](KeyStatus.md) | Lifecycle status of the key (active, revoked, expired). | [optional] 
**expires_at** | **datetime** | UTC timestamp when the key automatically expires. | [optional] 
**last_used_at** | **datetime** | UTC timestamp of the last successful request using the key. | [optional] 
**created_at** | **datetime** | UTC timestamp when the key was created. | [optional] 
**created_by** | **str** | User identifier that created the key. | [optional] 
**revoked_at** | **datetime** | UTC timestamp when the key was revoked (if applicable). | [optional] 
**revoked_by** | **str** | User identifier that revoked the key (if applicable). | [optional] 

## Example

```python
from mixpeek.models.api_key_model import APIKeyModel

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyModel from a JSON string
api_key_model_instance = APIKeyModel.from_json(json)
# print the JSON string representation of the object
print(APIKeyModel.to_json())

# convert the object into a dict
api_key_model_dict = api_key_model_instance.to_dict()
# create an instance of APIKeyModel from a dict
api_key_model_from_dict = APIKeyModel.from_dict(api_key_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


