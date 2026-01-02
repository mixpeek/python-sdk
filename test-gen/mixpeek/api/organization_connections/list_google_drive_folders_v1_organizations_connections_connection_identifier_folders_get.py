from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_folders_response import ListFoldersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    connection_identifier: str,
    *,
    path: str | Unset = "/",
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["path"] = path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/organizations/connections/{connection_identifier}/folders".format(
            connection_identifier=quote(str(connection_identifier), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | ListFoldersResponse | None:
    if response.status_code == 200:
        response_200 = ListFoldersResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | ListFoldersResponse]:
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
    path: str | Unset = "/",
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListFoldersResponse]:
    r""" List Google Drive Folders

     List folders in Google Drive for folder selection in sync configuration.

    Enables users to browse and select folders when configuring sync operations.
    Only available for Google Drive connections.

    **Use Cases:**
    - Browse available folders for sync configuration
    - Select source folder for bucket sync
    - Navigate nested folder structures

    **Example:**
    ```bash
    curl -X GET
    \"http://localhost:8000/v1/organizations/connections/conn_abc123/folders?path=/Marketing\" \
      -H \"Authorization: Bearer YOUR_API_KEY\"
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        path (str | Unset): Parent folder path to list from Default: '/'.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListFoldersResponse]
     """

    kwargs = _get_kwargs(
        connection_identifier=connection_identifier,
        path=path,
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
    path: str | Unset = "/",
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListFoldersResponse | None:
    r""" List Google Drive Folders

     List folders in Google Drive for folder selection in sync configuration.

    Enables users to browse and select folders when configuring sync operations.
    Only available for Google Drive connections.

    **Use Cases:**
    - Browse available folders for sync configuration
    - Select source folder for bucket sync
    - Navigate nested folder structures

    **Example:**
    ```bash
    curl -X GET
    \"http://localhost:8000/v1/organizations/connections/conn_abc123/folders?path=/Marketing\" \
      -H \"Authorization: Bearer YOUR_API_KEY\"
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        path (str | Unset): Parent folder path to list from Default: '/'.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListFoldersResponse
     """

    return sync_detailed(
        connection_identifier=connection_identifier,
        client=client,
        path=path,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    connection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = "/",
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListFoldersResponse]:
    r""" List Google Drive Folders

     List folders in Google Drive for folder selection in sync configuration.

    Enables users to browse and select folders when configuring sync operations.
    Only available for Google Drive connections.

    **Use Cases:**
    - Browse available folders for sync configuration
    - Select source folder for bucket sync
    - Navigate nested folder structures

    **Example:**
    ```bash
    curl -X GET
    \"http://localhost:8000/v1/organizations/connections/conn_abc123/folders?path=/Marketing\" \
      -H \"Authorization: Bearer YOUR_API_KEY\"
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        path (str | Unset): Parent folder path to list from Default: '/'.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListFoldersResponse]
     """

    kwargs = _get_kwargs(
        connection_identifier=connection_identifier,
        path=path,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = "/",
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListFoldersResponse | None:
    r""" List Google Drive Folders

     List folders in Google Drive for folder selection in sync configuration.

    Enables users to browse and select folders when configuring sync operations.
    Only available for Google Drive connections.

    **Use Cases:**
    - Browse available folders for sync configuration
    - Select source folder for bucket sync
    - Navigate nested folder structures

    **Example:**
    ```bash
    curl -X GET
    \"http://localhost:8000/v1/organizations/connections/conn_abc123/folders?path=/Marketing\" \
      -H \"Authorization: Bearer YOUR_API_KEY\"
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        path (str | Unset): Parent folder path to list from Default: '/'.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListFoldersResponse
     """

    return (
        await asyncio_detailed(
            connection_identifier=connection_identifier,
            client=client,
            path=path,
            authorization=authorization,
        )
    ).parsed
