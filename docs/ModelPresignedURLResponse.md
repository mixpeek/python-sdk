# ModelPresignedURLResponse

Response containing presigned URL for model upload.  After receiving this response: 1. PUT the model archive to `presigned_url` with Content-Type: application/gzip 2. Call POST /models/uploads/{upload_id}/confirm to finalize

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **str** | Upload ID to use when confirming | 
**presigned_url** | **str** | S3 presigned URL for PUT upload | 
**s3_key** | **str** | S3 object key where file will be stored | 
**expires_at** | **datetime** | When the presigned URL expires | 
**organization_id** | **str** | Organization ID | 
**name** | **str** | Model name | 
**version** | **str** | Model version | 
**model_format** | **str** | Model format | 

## Example

```python
from mixpeek.models.model_presigned_url_response import ModelPresignedURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPresignedURLResponse from a JSON string
model_presigned_url_response_instance = ModelPresignedURLResponse.from_json(json)
# print the JSON string representation of the object
print(ModelPresignedURLResponse.to_json())

# convert the object into a dict
model_presigned_url_response_dict = model_presigned_url_response_instance.to_dict()
# create an instance of ModelPresignedURLResponse from a dict
model_presigned_url_response_from_dict = ModelPresignedURLResponse.from_dict(model_presigned_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


