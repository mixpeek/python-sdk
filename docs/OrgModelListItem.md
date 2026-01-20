# OrgModelListItem

Model item in list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** |  | 
**name** | **str** |  | 
**version** | **str** |  | 
**model_format** | **str** |  | 
**description** | **str** |  | [optional] 
**framework** | **str** |  | [optional] 
**task_type** | **str** |  | [optional] 
**deployed** | **bool** |  | 
**validation_status** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from mixpeek.models.org_model_list_item import OrgModelListItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrgModelListItem from a JSON string
org_model_list_item_instance = OrgModelListItem.from_json(json)
# print the JSON string representation of the object
print(OrgModelListItem.to_json())

# convert the object into a dict
org_model_list_item_dict = org_model_list_item_instance.to_dict()
# create an instance of OrgModelListItem from a dict
org_model_list_item_from_dict = OrgModelListItem.from_dict(org_model_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


