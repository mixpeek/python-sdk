# PublishedRetrieverResponse

Response model for GET published retriever.  Returns the full published retriever config including the public API key since the user already has access to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retriever_id** | **str** | ID of the underlying retriever | 
**public_id** | **str** | Public identifier for this published retriever | 
**public_name** | **str** | Public URL-safe name | 
**description** | **str** | Description of this public retriever | [optional] 
**icon_base64** | **str** | Base64 encoded icon/favicon for this retriever | [optional] 
**public_api_key** | **str** | Public API key (safe to show to retriever owner) | 
**display_config** | [**DisplayConfigOutput**](DisplayConfigOutput.md) | Display configuration for UI rendering | 
**rate_limit_config** | [**RateLimitConfig**](RateLimitConfig.md) | Rate limiting configuration | 
**password_protected** | **bool** | Whether password protection is enabled | 
**is_active** | **bool** | Whether the published retriever is active | 
**retriever_metadata** | [**RetrieverMetadata**](RetrieverMetadata.md) | Optional technical metadata about the retriever | [optional] 
**created_at** | **datetime** | Timestamp when published | 
**updated_at** | **datetime** | Timestamp when last updated | 

## Example

```python
from mixpeek.models.published_retriever_response import PublishedRetrieverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublishedRetrieverResponse from a JSON string
published_retriever_response_instance = PublishedRetrieverResponse.from_json(json)
# print the JSON string representation of the object
print(PublishedRetrieverResponse.to_json())

# convert the object into a dict
published_retriever_response_dict = published_retriever_response_instance.to_dict()
# create an instance of PublishedRetrieverResponse from a dict
published_retriever_response_from_dict = PublishedRetrieverResponse.from_dict(published_retriever_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


