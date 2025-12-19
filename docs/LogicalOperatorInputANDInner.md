# LogicalOperatorInputANDInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[LogicalOperatorInputANDInner]**](LogicalOperatorInputANDInner.md) | Logical AND operation - all conditions must be true | [optional] 
**var_or** | [**List[LogicalOperatorInputANDInner]**](LogicalOperatorInputANDInner.md) | Logical OR operation - at least one condition must be true | [optional] 
**var_not** | [**List[LogicalOperatorInputANDInner]**](LogicalOperatorInputANDInner.md) | Logical NOT operation - all conditions must be false | [optional] 
**case_sensitive** | **bool** | Whether to perform case-sensitive matching | [optional] [default to False]
**var_field** | **str** | Field name to filter on | 
**operator** | [**FilterOperator**](FilterOperator.md) | Comparison operator | [optional] 
**value** | [**DynamicValue**](DynamicValue.md) |  | 

## Example

```python
from mixpeek.models.logical_operator_input_and_inner import LogicalOperatorInputANDInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalOperatorInputANDInner from a JSON string
logical_operator_input_and_inner_instance = LogicalOperatorInputANDInner.from_json(json)
# print the JSON string representation of the object
print(LogicalOperatorInputANDInner.to_json())

# convert the object into a dict
logical_operator_input_and_inner_dict = logical_operator_input_and_inner_instance.to_dict()
# create an instance of LogicalOperatorInputANDInner from a dict
logical_operator_input_and_inner_from_dict = LogicalOperatorInputANDInner.from_dict(logical_operator_input_and_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


