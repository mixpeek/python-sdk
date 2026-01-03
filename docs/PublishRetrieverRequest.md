# PublishRetrieverRequest

Request to publish a retriever.  Requires public_name. display_config is optional - if not provided, the retriever's stored display_config will be used (if available).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_name** | **str** | Public URL-safe name (lowercase, numbers, hyphens only). Must start and end with alphanumeric character. Will be used in URL: apps.mixpeek.com/r/{public_name} | 
**description** | **str** | Description of this public retriever. Explains what the retriever does and what it searches. Displayed in public listings and search results. | [optional] 
**icon_base64** | **str** | Base64 encoded icon/favicon for this public retriever. Data URI format recommended. Max size: ~200KB encoded. Displayed in public listings and as the retriever&#39;s icon. | [optional] 
**display_config** | [**DisplayConfigInput**](DisplayConfigInput.md) | Display configuration defining how the public UI should be rendered. Includes input fields, theme, layout, and exposed result fields. If not provided, uses the retriever&#39;s stored display_config. | [optional] 
**rate_limit_config** | [**RateLimitConfig**](RateLimitConfig.md) | Rate limiting configuration for public endpoint. Defaults to STANDARD tier (10/min, 100/hour, 1k/day). Use ELEVATED tier for trusted public apps (30/min, 500/hour, 5k/day). Use ENTERPRISE tier for monitored deployments (100/min, 2k/hour, 20k/day). Custom limits override tier defaults. | [optional] 
**password_secret_name** | **str** | OPTIONAL. Name of organization secret containing password for access protection. If provided, users must send password via X-Retriever-Password header. | [optional] 
**include_metadata** | **bool** | Whether to capture and store retriever metadata (stages, collections, capabilities). Recommended: True for better developer experience and debugging. Default: True. | [optional] [default to True]

## Example

```python
from mixpeek.models.publish_retriever_request import PublishRetrieverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishRetrieverRequest from a JSON string
publish_retriever_request_instance = PublishRetrieverRequest.from_json(json)
# print the JSON string representation of the object
print(PublishRetrieverRequest.to_json())

# convert the object into a dict
publish_retriever_request_dict = publish_retriever_request_instance.to_dict()
# create an instance of PublishRetrieverRequest from a dict
publish_retriever_request_from_dict = PublishRetrieverRequest.from_dict(publish_retriever_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


