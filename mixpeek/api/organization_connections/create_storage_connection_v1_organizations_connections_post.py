from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.storage_connection_create_request import StorageConnectionCreateRequest
from ...models.storage_connection_model import StorageConnectionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: StorageConnectionCreateRequest,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/organizations/connections",
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
    *,
    client: AuthenticatedClient | Client,
    body: StorageConnectionCreateRequest,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | StorageConnectionModel]:
    r""" Create Storage Connection

     Create a new storage provider connection.

    Establishes a connection to an external storage provider (Google Drive, S3, etc.)
    for use in sync operations. Credentials are validated before saving unless
    test_before_save is False.

    **Use Cases:**
    - Connect to team Google Drive for automated file ingestion
    - Link customer S3 buckets for batch processing
    - Set up storage connections for sync operations

    **Security:**
    - Requires ADMIN permission
    - Credentials are encrypted at rest
    - Connection is tested before saving (unless test_before_save=False)
    - Audit log entry created for compliance

    **Example:**
    ```bash
    curl -X POST \"http://localhost:8000/v1/organizations/connections\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"name\": \"Marketing Drive\",
        \"provider_type\": \"google_drive\",
        \"provider_config\": {
          \"credentials\": {...},
          \"shared_drive_id\": \"0AH-Xabc123\"
        }
      }'
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (StorageConnectionCreateRequest): Request payload for creating a new storage
            connection.

            Use this to connect Mixpeek to external storage providers like Google Drive
            or S3. The connection will be tested before being saved (unless
            test_before_save is False).

            **Use Cases:**
            - Connect to team Google Drive for automated file ingestion
            - Link customer S3 buckets for batch processing
            - Set up storage connections for sync operations

            **Security:**
            - Credentials are encrypted at rest using MongoDB field-level encryption
            - Credentials never appear in API responses or logs
            - Connection is tested before saving to validate credentials

            **Examples:**
            ```python
            # Google Drive connection
            {
                "name": "Marketing Drive",
                "provider_type": "google_drive",
                "provider_config": {
                    "credentials": {...},
                    "shared_drive_id": "0AH-Xabc123"
                },
                "description": "Team drive for marketing assets"
            }
            ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | StorageConnectionModel]
     """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: StorageConnectionCreateRequest,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | StorageConnectionModel | None:
    r""" Create Storage Connection

     Create a new storage provider connection.

    Establishes a connection to an external storage provider (Google Drive, S3, etc.)
    for use in sync operations. Credentials are validated before saving unless
    test_before_save is False.

    **Use Cases:**
    - Connect to team Google Drive for automated file ingestion
    - Link customer S3 buckets for batch processing
    - Set up storage connections for sync operations

    **Security:**
    - Requires ADMIN permission
    - Credentials are encrypted at rest
    - Connection is tested before saving (unless test_before_save=False)
    - Audit log entry created for compliance

    **Example:**
    ```bash
    curl -X POST \"http://localhost:8000/v1/organizations/connections\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"name\": \"Marketing Drive\",
        \"provider_type\": \"google_drive\",
        \"provider_config\": {
          \"credentials\": {...},
          \"shared_drive_id\": \"0AH-Xabc123\"
        }
      }'
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (StorageConnectionCreateRequest): Request payload for creating a new storage
            connection.

            Use this to connect Mixpeek to external storage providers like Google Drive
            or S3. The connection will be tested before being saved (unless
            test_before_save is False).

            **Use Cases:**
            - Connect to team Google Drive for automated file ingestion
            - Link customer S3 buckets for batch processing
            - Set up storage connections for sync operations

            **Security:**
            - Credentials are encrypted at rest using MongoDB field-level encryption
            - Credentials never appear in API responses or logs
            - Connection is tested before saving to validate credentials

            **Examples:**
            ```python
            # Google Drive connection
            {
                "name": "Marketing Drive",
                "provider_type": "google_drive",
                "provider_config": {
                    "credentials": {...},
                    "shared_drive_id": "0AH-Xabc123"
                },
                "description": "Team drive for marketing assets"
            }
            ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | StorageConnectionModel
     """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StorageConnectionCreateRequest,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | StorageConnectionModel]:
    r""" Create Storage Connection

     Create a new storage provider connection.

    Establishes a connection to an external storage provider (Google Drive, S3, etc.)
    for use in sync operations. Credentials are validated before saving unless
    test_before_save is False.

    **Use Cases:**
    - Connect to team Google Drive for automated file ingestion
    - Link customer S3 buckets for batch processing
    - Set up storage connections for sync operations

    **Security:**
    - Requires ADMIN permission
    - Credentials are encrypted at rest
    - Connection is tested before saving (unless test_before_save=False)
    - Audit log entry created for compliance

    **Example:**
    ```bash
    curl -X POST \"http://localhost:8000/v1/organizations/connections\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"name\": \"Marketing Drive\",
        \"provider_type\": \"google_drive\",
        \"provider_config\": {
          \"credentials\": {...},
          \"shared_drive_id\": \"0AH-Xabc123\"
        }
      }'
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (StorageConnectionCreateRequest): Request payload for creating a new storage
            connection.

            Use this to connect Mixpeek to external storage providers like Google Drive
            or S3. The connection will be tested before being saved (unless
            test_before_save is False).

            **Use Cases:**
            - Connect to team Google Drive for automated file ingestion
            - Link customer S3 buckets for batch processing
            - Set up storage connections for sync operations

            **Security:**
            - Credentials are encrypted at rest using MongoDB field-level encryption
            - Credentials never appear in API responses or logs
            - Connection is tested before saving to validate credentials

            **Examples:**
            ```python
            # Google Drive connection
            {
                "name": "Marketing Drive",
                "provider_type": "google_drive",
                "provider_config": {
                    "credentials": {...},
                    "shared_drive_id": "0AH-Xabc123"
                },
                "description": "Team drive for marketing assets"
            }
            ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | StorageConnectionModel]
     """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StorageConnectionCreateRequest,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | StorageConnectionModel | None:
    r""" Create Storage Connection

     Create a new storage provider connection.

    Establishes a connection to an external storage provider (Google Drive, S3, etc.)
    for use in sync operations. Credentials are validated before saving unless
    test_before_save is False.

    **Use Cases:**
    - Connect to team Google Drive for automated file ingestion
    - Link customer S3 buckets for batch processing
    - Set up storage connections for sync operations

    **Security:**
    - Requires ADMIN permission
    - Credentials are encrypted at rest
    - Connection is tested before saving (unless test_before_save=False)
    - Audit log entry created for compliance

    **Example:**
    ```bash
    curl -X POST \"http://localhost:8000/v1/organizations/connections\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"name\": \"Marketing Drive\",
        \"provider_type\": \"google_drive\",
        \"provider_config\": {
          \"credentials\": {...},
          \"shared_drive_id\": \"0AH-Xabc123\"
        }
      }'
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (StorageConnectionCreateRequest): Request payload for creating a new storage
            connection.

            Use this to connect Mixpeek to external storage providers like Google Drive
            or S3. The connection will be tested before being saved (unless
            test_before_save is False).

            **Use Cases:**
            - Connect to team Google Drive for automated file ingestion
            - Link customer S3 buckets for batch processing
            - Set up storage connections for sync operations

            **Security:**
            - Credentials are encrypted at rest using MongoDB field-level encryption
            - Credentials never appear in API responses or logs
            - Connection is tested before saving to validate credentials

            **Examples:**
            ```python
            # Google Drive connection
            {
                "name": "Marketing Drive",
                "provider_type": "google_drive",
                "provider_config": {
                    "credentials": {...},
                    "shared_drive_id": "0AH-Xabc123"
                },
                "description": "Team drive for marketing assets"
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
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
