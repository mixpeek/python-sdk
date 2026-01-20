# ModelListItem

Model item in list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** |  | 
**name** | **str** |  | 
**version** | **str** |  | 
**model_format** | **str** |  | 
**framework** | **str** |  | [optional] 
**task_type** | **str** |  | [optional] 
**deployed** | **bool** |  | 
**endpoint** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from mixpeek.models.model_list_item import ModelListItem

# TODO update the JSON string below
json = "{}"
# create an instance of ModelListItem from a JSON string
model_list_item_instance = ModelListItem.from_json(json)
# print the JSON string representation of the object
print(ModelListItem.to_json())

# convert the object into a dict
model_list_item_dict = model_list_item_instance.to_dict()
# create an instance of ModelListItem from a dict
model_list_item_from_dict = ModelListItem.from_dict(model_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


