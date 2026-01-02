from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_google_drive_files_v1_organizations_connections_connection_identifier_files_get_response_list_google_drive_files_v1_organizations_connections_connection_identifier_files_get import (
    ListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGetResponseListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    connection_identifier: str,
    *,
    path: str | Unset = "/",
    max_results: int | Unset = 50,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["path"] = path

    params["max_results"] = max_results

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/organizations/connections/{connection_identifier}/files".format(
            connection_identifier=quote(str(connection_identifier), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponse
    | HTTPValidationError
    | ListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGetResponseListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGet
    | None
):
    if response.status_code == 200:
        response_200 = ListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGetResponseListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGet.from_dict(
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
    ErrorResponse
    | HTTPValidationError
    | ListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGetResponseListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGet
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
    path: str | Unset = "/",
    max_results: int | Unset = 50,
    authorization: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | HTTPValidationError
    | ListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGetResponseListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGet
]:
    r""" List Google Drive Files

     List files in Google Drive folder for preview.

    Shows a preview of files in the selected folder when configuring sync operations.
    Only available for Google Drive connections.

    **Use Cases:**
    - Preview files in a folder before selecting it for sync
    - Verify folder contains expected files
    - Check file types and counts

    **Example:**
    ```bash
    curl -X GET \"http://localhost:8000/v1/organizations/connections/conn_abc123/files?path=/Marketing&m
    ax_results=20\" \
      -H \"Authorization: Bearer YOUR_API_KEY\"
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        path (str | Unset): Folder path to list files from Default: '/'.
        max_results (int | Unset): Maximum number of files to return Default: 50.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGetResponseListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGet]
     """

    kwargs = _get_kwargs(
        connection_identifier=connection_identifier,
        path=path,
        max_results=max_results,
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
    max_results: int | Unset = 50,
    authorization: str | Unset = UNSET,
) -> (
    ErrorResponse
    | HTTPValidationError
    | ListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGetResponseListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGet
    | None
):
    r""" List Google Drive Files

     List files in Google Drive folder for preview.

    Shows a preview of files in the selected folder when configuring sync operations.
    Only available for Google Drive connections.

    **Use Cases:**
    - Preview files in a folder before selecting it for sync
    - Verify folder contains expected files
    - Check file types and counts

    **Example:**
    ```bash
    curl -X GET \"http://localhost:8000/v1/organizations/connections/conn_abc123/files?path=/Marketing&m
    ax_results=20\" \
      -H \"Authorization: Bearer YOUR_API_KEY\"
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        path (str | Unset): Folder path to list files from Default: '/'.
        max_results (int | Unset): Maximum number of files to return Default: 50.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGetResponseListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGet
     """

    return sync_detailed(
        connection_identifier=connection_identifier,
        client=client,
        path=path,
        max_results=max_results,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    connection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = "/",
    max_results: int | Unset = 50,
    authorization: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | HTTPValidationError
    | ListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGetResponseListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGet
]:
    r""" List Google Drive Files

     List files in Google Drive folder for preview.

    Shows a preview of files in the selected folder when configuring sync operations.
    Only available for Google Drive connections.

    **Use Cases:**
    - Preview files in a folder before selecting it for sync
    - Verify folder contains expected files
    - Check file types and counts

    **Example:**
    ```bash
    curl -X GET \"http://localhost:8000/v1/organizations/connections/conn_abc123/files?path=/Marketing&m
    ax_results=20\" \
      -H \"Authorization: Bearer YOUR_API_KEY\"
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        path (str | Unset): Folder path to list files from Default: '/'.
        max_results (int | Unset): Maximum number of files to return Default: 50.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGetResponseListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGet]
     """

    kwargs = _get_kwargs(
        connection_identifier=connection_identifier,
        path=path,
        max_results=max_results,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = "/",
    max_results: int | Unset = 50,
    authorization: str | Unset = UNSET,
) -> (
    ErrorResponse
    | HTTPValidationError
    | ListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGetResponseListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGet
    | None
):
    r""" List Google Drive Files

     List files in Google Drive folder for preview.

    Shows a preview of files in the selected folder when configuring sync operations.
    Only available for Google Drive connections.

    **Use Cases:**
    - Preview files in a folder before selecting it for sync
    - Verify folder contains expected files
    - Check file types and counts

    **Example:**
    ```bash
    curl -X GET \"http://localhost:8000/v1/organizations/connections/conn_abc123/files?path=/Marketing&m
    ax_results=20\" \
      -H \"Authorization: Bearer YOUR_API_KEY\"
    ```

    Args:
        connection_identifier (str): Connection identifier - either connection ID (conn_...) or
            name. The system will automatically resolve names to IDs.
        path (str | Unset): Folder path to list files from Default: '/'.
        max_results (int | Unset): Maximum number of files to return Default: 50.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGetResponseListGoogleDriveFilesV1OrganizationsConnectionsConnectionIdentifierFilesGet
     """

    return (
        await asyncio_detailed(
            connection_identifier=connection_identifier,
            client=client,
            path=path,
            max_results=max_results,
            authorization=authorization,
        )
    ).parsed
