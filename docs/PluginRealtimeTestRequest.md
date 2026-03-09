# PluginRealtimeTestRequest

Request to test a plugin's realtime inference endpoint.  Use this to debug plugin inference responses before using them in retrievers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | **Dict[str, object]** | Input data to pass to the inference service (e.g., {&#39;text&#39;: &#39;hello&#39;}) | [optional] 
**parameters** | **Dict[str, object]** | Additional parameters for the inference call | [optional] 

## Example

```python
from mixpeek.models.plugin_realtime_test_request import PluginRealtimeTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PluginRealtimeTestRequest from a JSON string
plugin_realtime_test_request_instance = PluginRealtimeTestRequest.from_json(json)
# print the JSON string representation of the object
print(PluginRealtimeTestRequest.to_json())

# convert the object into a dict
plugin_realtime_test_request_dict = plugin_realtime_test_request_instance.to_dict()
# create an instance of PluginRealtimeTestRequest from a dict
plugin_realtime_test_request_from_dict = PluginRealtimeTestRequest.from_dict(plugin_realtime_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


