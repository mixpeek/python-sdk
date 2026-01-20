# EnableOrgPluginResponse

Response from enabling an org-level plugin for a namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the operation succeeded | 
**plugin_id** | **str** | The plugin ID that was enabled | 
**namespace_id** | **str** | The namespace where plugin was enabled | 
**feature_uri** | **str** | Feature URI to use in collections | 
**message** | **str** | Status message | 
**deployment_status** | **str** | Deployment status if deploy&#x3D;True | [optional] 

## Example

```python
from mixpeek.models.enable_org_plugin_response import EnableOrgPluginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnableOrgPluginResponse from a JSON string
enable_org_plugin_response_instance = EnableOrgPluginResponse.from_json(json)
# print the JSON string representation of the object
print(EnableOrgPluginResponse.to_json())

# convert the object into a dict
enable_org_plugin_response_dict = enable_org_plugin_response_instance.to_dict()
# create an instance of EnableOrgPluginResponse from a dict
enable_org_plugin_response_from_dict = EnableOrgPluginResponse.from_dict(enable_org_plugin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


