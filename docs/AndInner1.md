# AndInner1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AndInner1]**](AndInner1.md) | Logical AND operation - all conditions must be true | [optional] 
**var_or** | [**List[AndInner1]**](AndInner1.md) | Logical OR operation - at least one condition must be true | [optional] 
**var_not** | [**List[AndInner1]**](AndInner1.md) | Logical NOT operation - all conditions must be false | [optional] 
**case_sensitive** | **bool** | Whether to perform case-sensitive matching | [optional] [default to False]
**var_field** | **str** | Field name to filter on | 
**operator** | [**FilterOperator**](FilterOperator.md) | Comparison operator | [optional] 
**value** | [**DynamicValue**](DynamicValue.md) |  | 

## Example

```python
from mixpeek.models.and_inner1 import AndInner1

# TODO update the JSON string below
json = "{}"
# create an instance of AndInner1 from a JSON string
and_inner1_instance = AndInner1.from_json(json)
# print the JSON string representation of the object
print(AndInner1.to_json())

# convert the object into a dict
and_inner1_dict = and_inner1_instance.to_dict()
# create an instance of AndInner1 from a dict
and_inner1_from_dict = AndInner1.from_dict(and_inner1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


