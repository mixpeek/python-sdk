# PluginListItem

Plugin item in list response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin_id** | **str** |  | 
**name** | **str** |  | 
**version** | **str** |  | 
**description** | **str** |  | [optional] 
**deployed** | **bool** |  | 
**validation_status** | **str** |  | 
**feature_uri** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from mixpeek.models.plugin_list_item import PluginListItem

# TODO update the JSON string below
json = "{}"
# create an instance of PluginListItem from a JSON string
plugin_list_item_instance = PluginListItem.from_json(json)
# print the JSON string representation of the object
print(PluginListItem.to_json())

# convert the object into a dict
plugin_list_item_dict = plugin_list_item_instance.to_dict()
# create an instance of PluginListItem from a dict
plugin_list_item_from_dict = PluginListItem.from_dict(plugin_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


