# RetrieverAPIKeyResponse

Response model including the plaintext key (shown only once).  This response is returned immediately after key creation. The plaintext key is shown ONLY in this response and cannot be retrieved later. Users should save the key immediately for secure storage.  Security note:     The `key` field contains the plaintext secret and should be:     - Stored securely by the user (environment variables, secrets manager)     - Never committed to version control     - Never logged or exposed in error messages     - Rotated/revoked if accidentally exposed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Public identifier for the API key. | [optional] 
**key_hash** | **str** | SHA-256 hash of the plaintext key. | 
**key_prefix** | **str** | Visible prefix of the API key for user identification (e.g., &#39;sk_abc123...&#39;). Shows the first 10 characters of the plaintext key to help users identify which key is which in lists, without exposing the full secret. This follows industry best practices from GitHub, Stripe, and AWS. Generated automatically for new keys. Older keys may not have this field. | [optional] 
**key_type** | [**APIKeyType**](APIKeyType.md) | Type of API key. STANDARD for regular organization keys, MARKETPLACE_SUBSCRIPTION for marketplace subscription access tokens. | [optional] 
**subscription_id** | **str** | Marketplace subscription ID if this is a marketplace subscription key. Only set when key_type is MARKETPLACE_SUBSCRIPTION. | [optional] 
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
**allowed_origins** | **List[str]** | Optional list of allowed HTTP origins for this API key. When set, requests must include an Origin header matching one of these values. Supports exact matches (e.g., &#39;https://docs.example.com&#39;) and wildcard subdomains (e.g., &#39;https://*.example.com&#39;). Only enforced for browser requests (defense-in-depth, not a security boundary). Null means no origin restriction. | [optional] 
**key** | **str** | Plaintext API key (shown only once). Prefix: ret_sk_. Store securely immediately after creation. | 

## Example

```python
from mixpeek.models.retriever_api_key_response import RetrieverAPIKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverAPIKeyResponse from a JSON string
retriever_api_key_response_instance = RetrieverAPIKeyResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieverAPIKeyResponse.to_json())

# convert the object into a dict
retriever_api_key_response_dict = retriever_api_key_response_instance.to_dict()
# create an instance of RetrieverAPIKeyResponse from a dict
retriever_api_key_response_from_dict = RetrieverAPIKeyResponse.from_dict(retriever_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


