# DocumentResult

Represents a single document result from a retrieval operation.  Retriever stages may not include full document lineage. To accommodate provider payloads, make certain fields optional and expose the raw provider payload.

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

## Example

```python
from mixpeek.models.document_result import DocumentResult

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentResult from a JSON string
document_result_instance = DocumentResult.from_json(json)
# print the JSON string representation of the object
print(DocumentResult.to_json())

# convert the object into a dict
document_result_dict = document_result_instance.to_dict()
# create an instance of DocumentResult from a dict
document_result_from_dict = DocumentResult.from_dict(document_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


