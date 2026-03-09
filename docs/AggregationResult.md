# AggregationResult

Single aggregation result row.  Contains grouped field values and computed aggregations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **Dict[str, object]** | Grouped field values that define this result row. | 
**metrics** | **Dict[str, object]** | Computed aggregation values for this group. | 

## Example

```python
from mixpeek.models.aggregation_result import AggregationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationResult from a JSON string
aggregation_result_instance = AggregationResult.from_json(json)
# print the JSON string representation of the object
print(AggregationResult.to_json())

# convert the object into a dict
aggregation_result_dict = aggregation_result_instance.to_dict()
# create an instance of AggregationResult from a dict
aggregation_result_from_dict = AggregationResult.from_dict(aggregation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


