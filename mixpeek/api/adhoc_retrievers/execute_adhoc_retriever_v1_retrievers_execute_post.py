from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.adhoc_execute_request import AdhocExecuteRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AdhocExecuteRequest,
    return_presigned_urls: bool | Unset = False,
    return_vectors: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    params["return_presigned_urls"] = return_presigned_urls

    params["return_vectors"] = return_vectors

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/retrievers/execute",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AdhocExecuteRequest,
    return_presigned_urls: bool | Unset = False,
    return_vectors: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    r"""Execute Adhoc Retriever

     Execute a retriever ad-hoc without persisting the configuration.

    This endpoint allows you to execute a retriever without saving it to the database.
    Useful for one-time queries, testing configurations, or temporary searches.

    Streaming Execution (stream=True):
        Response uses Server-Sent Events (SSE) format with Content-Type: text/event-stream.
        Each stage emits events as it executes, formatted as: data: {json}\n\n

        Event Types (StreamEventType):
        - stage_start: Emitted when a stage begins (includes stage_name, stage_index, total_stages)
        - stage_complete: Emitted when a stage finishes (includes documents, statistics, budget_used)
        - stage_error: Emitted if a stage fails (includes error message)
        - execution_complete: Final event with complete results and pagination
        - execution_error: Emitted if entire execution fails

        StreamStageEvent Fields:
        - event_type: Type of event
        - execution_id: Unique execution identifier
        - stage_name/stage_index/total_stages: Stage progress info
        - documents: Intermediate results (stage_complete only)
        - statistics: Stage metrics (duration_ms, input_count, output_count, efficiency)
        - budget_used: Cumulative consumption (credits_used, time_elapsed_ms, tokens_used)

        Response Headers:
        - Content-Type: text/event-stream
        - Cache-Control: no-cache
        - Connection: keep-alive
        - X-Execution-Mode: adhoc

    Standard Execution (stream=False, default):
        - Returns ExecuteRetrieverResponse after all stages complete
        - Includes X-Execution-Mode: adhoc header
        - execution_metadata.retriever_persisted = False

    Use Cases:
        - One-time queries without saving retriever configuration
        - Testing stage configurations before persisting
        - Dynamic retrieval with varying parameters
        - Real-time progress tracking with streaming

    Args:
        return_presigned_urls (bool | Unset):  Default: False.
        return_vectors (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (AdhocExecuteRequest): Request to execute a retriever ad-hoc without persistence.

            This combines retriever creation parameters with execution inputs to allow
            one-time retrieval without saving the retriever configuration.

            Use Cases:
                - One-time queries without polluting retriever registry
                - Testing retriever configurations before persisting
                - Dynamic retrieval with varying stage configurations
                - Temporary search operations

            Behavior:
                - Retriever is NOT saved to database
                - Execution history is logged but marked as ad-hoc
                - Response includes X-Execution-Mode: adhoc header
                - execution_metadata.retriever_persisted = False

            Streaming Execution (stream=True):
                When streaming is enabled, the response uses Server-Sent Events (SSE) format
                with Content-Type: text/event-stream. Each stage emits events as it executes:

                Event Types:
                - stage_start: Emitted when a stage begins execution
                - stage_complete: Emitted when a stage finishes with results
                - stage_error: Emitted if a stage encounters an error
                - execution_complete: Emitted after all stages finish successfully
                - execution_error: Emitted if the entire execution fails

                Each event is a StreamStageEvent containing:
                - event_type: The type of event
                - execution_id: Unique execution identifier
                - stage_name: Human-readable stage name
                - stage_index: Zero-based stage position
                - total_stages: Total number of stages
                - documents: Intermediate results (for stage_complete)
                - statistics: Stage metrics (duration_ms, input_count, output_count, etc.)
                - budget_used: Cumulative resource consumption (credits, time, tokens)

                Response Headers (streaming):
                - Content-Type: text/event-stream
                - Cache-Control: no-cache
                - Connection: keep-alive
                - X-Execution-Mode: adhoc

                Example streaming request:
                ```python
                response = requests.post(
                    '/v1/retrievers/execute',
                    json={
                        'collection_identifiers': ['my_collection'],
                        'input_schema': {'query': {'type': 'text', 'required': True}},
                        'stages': [...],
                        'inputs': {'query': 'machine learning'},
                        'stream': True
                    },
                    stream=True
                )
                for line in response.iter_lines():
                    if line.startswith(b'data: '):
                        event = json.loads(line[6:])
                        print(f"{event['event_type']}: {event.get('stage_name')}")
                ```

            Standard Execution (stream=False, default):
                Returns a single ExecuteRetrieverResponse with final documents,
                pagination, and aggregate statistics after all stages complete.

            Examples:
                Simple ad-hoc search:
                    {
                        "collection_identifiers": ["col_123"],
                        "input_schema": {"query": {"type": "text", "required": True}},
                        "stages": [{
                            "stage_name": "search",
                            "stage_type": "filter",
                            "config": {
                                "stage_id": "feature_search",
                                "parameters": {
                                    "searches": [{
                                        "feature_uri": "mixpeek://text_extractor@v1/embedding",
                                        "query": {
                                            "input_mode": "text",
                                            "text": "{{INPUT.query}}"
                                        },
                                        "top_k": 100
                                    }],
                                    "final_top_k": 10
                                }
                            }
                        }],
                        "inputs": {"query": "machine learning"},
                        "stream": false
                    }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        return_presigned_urls=return_presigned_urls,
        return_vectors=return_vectors,
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
    body: AdhocExecuteRequest,
    return_presigned_urls: bool | Unset = False,
    return_vectors: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    r"""Execute Adhoc Retriever

     Execute a retriever ad-hoc without persisting the configuration.

    This endpoint allows you to execute a retriever without saving it to the database.
    Useful for one-time queries, testing configurations, or temporary searches.

    Streaming Execution (stream=True):
        Response uses Server-Sent Events (SSE) format with Content-Type: text/event-stream.
        Each stage emits events as it executes, formatted as: data: {json}\n\n

        Event Types (StreamEventType):
        - stage_start: Emitted when a stage begins (includes stage_name, stage_index, total_stages)
        - stage_complete: Emitted when a stage finishes (includes documents, statistics, budget_used)
        - stage_error: Emitted if a stage fails (includes error message)
        - execution_complete: Final event with complete results and pagination
        - execution_error: Emitted if entire execution fails

        StreamStageEvent Fields:
        - event_type: Type of event
        - execution_id: Unique execution identifier
        - stage_name/stage_index/total_stages: Stage progress info
        - documents: Intermediate results (stage_complete only)
        - statistics: Stage metrics (duration_ms, input_count, output_count, efficiency)
        - budget_used: Cumulative consumption (credits_used, time_elapsed_ms, tokens_used)

        Response Headers:
        - Content-Type: text/event-stream
        - Cache-Control: no-cache
        - Connection: keep-alive
        - X-Execution-Mode: adhoc

    Standard Execution (stream=False, default):
        - Returns ExecuteRetrieverResponse after all stages complete
        - Includes X-Execution-Mode: adhoc header
        - execution_metadata.retriever_persisted = False

    Use Cases:
        - One-time queries without saving retriever configuration
        - Testing stage configurations before persisting
        - Dynamic retrieval with varying parameters
        - Real-time progress tracking with streaming

    Args:
        return_presigned_urls (bool | Unset):  Default: False.
        return_vectors (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (AdhocExecuteRequest): Request to execute a retriever ad-hoc without persistence.

            This combines retriever creation parameters with execution inputs to allow
            one-time retrieval without saving the retriever configuration.

            Use Cases:
                - One-time queries without polluting retriever registry
                - Testing retriever configurations before persisting
                - Dynamic retrieval with varying stage configurations
                - Temporary search operations

            Behavior:
                - Retriever is NOT saved to database
                - Execution history is logged but marked as ad-hoc
                - Response includes X-Execution-Mode: adhoc header
                - execution_metadata.retriever_persisted = False

            Streaming Execution (stream=True):
                When streaming is enabled, the response uses Server-Sent Events (SSE) format
                with Content-Type: text/event-stream. Each stage emits events as it executes:

                Event Types:
                - stage_start: Emitted when a stage begins execution
                - stage_complete: Emitted when a stage finishes with results
                - stage_error: Emitted if a stage encounters an error
                - execution_complete: Emitted after all stages finish successfully
                - execution_error: Emitted if the entire execution fails

                Each event is a StreamStageEvent containing:
                - event_type: The type of event
                - execution_id: Unique execution identifier
                - stage_name: Human-readable stage name
                - stage_index: Zero-based stage position
                - total_stages: Total number of stages
                - documents: Intermediate results (for stage_complete)
                - statistics: Stage metrics (duration_ms, input_count, output_count, etc.)
                - budget_used: Cumulative resource consumption (credits, time, tokens)

                Response Headers (streaming):
                - Content-Type: text/event-stream
                - Cache-Control: no-cache
                - Connection: keep-alive
                - X-Execution-Mode: adhoc

                Example streaming request:
                ```python
                response = requests.post(
                    '/v1/retrievers/execute',
                    json={
                        'collection_identifiers': ['my_collection'],
                        'input_schema': {'query': {'type': 'text', 'required': True}},
                        'stages': [...],
                        'inputs': {'query': 'machine learning'},
                        'stream': True
                    },
                    stream=True
                )
                for line in response.iter_lines():
                    if line.startswith(b'data: '):
                        event = json.loads(line[6:])
                        print(f"{event['event_type']}: {event.get('stage_name')}")
                ```

            Standard Execution (stream=False, default):
                Returns a single ExecuteRetrieverResponse with final documents,
                pagination, and aggregate statistics after all stages complete.

            Examples:
                Simple ad-hoc search:
                    {
                        "collection_identifiers": ["col_123"],
                        "input_schema": {"query": {"type": "text", "required": True}},
                        "stages": [{
                            "stage_name": "search",
                            "stage_type": "filter",
                            "config": {
                                "stage_id": "feature_search",
                                "parameters": {
                                    "searches": [{
                                        "feature_uri": "mixpeek://text_extractor@v1/embedding",
                                        "query": {
                                            "input_mode": "text",
                                            "text": "{{INPUT.query}}"
                                        },
                                        "top_k": 100
                                    }],
                                    "final_top_k": 10
                                }
                            }
                        }],
                        "inputs": {"query": "machine learning"},
                        "stream": false
                    }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        return_presigned_urls=return_presigned_urls,
        return_vectors=return_vectors,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AdhocExecuteRequest,
    return_presigned_urls: bool | Unset = False,
    return_vectors: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    r"""Execute Adhoc Retriever

     Execute a retriever ad-hoc without persisting the configuration.

    This endpoint allows you to execute a retriever without saving it to the database.
    Useful for one-time queries, testing configurations, or temporary searches.

    Streaming Execution (stream=True):
        Response uses Server-Sent Events (SSE) format with Content-Type: text/event-stream.
        Each stage emits events as it executes, formatted as: data: {json}\n\n

        Event Types (StreamEventType):
        - stage_start: Emitted when a stage begins (includes stage_name, stage_index, total_stages)
        - stage_complete: Emitted when a stage finishes (includes documents, statistics, budget_used)
        - stage_error: Emitted if a stage fails (includes error message)
        - execution_complete: Final event with complete results and pagination
        - execution_error: Emitted if entire execution fails

        StreamStageEvent Fields:
        - event_type: Type of event
        - execution_id: Unique execution identifier
        - stage_name/stage_index/total_stages: Stage progress info
        - documents: Intermediate results (stage_complete only)
        - statistics: Stage metrics (duration_ms, input_count, output_count, efficiency)
        - budget_used: Cumulative consumption (credits_used, time_elapsed_ms, tokens_used)

        Response Headers:
        - Content-Type: text/event-stream
        - Cache-Control: no-cache
        - Connection: keep-alive
        - X-Execution-Mode: adhoc

    Standard Execution (stream=False, default):
        - Returns ExecuteRetrieverResponse after all stages complete
        - Includes X-Execution-Mode: adhoc header
        - execution_metadata.retriever_persisted = False

    Use Cases:
        - One-time queries without saving retriever configuration
        - Testing stage configurations before persisting
        - Dynamic retrieval with varying parameters
        - Real-time progress tracking with streaming

    Args:
        return_presigned_urls (bool | Unset):  Default: False.
        return_vectors (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (AdhocExecuteRequest): Request to execute a retriever ad-hoc without persistence.

            This combines retriever creation parameters with execution inputs to allow
            one-time retrieval without saving the retriever configuration.

            Use Cases:
                - One-time queries without polluting retriever registry
                - Testing retriever configurations before persisting
                - Dynamic retrieval with varying stage configurations
                - Temporary search operations

            Behavior:
                - Retriever is NOT saved to database
                - Execution history is logged but marked as ad-hoc
                - Response includes X-Execution-Mode: adhoc header
                - execution_metadata.retriever_persisted = False

            Streaming Execution (stream=True):
                When streaming is enabled, the response uses Server-Sent Events (SSE) format
                with Content-Type: text/event-stream. Each stage emits events as it executes:

                Event Types:
                - stage_start: Emitted when a stage begins execution
                - stage_complete: Emitted when a stage finishes with results
                - stage_error: Emitted if a stage encounters an error
                - execution_complete: Emitted after all stages finish successfully
                - execution_error: Emitted if the entire execution fails

                Each event is a StreamStageEvent containing:
                - event_type: The type of event
                - execution_id: Unique execution identifier
                - stage_name: Human-readable stage name
                - stage_index: Zero-based stage position
                - total_stages: Total number of stages
                - documents: Intermediate results (for stage_complete)
                - statistics: Stage metrics (duration_ms, input_count, output_count, etc.)
                - budget_used: Cumulative resource consumption (credits, time, tokens)

                Response Headers (streaming):
                - Content-Type: text/event-stream
                - Cache-Control: no-cache
                - Connection: keep-alive
                - X-Execution-Mode: adhoc

                Example streaming request:
                ```python
                response = requests.post(
                    '/v1/retrievers/execute',
                    json={
                        'collection_identifiers': ['my_collection'],
                        'input_schema': {'query': {'type': 'text', 'required': True}},
                        'stages': [...],
                        'inputs': {'query': 'machine learning'},
                        'stream': True
                    },
                    stream=True
                )
                for line in response.iter_lines():
                    if line.startswith(b'data: '):
                        event = json.loads(line[6:])
                        print(f"{event['event_type']}: {event.get('stage_name')}")
                ```

            Standard Execution (stream=False, default):
                Returns a single ExecuteRetrieverResponse with final documents,
                pagination, and aggregate statistics after all stages complete.

            Examples:
                Simple ad-hoc search:
                    {
                        "collection_identifiers": ["col_123"],
                        "input_schema": {"query": {"type": "text", "required": True}},
                        "stages": [{
                            "stage_name": "search",
                            "stage_type": "filter",
                            "config": {
                                "stage_id": "feature_search",
                                "parameters": {
                                    "searches": [{
                                        "feature_uri": "mixpeek://text_extractor@v1/embedding",
                                        "query": {
                                            "input_mode": "text",
                                            "text": "{{INPUT.query}}"
                                        },
                                        "top_k": 100
                                    }],
                                    "final_top_k": 10
                                }
                            }
                        }],
                        "inputs": {"query": "machine learning"},
                        "stream": false
                    }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        return_presigned_urls=return_presigned_urls,
        return_vectors=return_vectors,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AdhocExecuteRequest,
    return_presigned_urls: bool | Unset = False,
    return_vectors: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    r"""Execute Adhoc Retriever

     Execute a retriever ad-hoc without persisting the configuration.

    This endpoint allows you to execute a retriever without saving it to the database.
    Useful for one-time queries, testing configurations, or temporary searches.

    Streaming Execution (stream=True):
        Response uses Server-Sent Events (SSE) format with Content-Type: text/event-stream.
        Each stage emits events as it executes, formatted as: data: {json}\n\n

        Event Types (StreamEventType):
        - stage_start: Emitted when a stage begins (includes stage_name, stage_index, total_stages)
        - stage_complete: Emitted when a stage finishes (includes documents, statistics, budget_used)
        - stage_error: Emitted if a stage fails (includes error message)
        - execution_complete: Final event with complete results and pagination
        - execution_error: Emitted if entire execution fails

        StreamStageEvent Fields:
        - event_type: Type of event
        - execution_id: Unique execution identifier
        - stage_name/stage_index/total_stages: Stage progress info
        - documents: Intermediate results (stage_complete only)
        - statistics: Stage metrics (duration_ms, input_count, output_count, efficiency)
        - budget_used: Cumulative consumption (credits_used, time_elapsed_ms, tokens_used)

        Response Headers:
        - Content-Type: text/event-stream
        - Cache-Control: no-cache
        - Connection: keep-alive
        - X-Execution-Mode: adhoc

    Standard Execution (stream=False, default):
        - Returns ExecuteRetrieverResponse after all stages complete
        - Includes X-Execution-Mode: adhoc header
        - execution_metadata.retriever_persisted = False

    Use Cases:
        - One-time queries without saving retriever configuration
        - Testing stage configurations before persisting
        - Dynamic retrieval with varying parameters
        - Real-time progress tracking with streaming

    Args:
        return_presigned_urls (bool | Unset):  Default: False.
        return_vectors (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (AdhocExecuteRequest): Request to execute a retriever ad-hoc without persistence.

            This combines retriever creation parameters with execution inputs to allow
            one-time retrieval without saving the retriever configuration.

            Use Cases:
                - One-time queries without polluting retriever registry
                - Testing retriever configurations before persisting
                - Dynamic retrieval with varying stage configurations
                - Temporary search operations

            Behavior:
                - Retriever is NOT saved to database
                - Execution history is logged but marked as ad-hoc
                - Response includes X-Execution-Mode: adhoc header
                - execution_metadata.retriever_persisted = False

            Streaming Execution (stream=True):
                When streaming is enabled, the response uses Server-Sent Events (SSE) format
                with Content-Type: text/event-stream. Each stage emits events as it executes:

                Event Types:
                - stage_start: Emitted when a stage begins execution
                - stage_complete: Emitted when a stage finishes with results
                - stage_error: Emitted if a stage encounters an error
                - execution_complete: Emitted after all stages finish successfully
                - execution_error: Emitted if the entire execution fails

                Each event is a StreamStageEvent containing:
                - event_type: The type of event
                - execution_id: Unique execution identifier
                - stage_name: Human-readable stage name
                - stage_index: Zero-based stage position
                - total_stages: Total number of stages
                - documents: Intermediate results (for stage_complete)
                - statistics: Stage metrics (duration_ms, input_count, output_count, etc.)
                - budget_used: Cumulative resource consumption (credits, time, tokens)

                Response Headers (streaming):
                - Content-Type: text/event-stream
                - Cache-Control: no-cache
                - Connection: keep-alive
                - X-Execution-Mode: adhoc

                Example streaming request:
                ```python
                response = requests.post(
                    '/v1/retrievers/execute',
                    json={
                        'collection_identifiers': ['my_collection'],
                        'input_schema': {'query': {'type': 'text', 'required': True}},
                        'stages': [...],
                        'inputs': {'query': 'machine learning'},
                        'stream': True
                    },
                    stream=True
                )
                for line in response.iter_lines():
                    if line.startswith(b'data: '):
                        event = json.loads(line[6:])
                        print(f"{event['event_type']}: {event.get('stage_name')}")
                ```

            Standard Execution (stream=False, default):
                Returns a single ExecuteRetrieverResponse with final documents,
                pagination, and aggregate statistics after all stages complete.

            Examples:
                Simple ad-hoc search:
                    {
                        "collection_identifiers": ["col_123"],
                        "input_schema": {"query": {"type": "text", "required": True}},
                        "stages": [{
                            "stage_name": "search",
                            "stage_type": "filter",
                            "config": {
                                "stage_id": "feature_search",
                                "parameters": {
                                    "searches": [{
                                        "feature_uri": "mixpeek://text_extractor@v1/embedding",
                                        "query": {
                                            "input_mode": "text",
                                            "text": "{{INPUT.query}}"
                                        },
                                        "top_k": 100
                                    }],
                                    "final_top_k": 10
                                }
                            }
                        }],
                        "inputs": {"query": "machine learning"},
                        "stream": false
                    }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            return_presigned_urls=return_presigned_urls,
            return_vectors=return_vectors,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
