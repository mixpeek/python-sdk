# DocumentResponse

Response model for a single document.  This is the standard response format when fetching documents via API endpoints. Contains all document data plus optional presigned URLs for S3 blobs.  The document payload structure follows native Qdrant format:     - System fields are stored in `_internal` (lineage, metadata, blobs, etc.)     - User fields are at root level (brand_name, thumbnail_url, etc.)     - Only document_id and collection_id are Mixpeek IDs at root level     - No duplication between root and _internal  Query Parameters Affecting Response:     - return_url=true: Adds presigned_url to each document_blobs entry     - return_vectors=true: Includes embedding arrays in response  Use Cases:     - Display document details in UI     - Download source files or generated artifacts     - Understand document provenance and processing     - Access enrichment fields (flat) for filtering/display

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | REQUIRED. Unique identifier for the document. Format: &#39;doc_&#39; prefix + alphanumeric characters. Use for: API queries, references, filtering. | 
**collection_id** | **str** | REQUIRED. ID of the collection this document belongs to. Format: &#39;col_&#39; prefix + alphanumeric characters. Use for: Collection-scoped queries, filtering. | 
**document_blobs** | [**List[BlobURLRef]**](BlobURLRef.md) | Document blobs with presigned URLs when requested | [optional] 
**internal** | [**InternalPayloadModel**](InternalPayloadModel.md) | System-managed internal fields. Contains all Mixpeek-managed metadata including lineage, processing info, timestamps, and blob references. User-defined fields appear at root level alongside document_id and collection_id. | [optional] 

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


