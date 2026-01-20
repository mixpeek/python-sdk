# LogicalOperator3

Represents a logical operation (AND, OR, NOT) on filter conditions.  Allows nesting with a defined depth limit.  Also supports shorthand syntax where field names can be passed directly as key-value pairs for equality filtering (e.g., {\"metadata.title\": \"value\"}).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AndInner2]**](AndInner2.md) | Logical AND operation - all conditions must be true | [optional] 
**var_or** | [**List[AndInner2]**](AndInner2.md) | Logical OR operation - at least one condition must be true | [optional] 
**var_not** | [**List[AndInner2]**](AndInner2.md) | Logical NOT operation - all conditions must be false | [optional] 
**case_sensitive** | **bool** | Whether to perform case-sensitive matching | [optional] [default to False]

## Example

```python
from mixpeek.models.logical_operator3 import LogicalOperator3

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalOperator3 from a JSON string
logical_operator3_instance = LogicalOperator3.from_json(json)
# print the JSON string representation of the object
print(LogicalOperator3.to_json())

# convert the object into a dict
logical_operator3_dict = logical_operator3_instance.to_dict()
# create an instance of LogicalOperator3 from a dict
logical_operator3_from_dict = LogicalOperator3.from_dict(logical_operator3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


