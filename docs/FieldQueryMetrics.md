# FieldQueryMetrics

Metrics for a metadata field's query usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | Metadata field name | 
**query_count** | **int** | Number of queries using this field | 
**avg_latency_ms** | **float** | Average query latency in milliseconds | 
**p95_latency_ms** | **float** | 95th percentile latency in milliseconds | 

## Example

```python
from mixpeek.models.field_query_metrics import FieldQueryMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of FieldQueryMetrics from a JSON string
field_query_metrics_instance = FieldQueryMetrics.from_json(json)
# print the JSON string representation of the object
print(FieldQueryMetrics.to_json())

# convert the object into a dict
field_query_metrics_dict = field_query_metrics_instance.to_dict()
# create an instance of FieldQueryMetrics from a dict
field_query_metrics_from_dict = FieldQueryMetrics.from_dict(field_query_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


