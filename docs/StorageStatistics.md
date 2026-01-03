# StorageStatistics

Statistics about object storage in a bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_size_bytes** | **int** | Total size of all objects/blobs in the bucket in bytes | [optional] [default to 0]
**avg_size_bytes** | **int** | Average object size in bytes | [optional] [default to 0]
**max_size_bytes** | **int** | Size of the largest object in bytes | [optional] [default to 0]
**min_size_bytes** | **int** | Size of the smallest object in bytes | [optional] [default to 0]

## Example

```python
from mixpeek.models.storage_statistics import StorageStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of StorageStatistics from a JSON string
storage_statistics_instance = StorageStatistics.from_json(json)
# print the JSON string representation of the object
print(StorageStatistics.to_json())

# convert the object into a dict
storage_statistics_dict = storage_statistics_instance.to_dict()
# create an instance of StorageStatistics from a dict
storage_statistics_from_dict = StorageStatistics.from_dict(storage_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


