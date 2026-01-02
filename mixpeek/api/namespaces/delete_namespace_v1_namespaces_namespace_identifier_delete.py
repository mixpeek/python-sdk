from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    namespace_identifier: str,
    *,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/namespaces/{namespace_identifier}".format(
            namespace_identifier=quote(str(namespace_identifier), safe=""),
        ),
    }

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
    namespace_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    """Delete Namespace

     This endpoint deletes a namespace and ALL its resources including:
        - All buckets (with S3 objects, batches, uploads)
        - All collections (with Qdrant points, cache, webhooks)
        - All clusters (with Ray jobs, executions, triggers, S3 artifacts)
        - All retrievers (with executions, evaluations, interactions, cache)
        - Remaining MongoDB collections (tasks, uploads, taxonomies, API keys, etc.)
        - All S3 objects with namespace prefix
        - Qdrant collection (namespace's vector database)
        - All namespace cache (across all scopes)
        - Analytics data (ClickHouse tables)
        - Namespace metadata

        The deletion is performed asynchronously. Returns a task_id that can be used
        to poll for deletion progress via GET /v1/tasks/{task_id}.

        ⚠️  WARNING: This operation is irreversible and will delete ALL data in the namespace!

    Args:
        namespace_identifier (str): Either the namespace name or namespace ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        namespace_identifier=namespace_identifier,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    namespace_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    """Delete Namespace

     This endpoint deletes a namespace and ALL its resources including:
        - All buckets (with S3 objects, batches, uploads)
        - All collections (with Qdrant points, cache, webhooks)
        - All clusters (with Ray jobs, executions, triggers, S3 artifacts)
        - All retrievers (with executions, evaluations, interactions, cache)
        - Remaining MongoDB collections (tasks, uploads, taxonomies, API keys, etc.)
        - All S3 objects with namespace prefix
        - Qdrant collection (namespace's vector database)
        - All namespace cache (across all scopes)
        - Analytics data (ClickHouse tables)
        - Namespace metadata

        The deletion is performed asynchronously. Returns a task_id that can be used
        to poll for deletion progress via GET /v1/tasks/{task_id}.

        ⚠️  WARNING: This operation is irreversible and will delete ALL data in the namespace!

    Args:
        namespace_identifier (str): Either the namespace name or namespace ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        namespace_identifier=namespace_identifier,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    namespace_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    """Delete Namespace

     This endpoint deletes a namespace and ALL its resources including:
        - All buckets (with S3 objects, batches, uploads)
        - All collections (with Qdrant points, cache, webhooks)
        - All clusters (with Ray jobs, executions, triggers, S3 artifacts)
        - All retrievers (with executions, evaluations, interactions, cache)
        - Remaining MongoDB collections (tasks, uploads, taxonomies, API keys, etc.)
        - All S3 objects with namespace prefix
        - Qdrant collection (namespace's vector database)
        - All namespace cache (across all scopes)
        - Analytics data (ClickHouse tables)
        - Namespace metadata

        The deletion is performed asynchronously. Returns a task_id that can be used
        to poll for deletion progress via GET /v1/tasks/{task_id}.

        ⚠️  WARNING: This operation is irreversible and will delete ALL data in the namespace!

    Args:
        namespace_identifier (str): Either the namespace name or namespace ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        namespace_identifier=namespace_identifier,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    namespace_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    """Delete Namespace

     This endpoint deletes a namespace and ALL its resources including:
        - All buckets (with S3 objects, batches, uploads)
        - All collections (with Qdrant points, cache, webhooks)
        - All clusters (with Ray jobs, executions, triggers, S3 artifacts)
        - All retrievers (with executions, evaluations, interactions, cache)
        - Remaining MongoDB collections (tasks, uploads, taxonomies, API keys, etc.)
        - All S3 objects with namespace prefix
        - Qdrant collection (namespace's vector database)
        - All namespace cache (across all scopes)
        - Analytics data (ClickHouse tables)
        - Namespace metadata

        The deletion is performed asynchronously. Returns a task_id that can be used
        to poll for deletion progress via GET /v1/tasks/{task_id}.

        ⚠️  WARNING: This operation is irreversible and will delete ALL data in the namespace!

    Args:
        namespace_identifier (str): Either the namespace name or namespace ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            namespace_identifier=namespace_identifier,
            client=client,
            authorization=authorization,
        )
    ).parsed
