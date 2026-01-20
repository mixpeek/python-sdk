# UploadResponse

Response containing presigned URL and upload tracking information.  This response includes everything needed to: 1. Upload your file to S3 using the presigned_url 2. Track the upload status using upload_id 3. Confirm the upload using the confirmation endpoint  The presigned_url is time-limited and specific to this upload. After uploading to S3, call POST /v1/buckets/{bucket_id}/uploads/{upload_id}/confirm.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **str** | Unique identifier for this upload. Auto-generated.   ⚠️  NEXT STEP: After uploading to S3, you MUST confirm:   POST /v1/uploads/{upload_id}/confirm   Other operations:   - Check status: GET /v1/uploads/{upload_id}   - Cancel upload: DELETE /v1/uploads/{upload_id}   Format: &#39;upl_&#39; followed by 16 random characters. | 
**bucket_id** | **str** | Target bucket ID where object will be created | 
**filename** | **str** | Name of the file to upload | 
**content_type** | **str** | MIME type enforced by the presigned URL | 
**file_size_bytes** | **int** | Expected file size in bytes if provided in request. Will be validated during confirmation. | [optional] 
**presigned_url** | **str** | Time-limited HTTPS URL for uploading directly to S3.   **Step 1 - Upload to S3:**   curl -X PUT &#39;{presigned_url}&#39; -H &#39;Content-Type: {content_type}&#39; --upload-file {filename}   **Step 2 - REQUIRED: Confirm the upload:**   POST /v1/uploads/{upload_id}/confirm   (S3 has no callback - you MUST call confirm to finalize)   The URL includes authentication and expires after presigned_url_expiration seconds. S3 returns an ETag header on success - pass it to confirm for integrity validation. NOTE: This will be null if is_duplicate&#x3D;true (duplicate found, no upload needed). | [optional] 
**presigned_url_expiration** | **int** | How long the presigned URL is valid, in seconds | 
**s3_key** | **str** | Full S3 object key where the file will be stored. Format: {internal_id}/{namespace_id}/api_buckets_uploads_create/{upload_id}/{filename}. Used internally for verification and object creation. | 
**status** | [**TaskStatusEnum**](TaskStatusEnum.md) | Current upload status. After creation, always PENDING. Possible statuses: PENDING → IN_PROGRESS → PROCESSING → COMPLETED/FAILED/CANCELED | 
**metadata** | **object** | Custom metadata for tracking | [optional] 
**create_object_on_confirm** | **bool** | Whether bucket object will be auto-created on confirmation | 
**object_metadata** | **object** | Metadata for the bucket object (if create_object_on_confirm&#x3D;true) | [optional] 
**blob_property** | **str** | Property name for the blob in bucket object | [optional] 
**blob_type** | **str** | Type of blob (IMAGE, VIDEO, etc.) | [optional] 
**file_hash** | **str** | SHA256 hash of the file content. Set during confirmation from S3 metadata or provided in request. Used for duplicate detection. | [optional] 
**skip_duplicates** | **bool** | Whether duplicate detection was enabled for this upload | [optional] [default to True]
**is_duplicate** | **bool** | Whether this upload was identified as a duplicate of an existing file. If true:   - duplicate_of_upload_id contains the original upload   - presigned_url will be null (no upload needed)   - You can use the original upload&#39;s S3 object. This saves bandwidth and storage costs. | [optional] [default to False]
**duplicate_of_upload_id** | **str** | If skip_duplicates&#x3D;true and duplicate found, this is the original upload_id. The response will reference the existing upload instead of creating a new one. | [optional] 
**skipped_unique_key** | **bool** | Whether this upload was skipped because the unique key already exists in the bucket. If true:   - existing_object_id contains the ID of the existing object   - presigned_url will be null (no upload needed)   - No S3 upload is required This saves bandwidth and prevents duplicate objects. | [optional] [default to False]
**existing_object_id** | **str** | If skipped_unique_key&#x3D;true, this is the object_id of the existing object that has the same unique key values. The upload was skipped to prevent duplicates. | [optional] 
**message** | **str** | Human-readable message about the upload. Provided when is_duplicate&#x3D;true or other special conditions. Example: &#39;File already exists with the same content hash. No upload needed - returning existing upload.&#39; | [optional] 
**created_at** | **datetime** | When this upload record was created (ISO 8601 format) | 
**expires_at** | **datetime** | When the presigned URL expires (ISO 8601 format). After this time:   - The presigned URL cannot be used   - Upload status will be marked as FAILED if not completed   - The upload record will be auto-deleted 30 days later (MongoDB TTL) | 
**completed_at** | **datetime** | When the upload was completed and verified (ISO 8601 format) | [optional] 
**verified_at** | **datetime** | When S3 object existence was verified (ISO 8601 format) | [optional] 
**etag** | **str** | S3 ETag from the uploaded object (set during confirmation) | [optional] 
**object_id** | **str** | Created bucket object ID (if create_object_on_confirm was true) | [optional] 
**task_id** | **str** | Celery task ID for async confirmation (if processed asynchronously) | [optional] 

## Example

```python
from mixpeek.models.upload_response import UploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadResponse from a JSON string
upload_response_instance = UploadResponse.from_json(json)
# print the JSON string representation of the object
print(UploadResponse.to_json())

# convert the object into a dict
upload_response_dict = upload_response_instance.to_dict()
# create an instance of UploadResponse from a dict
upload_response_from_dict = UploadResponse.from_dict(upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


