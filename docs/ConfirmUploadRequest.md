# ConfirmUploadRequest

Request to confirm S3 upload completion and create bucket object.  ⚠️  THIS ENDPOINT IS REQUIRED AFTER UPLOADING TO S3!  S3 presigned URLs have no callback mechanism - the API cannot detect when your upload completes. You MUST call this endpoint to finalize the upload.  Why confirmation is required:     - S3 doesn't notify us when uploads complete     - We need to verify the file actually exists in S3     - We need to create the bucket object     - We need to update quotas and tracking  The system will: 1. Verify the S3 object exists (HeadObject call) 2. Validate ETag matches (if provided) - RECOMMENDED for integrity 3. Validate file size matches (if provided) 4. Create bucket object (default, unless create_object_on_confirm=false) 5. Update upload status to COMPLETED  If you don't call confirm:     - Upload stays in PENDING status     - No bucket object is created     - File is orphaned in S3

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **str** | S3 ETag returned from the upload. OPTIONAL but RECOMMENDED. After uploading to S3, the response includes an ETag header. Providing this ensures the file wasn&#39;t corrupted during upload. If provided and doesn&#39;t match S3&#39;s ETag, confirmation will fail with error. Format: Usually an MD5 hash, may be enclosed in quotes. | [optional] 
**file_size_bytes** | **int** | Actual file size uploaded, in bytes. OPTIONAL but RECOMMENDED. If provided, will be validated against the actual S3 object size. Mismatch indicates upload corruption or network issues. If not provided, size validation is skipped. | [optional] 

## Example

```python
from mixpeek.models.confirm_upload_request import ConfirmUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmUploadRequest from a JSON string
confirm_upload_request_instance = ConfirmUploadRequest.from_json(json)
# print the JSON string representation of the object
print(ConfirmUploadRequest.to_json())

# convert the object into a dict
confirm_upload_request_dict = confirm_upload_request_instance.to_dict()
# create an instance of ConfirmUploadRequest from a dict
confirm_upload_request_from_dict = ConfirmUploadRequest.from_dict(confirm_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


