# GroupedResultItem

Represents a single group of documents within grouped search results.  Attributes:     field: The field by which the results were grouped.     key: The value of the group_by field for this group.     group: The documents belonging to this group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The field by which the results were grouped. | 
**key** | **object** |  | 
**group** | [**List[DocumentResult]**](DocumentResult.md) | The documents belonging to this group. | 

## Example

```python
from mixpeek.models.grouped_result_item import GroupedResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of GroupedResultItem from a JSON string
grouped_result_item_instance = GroupedResultItem.from_json(json)
# print the JSON string representation of the object
print(GroupedResultItem.to_json())

# convert the object into a dict
grouped_result_item_dict = grouped_result_item_instance.to_dict()
# create an instance of GroupedResultItem from a dict
grouped_result_item_from_dict = GroupedResultItem.from_dict(grouped_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


