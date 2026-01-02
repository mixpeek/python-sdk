from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_history_response import GetHistoryResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    session_id: str,
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/agents/sessions/{session_id}/history".format(
            session_id=quote(str(session_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | GetHistoryResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = GetHistoryResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | GetHistoryResponse | HTTPValidationError]:
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
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | GetHistoryResponse | HTTPValidationError]:
    r""" Get History

     Get conversation history for a session.

    Returns messages in chronological order (oldest first).

    Args:
        request: FastAPI request with tenant context
        session_id: Session identifier
        limit: Maximum messages to return (default: 50, max: 200)
        offset: Pagination offset (default: 0)

    Returns:
        GetHistoryResponse with message history

    Raises:
        NotFoundError: If session not found

    Example:
        ```bash
        curl -X GET \"http://localhost:8000/v1/agents/sessions/ses_abc123/history?limit=20&offset=0\" \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\"
        ```

    Args:
        session_id (str): Session ID
        limit (int | Unset): Maximum messages to return Default: 50.
        offset (int | Unset): Pagination offset Default: 0.
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
        Response[ErrorResponse | GetHistoryResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        session_id=session_id,
        limit=limit,
        offset=offset,
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
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | GetHistoryResponse | HTTPValidationError | None:
    r""" Get History

     Get conversation history for a session.

    Returns messages in chronological order (oldest first).

    Args:
        request: FastAPI request with tenant context
        session_id: Session identifier
        limit: Maximum messages to return (default: 50, max: 200)
        offset: Pagination offset (default: 0)

    Returns:
        GetHistoryResponse with message history

    Raises:
        NotFoundError: If session not found

    Example:
        ```bash
        curl -X GET \"http://localhost:8000/v1/agents/sessions/ses_abc123/history?limit=20&offset=0\" \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\"
        ```

    Args:
        session_id (str): Session ID
        limit (int | Unset): Maximum messages to return Default: 50.
        offset (int | Unset): Pagination offset Default: 0.
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
        ErrorResponse | GetHistoryResponse | HTTPValidationError
     """

    return sync_detailed(
        session_id=session_id,
        client=client,
        limit=limit,
        offset=offset,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | GetHistoryResponse | HTTPValidationError]:
    r""" Get History

     Get conversation history for a session.

    Returns messages in chronological order (oldest first).

    Args:
        request: FastAPI request with tenant context
        session_id: Session identifier
        limit: Maximum messages to return (default: 50, max: 200)
        offset: Pagination offset (default: 0)

    Returns:
        GetHistoryResponse with message history

    Raises:
        NotFoundError: If session not found

    Example:
        ```bash
        curl -X GET \"http://localhost:8000/v1/agents/sessions/ses_abc123/history?limit=20&offset=0\" \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\"
        ```

    Args:
        session_id (str): Session ID
        limit (int | Unset): Maximum messages to return Default: 50.
        offset (int | Unset): Pagination offset Default: 0.
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
        Response[ErrorResponse | GetHistoryResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        session_id=session_id,
        limit=limit,
        offset=offset,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | GetHistoryResponse | HTTPValidationError | None:
    r""" Get History

     Get conversation history for a session.

    Returns messages in chronological order (oldest first).

    Args:
        request: FastAPI request with tenant context
        session_id: Session identifier
        limit: Maximum messages to return (default: 50, max: 200)
        offset: Pagination offset (default: 0)

    Returns:
        GetHistoryResponse with message history

    Raises:
        NotFoundError: If session not found

    Example:
        ```bash
        curl -X GET \"http://localhost:8000/v1/agents/sessions/ses_abc123/history?limit=20&offset=0\" \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\"
        ```

    Args:
        session_id (str): Session ID
        limit (int | Unset): Maximum messages to return Default: 50.
        offset (int | Unset): Pagination offset Default: 0.
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
        ErrorResponse | GetHistoryResponse | HTTPValidationError
     """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            limit=limit,
            offset=offset,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
