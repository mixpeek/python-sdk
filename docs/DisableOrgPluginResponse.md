# DisableOrgPluginResponse

Response from disabling an org-level plugin for a namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the operation succeeded | 
**plugin_id** | **str** | The plugin ID that was disabled | 
**namespace_id** | **str** | The namespace where plugin was disabled | 
**message** | **str** | Status message | 

## Example

```python
from mixpeek.models.disable_org_plugin_response import DisableOrgPluginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DisableOrgPluginResponse from a JSON string
disable_org_plugin_response_instance = DisableOrgPluginResponse.from_json(json)
# print the JSON string representation of the object
print(DisableOrgPluginResponse.to_json())

# convert the object into a dict
disable_org_plugin_response_dict = disable_org_plugin_response_instance.to_dict()
# create an instance of DisableOrgPluginResponse from a dict
disable_org_plugin_response_from_dict = DisableOrgPluginResponse.from_dict(disable_org_plugin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


