# StageDefsAggregationOperation

Configuration for a single aggregation operation.  Defines what function to apply and on which field(s).  Examples:     Count documents:         ```json         {\"function\": \"count\", \"alias\": \"total\"}         ```      Sum a numeric field:         ```json         {\"function\": \"sum\", \"field\": \"metadata.views\", \"alias\": \"total_views\"}         ```      Count distinct values:         ```json         {\"function\": \"count_distinct\", \"field\": \"metadata.author\", \"alias\": \"unique_authors\"}         ```

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function** | [**StageDefsAggregationFunction**](StageDefsAggregationFunction.md) | REQUIRED. Aggregation function to apply. count/count_distinct: Count documents or unique values. sum/avg/min/max: Numeric aggregations on a field. first/last: Get first or last value (by score order). collect/collect_distinct: Gather values into a list. | 
**var_field** | **str** | OPTIONAL. Field path to aggregate (dot notation supported). Required for: sum, avg, min, max, count_distinct, first, last, collect, collect_distinct. Not needed for: count (counts documents). Examples: &#39;score&#39;, &#39;metadata.views&#39;, &#39;payload.price&#39;. | [optional] 
**alias** | **str** | REQUIRED. Name for this aggregation result in the output. Must be unique within the stage configuration. Used as the key in the aggregation results. | 

## Example

```python
from mixpeek.models.stage_defs_aggregation_operation import StageDefsAggregationOperation

# TODO update the JSON string below
json = "{}"
# create an instance of StageDefsAggregationOperation from a JSON string
stage_defs_aggregation_operation_instance = StageDefsAggregationOperation.from_json(json)
# print the JSON string representation of the object
print(StageDefsAggregationOperation.to_json())

# convert the object into a dict
stage_defs_aggregation_operation_dict = stage_defs_aggregation_operation_instance.to_dict()
# create an instance of StageDefsAggregationOperation from a dict
stage_defs_aggregation_operation_from_dict = StageDefsAggregationOperation.from_dict(stage_defs_aggregation_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


