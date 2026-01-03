# BucketPatchRequest

Request model for partial update of an existing bucket (PATCH operation).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Human-readable name for the bucket | [optional] 
**description** | **str** | Description of the bucket | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata for the bucket | [optional] 

## Example

```python
from mixpeek.models.bucket_patch_request import BucketPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BucketPatchRequest from a JSON string
bucket_patch_request_instance = BucketPatchRequest.from_json(json)
# print the JSON string representation of the object
print(BucketPatchRequest.to_json())

# convert the object into a dict
bucket_patch_request_dict = bucket_patch_request_instance.to_dict()
# create an instance of BucketPatchRequest from a dict
bucket_patch_request_from_dict = BucketPatchRequest.from_dict(bucket_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


