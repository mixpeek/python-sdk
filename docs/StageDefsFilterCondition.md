# StageDefsFilterCondition

Represents a single filter condition.  Attributes:     field: The field to filter on     operator: The comparison operator     value: The value to compare against

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name to filter on | 
**operator** | [**StageDefsFilterOperator**](StageDefsFilterOperator.md) | Comparison operator | [optional] 
**value** | [**StageDefsDynamicValue**](StageDefsDynamicValue.md) |  | 

## Example

```python
from mixpeek.models.stage_defs_filter_condition import StageDefsFilterCondition

# TODO update the JSON string below
json = "{}"
# create an instance of StageDefsFilterCondition from a JSON string
stage_defs_filter_condition_instance = StageDefsFilterCondition.from_json(json)
# print the JSON string representation of the object
print(StageDefsFilterCondition.to_json())

# convert the object into a dict
stage_defs_filter_condition_dict = stage_defs_filter_condition_instance.to_dict()
# create an instance of StageDefsFilterCondition from a dict
stage_defs_filter_condition_from_dict = StageDefsFilterCondition.from_dict(stage_defs_filter_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


