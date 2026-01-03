# DiffItem

A single difference between manifest and current state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | Type of resource | 
**name** | **str** | Resource name | 
**action** | **str** | Action: create, update, delete, unchanged | 
**details** | **str** | Details about the difference | [optional] 

## Example

```python
from mixpeek.models.diff_item import DiffItem

# TODO update the JSON string below
json = "{}"
# create an instance of DiffItem from a JSON string
diff_item_instance = DiffItem.from_json(json)
# print the JSON string representation of the object
print(DiffItem.to_json())

# convert the object into a dict
diff_item_dict = diff_item_instance.to_dict()
# create an instance of DiffItem from a dict
diff_item_from_dict = DiffItem.from_dict(diff_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


