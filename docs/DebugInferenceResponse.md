# DebugInferenceResponse

Response model for the debug inference endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inference_result** | **Dict[str, object]** | The raw data returned by the inference API. | 
**debug_metadata** | **Dict[str, object]** | Additional metadata for the debug call. | [optional] 

## Example

```python
from mixpeek.models.debug_inference_response import DebugInferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DebugInferenceResponse from a JSON string
debug_inference_response_instance = DebugInferenceResponse.from_json(json)
# print the JSON string representation of the object
print(DebugInferenceResponse.to_json())

# convert the object into a dict
debug_inference_response_dict = debug_inference_response_instance.to_dict()
# create an instance of DebugInferenceResponse from a dict
debug_inference_response_from_dict = DebugInferenceResponse.from_dict(debug_inference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


