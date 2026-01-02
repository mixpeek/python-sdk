from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.start_migration_request import StartMigrationRequest
from ...models.start_migration_response import StartMigrationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    migration_id: str,
    *,
    body: StartMigrationRequest | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/namespaces/migrations/{migration_id}/start".format(
            migration_id=quote(str(migration_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | StartMigrationResponse | None:
    if response.status_code == 200:
        response_200 = StartMigrationResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | StartMigrationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    migration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StartMigrationRequest | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | StartMigrationResponse]:
    """Start Migration

     Start a migration execution.

    Args:
        request: FastAPI request
        migration_id: Migration ID
        start_request: Start options

    Returns:
        StartMigrationResponse with task ID

    Args:
        migration_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (StartMigrationRequest | Unset): Request to start a migration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | StartMigrationResponse]
    """

    kwargs = _get_kwargs(
        migration_id=migration_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    migration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StartMigrationRequest | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | StartMigrationResponse | None:
    """Start Migration

     Start a migration execution.

    Args:
        request: FastAPI request
        migration_id: Migration ID
        start_request: Start options

    Returns:
        StartMigrationResponse with task ID

    Args:
        migration_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (StartMigrationRequest | Unset): Request to start a migration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | StartMigrationResponse
    """

    return sync_detailed(
        migration_id=migration_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    migration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StartMigrationRequest | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | StartMigrationResponse]:
    """Start Migration

     Start a migration execution.

    Args:
        request: FastAPI request
        migration_id: Migration ID
        start_request: Start options

    Returns:
        StartMigrationResponse with task ID

    Args:
        migration_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (StartMigrationRequest | Unset): Request to start a migration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | StartMigrationResponse]
    """

    kwargs = _get_kwargs(
        migration_id=migration_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    migration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StartMigrationRequest | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | StartMigrationResponse | None:
    """Start Migration

     Start a migration execution.

    Args:
        request: FastAPI request
        migration_id: Migration ID
        start_request: Start options

    Returns:
        StartMigrationResponse with task ID

    Args:
        migration_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (StartMigrationRequest | Unset): Request to start a migration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | StartMigrationResponse
    """

    return (
        await asyncio_detailed(
            migration_id=migration_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
