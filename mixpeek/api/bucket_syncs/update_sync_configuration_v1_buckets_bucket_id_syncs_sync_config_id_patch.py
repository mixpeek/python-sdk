from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.sync_update_request import SyncUpdateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket_id: str,
    sync_config_id: str,
    *,
    body: SyncUpdateRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/buckets/{bucket_id}/syncs/{sync_config_id}".format(
            bucket_id=quote(str(bucket_id), safe=""),
            sync_config_id=quote(str(sync_config_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | None:
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
) -> Response[ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bucket_id: str,
    sync_config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyncUpdateRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Update Sync Configuration

     Update a sync configuration.

    Args:
        bucket_id (str):
        sync_config_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SyncUpdateRequest): Request to update an existing sync configuration.

            Allows partial updates to sync settings without recreating the configuration.
            All fields are optional - only provided fields will be updated.

            Use Cases:
                - Pause/resume syncs by toggling is_active
                - Adjust polling intervals based on activity patterns
                - Update batch sizes for performance tuning
                - Add metadata tags for organization

            Requirements:
                - All fields are OPTIONAL
                - At least one field should be provided for the update
                - Changes take effect on the next sync cycle

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bucket_id=bucket_id,
        sync_config_id=sync_config_id,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bucket_id: str,
    sync_config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyncUpdateRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Update Sync Configuration

     Update a sync configuration.

    Args:
        bucket_id (str):
        sync_config_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SyncUpdateRequest): Request to update an existing sync configuration.

            Allows partial updates to sync settings without recreating the configuration.
            All fields are optional - only provided fields will be updated.

            Use Cases:
                - Pause/resume syncs by toggling is_active
                - Adjust polling intervals based on activity patterns
                - Update batch sizes for performance tuning
                - Add metadata tags for organization

            Requirements:
                - All fields are OPTIONAL
                - At least one field should be provided for the update
                - Changes take effect on the next sync cycle

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        bucket_id=bucket_id,
        sync_config_id=sync_config_id,
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    bucket_id: str,
    sync_config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyncUpdateRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Update Sync Configuration

     Update a sync configuration.

    Args:
        bucket_id (str):
        sync_config_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SyncUpdateRequest): Request to update an existing sync configuration.

            Allows partial updates to sync settings without recreating the configuration.
            All fields are optional - only provided fields will be updated.

            Use Cases:
                - Pause/resume syncs by toggling is_active
                - Adjust polling intervals based on activity patterns
                - Update batch sizes for performance tuning
                - Add metadata tags for organization

            Requirements:
                - All fields are OPTIONAL
                - At least one field should be provided for the update
                - Changes take effect on the next sync cycle

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bucket_id=bucket_id,
        sync_config_id=sync_config_id,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket_id: str,
    sync_config_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyncUpdateRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Update Sync Configuration

     Update a sync configuration.

    Args:
        bucket_id (str):
        sync_config_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SyncUpdateRequest): Request to update an existing sync configuration.

            Allows partial updates to sync settings without recreating the configuration.
            All fields are optional - only provided fields will be updated.

            Use Cases:
                - Pause/resume syncs by toggling is_active
                - Adjust polling intervals based on activity patterns
                - Update batch sizes for performance tuning
                - Add metadata tags for organization

            Requirements:
                - All fields are OPTIONAL
                - At least one field should be provided for the update
                - Changes take effect on the next sync cycle

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            bucket_id=bucket_id,
            sync_config_id=sync_config_id,
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
