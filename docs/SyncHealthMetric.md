# SyncHealthMetric

Sync health metrics per config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_config_id** | **str** | Sync config identifier | 
**consecutive_failures** | **int** | Consecutive failure count | 
**last_success_at** | **datetime** | Last successful sync | [optional] 
**last_failure_at** | **datetime** | Last failed sync | [optional] 
**failure_rate** | **float** | Failure rate (0-1) | 

## Example

```python
from mixpeek.models.sync_health_metric import SyncHealthMetric

# TODO update the JSON string below
json = "{}"
# create an instance of SyncHealthMetric from a JSON string
sync_health_metric_instance = SyncHealthMetric.from_json(json)
# print the JSON string representation of the object
print(SyncHealthMetric.to_json())

# convert the object into a dict
sync_health_metric_dict = sync_health_metric_instance.to_dict()
# create an instance of SyncHealthMetric from a dict
sync_health_metric_from_dict = SyncHealthMetric.from_dict(sync_health_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


