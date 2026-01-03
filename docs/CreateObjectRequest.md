# CreateObjectRequest

Request model for creating a bucket object.  Objects can be created with blobs from two sources: 1. Direct data (URLs, base64) - Use CreateBlobRequest.data field 2. Upload references - Use CreateBlobRequest.upload_id field (from POST /buckets/{id}/uploads)  Upload Reference Workflow:     For large files or client-side uploads, use the presigned URL workflow:     1. POST /buckets/{id}/uploads → Returns {upload_id, presigned_url}     2. User uploads file to presigned_url (client-side)     3. POST /uploads/{upload_id}/confirm → Validates upload     4. POST /buckets/{id}/objects with upload_id in blobs (this endpoint)  Use Cases:     - Single blob with direct data (simple)     - Multiple blobs from presigned uploads (recommended for large files)     - Mix of direct data and upload references     - Combine multiple uploads into one object  See Also:     - CreateBlobRequest for blob field documentation     - POST /buckets/{id}/uploads for presigned URL generation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_prefix** | **str** | Storage key/path prefix of the object, this will be used to retrieve the object from the storage. It&#39;s at the root of the object. | [optional] 
**blobs** | [**List[CreateBlobRequest]**](CreateBlobRequest.md) | List of blobs to be created in this object | [optional] 
**skip_duplicates** | **bool** | Skip duplicate blobs, if a blob with the same hash already exists, it will be skipped. | [optional] [default to False]
**canonicalize_source** | **bool** | Mirror non-S3 sources into internal S3 and reference canonically. | [optional] [default to True]
**force_remirror** | **bool** | Force re-upload to S3 even if a blob with identical content already exists. | [optional] [default to False]

## Example

```python
from mixpeek.models.create_object_request import CreateObjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateObjectRequest from a JSON string
create_object_request_instance = CreateObjectRequest.from_json(json)
# print the JSON string representation of the object
print(CreateObjectRequest.to_json())

# convert the object into a dict
create_object_request_dict = create_object_request_instance.to_dict()
# create an instance of CreateObjectRequest from a dict
create_object_request_from_dict = CreateObjectRequest.from_dict(create_object_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


