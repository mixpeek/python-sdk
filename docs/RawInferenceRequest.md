# RawInferenceRequest

Request for raw inference without retriever framework.  This endpoint provides direct access to inference services with minimal configuration. Ideal for simple LLM calls, embeddings, transcription, or vision tasks without requiring collection setup or retriever configuration.  You can either use: - `provider` + `model` for standard providers (openai, google, anthropic) - `inference_name` for custom plugins  Examples:     # Chat completion (provider + model)     {         \"provider\": \"openai\",         \"model\": \"gpt-4o-mini\",         \"inputs\": {\"prompts\": [\"What is AI?\"]},         \"parameters\": {\"temperature\": 0.7, \"max_tokens\": 500}     }      # Text embedding (provider + model)     {         \"provider\": \"openai\",         \"model\": \"text-embedding-3-large\",         \"inputs\": {\"text\": \"machine learning\"},         \"parameters\": {}     }      # Custom plugin (inference_name)     {         \"inference_name\": \"my_text_embedder_1_0_0\",         \"inputs\": {\"text\": \"hello world\"},         \"parameters\": {}     }      # Audio transcription     {         \"provider\": \"openai\",         \"model\": \"whisper-1\",         \"inputs\": {\"audio_url\": \"https://example.com/audio.mp3\"},         \"parameters\": {}     }      # Vision (multimodal)     {         \"provider\": \"openai\",         \"model\": \"gpt-4o\",         \"inputs\": {             \"prompts\": [\"Describe this image\"],             \"image_url\": \"https://example.com/image.jpg\"         },         \"parameters\": {\"temperature\": 0.5}     }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Provider name: openai, google, anthropic (required if inference_name not set) | [optional] 
**model** | **str** | Model identifier specific to the provider (required if inference_name not set) | [optional] 
**inference_name** | **str** | Custom plugin inference name (alternative to provider+model) | [optional] 
**feature_uri** | **str** | Feature URI to resolve to inference_name (alternative to inference_name). Format: mixpeek://{extractor}@{version}/{vector_index_name} | [optional] 
**inputs** | **object** | Model-specific inputs. Chat: {prompts: [str]}, Embeddings: {text: str} or {texts: [str]}, Transcription: {audio_url: str}, Vision: {prompts: [str], image_url: str} | 
**parameters** | **object** | Optional parameters for inference. Common: temperature (float), max_tokens (int), schema (dict for structured output) | [optional] 
**enable_semantic_cache** | **bool** | Enable semantic caching (vCache) for LLM chat operations. When enabled, semantically similar prompts may return cached responses, reducing latency and cost. Only applies to chat/completion models. | [optional] [default to False]
**cache_delta** | **float** | Maximum error rate for semantic cache (0.0-1.0). Lower values are more conservative. Default uses system setting (0.02 &#x3D; 2%). | [optional] 

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


