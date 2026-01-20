# FilterCondition4

Represents a single filter condition.  Attributes:     field: The field to filter on     operator: The comparison operator     value: The value to compare against

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name to filter on | 
**operator** | [**FilterOperator**](FilterOperator.md) | Comparison operator | [optional] 
**value** | [**DynamicValue**](DynamicValue.md) |  | 

## Example

```python
from mixpeek.models.filter_condition4 import FilterCondition4

# TODO update the JSON string below
json = "{}"
# create an instance of FilterCondition4 from a JSON string
filter_condition4_instance = FilterCondition4.from_json(json)
# print the JSON string representation of the object
print(FilterCondition4.to_json())

# convert the object into a dict
filter_condition4_dict = filter_condition4_instance.to_dict()
# create an instance of FilterCondition4 from a dict
filter_condition4_from_dict = FilterCondition4.from_dict(filter_condition4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


