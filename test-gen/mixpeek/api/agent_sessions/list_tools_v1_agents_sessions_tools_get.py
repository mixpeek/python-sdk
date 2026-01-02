from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_tools_response import ListToolsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    json_category: None | str | Unset
    if isinstance(category, Unset):
        json_category = UNSET
    else:
        json_category = category
    params["category"] = json_category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/sessions/tools",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | ListToolsResponse | None:
    if response.status_code == 200:
        response_200 = ListToolsResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | ListToolsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListToolsResponse]:
    r""" List Tools

     List all available agent tools.

    Use this endpoint to discover available tools before creating a session.
    Pass tool names to `available_tools` in AgentConfig when creating a session.

    Tool Categories:
    - search: Tools for searching data (smart_search, execute_retriever, execute_adhoc_retriever)
    - read: Tools for reading resources (list_*, get_*)
    - create: Tools for creating resources (create_*)
    - analyze: Tools for analyzing content (analyze_sample_with_pipeline, transcribe_with_pipeline)
    - upload: Tools for file uploads (create_upload, confirm_upload, get_upload_status)
    - memory: Tools for agent memory (search_feedback)
    - recommendations: Tools for getting recommendations

    Args:
        request: FastAPI request with tenant context
        category: Optional filter by tool category

    Returns:
        ListToolsResponse with available tools

    Example:
        ```bash
        # List all tools
        curl -X GET http://localhost:8000/v1/agents/tools \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\"

        # List only search tools
        curl -X GET \"http://localhost:8000/v1/agents/tools?category=search\" \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\"
        ```

    Args:
        category (None | str | Unset): Filter by tool category
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListToolsResponse]
     """

    kwargs = _get_kwargs(
        category=category,
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
    category: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListToolsResponse | None:
    r""" List Tools

     List all available agent tools.

    Use this endpoint to discover available tools before creating a session.
    Pass tool names to `available_tools` in AgentConfig when creating a session.

    Tool Categories:
    - search: Tools for searching data (smart_search, execute_retriever, execute_adhoc_retriever)
    - read: Tools for reading resources (list_*, get_*)
    - create: Tools for creating resources (create_*)
    - analyze: Tools for analyzing content (analyze_sample_with_pipeline, transcribe_with_pipeline)
    - upload: Tools for file uploads (create_upload, confirm_upload, get_upload_status)
    - memory: Tools for agent memory (search_feedback)
    - recommendations: Tools for getting recommendations

    Args:
        request: FastAPI request with tenant context
        category: Optional filter by tool category

    Returns:
        ListToolsResponse with available tools

    Example:
        ```bash
        # List all tools
        curl -X GET http://localhost:8000/v1/agents/tools \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\"

        # List only search tools
        curl -X GET \"http://localhost:8000/v1/agents/tools?category=search\" \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\"
        ```

    Args:
        category (None | str | Unset): Filter by tool category
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListToolsResponse
     """

    return sync_detailed(
        client=client,
        category=category,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListToolsResponse]:
    r""" List Tools

     List all available agent tools.

    Use this endpoint to discover available tools before creating a session.
    Pass tool names to `available_tools` in AgentConfig when creating a session.

    Tool Categories:
    - search: Tools for searching data (smart_search, execute_retriever, execute_adhoc_retriever)
    - read: Tools for reading resources (list_*, get_*)
    - create: Tools for creating resources (create_*)
    - analyze: Tools for analyzing content (analyze_sample_with_pipeline, transcribe_with_pipeline)
    - upload: Tools for file uploads (create_upload, confirm_upload, get_upload_status)
    - memory: Tools for agent memory (search_feedback)
    - recommendations: Tools for getting recommendations

    Args:
        request: FastAPI request with tenant context
        category: Optional filter by tool category

    Returns:
        ListToolsResponse with available tools

    Example:
        ```bash
        # List all tools
        curl -X GET http://localhost:8000/v1/agents/tools \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\"

        # List only search tools
        curl -X GET \"http://localhost:8000/v1/agents/tools?category=search\" \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\"
        ```

    Args:
        category (None | str | Unset): Filter by tool category
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListToolsResponse]
     """

    kwargs = _get_kwargs(
        category=category,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListToolsResponse | None:
    r""" List Tools

     List all available agent tools.

    Use this endpoint to discover available tools before creating a session.
    Pass tool names to `available_tools` in AgentConfig when creating a session.

    Tool Categories:
    - search: Tools for searching data (smart_search, execute_retriever, execute_adhoc_retriever)
    - read: Tools for reading resources (list_*, get_*)
    - create: Tools for creating resources (create_*)
    - analyze: Tools for analyzing content (analyze_sample_with_pipeline, transcribe_with_pipeline)
    - upload: Tools for file uploads (create_upload, confirm_upload, get_upload_status)
    - memory: Tools for agent memory (search_feedback)
    - recommendations: Tools for getting recommendations

    Args:
        request: FastAPI request with tenant context
        category: Optional filter by tool category

    Returns:
        ListToolsResponse with available tools

    Example:
        ```bash
        # List all tools
        curl -X GET http://localhost:8000/v1/agents/tools \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\"

        # List only search tools
        curl -X GET \"http://localhost:8000/v1/agents/tools?category=search\" \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\"
        ```

    Args:
        category (None | str | Unset): Filter by tool category
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListToolsResponse
     """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
