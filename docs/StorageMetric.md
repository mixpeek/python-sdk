# StorageMetric

Single time bucket storage metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_bucket** | **datetime** | Time bucket timestamp | 
**total_size_bytes** | **int** | Total storage size in bytes | 
**object_count** | **int** | Number of objects | 
**avg_size_bytes** | **int** | Average object size in bytes | 
**growth_rate_percent** | **float** | Growth rate vs previous period | [optional] 

## Example

```python
from mixpeek.models.storage_metric import StorageMetric

# TODO update the JSON string below
json = "{}"
# create an instance of StorageMetric from a JSON string
storage_metric_instance = StorageMetric.from_json(json)
# print the JSON string representation of the object
print(StorageMetric.to_json())

# convert the object into a dict
storage_metric_dict = storage_metric_instance.to_dict()
# create an instance of StorageMetric from a dict
storage_metric_from_dict = StorageMetric.from_dict(storage_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


