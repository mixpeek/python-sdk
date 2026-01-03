# SyncRunMetric

Single sync run metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_run_id** | **str** | Sync run identifier | 
**started_at** | **datetime** | Sync start time | 
**duration_seconds** | **float** | Sync duration in seconds | 
**files_discovered** | **int** | Files discovered | 
**files_synced** | **int** | Files successfully synced | 
**files_failed** | **int** | Files that failed | 
**bytes_synced** | **int** | Bytes synced | 
**throughput_mbps** | **float** | Throughput in MB/s | 
**status** | **str** | Sync status | 
**provider_type** | **str** | Provider type (s3, gcs, etc) | 

## Example

```python
from mixpeek.models.sync_run_metric import SyncRunMetric

# TODO update the JSON string below
json = "{}"
# create an instance of SyncRunMetric from a JSON string
sync_run_metric_instance = SyncRunMetric.from_json(json)
# print the JSON string representation of the object
print(SyncRunMetric.to_json())

# convert the object into a dict
sync_run_metric_dict = sync_run_metric_instance.to_dict()
# create an instance of SyncRunMetric from a dict
sync_run_metric_from_dict = SyncRunMetric.from_dict(sync_run_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


