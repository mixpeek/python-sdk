# mixpeek.InferenceApi

All URIs are relative to *https://api.mixpeek.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_raw_inference**](InferenceApi.md#execute_raw_inference) | **POST** /v1/inference | Execute Raw Inference


# **execute_raw_inference**
> RawInferenceResponse execute_raw_inference(raw_inference_request, authorization=authorization, x_namespace=x_namespace)

Execute Raw Inference

Execute raw inference with provider+model or custom plugin.

This endpoint provides direct access to inference services without
the retriever framework overhead. Supports two modes:

1. **Provider + Model**: Use standard providers (openai, google, anthropic)
2. **Custom Plugin**: Use your custom inference plugins by inference_name

## Supported Providers

- **openai**: GPT models, embeddings, Whisper transcription
- **google**: Gemini models, Vertex multimodal embeddings (1408D)
- **anthropic**: Claude models

## Examples

### Custom Plugin (by inference_name)
```json
{
    "inference_name": "my_text_embedder_1_0_0",
    "inputs": {"text": "hello world"},
    "parameters": {}
}
```

### Custom Plugin (by feature_uri)
```json
{
    "feature_uri": "mixpeek://my_custom_embedder@1.0.0/embedding",
    "inputs": {"text": "hello world"},
    "parameters": {}
}
```

### Builtin Embedder (by feature_uri)
```json
{
    "feature_uri": "mixpeek://text_extractor@v1/multilingual_e5_large_instruct_v1",
    "inputs": {"text": "hello world"},
    "parameters": {}
}
```

### Chat Completion
```json
{
    "provider": "openai",
    "model": "gpt-4o-mini",
    "inputs": {"prompts": ["What is AI?"]},
    "parameters": {"temperature": 0.7, "max_tokens": 500}
}
```

### Text Embedding (OpenAI)
```json
{
    "provider": "openai",
    "model": "text-embedding-3-large",
    "inputs": {"text": "machine learning"},
    "parameters": {}
}
```

### Text Embedding (Google Vertex Multimodal - 1408D)
```json
{
    "provider": "google",
    "model": "multimodalembedding",
    "inputs": {"text": "machine learning"},
    "parameters": {}
}
```

### Image Embedding (Google Vertex Multimodal - 1408D)
```json
{
    "provider": "google",
    "model": "multimodalembedding",
    "inputs": {"image_url": "https://example.com/image.jpg"},
    "parameters": {}
}
```

### Image Embedding from Base64
```json
{
    "provider": "google",
    "model": "multimodalembedding",
    "inputs": {"image_base64": "<base64-encoded-image>"},
    "parameters": {}
}
```

### Video Embedding (Google Vertex Multimodal - 1408D)
```json
{
    "provider": "google",
    "model": "multimodalembedding",
    "inputs": {"video_url": "https://example.com/video.mp4"},
    "parameters": {}
}
```

### Video Embedding from Base64
```json
{
    "provider": "google",
    "model": "multimodalembedding",
    "inputs": {"video_base64": "<base64-encoded-video>"},
    "parameters": {}
}
```

### Audio Transcription
```json
{
    "provider": "openai",
    "model": "whisper-1",
    "inputs": {"audio_url": "https://example.com/audio.mp3"},
    "parameters": {}
}
```

### Vision (Multimodal LLM)
```json
{
    "provider": "openai",
    "model": "gpt-4o",
    "inputs": {
        "prompts": ["Describe this image"],
        "image_url": "https://example.com/image.jpg"
    },
    "parameters": {"temperature": 0.5}
}
```

Args:
    request: FastAPI request object (populated by middleware)
    payload: Raw inference request

Returns:
    Inference response with results and metadata

Raises:
    400 Bad Request: Invalid provider, model, or inputs
    401 Unauthorized: Missing or invalid API key
    429 Too Many Requests: Rate limit exceeded
    500 Internal Server Error: Inference execution failed

### Example


```python
import mixpeek
from mixpeek.models.raw_inference_request import RawInferenceRequest
from mixpeek.models.raw_inference_response import RawInferenceResponse
from mixpeek.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mixpeek.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mixpeek.Configuration(
    host = "https://api.mixpeek.com"
)


# Enter a context with an instance of the API client
with mixpeek.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mixpeek.InferenceApi(api_client)
    raw_inference_request = mixpeek.RawInferenceRequest() # RawInferenceRequest | 
    authorization = 'authorization_example' # str | REQUIRED: Bearer token authentication using your API key. Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under Organization Settings. (optional)
    x_namespace = 'x_namespace_example' # str | REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like 'my-namespace' (optional)

    try:
        # Execute Raw Inference
        api_response = api_instance.execute_raw_inference(raw_inference_request, authorization=authorization, x_namespace=x_namespace)
        print("The response of InferenceApi->execute_raw_inference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->execute_raw_inference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_inference_request** | [**RawInferenceRequest**](RawInferenceRequest.md)|  | 
 **authorization** | **str**| REQUIRED: Bearer token authentication using your API key. Format: &#39;Bearer sk_xxxxxxxxxxxxx&#39;. You can create API keys in the Mixpeek dashboard under Organization Settings. | [optional] 
 **x_namespace** | **str**| REQUIRED: Namespace identifier for scoping this request. All resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a custom name like &#39;my-namespace&#39; | [optional] 

### Return type

[**RawInferenceResponse**](RawInferenceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

