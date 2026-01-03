# FieldUsageStat

Usage statistics for a filtered field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Field name | 
**query_count** | **int** | Number of queries using this field | 
**unique_queries** | **int** | Number of unique query executions | 
**is_indexed** | **bool** | Whether field has an index | 
**is_protected** | **bool** | Whether field is system-protected | 
**avg_latency_ms** | **float** | Average query latency | 
**p95_latency_ms** | **float** | 95th percentile latency | 
**first_seen** | **datetime** | First usage timestamp | 
**last_seen** | **datetime** | Most recent usage timestamp | 

## Example

```python
from mixpeek.models.field_usage_stat import FieldUsageStat

# TODO update the JSON string below
json = "{}"
# create an instance of FieldUsageStat from a JSON string
field_usage_stat_instance = FieldUsageStat.from_json(json)
# print the JSON string representation of the object
print(FieldUsageStat.to_json())

# convert the object into a dict
field_usage_stat_dict = field_usage_stat_instance.to_dict()
# create an instance of FieldUsageStat from a dict
field_usage_stat_from_dict = FieldUsageStat.from_dict(field_usage_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


