# LogicalOperatorOutputANDInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[LogicalOperatorOutputANDInner]**](LogicalOperatorOutputANDInner.md) | Logical AND operation - all conditions must be true | [optional] 
**var_or** | [**List[LogicalOperatorOutputANDInner]**](LogicalOperatorOutputANDInner.md) | Logical OR operation - at least one condition must be true | [optional] 
**var_not** | [**List[LogicalOperatorOutputANDInner]**](LogicalOperatorOutputANDInner.md) | Logical NOT operation - all conditions must be false | [optional] 
**case_sensitive** | **bool** | Whether to perform case-sensitive matching | [optional] [default to False]
**var_field** | **str** | Field name to filter on | 
**operator** | [**FilterOperator**](FilterOperator.md) | Comparison operator | [optional] 
**value** | [**DynamicValue**](DynamicValue.md) |  | 

## Example

```python
from mixpeek.models.logical_operator_output_and_inner import LogicalOperatorOutputANDInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalOperatorOutputANDInner from a JSON string
logical_operator_output_and_inner_instance = LogicalOperatorOutputANDInner.from_json(json)
# print the JSON string representation of the object
print(LogicalOperatorOutputANDInner.to_json())

# convert the object into a dict
logical_operator_output_and_inner_dict = logical_operator_output_and_inner_instance.to_dict()
# create an instance of LogicalOperatorOutputANDInner from a dict
logical_operator_output_and_inner_from_dict = LogicalOperatorOutputANDInner.from_dict(logical_operator_output_and_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


