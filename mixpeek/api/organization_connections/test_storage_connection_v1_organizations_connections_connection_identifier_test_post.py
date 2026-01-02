from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.storage_connection_test_response import StorageConnectionTestResponse
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
        "method": "post",
        "url": "/v1/organizations/connections/{connection_identifier}/test".format(
            connection_identifier=quote(str(connection_identifier), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | StorageConnectionTestResponse | None:
    if response.status_code == 200:
        response_200 = StorageConnectionTestResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | StorageConnectionTestResponse]:
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
) -> Response[ErrorResponse | HTTPValidationError | StorageConnectionTestResponse]:
    r""" Test Storage Connection

     Perform a credential test against the external provider.

    Validates that connection credentials are still valid and the provider
    is accessible. Result is logged in audit trail.

    **Use Cases:**
    - Validate credentials before using in sync operations
    - Diagnose connection issues
    - Refresh credentials after expiration

    **Example:**
    ```bash
    curl -X POST \"http://localhost:8000/v1/organizations/connections/conn_abc123/test\" \
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
        Response[ErrorResponse | HTTPValidationError | StorageConnectionTestResponse]
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
) -> ErrorResponse | HTTPValidationError | StorageConnectionTestResponse | None:
    r""" Test Storage Connection

     Perform a credential test against the external provider.

    Validates that connection credentials are still valid and the provider
    is accessible. Result is logged in audit trail.

    **Use Cases:**
    - Validate credentials before using in sync operations
    - Diagnose connection issues
    - Refresh credentials after expiration

    **Example:**
    ```bash
    curl -X POST \"http://localhost:8000/v1/organizations/connections/conn_abc123/test\" \
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
        ErrorResponse | HTTPValidationError | StorageConnectionTestResponse
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
) -> Response[ErrorResponse | HTTPValidationError | StorageConnectionTestResponse]:
    r""" Test Storage Connection

     Perform a credential test against the external provider.

    Validates that connection credentials are still valid and the provider
    is accessible. Result is logged in audit trail.

    **Use Cases:**
    - Validate credentials before using in sync operations
    - Diagnose connection issues
    - Refresh credentials after expiration

    **Example:**
    ```bash
    curl -X POST \"http://localhost:8000/v1/organizations/connections/conn_abc123/test\" \
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
        Response[ErrorResponse | HTTPValidationError | StorageConnectionTestResponse]
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
) -> ErrorResponse | HTTPValidationError | StorageConnectionTestResponse | None:
    r""" Test Storage Connection

     Perform a credential test against the external provider.

    Validates that connection credentials are still valid and the provider
    is accessible. Result is logged in audit trail.

    **Use Cases:**
    - Validate credentials before using in sync operations
    - Diagnose connection issues
    - Refresh credentials after expiration

    **Example:**
    ```bash
    curl -X POST \"http://localhost:8000/v1/organizations/connections/conn_abc123/test\" \
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
        ErrorResponse | HTTPValidationError | StorageConnectionTestResponse
     """

    return (
        await asyncio_detailed(
            connection_identifier=connection_identifier,
            client=client,
            authorization=authorization,
        )
    ).parsed
