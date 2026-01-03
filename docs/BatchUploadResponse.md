# BatchUploadResponse

Response from batch upload request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uploads** | [**List[UploadResponse]**](UploadResponse.md) | Generated uploads with presigned URLs | 
**total** | **int** | Total number of uploads created | 

## Example

```python
from mixpeek.models.batch_upload_response import BatchUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUploadResponse from a JSON string
batch_upload_response_instance = BatchUploadResponse.from_json(json)
# print the JSON string representation of the object
print(BatchUploadResponse.to_json())

# convert the object into a dict
batch_upload_response_dict = batch_upload_response_instance.to_dict()
# create an instance of BatchUploadResponse from a dict
batch_upload_response_from_dict = BatchUploadResponse.from_dict(batch_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


