# SyncConfigMetric

Sync configuration comparison metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_config_id** | **str** | Sync config identifier | 
**provider_type** | **str** | Provider type | 
**avg_duration_seconds** | **float** | Average sync duration | 
**avg_throughput_mbps** | **float** | Average throughput | 
**success_rate** | **float** | Success rate (0-1) | 
**total_files_synced** | **int** | Total files synced | 
**total_bytes_synced** | **int** | Total bytes synced | 

## Example

```python
from mixpeek.models.sync_config_metric import SyncConfigMetric

# TODO update the JSON string below
json = "{}"
# create an instance of SyncConfigMetric from a JSON string
sync_config_metric_instance = SyncConfigMetric.from_json(json)
# print the JSON string representation of the object
print(SyncConfigMetric.to_json())

# convert the object into a dict
sync_config_metric_dict = sync_config_metric_instance.to_dict()
# create an instance of SyncConfigMetric from a dict
sync_config_metric_from_dict = SyncConfigMetric.from_dict(sync_config_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


