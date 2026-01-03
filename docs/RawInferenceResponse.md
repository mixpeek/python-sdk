# RawInferenceResponse

Response from raw inference.  Returns the inference results along with metadata about the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**provider** | **str** | Provider that was used | 
**model** | **str** | Model that was used | 
**tokens_used** | **Dict[str, int]** | Token usage statistics (if available) | [optional] 
**latency_ms** | **float** | Total inference latency in milliseconds | 

## Example

```python
from mixpeek.models.raw_inference_response import RawInferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RawInferenceResponse from a JSON string
raw_inference_response_instance = RawInferenceResponse.from_json(json)
# print the JSON string representation of the object
print(RawInferenceResponse.to_json())

# convert the object into a dict
raw_inference_response_dict = raw_inference_response_instance.to_dict()
# create an instance of RawInferenceResponse from a dict
raw_inference_response_from_dict = RawInferenceResponse.from_dict(raw_inference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


