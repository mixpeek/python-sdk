# RawInferenceRequest

Request for raw inference without retriever framework.  This endpoint provides direct access to inference services with minimal configuration. Ideal for simple LLM calls, embeddings, transcription, or vision tasks without requiring collection setup or retriever configuration.  Examples:     # Chat completion     {         \"provider\": \"openai\",         \"model\": \"gpt-4o-mini\",         \"inputs\": {\"prompts\": [\"What is AI?\"]},         \"parameters\": {\"temperature\": 0.7, \"max_tokens\": 500}     }      # Text embedding     {         \"provider\": \"openai\",         \"model\": \"text-embedding-3-large\",         \"inputs\": {\"text\": \"machine learning\"},         \"parameters\": {}     }      # Audio transcription     {         \"provider\": \"openai\",         \"model\": \"whisper-1\",         \"inputs\": {\"audio_url\": \"https://example.com/audio.mp3\"},         \"parameters\": {}     }      # Vision (multimodal)     {         \"provider\": \"openai\",         \"model\": \"gpt-4o\",         \"inputs\": {             \"prompts\": [\"Describe this image\"],             \"image_url\": \"https://example.com/image.jpg\"         },         \"parameters\": {\"temperature\": 0.5}     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Provider name: openai, google, anthropic | 
**model** | **str** | Model identifier specific to the provider | 
**inputs** | **Dict[str, object]** | Model-specific inputs. Chat: {prompts: [str]}, Embeddings: {text: str} or {texts: [str]}, Transcription: {audio_url: str}, Vision: {prompts: [str], image_url: str} | 
**parameters** | **Dict[str, object]** | Optional parameters for inference. Common: temperature (float), max_tokens (int), schema (dict for structured output) | [optional] 

## Example

```python
from mixpeek.models.raw_inference_request import RawInferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RawInferenceRequest from a JSON string
raw_inference_request_instance = RawInferenceRequest.from_json(json)
# print the JSON string representation of the object
print(RawInferenceRequest.to_json())

# convert the object into a dict
raw_inference_request_dict = raw_inference_request_instance.to_dict()
# create an instance of RawInferenceRequest from a dict
raw_inference_request_from_dict = RawInferenceRequest.from_dict(raw_inference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


