from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_session_request import CreateSessionRequest
from ...models.create_session_response import CreateSessionResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateSessionRequest,
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
        "url": "/v1/agents/sessions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateSessionResponse | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CreateSessionResponse.from_dict(response.json())

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
) -> Response[CreateSessionResponse | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSessionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[CreateSessionResponse | ErrorResponse | HTTPValidationError]:
    r""" Create Session

     Create a new agent session.

    A session represents a stateful conversation with an AI agent that can
    call tools to search data, filter results, and perform multi-step reasoning.

    Args:
        request: FastAPI request with tenant context
        payload: Session creation request

    Returns:
        CreateSessionResponse with session metadata

    Example:
        ```bash
        curl -X POST http://localhost:8000/v1/agents/sessions \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"agent_config\": {
              \"model\": \"claude-3-5-sonnet-20241022\",
              \"temperature\": 0.7,
              \"available_tools\": [\"search_retrievers\", \"execute_retriever\"]
            },
            \"quotas\": {
              \"max_messages\": 100,
              \"max_tokens_total\": 100000
            }
          }'
        ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateSessionRequest): Request payload for creating a new agent session.

            Attributes:
                agent_config: Agent configuration (model, temperature, tools, etc.)
                quotas: Optional session quotas and rate limits
                user_id: Optional user identifier
                user_memory: Optional initial user memory/preferences
                metadata: Optional session metadata

            Example:
                ```python
                request = CreateSessionRequest(
                    agent_config=AgentConfig(
                        model="claude-3-5-sonnet-20241022",
                        temperature=0.7,
                        available_tools=["search_retrievers", "execute_retriever"]
                    ),
                    quotas=SessionQuotas(
                        max_messages=100,
                        max_tokens_total=100000
                    ),
                    user_id="user_123",
                    user_memory={"preferences": {"language": "en"}}
                )
                ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSessionResponse | ErrorResponse | HTTPValidationError]
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
    body: CreateSessionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> CreateSessionResponse | ErrorResponse | HTTPValidationError | None:
    r""" Create Session

     Create a new agent session.

    A session represents a stateful conversation with an AI agent that can
    call tools to search data, filter results, and perform multi-step reasoning.

    Args:
        request: FastAPI request with tenant context
        payload: Session creation request

    Returns:
        CreateSessionResponse with session metadata

    Example:
        ```bash
        curl -X POST http://localhost:8000/v1/agents/sessions \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"agent_config\": {
              \"model\": \"claude-3-5-sonnet-20241022\",
              \"temperature\": 0.7,
              \"available_tools\": [\"search_retrievers\", \"execute_retriever\"]
            },
            \"quotas\": {
              \"max_messages\": 100,
              \"max_tokens_total\": 100000
            }
          }'
        ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateSessionRequest): Request payload for creating a new agent session.

            Attributes:
                agent_config: Agent configuration (model, temperature, tools, etc.)
                quotas: Optional session quotas and rate limits
                user_id: Optional user identifier
                user_memory: Optional initial user memory/preferences
                metadata: Optional session metadata

            Example:
                ```python
                request = CreateSessionRequest(
                    agent_config=AgentConfig(
                        model="claude-3-5-sonnet-20241022",
                        temperature=0.7,
                        available_tools=["search_retrievers", "execute_retriever"]
                    ),
                    quotas=SessionQuotas(
                        max_messages=100,
                        max_tokens_total=100000
                    ),
                    user_id="user_123",
                    user_memory={"preferences": {"language": "en"}}
                )
                ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSessionResponse | ErrorResponse | HTTPValidationError
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
    body: CreateSessionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[CreateSessionResponse | ErrorResponse | HTTPValidationError]:
    r""" Create Session

     Create a new agent session.

    A session represents a stateful conversation with an AI agent that can
    call tools to search data, filter results, and perform multi-step reasoning.

    Args:
        request: FastAPI request with tenant context
        payload: Session creation request

    Returns:
        CreateSessionResponse with session metadata

    Example:
        ```bash
        curl -X POST http://localhost:8000/v1/agents/sessions \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"agent_config\": {
              \"model\": \"claude-3-5-sonnet-20241022\",
              \"temperature\": 0.7,
              \"available_tools\": [\"search_retrievers\", \"execute_retriever\"]
            },
            \"quotas\": {
              \"max_messages\": 100,
              \"max_tokens_total\": 100000
            }
          }'
        ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateSessionRequest): Request payload for creating a new agent session.

            Attributes:
                agent_config: Agent configuration (model, temperature, tools, etc.)
                quotas: Optional session quotas and rate limits
                user_id: Optional user identifier
                user_memory: Optional initial user memory/preferences
                metadata: Optional session metadata

            Example:
                ```python
                request = CreateSessionRequest(
                    agent_config=AgentConfig(
                        model="claude-3-5-sonnet-20241022",
                        temperature=0.7,
                        available_tools=["search_retrievers", "execute_retriever"]
                    ),
                    quotas=SessionQuotas(
                        max_messages=100,
                        max_tokens_total=100000
                    ),
                    user_id="user_123",
                    user_memory={"preferences": {"language": "en"}}
                )
                ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSessionResponse | ErrorResponse | HTTPValidationError]
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
    body: CreateSessionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> CreateSessionResponse | ErrorResponse | HTTPValidationError | None:
    r""" Create Session

     Create a new agent session.

    A session represents a stateful conversation with an AI agent that can
    call tools to search data, filter results, and perform multi-step reasoning.

    Args:
        request: FastAPI request with tenant context
        payload: Session creation request

    Returns:
        CreateSessionResponse with session metadata

    Example:
        ```bash
        curl -X POST http://localhost:8000/v1/agents/sessions \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"agent_config\": {
              \"model\": \"claude-3-5-sonnet-20241022\",
              \"temperature\": 0.7,
              \"available_tools\": [\"search_retrievers\", \"execute_retriever\"]
            },
            \"quotas\": {
              \"max_messages\": 100,
              \"max_tokens_total\": 100000
            }
          }'
        ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateSessionRequest): Request payload for creating a new agent session.

            Attributes:
                agent_config: Agent configuration (model, temperature, tools, etc.)
                quotas: Optional session quotas and rate limits
                user_id: Optional user identifier
                user_memory: Optional initial user memory/preferences
                metadata: Optional session metadata

            Example:
                ```python
                request = CreateSessionRequest(
                    agent_config=AgentConfig(
                        model="claude-3-5-sonnet-20241022",
                        temperature=0.7,
                        available_tools=["search_retrievers", "execute_retriever"]
                    ),
                    quotas=SessionQuotas(
                        max_messages=100,
                        max_tokens_total=100000
                    ),
                    user_id="user_123",
                    user_memory={"preferences": {"language": "en"}}
                )
                ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSessionResponse | ErrorResponse | HTTPValidationError
     """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
