# UpdatePublishedRetrieverRequest

Request to update a published retriever configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_config** | [**DisplayConfigInput**](DisplayConfigInput.md) | Update the display configuration | [optional] 
**rate_limit_config** | [**RateLimitConfig**](RateLimitConfig.md) | Update rate limiting configuration | [optional] 
**password_secret_name** | **str** | Update or remove password protection (set to empty string to remove) | [optional] 
**is_active** | **bool** | Activate or deactivate the published retriever | [optional] 

## Example

```python
from mixpeek.models.update_published_retriever_request import UpdatePublishedRetrieverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePublishedRetrieverRequest from a JSON string
update_published_retriever_request_instance = UpdatePublishedRetrieverRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePublishedRetrieverRequest.to_json())

# convert the object into a dict
update_published_retriever_request_dict = update_published_retriever_request_instance.to_dict()
# create an instance of UpdatePublishedRetrieverRequest from a dict
update_published_retriever_request_from_dict = UpdatePublishedRetrieverRequest.from_dict(update_published_retriever_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


