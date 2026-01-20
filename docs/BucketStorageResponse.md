# BucketStorageResponse

Storage growth trends response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** | Bucket identifier | 
**time_range** | [**ApiAnalyticsBucketsModelsTimeRange**](ApiAnalyticsBucketsModelsTimeRange.md) | Query time range | 
**metrics** | [**List[StorageMetric]**](StorageMetric.md) | Time-series storage metrics | 
**summary** | **object** | Summary statistics | [optional] 

## Example

```python
from mixpeek.models.bucket_storage_response import BucketStorageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BucketStorageResponse from a JSON string
bucket_storage_response_instance = BucketStorageResponse.from_json(json)
# print the JSON string representation of the object
print(BucketStorageResponse.to_json())

# convert the object into a dict
bucket_storage_response_dict = bucket_storage_response_instance.to_dict()
# create an instance of BucketStorageResponse from a dict
bucket_storage_response_from_dict = BucketStorageResponse.from_dict(bucket_storage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


