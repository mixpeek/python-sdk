# InferenceRequest

Request model for inference services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inference_name** | **str** | Name of the inference model to use | 
**inputs** | **Dict[str, object]** | Input data for the inference | 
**parameters** | **Dict[str, object]** | Additional parameters for the inference | [optional] 

## Example

```python
from mixpeek.models.inference_request import InferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InferenceRequest from a JSON string
inference_request_instance = InferenceRequest.from_json(json)
# print the JSON string representation of the object
print(InferenceRequest.to_json())

# convert the object into a dict
inference_request_dict = inference_request_instance.to_dict()
# create an instance of InferenceRequest from a dict
inference_request_from_dict = InferenceRequest.from_dict(inference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


