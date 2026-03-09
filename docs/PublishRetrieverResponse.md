# PublishRetrieverResponse

Response after successfully publishing a retriever.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_id** | **str** | Public identifier for this published retriever | 
**retriever_id** | **str** | ID of the underlying retriever | 
**public_url** | **str** | Full public URL to the retriever page | 
**short_url** | **str** | Short URL via mxp.co redirect (same as public_url) | 
**public_api_key** | **str** | DEPRECATED: API keys are no longer required for public retriever access. For programmatic SDK access, create a ret_sk_ key via the retrievers/{id}/keys endpoint. | [optional] 

## Example

```python
from mixpeek.models.publish_retriever_response import PublishRetrieverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublishRetrieverResponse from a JSON string
publish_retriever_response_instance = PublishRetrieverResponse.from_json(json)
# print the JSON string representation of the object
print(PublishRetrieverResponse.to_json())

# convert the object into a dict
publish_retriever_response_dict = publish_retriever_response_instance.to_dict()
# create an instance of PublishRetrieverResponse from a dict
publish_retriever_response_from_dict = PublishRetrieverResponse.from_dict(publish_retriever_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


