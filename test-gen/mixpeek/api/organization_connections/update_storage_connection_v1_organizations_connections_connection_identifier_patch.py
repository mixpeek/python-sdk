from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.storage_connection_model import StorageConnectionModel
from ...models.storage_connection_update_request import StorageConnectionUpdateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    connection_identifier: str,
    *,
    body: StorageConnectionUpdateRequest,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/organizations/connections/{connection_identifier}".format(
            connection_identifier=quote(str(connection_identifier), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | StorageConnectionModel | None:
    if response.status_code == 200:
        response_200 = StorageConnectionModel.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | StorageConnectionModel]:
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
    body: StorageConnectionUpdateRequest,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | StorageConnectionModel]:
    r""" Update Storage Connection

     Update connection metadata or credentials.

    Allows partial updates to connection metadata without changing credentials.
    Credentials can be updated via provider_config. All changes are logged
    in audit trail.

    **What You Can Update:**
    - Connection name and description
    - Metadata tags
    - Status (active/suspended)
    - Provider credentials (via provider_config)

    **Example:**
    ```bash
    curl -X PATCH \"http://localhost:8000/v1/organizations/connections/conn_abc123\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"name\": \"Updated Drive Name\",
        \"status\": \"suspended\"
      }'
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (StorageConnectionUpdateRequest): Request payload for updating storage connection
            metadata.

            Allows partial updates to connection metadata without changing credentials.
            Credentials can be updated via provider_config.

            **What You Can Update:**
            - Connection name and description
            - Metadata tags
            - Status (active/suspended)
            - Provider credentials (via provider_config)

            **Examples:**
            ```python
            # Update name and description
            {
                "name": "Updated Drive Name",
                "description": "New description"
            }

            # Suspend connection
            {
                "status": "suspended",
                "is_active": False
            }

            # Refresh credentials
            {
                "provider_config": {
                    "credentials": {...}
                }
            }
            ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | StorageConnectionModel]
     """

    kwargs = _get_kwargs(
        connection_identifier=connection_identifier,
        body=body,
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
    body: StorageConnectionUpdateRequest,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | StorageConnectionModel | None:
    r""" Update Storage Connection

     Update connection metadata or credentials.

    Allows partial updates to connection metadata without changing credentials.
    Credentials can be updated via provider_config. All changes are logged
    in audit trail.

    **What You Can Update:**
    - Connection name and description
    - Metadata tags
    - Status (active/suspended)
    - Provider credentials (via provider_config)

    **Example:**
    ```bash
    curl -X PATCH \"http://localhost:8000/v1/organizations/connections/conn_abc123\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"name\": \"Updated Drive Name\",
        \"status\": \"suspended\"
      }'
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (StorageConnectionUpdateRequest): Request payload for updating storage connection
            metadata.

            Allows partial updates to connection metadata without changing credentials.
            Credentials can be updated via provider_config.

            **What You Can Update:**
            - Connection name and description
            - Metadata tags
            - Status (active/suspended)
            - Provider credentials (via provider_config)

            **Examples:**
            ```python
            # Update name and description
            {
                "name": "Updated Drive Name",
                "description": "New description"
            }

            # Suspend connection
            {
                "status": "suspended",
                "is_active": False
            }

            # Refresh credentials
            {
                "provider_config": {
                    "credentials": {...}
                }
            }
            ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | StorageConnectionModel
     """

    return sync_detailed(
        connection_identifier=connection_identifier,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    connection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageConnectionUpdateRequest,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | StorageConnectionModel]:
    r""" Update Storage Connection

     Update connection metadata or credentials.

    Allows partial updates to connection metadata without changing credentials.
    Credentials can be updated via provider_config. All changes are logged
    in audit trail.

    **What You Can Update:**
    - Connection name and description
    - Metadata tags
    - Status (active/suspended)
    - Provider credentials (via provider_config)

    **Example:**
    ```bash
    curl -X PATCH \"http://localhost:8000/v1/organizations/connections/conn_abc123\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"name\": \"Updated Drive Name\",
        \"status\": \"suspended\"
      }'
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (StorageConnectionUpdateRequest): Request payload for updating storage connection
            metadata.

            Allows partial updates to connection metadata without changing credentials.
            Credentials can be updated via provider_config.

            **What You Can Update:**
            - Connection name and description
            - Metadata tags
            - Status (active/suspended)
            - Provider credentials (via provider_config)

            **Examples:**
            ```python
            # Update name and description
            {
                "name": "Updated Drive Name",
                "description": "New description"
            }

            # Suspend connection
            {
                "status": "suspended",
                "is_active": False
            }

            # Refresh credentials
            {
                "provider_config": {
                    "credentials": {...}
                }
            }
            ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | StorageConnectionModel]
     """

    kwargs = _get_kwargs(
        connection_identifier=connection_identifier,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageConnectionUpdateRequest,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | StorageConnectionModel | None:
    r""" Update Storage Connection

     Update connection metadata or credentials.

    Allows partial updates to connection metadata without changing credentials.
    Credentials can be updated via provider_config. All changes are logged
    in audit trail.

    **What You Can Update:**
    - Connection name and description
    - Metadata tags
    - Status (active/suspended)
    - Provider credentials (via provider_config)

    **Example:**
    ```bash
    curl -X PATCH \"http://localhost:8000/v1/organizations/connections/conn_abc123\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"name\": \"Updated Drive Name\",
        \"status\": \"suspended\"
      }'
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (StorageConnectionUpdateRequest): Request payload for updating storage connection
            metadata.

            Allows partial updates to connection metadata without changing credentials.
            Credentials can be updated via provider_config.

            **What You Can Update:**
            - Connection name and description
            - Metadata tags
            - Status (active/suspended)
            - Provider credentials (via provider_config)

            **Examples:**
            ```python
            # Update name and description
            {
                "name": "Updated Drive Name",
                "description": "New description"
            }

            # Suspend connection
            {
                "status": "suspended",
                "is_active": False
            }

            # Refresh credentials
            {
                "provider_config": {
                    "credentials": {...}
                }
            }
            ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | StorageConnectionModel
     """

    return (
        await asyncio_detailed(
            connection_identifier=connection_identifier,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
