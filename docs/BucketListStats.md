# BucketListStats

Aggregate statistics for a list of buckets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_objects** | **int** | Total number of objects across all buckets | [optional] [default to 0]
**total_size_bytes** | **int** | Total size in bytes across all buckets | [optional] [default to 0]
**avg_objects_per_bucket** | **float** | Average number of objects per bucket | [optional] [default to 0.0]
**avg_size_per_bucket** | **float** | Average size in bytes per bucket | [optional] [default to 0.0]

## Example

```python
from mixpeek.models.bucket_list_stats import BucketListStats

# TODO update the JSON string below
json = "{}"
# create an instance of BucketListStats from a JSON string
bucket_list_stats_instance = BucketListStats.from_json(json)
# print the JSON string representation of the object
print(BucketListStats.to_json())

# convert the object into a dict
bucket_list_stats_dict = bucket_list_stats_instance.to_dict()
# create an instance of BucketListStats from a dict
bucket_list_stats_from_dict = BucketListStats.from_dict(bucket_list_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


