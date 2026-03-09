# PluginRealtimeTestResponse

Response from testing a plugin's realtime inference endpoint.  Returns the raw inference response so users can verify their plugin is returning the expected format (e.g., embedding vectors).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Test result status: &#39;success&#39; or &#39;error&#39; | 
**inference_name** | **str** | The resolved inference service name that was called | 
**raw_response** | **object** |  | [optional] 
**response_type** | **str** | Python type of the response (e.g., &#39;dict&#39;, &#39;list&#39;) | [optional] 
**response_keys** | **List[str]** | Top-level keys if response is a dict | [optional] 
**error** | **str** | Error message if test failed | [optional] 
**message** | **str** | Human-readable status message | [optional] 

## Example

```python
from mixpeek.models.plugin_realtime_test_response import PluginRealtimeTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PluginRealtimeTestResponse from a JSON string
plugin_realtime_test_response_instance = PluginRealtimeTestResponse.from_json(json)
# print the JSON string representation of the object
print(PluginRealtimeTestResponse.to_json())

# convert the object into a dict
plugin_realtime_test_response_dict = plugin_realtime_test_response_instance.to_dict()
# create an instance of PluginRealtimeTestResponse from a dict
plugin_realtime_test_response_from_dict = PluginRealtimeTestResponse.from_dict(plugin_realtime_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


