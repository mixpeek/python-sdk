# HavingCondition

Filtering condition for aggregated results.  Filters groups after aggregation (like SQL HAVING clause).  Requirements:     - field: REQUIRED, the aggregation alias to filter on     - operator: REQUIRED, comparison operator     - value: REQUIRED, value to compare against  Examples:     - Keep high-count groups: HavingCondition(field=\"total_count\", operator=\"gt\", value=100)     - Filter by average: HavingCondition(field=\"avg_duration\", operator=\"gte\", value=60)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The aggregated field to filter on. REQUIRED, must match an aggregation operation alias. Used after aggregation to filter groups. Not a source field, but a computed field. | 
**operator** | **str** | Comparison operator. REQUIRED, valid operators: gt (greater than), gte (greater than or equal), lt (less than), lte (less than or equal), eq (equal), ne (not equal). | 
**value** | [**Value**](Value.md) |  | 

## Example

```python
from mixpeek.models.having_condition import HavingCondition

# TODO update the JSON string below
json = "{}"
# create an instance of HavingCondition from a JSON string
having_condition_instance = HavingCondition.from_json(json)
# print the JSON string representation of the object
print(HavingCondition.to_json())

# convert the object into a dict
having_condition_dict = having_condition_instance.to_dict()
# create an instance of HavingCondition from a dict
having_condition_from_dict = HavingCondition.from_dict(having_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


