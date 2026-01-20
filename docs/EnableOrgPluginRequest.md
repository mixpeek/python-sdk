# EnableOrgPluginRequest

Request to enable an org-level plugin for a namespace.  This adds the plugin to the namespace's feature_extractors array, making it available for use in collections within this namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**params** | **Dict[str, object]** | Optional parameters to configure the plugin for this namespace | [optional] 
**deploy** | **bool** | Whether to deploy the plugin to Ray immediately after enabling | [optional] [default to True]

## Example

```python
from mixpeek.models.enable_org_plugin_request import EnableOrgPluginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnableOrgPluginRequest from a JSON string
enable_org_plugin_request_instance = EnableOrgPluginRequest.from_json(json)
# print the JSON string representation of the object
print(EnableOrgPluginRequest.to_json())

# convert the object into a dict
enable_org_plugin_request_dict = enable_org_plugin_request_instance.to_dict()
# create an instance of EnableOrgPluginRequest from a dict
enable_org_plugin_request_from_dict = EnableOrgPluginRequest.from_dict(enable_org_plugin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


