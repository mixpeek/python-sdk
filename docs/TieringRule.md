# TieringRule

A single automatic storage tiering rule (V1: stored but not enforced).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_type** | **str** |  | 
**enabled** | **bool** |  | [optional] [default to False]
**threshold_days** | **int** |  | [optional] 

## Example

```python
from mixpeek.models.tiering_rule import TieringRule

# TODO update the JSON string below
json = "{}"
# create an instance of TieringRule from a JSON string
tiering_rule_instance = TieringRule.from_json(json)
# print the JSON string representation of the object
print(TieringRule.to_json())

# convert the object into a dict
tiering_rule_dict = tiering_rule_instance.to_dict()
# create an instance of TieringRule from a dict
tiering_rule_from_dict = TieringRule.from_dict(tiering_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


