from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_storage_connection_v1_organizations_connections_connection_identifier_delete_response_delete_storage_connection_v1_organizations_connections_connection_identifier_delete import (
    DeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDeleteResponseDeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDelete,
)
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    connection_identifier: str,
    *,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/organizations/connections/{connection_identifier}".format(
            connection_identifier=quote(str(connection_identifier), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDeleteResponseDeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDelete
    | ErrorResponse
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = DeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDeleteResponseDeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDelete.from_dict(
            response.json()
        )

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
) -> Response[
    DeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDeleteResponseDeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDelete
    | ErrorResponse
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> Response[
    DeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDeleteResponseDeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDelete
    | ErrorResponse
    | HTTPValidationError
]:
    r""" Delete Storage Connection

     Soft-delete a connection (mark archived).

    Permanently retires a connection by marking it as ARCHIVED. The connection
    cannot be reactivated after deletion. Credentials are preserved for audit
    purposes but the connection is no longer usable.

    **Example:**
    ```bash
    curl -X DELETE \"http://localhost:8000/v1/organizations/connections/conn_abc123\" \
      -H \"Authorization: Bearer YOUR_API_KEY\"
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDeleteResponseDeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDelete | ErrorResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        connection_identifier=connection_identifier,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> (
    DeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDeleteResponseDeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDelete
    | ErrorResponse
    | HTTPValidationError
    | None
):
    r""" Delete Storage Connection

     Soft-delete a connection (mark archived).

    Permanently retires a connection by marking it as ARCHIVED. The connection
    cannot be reactivated after deletion. Credentials are preserved for audit
    purposes but the connection is no longer usable.

    **Example:**
    ```bash
    curl -X DELETE \"http://localhost:8000/v1/organizations/connections/conn_abc123\" \
      -H \"Authorization: Bearer YOUR_API_KEY\"
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDeleteResponseDeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDelete | ErrorResponse | HTTPValidationError
     """

    return sync_detailed(
        connection_identifier=connection_identifier,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    connection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> Response[
    DeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDeleteResponseDeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDelete
    | ErrorResponse
    | HTTPValidationError
]:
    r""" Delete Storage Connection

     Soft-delete a connection (mark archived).

    Permanently retires a connection by marking it as ARCHIVED. The connection
    cannot be reactivated after deletion. Credentials are preserved for audit
    purposes but the connection is no longer usable.

    **Example:**
    ```bash
    curl -X DELETE \"http://localhost:8000/v1/organizations/connections/conn_abc123\" \
      -H \"Authorization: Bearer YOUR_API_KEY\"
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDeleteResponseDeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDelete | ErrorResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        connection_identifier=connection_identifier,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> (
    DeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDeleteResponseDeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDelete
    | ErrorResponse
    | HTTPValidationError
    | None
):
    r""" Delete Storage Connection

     Soft-delete a connection (mark archived).

    Permanently retires a connection by marking it as ARCHIVED. The connection
    cannot be reactivated after deletion. Credentials are preserved for audit
    purposes but the connection is no longer usable.

    **Example:**
    ```bash
    curl -X DELETE \"http://localhost:8000/v1/organizations/connections/conn_abc123\" \
      -H \"Authorization: Bearer YOUR_API_KEY\"
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDeleteResponseDeleteStorageConnectionV1OrganizationsConnectionsConnectionIdentifierDelete | ErrorResponse | HTTPValidationError
     """

    return (
        await asyncio_detailed(
            connection_identifier=connection_identifier,
            client=client,
            authorization=authorization,
        )
    ).parsed
