# BatchUploadRequest

Request to generate multiple presigned URLs in a single request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uploads** | [**List[CreateUploadRequest]**](CreateUploadRequest.md) | List of upload requests (max 100) | 
**shared_metadata** | **Dict[str, object]** | Metadata to apply to all uploads (merged with individual metadata) | [optional] 
**shared_object_metadata** | **Dict[str, object]** | Object metadata to apply to all uploads (merged with individual) | [optional] 

## Example

```python
from mixpeek.models.batch_upload_request import BatchUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUploadRequest from a JSON string
batch_upload_request_instance = BatchUploadRequest.from_json(json)
# print the JSON string representation of the object
print(BatchUploadRequest.to_json())

# convert the object into a dict
batch_upload_request_dict = batch_upload_request_instance.to_dict()
# create an instance of BatchUploadRequest from a dict
batch_upload_request_from_dict = BatchUploadRequest.from_dict(batch_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


