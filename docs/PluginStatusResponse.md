# PluginStatusResponse

Response model for plugin deployment status.  Status values: - QUEUED: Plugin is waiting in the deployment queue - PENDING: Deployment triggered, waiting for Anyscale to start - IN_PROGRESS: Blue-green deployment in progress - DEPLOYED: Plugin successfully deployed and ready - FAILED: Deployment failed - NOT_DEPLOYED: Plugin not deployed for realtime inference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin_id** | **str** | Plugin identifier | 
**namespace_id** | **str** | Namespace ID | 
**status** | **str** | Deployment status (QUEUED, PENDING, IN_PROGRESS, DEPLOYED, FAILED, NOT_DEPLOYED) | 
**name** | **str** | Plugin name | [optional] 
**version** | **str** | Plugin version | [optional] 
**realtime_enabled** | **bool** | Whether realtime inference is enabled | [optional] [default to False]
**message** | **str** | Human-readable status message | [optional] 
**queued_at** | **str** | When plugin was queued (ISO format) | [optional] 
**estimated_completion_seconds** | **int** | Estimated time to deployment completion in seconds | [optional] 
**deployed** | **bool** | Whether plugin is deployed | [optional] 
**route_prefix** | **str** | HTTP route prefix for realtime inference | [optional] 
**feature_uri** | **str** | Feature URI for using the plugin | [optional] 
**deployed_at** | **str** | When plugin was deployed (ISO format) | [optional] 
**error** | **str** | Error message if deployment failed | [optional] 

## Example

```python
from mixpeek.models.plugin_status_response import PluginStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PluginStatusResponse from a JSON string
plugin_status_response_instance = PluginStatusResponse.from_json(json)
# print the JSON string representation of the object
print(PluginStatusResponse.to_json())

# convert the object into a dict
plugin_status_response_dict = plugin_status_response_instance.to_dict()
# create an instance of PluginStatusResponse from a dict
plugin_status_response_from_dict = PluginStatusResponse.from_dict(plugin_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


