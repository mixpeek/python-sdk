from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.execute_retriever_request import ExecuteRetrieverRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    retriever_id: str,
    *,
    body: ExecuteRetrieverRequest,
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
        "url": "/v1/retrievers/{retriever_id}/execute".format(
            retriever_id=quote(str(retriever_id), safe=""),
        ),
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
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExecuteRetrieverRequest,
    return_presigned_urls: bool | Unset = False,
    return_vectors: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    r"""Execute Retriever (Auto-Optimized)

     Execute a retriever and return matching documents. The pipeline is automatically optimized before
    execution for best performance.

    **Automatic Optimization:**
    Your pipeline stages are automatically transformed for optimal performance:
    - Filters pushed down to reduce expensive operations
    - Redundant stages merged or eliminated
    - Grouping operations pushed to database layer (10-100x faster)
    - Operations reordered for efficiency

    **Streaming Support:**
    Set stream=true in the request body to receive real-time stage updates via SSE:
    - Response uses text/event-stream content type
    - Each stage emits stage_start and stage_complete events
    - Final event contains complete results and pagination
    - Useful for progress tracking and debugging

    **Response Includes (when stream=false):**
    - documents: Final matching documents
    - pagination: Pagination metadata
    - stage_statistics: Per-stage execution metrics
    - budget: Credit/time consumption
    - optimization_applied: Whether optimizations were applied
    - optimization_summary: Details about transformations (when applied)

    **Optimization Summary Example:**
    ```json
    {
      \"optimization_applied\": true,
      \"optimization_summary\": {
        \"original_stage_count\": 5,
        \"optimized_stage_count\": 3,
        \"optimization_time_ms\": 8.2,
        \"rules_applied\": [\"push_down_filters\", \"group_by_push_down\"],
        \"stage_reduction_pct\": 40.0
      }
    }
    ```

    Use the /explain endpoint to see the optimized execution plan before running.

    Args:
        retriever_id (str): Retriever ID or name. Pipeline will be automatically optimized before
            execution.
        return_presigned_urls (bool | Unset):  Default: False.
        return_vectors (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ExecuteRetrieverRequest): Request to execute a retriever with optional streaming
            support.

            Inherits all fields from RetrieverExecutionRequest including:
            - inputs: Runtime input values matching the retriever's input_schema
            - pagination: Pagination configuration (cursor, offset, etc.)
            - stream: Enable SSE streaming for real-time stage updates

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
                - statistics: Stage metrics (duration, counts, etc.)
                - budget_used: Cumulative resource consumption

                Example streaming client:
                ```python
                response = requests.post(
                    '/v1/retrievers/{id}/execute',
                    json={'inputs': {...}, 'stream': True},
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        retriever_id=retriever_id,
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
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExecuteRetrieverRequest,
    return_presigned_urls: bool | Unset = False,
    return_vectors: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    r"""Execute Retriever (Auto-Optimized)

     Execute a retriever and return matching documents. The pipeline is automatically optimized before
    execution for best performance.

    **Automatic Optimization:**
    Your pipeline stages are automatically transformed for optimal performance:
    - Filters pushed down to reduce expensive operations
    - Redundant stages merged or eliminated
    - Grouping operations pushed to database layer (10-100x faster)
    - Operations reordered for efficiency

    **Streaming Support:**
    Set stream=true in the request body to receive real-time stage updates via SSE:
    - Response uses text/event-stream content type
    - Each stage emits stage_start and stage_complete events
    - Final event contains complete results and pagination
    - Useful for progress tracking and debugging

    **Response Includes (when stream=false):**
    - documents: Final matching documents
    - pagination: Pagination metadata
    - stage_statistics: Per-stage execution metrics
    - budget: Credit/time consumption
    - optimization_applied: Whether optimizations were applied
    - optimization_summary: Details about transformations (when applied)

    **Optimization Summary Example:**
    ```json
    {
      \"optimization_applied\": true,
      \"optimization_summary\": {
        \"original_stage_count\": 5,
        \"optimized_stage_count\": 3,
        \"optimization_time_ms\": 8.2,
        \"rules_applied\": [\"push_down_filters\", \"group_by_push_down\"],
        \"stage_reduction_pct\": 40.0
      }
    }
    ```

    Use the /explain endpoint to see the optimized execution plan before running.

    Args:
        retriever_id (str): Retriever ID or name. Pipeline will be automatically optimized before
            execution.
        return_presigned_urls (bool | Unset):  Default: False.
        return_vectors (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ExecuteRetrieverRequest): Request to execute a retriever with optional streaming
            support.

            Inherits all fields from RetrieverExecutionRequest including:
            - inputs: Runtime input values matching the retriever's input_schema
            - pagination: Pagination configuration (cursor, offset, etc.)
            - stream: Enable SSE streaming for real-time stage updates

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
                - statistics: Stage metrics (duration, counts, etc.)
                - budget_used: Cumulative resource consumption

                Example streaming client:
                ```python
                response = requests.post(
                    '/v1/retrievers/{id}/execute',
                    json={'inputs': {...}, 'stream': True},
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        retriever_id=retriever_id,
        client=client,
        body=body,
        return_presigned_urls=return_presigned_urls,
        return_vectors=return_vectors,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExecuteRetrieverRequest,
    return_presigned_urls: bool | Unset = False,
    return_vectors: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    r"""Execute Retriever (Auto-Optimized)

     Execute a retriever and return matching documents. The pipeline is automatically optimized before
    execution for best performance.

    **Automatic Optimization:**
    Your pipeline stages are automatically transformed for optimal performance:
    - Filters pushed down to reduce expensive operations
    - Redundant stages merged or eliminated
    - Grouping operations pushed to database layer (10-100x faster)
    - Operations reordered for efficiency

    **Streaming Support:**
    Set stream=true in the request body to receive real-time stage updates via SSE:
    - Response uses text/event-stream content type
    - Each stage emits stage_start and stage_complete events
    - Final event contains complete results and pagination
    - Useful for progress tracking and debugging

    **Response Includes (when stream=false):**
    - documents: Final matching documents
    - pagination: Pagination metadata
    - stage_statistics: Per-stage execution metrics
    - budget: Credit/time consumption
    - optimization_applied: Whether optimizations were applied
    - optimization_summary: Details about transformations (when applied)

    **Optimization Summary Example:**
    ```json
    {
      \"optimization_applied\": true,
      \"optimization_summary\": {
        \"original_stage_count\": 5,
        \"optimized_stage_count\": 3,
        \"optimization_time_ms\": 8.2,
        \"rules_applied\": [\"push_down_filters\", \"group_by_push_down\"],
        \"stage_reduction_pct\": 40.0
      }
    }
    ```

    Use the /explain endpoint to see the optimized execution plan before running.

    Args:
        retriever_id (str): Retriever ID or name. Pipeline will be automatically optimized before
            execution.
        return_presigned_urls (bool | Unset):  Default: False.
        return_vectors (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ExecuteRetrieverRequest): Request to execute a retriever with optional streaming
            support.

            Inherits all fields from RetrieverExecutionRequest including:
            - inputs: Runtime input values matching the retriever's input_schema
            - pagination: Pagination configuration (cursor, offset, etc.)
            - stream: Enable SSE streaming for real-time stage updates

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
                - statistics: Stage metrics (duration, counts, etc.)
                - budget_used: Cumulative resource consumption

                Example streaming client:
                ```python
                response = requests.post(
                    '/v1/retrievers/{id}/execute',
                    json={'inputs': {...}, 'stream': True},
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        retriever_id=retriever_id,
        body=body,
        return_presigned_urls=return_presigned_urls,
        return_vectors=return_vectors,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExecuteRetrieverRequest,
    return_presigned_urls: bool | Unset = False,
    return_vectors: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    r"""Execute Retriever (Auto-Optimized)

     Execute a retriever and return matching documents. The pipeline is automatically optimized before
    execution for best performance.

    **Automatic Optimization:**
    Your pipeline stages are automatically transformed for optimal performance:
    - Filters pushed down to reduce expensive operations
    - Redundant stages merged or eliminated
    - Grouping operations pushed to database layer (10-100x faster)
    - Operations reordered for efficiency

    **Streaming Support:**
    Set stream=true in the request body to receive real-time stage updates via SSE:
    - Response uses text/event-stream content type
    - Each stage emits stage_start and stage_complete events
    - Final event contains complete results and pagination
    - Useful for progress tracking and debugging

    **Response Includes (when stream=false):**
    - documents: Final matching documents
    - pagination: Pagination metadata
    - stage_statistics: Per-stage execution metrics
    - budget: Credit/time consumption
    - optimization_applied: Whether optimizations were applied
    - optimization_summary: Details about transformations (when applied)

    **Optimization Summary Example:**
    ```json
    {
      \"optimization_applied\": true,
      \"optimization_summary\": {
        \"original_stage_count\": 5,
        \"optimized_stage_count\": 3,
        \"optimization_time_ms\": 8.2,
        \"rules_applied\": [\"push_down_filters\", \"group_by_push_down\"],
        \"stage_reduction_pct\": 40.0
      }
    }
    ```

    Use the /explain endpoint to see the optimized execution plan before running.

    Args:
        retriever_id (str): Retriever ID or name. Pipeline will be automatically optimized before
            execution.
        return_presigned_urls (bool | Unset):  Default: False.
        return_vectors (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ExecuteRetrieverRequest): Request to execute a retriever with optional streaming
            support.

            Inherits all fields from RetrieverExecutionRequest including:
            - inputs: Runtime input values matching the retriever's input_schema
            - pagination: Pagination configuration (cursor, offset, etc.)
            - stream: Enable SSE streaming for real-time stage updates

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
                - statistics: Stage metrics (duration, counts, etc.)
                - budget_used: Cumulative resource consumption

                Example streaming client:
                ```python
                response = requests.post(
                    '/v1/retrievers/{id}/execute',
                    json={'inputs': {...}, 'stream': True},
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            retriever_id=retriever_id,
            client=client,
            body=body,
            return_presigned_urls=return_presigned_urls,
            return_vectors=return_vectors,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
