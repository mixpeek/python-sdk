# CreateRetrieverAPIKeyRequest

Request payload for creating a retriever-scoped API key.  Retriever keys are automatically scoped to execute a specific retriever. The scope and permissions are auto-populated by the service layer and cannot be modified.  Example:     {         \"name\": \"production-api\",         \"description\": \"Production API key for customer integrations\",         \"expires_at\": \"2026-12-31T23:59:59Z\"     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-friendly key label for identification. | 
**description** | **str** | Optional description explaining the key&#39;s purpose. | [optional] 
**expires_at** | **datetime** | Optional UTC timestamp when the key automatically expires. | [optional] 
**allowed_origins** | **List[str]** | Optional list of allowed HTTP origins for this API key. When set, browser requests must include a matching Origin header. Supports exact matches and wildcard subdomains (e.g., &#39;https://*.example.com&#39;). Defense-in-depth: Origin headers can be spoofed from non-browser contexts. | [optional] 

## Example

```python
from mixpeek.models.create_retriever_api_key_request import CreateRetrieverAPIKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRetrieverAPIKeyRequest from a JSON string
create_retriever_api_key_request_instance = CreateRetrieverAPIKeyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRetrieverAPIKeyRequest.to_json())

# convert the object into a dict
create_retriever_api_key_request_dict = create_retriever_api_key_request_instance.to_dict()
# create an instance of CreateRetrieverAPIKeyRequest from a dict
create_retriever_api_key_request_from_dict = CreateRetrieverAPIKeyRequest.from_dict(create_retriever_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


