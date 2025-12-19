# BlobURLRef

Reference to a document-related blob (thumbnails, sources, artifacts).  DevEx guidelines: - field: Use a stable, semantic label such as \"thumbnail\", \"source\", or a domain term.   Avoid leaking internal paths like \"metadata.thumbnail[0]\"; indexing (e.g., per-chunk)   should be inferred from filenames or stored separately (e.g., ordinal) if needed. - role: Determines behavior/UX grouping (thumbnail|source|artifact|aux). Prefer using role for UI. - url: Canonical locator. s3:// URLs are presignable via API when return_url=true. - presigned_url: Response-only, set by API to a time-limited https link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Stable semantic label for the blob (e.g., &#39;thumbnail&#39;, &#39;source&#39;). | 
**role** | **str** | Semantic role of this blob | [optional] [default to 'source']
**type** | **str** | Schema/blob type | [optional] [default to 'other']
**url** | **str** | Canonical blob URL; s3:// URLs are presignable | 
**object_key** | **str** | S3 object key if available (no bucket prefix) | [optional] 
**filename** | **str** | Leaf filename | [optional] 
**size_bytes** | **int** | Blob size in bytes | [optional] 
**content_type** | **str** | MIME content type | [optional] 
**checksum** | **str** | Optional checksum | [optional] 
**created_at** | **datetime** | Blob create time | [optional] 
**source_blob_id** | **str** | Cross-reference to source blob in Mongo lineage | [optional] 
**presigned_url** | **str** | Response-only presigned https URL | [optional] 

## Example

```python
from mixpeek.models.blob_url_ref import BlobURLRef

# TODO update the JSON string below
json = "{}"
# create an instance of BlobURLRef from a JSON string
blob_url_ref_instance = BlobURLRef.from_json(json)
# print the JSON string representation of the object
print(BlobURLRef.to_json())

# convert the object into a dict
blob_url_ref_dict = blob_url_ref_instance.to_dict()
# create an instance of BlobURLRef from a dict
blob_url_ref_from_dict = BlobURLRef.from_dict(blob_url_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


