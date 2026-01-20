# AvailableOrgModelItem

Available org model item.

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
**enabled_in_namespace** | **bool** | Whether already enabled in the target namespace | 

## Example

```python
from mixpeek.models.available_org_model_item import AvailableOrgModelItem

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableOrgModelItem from a JSON string
available_org_model_item_instance = AvailableOrgModelItem.from_json(json)
# print the JSON string representation of the object
print(AvailableOrgModelItem.to_json())

# convert the object into a dict
available_org_model_item_dict = available_org_model_item_instance.to_dict()
# create an instance of AvailableOrgModelItem from a dict
available_org_model_item_from_dict = AvailableOrgModelItem.from_dict(available_org_model_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


