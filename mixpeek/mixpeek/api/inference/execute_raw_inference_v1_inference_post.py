from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.raw_inference_request import RawInferenceRequest
from ...models.raw_inference_response import RawInferenceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RawInferenceRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/inference",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | RawInferenceResponse | None:
    if response.status_code == 200:
        response_200 = RawInferenceResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | HTTPValidationError | RawInferenceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RawInferenceRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | RawInferenceResponse]:
    r"""Execute Raw Inference

     Execute raw inference with provider and model parameters.

    This endpoint provides direct access to inference services without
    the retriever framework overhead. Ideal for simple LLM calls,
    embeddings, transcription, or vision tasks.

    ## Supported Providers

    - **openai**: GPT models, embeddings, Whisper transcription
    - **google**: Gemini models, Vertex multimodal embeddings (1408D)
    - **anthropic**: Claude models

    ## Examples

    ### Chat Completion
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"gpt-4o-mini\",
        \"inputs\": {\"prompts\": [\"What is AI?\"]},
        \"parameters\": {\"temperature\": 0.7, \"max_tokens\": 500}
    }
    ```

    ### Text Embedding (OpenAI)
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"text-embedding-3-large\",
        \"inputs\": {\"text\": \"machine learning\"},
        \"parameters\": {}
    }
    ```

    ### Text Embedding (Google Vertex Multimodal - 1408D)
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"text\": \"machine learning\"},
        \"parameters\": {}
    }
    ```

    ### Image Embedding (Google Vertex Multimodal - 1408D)
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"image_url\": \"https://example.com/image.jpg\"},
        \"parameters\": {}
    }
    ```

    ### Image Embedding from Base64
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"image_base64\": \"<base64-encoded-image>\"},
        \"parameters\": {}
    }
    ```

    ### Video Embedding (Google Vertex Multimodal - 1408D)
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"video_url\": \"https://example.com/video.mp4\"},
        \"parameters\": {}
    }
    ```

    ### Video Embedding from Base64
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"video_base64\": \"<base64-encoded-video>\"},
        \"parameters\": {}
    }
    ```

    ### Audio Transcription
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"whisper-1\",
        \"inputs\": {\"audio_url\": \"https://example.com/audio.mp3\"},
        \"parameters\": {}
    }
    ```

    ### Vision (Multimodal LLM)
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"gpt-4o\",
        \"inputs\": {
            \"prompts\": [\"Describe this image\"],
            \"image_url\": \"https://example.com/image.jpg\"
        },
        \"parameters\": {\"temperature\": 0.5}
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

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (RawInferenceRequest): Request for raw inference without retriever framework.

            This endpoint provides direct access to inference services with minimal configuration.
            Ideal for simple LLM calls, embeddings, transcription, or vision tasks without
            requiring collection setup or retriever configuration.

            Examples:
                # Chat completion
                {
                    "provider": "openai",
                    "model": "gpt-4o-mini",
                    "inputs": {"prompts": ["What is AI?"]},
                    "parameters": {"temperature": 0.7, "max_tokens": 500}
                }

                # Text embedding
                {
                    "provider": "openai",
                    "model": "text-embedding-3-large",
                    "inputs": {"text": "machine learning"},
                    "parameters": {}
                }

                # Audio transcription
                {
                    "provider": "openai",
                    "model": "whisper-1",
                    "inputs": {"audio_url": "https://example.com/audio.mp3"},
                    "parameters": {}
                }

                # Vision (multimodal)
                {
                    "provider": "openai",
                    "model": "gpt-4o",
                    "inputs": {
                        "prompts": ["Describe this image"],
                        "image_url": "https://example.com/image.jpg"
                    },
                    "parameters": {"temperature": 0.5}
                }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | RawInferenceResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RawInferenceRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | RawInferenceResponse | None:
    r"""Execute Raw Inference

     Execute raw inference with provider and model parameters.

    This endpoint provides direct access to inference services without
    the retriever framework overhead. Ideal for simple LLM calls,
    embeddings, transcription, or vision tasks.

    ## Supported Providers

    - **openai**: GPT models, embeddings, Whisper transcription
    - **google**: Gemini models, Vertex multimodal embeddings (1408D)
    - **anthropic**: Claude models

    ## Examples

    ### Chat Completion
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"gpt-4o-mini\",
        \"inputs\": {\"prompts\": [\"What is AI?\"]},
        \"parameters\": {\"temperature\": 0.7, \"max_tokens\": 500}
    }
    ```

    ### Text Embedding (OpenAI)
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"text-embedding-3-large\",
        \"inputs\": {\"text\": \"machine learning\"},
        \"parameters\": {}
    }
    ```

    ### Text Embedding (Google Vertex Multimodal - 1408D)
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"text\": \"machine learning\"},
        \"parameters\": {}
    }
    ```

    ### Image Embedding (Google Vertex Multimodal - 1408D)
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"image_url\": \"https://example.com/image.jpg\"},
        \"parameters\": {}
    }
    ```

    ### Image Embedding from Base64
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"image_base64\": \"<base64-encoded-image>\"},
        \"parameters\": {}
    }
    ```

    ### Video Embedding (Google Vertex Multimodal - 1408D)
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"video_url\": \"https://example.com/video.mp4\"},
        \"parameters\": {}
    }
    ```

    ### Video Embedding from Base64
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"video_base64\": \"<base64-encoded-video>\"},
        \"parameters\": {}
    }
    ```

    ### Audio Transcription
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"whisper-1\",
        \"inputs\": {\"audio_url\": \"https://example.com/audio.mp3\"},
        \"parameters\": {}
    }
    ```

    ### Vision (Multimodal LLM)
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"gpt-4o\",
        \"inputs\": {
            \"prompts\": [\"Describe this image\"],
            \"image_url\": \"https://example.com/image.jpg\"
        },
        \"parameters\": {\"temperature\": 0.5}
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

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (RawInferenceRequest): Request for raw inference without retriever framework.

            This endpoint provides direct access to inference services with minimal configuration.
            Ideal for simple LLM calls, embeddings, transcription, or vision tasks without
            requiring collection setup or retriever configuration.

            Examples:
                # Chat completion
                {
                    "provider": "openai",
                    "model": "gpt-4o-mini",
                    "inputs": {"prompts": ["What is AI?"]},
                    "parameters": {"temperature": 0.7, "max_tokens": 500}
                }

                # Text embedding
                {
                    "provider": "openai",
                    "model": "text-embedding-3-large",
                    "inputs": {"text": "machine learning"},
                    "parameters": {}
                }

                # Audio transcription
                {
                    "provider": "openai",
                    "model": "whisper-1",
                    "inputs": {"audio_url": "https://example.com/audio.mp3"},
                    "parameters": {}
                }

                # Vision (multimodal)
                {
                    "provider": "openai",
                    "model": "gpt-4o",
                    "inputs": {
                        "prompts": ["Describe this image"],
                        "image_url": "https://example.com/image.jpg"
                    },
                    "parameters": {"temperature": 0.5}
                }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | RawInferenceResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RawInferenceRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | RawInferenceResponse]:
    r"""Execute Raw Inference

     Execute raw inference with provider and model parameters.

    This endpoint provides direct access to inference services without
    the retriever framework overhead. Ideal for simple LLM calls,
    embeddings, transcription, or vision tasks.

    ## Supported Providers

    - **openai**: GPT models, embeddings, Whisper transcription
    - **google**: Gemini models, Vertex multimodal embeddings (1408D)
    - **anthropic**: Claude models

    ## Examples

    ### Chat Completion
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"gpt-4o-mini\",
        \"inputs\": {\"prompts\": [\"What is AI?\"]},
        \"parameters\": {\"temperature\": 0.7, \"max_tokens\": 500}
    }
    ```

    ### Text Embedding (OpenAI)
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"text-embedding-3-large\",
        \"inputs\": {\"text\": \"machine learning\"},
        \"parameters\": {}
    }
    ```

    ### Text Embedding (Google Vertex Multimodal - 1408D)
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"text\": \"machine learning\"},
        \"parameters\": {}
    }
    ```

    ### Image Embedding (Google Vertex Multimodal - 1408D)
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"image_url\": \"https://example.com/image.jpg\"},
        \"parameters\": {}
    }
    ```

    ### Image Embedding from Base64
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"image_base64\": \"<base64-encoded-image>\"},
        \"parameters\": {}
    }
    ```

    ### Video Embedding (Google Vertex Multimodal - 1408D)
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"video_url\": \"https://example.com/video.mp4\"},
        \"parameters\": {}
    }
    ```

    ### Video Embedding from Base64
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"video_base64\": \"<base64-encoded-video>\"},
        \"parameters\": {}
    }
    ```

    ### Audio Transcription
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"whisper-1\",
        \"inputs\": {\"audio_url\": \"https://example.com/audio.mp3\"},
        \"parameters\": {}
    }
    ```

    ### Vision (Multimodal LLM)
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"gpt-4o\",
        \"inputs\": {
            \"prompts\": [\"Describe this image\"],
            \"image_url\": \"https://example.com/image.jpg\"
        },
        \"parameters\": {\"temperature\": 0.5}
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

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (RawInferenceRequest): Request for raw inference without retriever framework.

            This endpoint provides direct access to inference services with minimal configuration.
            Ideal for simple LLM calls, embeddings, transcription, or vision tasks without
            requiring collection setup or retriever configuration.

            Examples:
                # Chat completion
                {
                    "provider": "openai",
                    "model": "gpt-4o-mini",
                    "inputs": {"prompts": ["What is AI?"]},
                    "parameters": {"temperature": 0.7, "max_tokens": 500}
                }

                # Text embedding
                {
                    "provider": "openai",
                    "model": "text-embedding-3-large",
                    "inputs": {"text": "machine learning"},
                    "parameters": {}
                }

                # Audio transcription
                {
                    "provider": "openai",
                    "model": "whisper-1",
                    "inputs": {"audio_url": "https://example.com/audio.mp3"},
                    "parameters": {}
                }

                # Vision (multimodal)
                {
                    "provider": "openai",
                    "model": "gpt-4o",
                    "inputs": {
                        "prompts": ["Describe this image"],
                        "image_url": "https://example.com/image.jpg"
                    },
                    "parameters": {"temperature": 0.5}
                }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | RawInferenceResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RawInferenceRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | RawInferenceResponse | None:
    r"""Execute Raw Inference

     Execute raw inference with provider and model parameters.

    This endpoint provides direct access to inference services without
    the retriever framework overhead. Ideal for simple LLM calls,
    embeddings, transcription, or vision tasks.

    ## Supported Providers

    - **openai**: GPT models, embeddings, Whisper transcription
    - **google**: Gemini models, Vertex multimodal embeddings (1408D)
    - **anthropic**: Claude models

    ## Examples

    ### Chat Completion
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"gpt-4o-mini\",
        \"inputs\": {\"prompts\": [\"What is AI?\"]},
        \"parameters\": {\"temperature\": 0.7, \"max_tokens\": 500}
    }
    ```

    ### Text Embedding (OpenAI)
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"text-embedding-3-large\",
        \"inputs\": {\"text\": \"machine learning\"},
        \"parameters\": {}
    }
    ```

    ### Text Embedding (Google Vertex Multimodal - 1408D)
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"text\": \"machine learning\"},
        \"parameters\": {}
    }
    ```

    ### Image Embedding (Google Vertex Multimodal - 1408D)
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"image_url\": \"https://example.com/image.jpg\"},
        \"parameters\": {}
    }
    ```

    ### Image Embedding from Base64
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"image_base64\": \"<base64-encoded-image>\"},
        \"parameters\": {}
    }
    ```

    ### Video Embedding (Google Vertex Multimodal - 1408D)
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"video_url\": \"https://example.com/video.mp4\"},
        \"parameters\": {}
    }
    ```

    ### Video Embedding from Base64
    ```json
    {
        \"provider\": \"google\",
        \"model\": \"multimodalembedding\",
        \"inputs\": {\"video_base64\": \"<base64-encoded-video>\"},
        \"parameters\": {}
    }
    ```

    ### Audio Transcription
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"whisper-1\",
        \"inputs\": {\"audio_url\": \"https://example.com/audio.mp3\"},
        \"parameters\": {}
    }
    ```

    ### Vision (Multimodal LLM)
    ```json
    {
        \"provider\": \"openai\",
        \"model\": \"gpt-4o\",
        \"inputs\": {
            \"prompts\": [\"Describe this image\"],
            \"image_url\": \"https://example.com/image.jpg\"
        },
        \"parameters\": {\"temperature\": 0.5}
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

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (RawInferenceRequest): Request for raw inference without retriever framework.

            This endpoint provides direct access to inference services with minimal configuration.
            Ideal for simple LLM calls, embeddings, transcription, or vision tasks without
            requiring collection setup or retriever configuration.

            Examples:
                # Chat completion
                {
                    "provider": "openai",
                    "model": "gpt-4o-mini",
                    "inputs": {"prompts": ["What is AI?"]},
                    "parameters": {"temperature": 0.7, "max_tokens": 500}
                }

                # Text embedding
                {
                    "provider": "openai",
                    "model": "text-embedding-3-large",
                    "inputs": {"text": "machine learning"},
                    "parameters": {}
                }

                # Audio transcription
                {
                    "provider": "openai",
                    "model": "whisper-1",
                    "inputs": {"audio_url": "https://example.com/audio.mp3"},
                    "parameters": {}
                }

                # Vision (multimodal)
                {
                    "provider": "openai",
                    "model": "gpt-4o",
                    "inputs": {
                        "prompts": ["Describe this image"],
                        "image_url": "https://example.com/image.jpg"
                    },
                    "parameters": {"temperature": 0.5}
                }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | RawInferenceResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
