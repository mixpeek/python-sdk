# DocumentResponse

Response model for a single document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | ID of the document | 
**collection_id** | **str** | ID of the collection | 
**object_id** | **str** | ID of the source object for this document | 
**enrichments** | [**Enrichments**](Enrichments.md) | Enrichments from clusters, taxonomies, joins, etc. | [optional] 
**source_blobs** | **List[Dict[str, object]]** | A list of the source blobs for the object. | [optional] 
**internal_metadata** | **Dict[str, object]** | Internal metadata calculated during processing. | [optional] 
**metadata** | **Dict[str, object]** | Metadata associated with the document | [optional] 
**vector** | **List[float]** | Vector embedding for the document | [optional] 
**presigned_url** | **str** | Deprecated. Use &#39;presigned_urls&#39; or document_blobs[*].presigned_url. | [optional] 
**document_blobs** | [**List[BlobURLRef]**](BlobURLRef.md) | Related blobs for this document (e.g., thumbnails, source). When return_url&#x3D;true, each BlobURLRef.presigned_url will be populated alongside the canonical url. | [optional] 
**presigned_urls** | [**List[PresignedURLModel]**](PresignedURLModel.md) | Aggregated presigned URLs keyed by logical name or filename. | [optional] 

## Example

```python
from mixpeek.models.document_response import DocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentResponse from a JSON string
document_response_instance = DocumentResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentResponse.to_json())

# convert the object into a dict
document_response_dict = document_response_instance.to_dict()
# create an instance of DocumentResponse from a dict
document_response_from_dict = DocumentResponse.from_dict(document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


