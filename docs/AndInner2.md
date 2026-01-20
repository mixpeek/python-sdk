# AndInner2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AndInner2]**](AndInner2.md) | Logical AND operation - all conditions must be true | [optional] 
**var_or** | [**List[AndInner2]**](AndInner2.md) | Logical OR operation - at least one condition must be true | [optional] 
**var_not** | [**List[AndInner2]**](AndInner2.md) | Logical NOT operation - all conditions must be false | [optional] 
**case_sensitive** | **bool** | Whether to perform case-sensitive matching | [optional] [default to False]
**var_field** | **str** | Field name to filter on | 
**operator** | [**FilterOperator**](FilterOperator.md) | Comparison operator | [optional] 
**value** | [**DynamicValue**](DynamicValue.md) |  | 

## Example

```python
from mixpeek.models.and_inner2 import AndInner2

# TODO update the JSON string below
json = "{}"
# create an instance of AndInner2 from a JSON string
and_inner2_instance = AndInner2.from_json(json)
# print the JSON string representation of the object
print(AndInner2.to_json())

# convert the object into a dict
and_inner2_dict = and_inner2_instance.to_dict()
# create an instance of AndInner2 from a dict
and_inner2_from_dict = AndInner2.from_dict(and_inner2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


