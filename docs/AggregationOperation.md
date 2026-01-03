# AggregationOperation

Configuration for an aggregation operation.  Defines a calculation to perform on grouped data.  Requirements:     - function: REQUIRED, the aggregation function to apply     - field: REQUIRED for most functions (except COUNT), field to aggregate     - alias: REQUIRED, name for the result in output  Examples:     - Count: AggregationOperation(function=\"count\", alias=\"total_count\")     - Sum: AggregationOperation(function=\"sum\", field=\"metadata.views\", alias=\"total_views\")     - Average: AggregationOperation(function=\"avg\", field=\"metadata.duration\", alias=\"avg_duration\")

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function** | [**AggregationFunction**](AggregationFunction.md) | The aggregation function to apply. Different functions require different field types: COUNT: no field required. SUM/AVG: numeric fields only. MIN/MAX: numeric or date fields. COUNT_DISTINCT: any field type. | 
**var_field** | **str** | The field to aggregate. REQUIRED for all functions except COUNT. NOT REQUIRED for COUNT (counts documents). Supports dot notation for nested fields. Field type must be compatible with function. | [optional] 
**alias** | **str** | Name for the aggregation result in output. REQUIRED for all operations. Should be descriptive of the calculation. Used to reference results in post-filtering. | 
**distinct_field** | **str** | Field to count distinct values from. REQUIRED when function is COUNT_DISTINCT. NOT REQUIRED for other functions. Supports dot notation for nested fields. | [optional] 

## Example

```python
from mixpeek.models.aggregation_operation import AggregationOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AggregationOperation from a JSON string
aggregation_operation_instance = AggregationOperation.from_json(json)
# print the JSON string representation of the object
print(AggregationOperation.to_json())

# convert the object into a dict
aggregation_operation_dict = aggregation_operation_instance.to_dict()
# create an instance of AggregationOperation from a dict
aggregation_operation_from_dict = AggregationOperation.from_dict(aggregation_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


