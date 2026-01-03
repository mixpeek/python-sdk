# UsageMetric

Usage and cost metrics for a time bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_bucket** | **datetime** | Time bucket timestamp | 
**storage_gb_hours** | **float** | Storage GB-hours | 
**upload_operations** | **int** | Upload operation count | 
**sync_operations** | **int** | Sync operation count | 
**total_credits** | **int** | Total credits consumed | 
**estimated_cost_usd** | **float** | Estimated cost in USD | 

## Example

```python
from mixpeek.models.usage_metric import UsageMetric

# TODO update the JSON string below
json = "{}"
# create an instance of UsageMetric from a JSON string
usage_metric_instance = UsageMetric.from_json(json)
# print the JSON string representation of the object
print(UsageMetric.to_json())

# convert the object into a dict
usage_metric_dict = usage_metric_instance.to_dict()
# create an instance of UsageMetric from a dict
usage_metric_from_dict = UsageMetric.from_dict(usage_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


