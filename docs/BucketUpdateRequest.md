# BucketUpdateRequest

Request model for updating an existing bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Human-readable name for the bucket | [optional] 
**description** | **str** | Description of the bucket | [optional] 
**metadata** | **Dict[str, object]** | Additional metadata for the bucket | [optional] 

## Example

```python
from mixpeek.models.bucket_update_request import BucketUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BucketUpdateRequest from a JSON string
bucket_update_request_instance = BucketUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(BucketUpdateRequest.to_json())

# convert the object into a dict
bucket_update_request_dict = bucket_update_request_instance.to_dict()
# create an instance of BucketUpdateRequest from a dict
bucket_update_request_from_dict = BucketUpdateRequest.from_dict(bucket_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


