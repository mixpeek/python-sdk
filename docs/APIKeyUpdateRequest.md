# APIKeyUpdateRequest

Partial update payload for an API key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New key label. | [optional] 
**description** | **str** | Updated description for the key. | [optional] 
**permissions** | [**List[Permission]**](Permission.md) | Replace existing permissions with the provided list. | [optional] 
**scopes** | [**List[ResourceScopeInput]**](ResourceScopeInput.md) | Replace existing scopes. Use empty list for global access. | [optional] 
**rate_limit_override** | **int** | Updated per-key rate limit override. | [optional] 
**expires_at** | **datetime** | New expiration timestamp. Use null to remove expiration. | [optional] 
**status** | [**KeyStatus**](KeyStatus.md) | Manually set key status (e.g. revoke). | [optional] 

## Example

```python
from mixpeek.models.api_key_update_request import APIKeyUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyUpdateRequest from a JSON string
api_key_update_request_instance = APIKeyUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(APIKeyUpdateRequest.to_json())

# convert the object into a dict
api_key_update_request_dict = api_key_update_request_instance.to_dict()
# create an instance of APIKeyUpdateRequest from a dict
api_key_update_request_from_dict = APIKeyUpdateRequest.from_dict(api_key_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


