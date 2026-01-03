# APIKeyCreateRequest

Payload for creating a new API key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-friendly key label shown in dashboards. | 
**description** | **str** | Optional description explaining the key&#39;s purpose. | [optional] 
**permissions** | [**List[Permission]**](Permission.md) | Set of permissions granted to the API key (least privilege). | [optional] 
**scopes** | [**List[ResourceScopeInput]**](ResourceScopeInput.md) | Optional resource scope restrictions applied to the key. | [optional] 
**rate_limit_override** | **int** | Per-key requests-per-minute override (defaults to plan limit when absent). | [optional] 
**expires_at** | **datetime** | Optional UTC timestamp when the key automatically expires. | [optional] 

## Example

```python
from mixpeek.models.api_key_create_request import APIKeyCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyCreateRequest from a JSON string
api_key_create_request_instance = APIKeyCreateRequest.from_json(json)
# print the JSON string representation of the object
print(APIKeyCreateRequest.to_json())

# convert the object into a dict
api_key_create_request_dict = api_key_create_request_instance.to_dict()
# create an instance of APIKeyCreateRequest from a dict
api_key_create_request_from_dict = APIKeyCreateRequest.from_dict(api_key_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


