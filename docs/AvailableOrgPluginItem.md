# AvailableOrgPluginItem

An org-level plugin available to enable for a namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin_id** | **str** | Unique plugin identifier | 
**name** | **str** | Plugin name | 
**version** | **str** | Plugin version | 
**description** | **str** | Plugin description | [optional] 
**feature_uri** | **str** | Feature URI to use when enabled | 
**validation_status** | **str** | Validation status | 
**enabled_in_namespace** | **bool** | Whether this plugin is enabled in the current namespace | 
**created_at** | **datetime** | When the plugin was created | 

## Example

```python
from mixpeek.models.available_org_plugin_item import AvailableOrgPluginItem

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableOrgPluginItem from a JSON string
available_org_plugin_item_instance = AvailableOrgPluginItem.from_json(json)
# print the JSON string representation of the object
print(AvailableOrgPluginItem.to_json())

# convert the object into a dict
available_org_plugin_item_dict = available_org_plugin_item_instance.to_dict()
# create an instance of AvailableOrgPluginItem from a dict
available_org_plugin_item_from_dict = AvailableOrgPluginItem.from_dict(available_org_plugin_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


