# DocsSearchResponse

Response after provisioning a docs search pipeline.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_key** | **str** | Retriever-scoped API key (ret_sk_...) for widget authentication. | 
**public_name** | **str** | Public retriever name for API access. | 
**retriever_id** | **str** | ID of the created retriever. | 
**collection_id** | **str** | ID of the web crawl collection. | 
**batch_id** | **str** | ID of the crawl batch (if processing started). | [optional] 
**namespace_id** | **str** | Namespace ID for all resources. | 
**bucket_id** | **str** | Bucket ID where seed URLs are stored. | 
**embed_snippet** | **str** | HTML snippet for drop-in integration. | 
**react_snippet** | **str** | React component snippet. | 

## Example

```python
from mixpeek.models.docs_search_response import DocsSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocsSearchResponse from a JSON string
docs_search_response_instance = DocsSearchResponse.from_json(json)
# print the JSON string representation of the object
print(DocsSearchResponse.to_json())

# convert the object into a dict
docs_search_response_dict = docs_search_response_instance.to_dict()
# create an instance of DocsSearchResponse from a dict
docs_search_response_from_dict = DocsSearchResponse.from_dict(docs_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


