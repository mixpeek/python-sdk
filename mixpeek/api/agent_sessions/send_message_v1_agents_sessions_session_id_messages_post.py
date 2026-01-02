from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.send_message_request import SendMessageRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    session_id: str,
    *,
    body: SendMessageRequest,
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
        "url": "/v1/agents/sessions/{session_id}/messages".format(
            session_id=quote(str(session_id), safe=""),
        ),
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
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendMessageRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    r""" Send Message

     Send a message to the agent and stream the response.

    This endpoint streams Server-Sent Events (SSE) back to the client as
    the agent processes the message through its workflow.

    ## SSE Event Types

    **Core Events:**
    - `intent`: Intent classification result (emitted first)
        - `{intent, confidence, category, reasoning, context_scope}`
    - `thinking`: Agent is analyzing/planning
        - `{step, message}`
    - `tool_call`: Agent is calling a tool
        - `{tool_name, tool_call_id, inputs}`
    - `tool_result`: Tool execution completed
        - `{tool_name, tool_call_id, success, output, latency_ms}`
    - `token`: Response token (streaming)
        - `{content}`
    - `message`: Final response content
        - `{content, message_id, is_final}`
    - `session_name`: Auto-generated session name (first message only)
        - `{session_name}`
    - `done`: Processing complete
        - `{latency_ms, tool_calls_made, message_id, retriever_summary, data_accessed_via_retriever}`
    - `error`: Error occurred
        - `{message, recoverable}`

    **Retriever Events (IMPORTANT - Primary Data Pathway):**
    - `retriever_execution`: Retriever was used for data access
        - `{tool_name, execution_id, retriever_id, is_adhoc, documents_returned, latency_ms, message}`
        - Emitted whenever data is accessed via retriever (saved or ad-hoc)
    - `pipeline_config`: Ad-hoc retriever configuration
        - `{tool_name, config, message}`
        - Contains the exact pipeline config users can save as a named retriever

    **Retriever Summary in `done` Event:**
    ```json
    {
      \"retriever_summary\": {
        \"used_retrievers\": true,
        \"retriever_count\": 2,
        \"saved_retrievers\": 1,
        \"adhoc_retrievers\": 1,
        \"total_documents\": 25,
        \"executions\": [...]
      },
      \"data_accessed_via_retriever\": true
    }
    ```

    Args:
        request: FastAPI request with tenant context
        session_id: Session identifier
        payload: Message request

    Returns:
        StreamingResponse with SSE events

    Raises:
        NotFoundError: If session not found

    Example:
        ```bash
        curl -N -X POST http://localhost:8000/v1/agents/sessions/ses_abc123/messages \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"content\": \"Find videos about machine learning\",
            \"stream\": true
          }'

        # SSE Output:
        event: intent
        data: {\"intent\": \"retriever_search\", \"confidence\": 0.92, \"category\": \"retriever\"}

        event: thinking
        data: {\"step\": \"processing\", \"message\": \"Analyzing your request...\"}

        event: tool_call
        data: {\"tool_name\": \"execute_retriever\", \"tool_call_id\": \"run_abc\", \"inputs\": {...}}

        event: tool_result
        data: {\"tool_name\": \"execute_retriever\", \"success\": true, \"output\": {...}}

        event: retriever_execution
        data: {\"tool_name\": \"execute_retriever\", \"is_adhoc\": false, \"documents_returned\": 5}

        event: message
        data: {\"content\": \"I found 5 videos about machine learning...\", \"is_final\": true}

        event: done
        data: {\"latency_ms\": 1250.5, \"data_accessed_via_retriever\": true, \"retriever_summary\":
    {...}}
        ```

    Args:
        session_id (str): Session ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SendMessageRequest): Request payload for sending a message to the agent.

            Attributes:
                content: Message text content
                metadata: Optional message metadata
                stream: Whether to stream response as SSE (default: True)

            Note:
                When stream=True, the response will be Server-Sent Events (SSE).
                When stream=False, the response will be a MessageResponse object.

            Example:
                ```python
                # Streaming request (SSE)
                request = SendMessageRequest(
                    content="Find videos about machine learning",
                    stream=True
                )

                # Non-streaming request
                request = SendMessageRequest(
                    content="Find videos about machine learning",
                    stream=False
                )
                ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        session_id=session_id,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendMessageRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    r""" Send Message

     Send a message to the agent and stream the response.

    This endpoint streams Server-Sent Events (SSE) back to the client as
    the agent processes the message through its workflow.

    ## SSE Event Types

    **Core Events:**
    - `intent`: Intent classification result (emitted first)
        - `{intent, confidence, category, reasoning, context_scope}`
    - `thinking`: Agent is analyzing/planning
        - `{step, message}`
    - `tool_call`: Agent is calling a tool
        - `{tool_name, tool_call_id, inputs}`
    - `tool_result`: Tool execution completed
        - `{tool_name, tool_call_id, success, output, latency_ms}`
    - `token`: Response token (streaming)
        - `{content}`
    - `message`: Final response content
        - `{content, message_id, is_final}`
    - `session_name`: Auto-generated session name (first message only)
        - `{session_name}`
    - `done`: Processing complete
        - `{latency_ms, tool_calls_made, message_id, retriever_summary, data_accessed_via_retriever}`
    - `error`: Error occurred
        - `{message, recoverable}`

    **Retriever Events (IMPORTANT - Primary Data Pathway):**
    - `retriever_execution`: Retriever was used for data access
        - `{tool_name, execution_id, retriever_id, is_adhoc, documents_returned, latency_ms, message}`
        - Emitted whenever data is accessed via retriever (saved or ad-hoc)
    - `pipeline_config`: Ad-hoc retriever configuration
        - `{tool_name, config, message}`
        - Contains the exact pipeline config users can save as a named retriever

    **Retriever Summary in `done` Event:**
    ```json
    {
      \"retriever_summary\": {
        \"used_retrievers\": true,
        \"retriever_count\": 2,
        \"saved_retrievers\": 1,
        \"adhoc_retrievers\": 1,
        \"total_documents\": 25,
        \"executions\": [...]
      },
      \"data_accessed_via_retriever\": true
    }
    ```

    Args:
        request: FastAPI request with tenant context
        session_id: Session identifier
        payload: Message request

    Returns:
        StreamingResponse with SSE events

    Raises:
        NotFoundError: If session not found

    Example:
        ```bash
        curl -N -X POST http://localhost:8000/v1/agents/sessions/ses_abc123/messages \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"content\": \"Find videos about machine learning\",
            \"stream\": true
          }'

        # SSE Output:
        event: intent
        data: {\"intent\": \"retriever_search\", \"confidence\": 0.92, \"category\": \"retriever\"}

        event: thinking
        data: {\"step\": \"processing\", \"message\": \"Analyzing your request...\"}

        event: tool_call
        data: {\"tool_name\": \"execute_retriever\", \"tool_call_id\": \"run_abc\", \"inputs\": {...}}

        event: tool_result
        data: {\"tool_name\": \"execute_retriever\", \"success\": true, \"output\": {...}}

        event: retriever_execution
        data: {\"tool_name\": \"execute_retriever\", \"is_adhoc\": false, \"documents_returned\": 5}

        event: message
        data: {\"content\": \"I found 5 videos about machine learning...\", \"is_final\": true}

        event: done
        data: {\"latency_ms\": 1250.5, \"data_accessed_via_retriever\": true, \"retriever_summary\":
    {...}}
        ```

    Args:
        session_id (str): Session ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SendMessageRequest): Request payload for sending a message to the agent.

            Attributes:
                content: Message text content
                metadata: Optional message metadata
                stream: Whether to stream response as SSE (default: True)

            Note:
                When stream=True, the response will be Server-Sent Events (SSE).
                When stream=False, the response will be a MessageResponse object.

            Example:
                ```python
                # Streaming request (SSE)
                request = SendMessageRequest(
                    content="Find videos about machine learning",
                    stream=True
                )

                # Non-streaming request
                request = SendMessageRequest(
                    content="Find videos about machine learning",
                    stream=False
                )
                ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
     """

    return sync_detailed(
        session_id=session_id,
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendMessageRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    r""" Send Message

     Send a message to the agent and stream the response.

    This endpoint streams Server-Sent Events (SSE) back to the client as
    the agent processes the message through its workflow.

    ## SSE Event Types

    **Core Events:**
    - `intent`: Intent classification result (emitted first)
        - `{intent, confidence, category, reasoning, context_scope}`
    - `thinking`: Agent is analyzing/planning
        - `{step, message}`
    - `tool_call`: Agent is calling a tool
        - `{tool_name, tool_call_id, inputs}`
    - `tool_result`: Tool execution completed
        - `{tool_name, tool_call_id, success, output, latency_ms}`
    - `token`: Response token (streaming)
        - `{content}`
    - `message`: Final response content
        - `{content, message_id, is_final}`
    - `session_name`: Auto-generated session name (first message only)
        - `{session_name}`
    - `done`: Processing complete
        - `{latency_ms, tool_calls_made, message_id, retriever_summary, data_accessed_via_retriever}`
    - `error`: Error occurred
        - `{message, recoverable}`

    **Retriever Events (IMPORTANT - Primary Data Pathway):**
    - `retriever_execution`: Retriever was used for data access
        - `{tool_name, execution_id, retriever_id, is_adhoc, documents_returned, latency_ms, message}`
        - Emitted whenever data is accessed via retriever (saved or ad-hoc)
    - `pipeline_config`: Ad-hoc retriever configuration
        - `{tool_name, config, message}`
        - Contains the exact pipeline config users can save as a named retriever

    **Retriever Summary in `done` Event:**
    ```json
    {
      \"retriever_summary\": {
        \"used_retrievers\": true,
        \"retriever_count\": 2,
        \"saved_retrievers\": 1,
        \"adhoc_retrievers\": 1,
        \"total_documents\": 25,
        \"executions\": [...]
      },
      \"data_accessed_via_retriever\": true
    }
    ```

    Args:
        request: FastAPI request with tenant context
        session_id: Session identifier
        payload: Message request

    Returns:
        StreamingResponse with SSE events

    Raises:
        NotFoundError: If session not found

    Example:
        ```bash
        curl -N -X POST http://localhost:8000/v1/agents/sessions/ses_abc123/messages \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"content\": \"Find videos about machine learning\",
            \"stream\": true
          }'

        # SSE Output:
        event: intent
        data: {\"intent\": \"retriever_search\", \"confidence\": 0.92, \"category\": \"retriever\"}

        event: thinking
        data: {\"step\": \"processing\", \"message\": \"Analyzing your request...\"}

        event: tool_call
        data: {\"tool_name\": \"execute_retriever\", \"tool_call_id\": \"run_abc\", \"inputs\": {...}}

        event: tool_result
        data: {\"tool_name\": \"execute_retriever\", \"success\": true, \"output\": {...}}

        event: retriever_execution
        data: {\"tool_name\": \"execute_retriever\", \"is_adhoc\": false, \"documents_returned\": 5}

        event: message
        data: {\"content\": \"I found 5 videos about machine learning...\", \"is_final\": true}

        event: done
        data: {\"latency_ms\": 1250.5, \"data_accessed_via_retriever\": true, \"retriever_summary\":
    {...}}
        ```

    Args:
        session_id (str): Session ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SendMessageRequest): Request payload for sending a message to the agent.

            Attributes:
                content: Message text content
                metadata: Optional message metadata
                stream: Whether to stream response as SSE (default: True)

            Note:
                When stream=True, the response will be Server-Sent Events (SSE).
                When stream=False, the response will be a MessageResponse object.

            Example:
                ```python
                # Streaming request (SSE)
                request = SendMessageRequest(
                    content="Find videos about machine learning",
                    stream=True
                )

                # Non-streaming request
                request = SendMessageRequest(
                    content="Find videos about machine learning",
                    stream=False
                )
                ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        session_id=session_id,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendMessageRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    r""" Send Message

     Send a message to the agent and stream the response.

    This endpoint streams Server-Sent Events (SSE) back to the client as
    the agent processes the message through its workflow.

    ## SSE Event Types

    **Core Events:**
    - `intent`: Intent classification result (emitted first)
        - `{intent, confidence, category, reasoning, context_scope}`
    - `thinking`: Agent is analyzing/planning
        - `{step, message}`
    - `tool_call`: Agent is calling a tool
        - `{tool_name, tool_call_id, inputs}`
    - `tool_result`: Tool execution completed
        - `{tool_name, tool_call_id, success, output, latency_ms}`
    - `token`: Response token (streaming)
        - `{content}`
    - `message`: Final response content
        - `{content, message_id, is_final}`
    - `session_name`: Auto-generated session name (first message only)
        - `{session_name}`
    - `done`: Processing complete
        - `{latency_ms, tool_calls_made, message_id, retriever_summary, data_accessed_via_retriever}`
    - `error`: Error occurred
        - `{message, recoverable}`

    **Retriever Events (IMPORTANT - Primary Data Pathway):**
    - `retriever_execution`: Retriever was used for data access
        - `{tool_name, execution_id, retriever_id, is_adhoc, documents_returned, latency_ms, message}`
        - Emitted whenever data is accessed via retriever (saved or ad-hoc)
    - `pipeline_config`: Ad-hoc retriever configuration
        - `{tool_name, config, message}`
        - Contains the exact pipeline config users can save as a named retriever

    **Retriever Summary in `done` Event:**
    ```json
    {
      \"retriever_summary\": {
        \"used_retrievers\": true,
        \"retriever_count\": 2,
        \"saved_retrievers\": 1,
        \"adhoc_retrievers\": 1,
        \"total_documents\": 25,
        \"executions\": [...]
      },
      \"data_accessed_via_retriever\": true
    }
    ```

    Args:
        request: FastAPI request with tenant context
        session_id: Session identifier
        payload: Message request

    Returns:
        StreamingResponse with SSE events

    Raises:
        NotFoundError: If session not found

    Example:
        ```bash
        curl -N -X POST http://localhost:8000/v1/agents/sessions/ses_abc123/messages \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"content\": \"Find videos about machine learning\",
            \"stream\": true
          }'

        # SSE Output:
        event: intent
        data: {\"intent\": \"retriever_search\", \"confidence\": 0.92, \"category\": \"retriever\"}

        event: thinking
        data: {\"step\": \"processing\", \"message\": \"Analyzing your request...\"}

        event: tool_call
        data: {\"tool_name\": \"execute_retriever\", \"tool_call_id\": \"run_abc\", \"inputs\": {...}}

        event: tool_result
        data: {\"tool_name\": \"execute_retriever\", \"success\": true, \"output\": {...}}

        event: retriever_execution
        data: {\"tool_name\": \"execute_retriever\", \"is_adhoc\": false, \"documents_returned\": 5}

        event: message
        data: {\"content\": \"I found 5 videos about machine learning...\", \"is_final\": true}

        event: done
        data: {\"latency_ms\": 1250.5, \"data_accessed_via_retriever\": true, \"retriever_summary\":
    {...}}
        ```

    Args:
        session_id (str): Session ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SendMessageRequest): Request payload for sending a message to the agent.

            Attributes:
                content: Message text content
                metadata: Optional message metadata
                stream: Whether to stream response as SSE (default: True)

            Note:
                When stream=True, the response will be Server-Sent Events (SSE).
                When stream=False, the response will be a MessageResponse object.

            Example:
                ```python
                # Streaming request (SSE)
                request = SendMessageRequest(
                    content="Find videos about machine learning",
                    stream=True
                )

                # Non-streaming request
                request = SendMessageRequest(
                    content="Find videos about machine learning",
                    stream=False
                )
                ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
     """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
