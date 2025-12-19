# RetrieverResponseFinalResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | ID of the document | [optional] 
**collection_id** | **str** | ID of the collection (optional in retriever outputs) | [optional] 
**object_id** | **str** | ID of the source object (optional in retriever outputs) | [optional] 
**enrichments** | [**Enrichments**](Enrichments.md) | Enrichments from clusters, taxonomies, joins, etc. | [optional] 
**internal_metadata** | **Dict[str, object]** | Internal metadata calculated during processing. | [optional] 
**metadata** | **Dict[str, object]** | Metadata associated with the document, user provided | [optional] 
**source_blobs** | **List[Dict[str, object]]** | Blobs that constituted the original source object (lightweight). | [optional] 
**document_blobs** | [**List[BlobURLRef]**](BlobURLRef.md) | Related blobs (thumbnails, sources, artifacts) for this document. Each entry should use a stable field like &#39;thumbnail&#39; or &#39;source&#39; rather than dot-paths; chunk ordinals can be inferred from filenames or tracked separately. | [optional] 
**presigned_urls** | [**List[PresignedURLModel]**](PresignedURLModel.md) | Aggregated presigned URL entries for related blobs. Populated by API when return_url&#x3D;true. | [optional] 
**score** | **float** | Relevance score of the document in the search results. | [optional] 
**payload** | **Dict[str, object]** | Raw provider payload (e.g., Qdrant hit payload) | [optional] 
**var_field** | **str** | The field by which the results were grouped. | 
**key** | **object** |  | 
**group** | [**List[DocumentResult]**](DocumentResult.md) | The documents belonging to this group. | 

## Example

```python
from mixpeek.models.retriever_response_final_results_inner import RetrieverResponseFinalResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieverResponseFinalResultsInner from a JSON string
retriever_response_final_results_inner_instance = RetrieverResponseFinalResultsInner.from_json(json)
# print the JSON string representation of the object
print(RetrieverResponseFinalResultsInner.to_json())

# convert the object into a dict
retriever_response_final_results_inner_dict = retriever_response_final_results_inner_instance.to_dict()
# create an instance of RetrieverResponseFinalResultsInner from a dict
retriever_response_final_results_inner_from_dict = RetrieverResponseFinalResultsInner.from_dict(retriever_response_final_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


