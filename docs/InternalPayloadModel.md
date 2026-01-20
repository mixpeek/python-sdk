# InternalPayloadModel

Complete _internal field structure for Qdrant document payloads.  All Mixpeek-managed system fields are namespaced under this structure to: - Prevent collision with user-defined fields - Provide clear separation of system vs user data - Enable filtering on internal fields via _internal.field_name paths  This structure is stored in Qdrant and returned in API responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_id** | **str** | Organization/tenant identifier for multi-tenancy isolation. | [optional] 
**namespace_id** | **str** | Namespace identifier within the organization. | [optional] 
**document_id** | **str** | Document identifier (also at root level for convenience). | [optional] 
**collection_id** | **str** | Collection identifier (also at root level for convenience). | [optional] 
**created_at** | **str** | ISO 8601 timestamp when document was created. | [optional] 
**updated_at** | **str** | ISO 8601 timestamp when document was last updated. | [optional] 
**lineage** | [**InternalLineageModel**](InternalLineageModel.md) | Document lineage and provenance tracking. | [optional] 
**processing** | [**InternalProcessingModel**](InternalProcessingModel.md) | Processing history and provenance metadata. | [optional] 
**source_blobs** | **List[object]** | Blobs that constituted the original source object. | [optional] 
**document_blobs** | **List[object]** | Blobs generated during document processing (thumbnails, etc.). | [optional] 
**source_details** | **List[object]** | Enrichment tracking and source detail entries. | [optional] 
**modality** | **str** | Content modality (text, image, video, audio, etc.). | [optional] 
**metadata** | **object** | System metadata including ingestion_status, feature_extractor_config_hash, and other processing-related information. | [optional] 
**mime_type** | **str** | MIME type of the source content. | [optional] 
**size_bytes** | **int** | Size of the source content in bytes. | [optional] 
**content_hash** | **str** | SHA256 hash of the source content for deduplication. | [optional] 

## Example

```python
from mixpeek.models.internal_payload_model import InternalPayloadModel

# TODO update the JSON string below
json = "{}"
# create an instance of InternalPayloadModel from a JSON string
internal_payload_model_instance = InternalPayloadModel.from_json(json)
# print the JSON string representation of the object
print(InternalPayloadModel.to_json())

# convert the object into a dict
internal_payload_model_dict = internal_payload_model_instance.to_dict()
# create an instance of InternalPayloadModel from a dict
internal_payload_model_from_dict = InternalPayloadModel.from_dict(internal_payload_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


