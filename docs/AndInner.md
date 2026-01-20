# AndInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AndInner]**](AndInner.md) | Logical AND operation - all conditions must be true | [optional] 
**var_or** | [**List[AndInner]**](AndInner.md) | Logical OR operation - at least one condition must be true | [optional] 
**var_not** | [**List[AndInner]**](AndInner.md) | Logical NOT operation - all conditions must be false | [optional] 
**case_sensitive** | **bool** | Whether to perform case-sensitive matching | [optional] [default to False]
**var_field** | **str** | Field name to filter on | 
**operator** | [**FilterOperator**](FilterOperator.md) | Comparison operator | [optional] 
**value** | [**DynamicValue**](DynamicValue.md) |  | 

## Example

```python
from mixpeek.models.and_inner import AndInner

# TODO update the JSON string below
json = "{}"
# create an instance of AndInner from a JSON string
and_inner_instance = AndInner.from_json(json)
# print the JSON string representation of the object
print(AndInner.to_json())

# convert the object into a dict
and_inner_dict = and_inner_instance.to_dict()
# create an instance of AndInner from a dict
and_inner_from_dict = AndInner.from_dict(and_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


