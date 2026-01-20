# CreateModelUploadRequest

Request to generate a presigned URL for model archive upload.  This is step 1 of the presigned URL workflow: 1. POST /models/uploads → Returns presigned_url + upload_id 2. PUT presigned_url with model archive (client uploads directly to S3) 3. POST /models/uploads/{upload_id}/confirm → Validates and creates model  Requirements:     - name: Model name (e.g., 'my_custom_embedder')     - version: Semantic version (e.g., '1.0.0')     - model_format: Format of the model weights     - file_size_bytes: Expected archive size for quota validation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Model name (alphanumeric with underscores, no spaces) | 
**version** | **str** | Semantic version string | 
**model_format** | **str** | Format of the model weights | 
**description** | **str** | Optional description of the model | [optional] 
**file_size_bytes** | **int** | Expected file size in bytes for quota validation | [optional] 
**presigned_url_expiration** | **int** | Presigned URL expiration time in seconds (1-24 hours) | [optional] [default to 3600]
**resource_requirements** | [**ModelResourceRequirements**](ModelResourceRequirements.md) | Resource requirements for model deployment | [optional] 
**framework** | **str** | ML framework (e.g., sentence-transformers, transformers) | [optional] 
**task_type** | **str** | Task type (e.g., embedding, classification, generation) | [optional] 

## Example

```python
from mixpeek.models.create_model_upload_request import CreateModelUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModelUploadRequest from a JSON string
create_model_upload_request_instance = CreateModelUploadRequest.from_json(json)
# print the JSON string representation of the object
print(CreateModelUploadRequest.to_json())

# convert the object into a dict
create_model_upload_request_dict = create_model_upload_request_instance.to_dict()
# create an instance of CreateModelUploadRequest from a dict
create_model_upload_request_from_dict = CreateModelUploadRequest.from_dict(create_model_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


