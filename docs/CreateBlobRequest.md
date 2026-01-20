# CreateBlobRequest

Request model for creating a new blob.  ⚠️  IMPORTANT: For presigned URL uploads, use the existing /buckets/{id}/uploads system!     DO NOT create a new presigned upload endpoint - one already exists.  Supports two modes:  Mode 1: Direct Data Upload     - Provide 'data' field with URL or base64 content     - File is processed immediately during object creation     - Use for: Small files, public URLs, inline data  Mode 2: Upload Reference (Recommended for large files)     - First: POST /buckets/{id}/uploads → Returns presigned_url + upload_id     - User uploads file directly to S3 via presigned_url     - Then: POST /uploads/{upload_id}/confirm → Validates upload     - Finally: Reference upload_id in this blob request     - Use for: Large files, client-side uploads, multi-blob objects  Why upload_id?     - Combine multiple uploads into one object     - Upload files in parallel, create object later     - Reuse uploads across multiple objects     - Better UX: upload progress, retry logic, validation  Related Endpoints:     - POST /buckets/{id}/uploads - Generate presigned URLs (EXISTING SYSTEM)     - POST /uploads/{id}/confirm - Confirm upload completed     - See: api/buckets/uploads/services.py for full upload workflow  Examples:     # Direct data (simple)     {       \"property\": \"thumbnail\",       \"type\": \"IMAGE\",       \"data\": \"https://example.com/image.jpg\"     }      # Upload reference (recommended)     {       \"property\": \"video\",       \"type\": \"VIDEO\",       \"upload_id\": \"upl_abc123\"  # From /uploads endpoint     }      # Multiple uploads → one object     {       \"blobs\": [         {\"property\": \"video\", \"upload_id\": \"upl_video123\"},         {\"property\": \"thumbnail\", \"upload_id\": \"upl_thumb456\"},         {\"property\": \"transcript\", \"upload_id\": \"upl_trans789\"}       ]     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | REQUIRED. Property name from the bucket schema that this blob belongs to. Must match a field defined in the bucket&#39;s schema. Used to validate blob type compatibility and determine storage path. Common values: &#39;video&#39;, &#39;thumbnail&#39;, &#39;transcript&#39;, &#39;document&#39;, &#39;image&#39; | 
**key_prefix** | **str** | OPTIONAL. Storage path prefix for organizing blobs within the bucket. If not provided, uses default bucket organization. Use for: grouping blobs by campaign, date, category, etc. Example: &#39;campaigns/summer_2025&#39; or &#39;products/electronics&#39; | [optional] 
**type** | [**BucketSchemaFieldType**](BucketSchemaFieldType.md) | REQUIRED. The schema field type for this blob. Must match the bucket schema definition for the property. Determines validation rules and processing pipeline. Common types: IMAGE, VIDEO, AUDIO, PDF, DOCUMENT, TEXT | 
**data** | [**Data**](Data.md) |  | [optional] 
**upload_id** | **str** | EITHER upload_id OR data must be provided. Reference to an existing upload from the presigned URL workflow.   ⚠️  PRESIGNED URLS: Use existing POST /buckets/{id}/uploads endpoint! It already handles presigned URL generation, upload tracking, and validation. DO NOT create a new /presigned-upload endpoint - it&#39;s redundant.   Workflow: 1. POST /buckets/{id}/uploads → {upload_id, presigned_url} 2. User uploads file to presigned_url 3. POST /uploads/{upload_id}/confirm → Validates upload 4. Use upload_id here to reference the uploaded file   The upload must be in CONFIRMED or ACTIVE status. Format: &#39;upl_&#39; prefix followed by alphanumeric characters.   Use Cases: - Combine multiple uploads into one object - Upload files in parallel, create object later - Reuse same upload across multiple objects   See: api/buckets/uploads/ for the complete upload system | [optional] 
**metadata** | **object** | Metadata for the blob, this will only be applied to the documents that use this blob | [optional] 
**canonicalize_source** | **bool** | If set, override object-level default to control source canonicalization for this blob. | [optional] 
**force_remirror** | **bool** | If set, override object-level default to force re-upload even if an identical blob exists. | [optional] 

## Example

```python
from mixpeek.models.create_blob_request import CreateBlobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBlobRequest from a JSON string
create_blob_request_instance = CreateBlobRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBlobRequest.to_json())

# convert the object into a dict
create_blob_request_dict = create_blob_request_instance.to_dict()
# create an instance of CreateBlobRequest from a dict
create_blob_request_from_dict = CreateBlobRequest.from_dict(create_blob_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


