from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.sync_create_request import SyncCreateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket_id: str,
    *,
    body: SyncCreateRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/buckets/{bucket_id}/syncs".format(
            bucket_id=quote(str(bucket_id), safe=""),
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
    *,
    client: AuthenticatedClient | Client,
    body: SyncCreateRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Create Sync Configuration

     Create a sync configuration for automated storage ingestion.

    Establishes automated synchronization between an external storage provider
    and a Mixpeek bucket. The sync monitors the source path and ingests files
    according to the specified mode and filters.

    **Supported Providers:** google_drive, s3, snowflake, sharepoint, tigris

    **Built-in Robustness:**
    - Dead Letter Queue (DLQ): Failed objects tracked with 3 retries
    - Idempotent ingestion: Deduplication prevents duplicate objects
    - Distributed locking: Prevents concurrent sync execution
    - Rate limit handling: Automatic backoff on 429 responses
    - Metrics: Duration, files synced/failed, batches created

    **Sync Modes:**
    - `continuous`: Real-time monitoring with configurable polling interval
    - `one_time`: Single bulk import, then sync stops
    - `scheduled`: Polling-based batch imports at fixed intervals

    Args:
        bucket_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SyncCreateRequest): Request to create a bucket sync configuration.

            Establishes automated synchronization between a storage connection and a bucket.
            The sync monitors the source path for changes and ingests files according to
            the specified mode and filters.

            Supported Storage Providers:
                - google_drive: Google Drive and Workspace shared drives
                - s3: Amazon S3 and S3-compatible (MinIO, DigitalOcean Spaces, Wasabi)
                - snowflake: Snowflake data warehouse tables (rows become objects)
                - sharepoint: Microsoft SharePoint and OneDrive for Business
                - tigris: Tigris globally distributed object storage

            Robustness Features (built-in):
                - Dead Letter Queue (DLQ): Failed objects tracked with 3 retries before quarantine
                - Idempotent ingestion: Deduplication via (bucket_id, source_provider,
            source_object_id)
                - Distributed locking: Prevents concurrent execution of same sync config
                - Rate limit handling: Automatic backoff on provider 429 responses
                - Metrics: Duration, files synced/failed, batches created, rate limit hits

            Sync Modes:
                - continuous: Real-time monitoring with polling interval
                - one_time: Single bulk import then stops
                - scheduled: Polling-based batch imports

            Requirements:
                - connection_id: REQUIRED, must be an existing connection
                - source_path: REQUIRED, path must exist in the storage provider
                - sync_mode: OPTIONAL, defaults to 'continuous'
                - All other fields are OPTIONAL with sensible defaults

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bucket_id=bucket_id,
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
    *,
    client: AuthenticatedClient | Client,
    body: SyncCreateRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Create Sync Configuration

     Create a sync configuration for automated storage ingestion.

    Establishes automated synchronization between an external storage provider
    and a Mixpeek bucket. The sync monitors the source path and ingests files
    according to the specified mode and filters.

    **Supported Providers:** google_drive, s3, snowflake, sharepoint, tigris

    **Built-in Robustness:**
    - Dead Letter Queue (DLQ): Failed objects tracked with 3 retries
    - Idempotent ingestion: Deduplication prevents duplicate objects
    - Distributed locking: Prevents concurrent sync execution
    - Rate limit handling: Automatic backoff on 429 responses
    - Metrics: Duration, files synced/failed, batches created

    **Sync Modes:**
    - `continuous`: Real-time monitoring with configurable polling interval
    - `one_time`: Single bulk import, then sync stops
    - `scheduled`: Polling-based batch imports at fixed intervals

    Args:
        bucket_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SyncCreateRequest): Request to create a bucket sync configuration.

            Establishes automated synchronization between a storage connection and a bucket.
            The sync monitors the source path for changes and ingests files according to
            the specified mode and filters.

            Supported Storage Providers:
                - google_drive: Google Drive and Workspace shared drives
                - s3: Amazon S3 and S3-compatible (MinIO, DigitalOcean Spaces, Wasabi)
                - snowflake: Snowflake data warehouse tables (rows become objects)
                - sharepoint: Microsoft SharePoint and OneDrive for Business
                - tigris: Tigris globally distributed object storage

            Robustness Features (built-in):
                - Dead Letter Queue (DLQ): Failed objects tracked with 3 retries before quarantine
                - Idempotent ingestion: Deduplication via (bucket_id, source_provider,
            source_object_id)
                - Distributed locking: Prevents concurrent execution of same sync config
                - Rate limit handling: Automatic backoff on provider 429 responses
                - Metrics: Duration, files synced/failed, batches created, rate limit hits

            Sync Modes:
                - continuous: Real-time monitoring with polling interval
                - one_time: Single bulk import then stops
                - scheduled: Polling-based batch imports

            Requirements:
                - connection_id: REQUIRED, must be an existing connection
                - source_path: REQUIRED, path must exist in the storage provider
                - sync_mode: OPTIONAL, defaults to 'continuous'
                - All other fields are OPTIONAL with sensible defaults

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        bucket_id=bucket_id,
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    bucket_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyncCreateRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Create Sync Configuration

     Create a sync configuration for automated storage ingestion.

    Establishes automated synchronization between an external storage provider
    and a Mixpeek bucket. The sync monitors the source path and ingests files
    according to the specified mode and filters.

    **Supported Providers:** google_drive, s3, snowflake, sharepoint, tigris

    **Built-in Robustness:**
    - Dead Letter Queue (DLQ): Failed objects tracked with 3 retries
    - Idempotent ingestion: Deduplication prevents duplicate objects
    - Distributed locking: Prevents concurrent sync execution
    - Rate limit handling: Automatic backoff on 429 responses
    - Metrics: Duration, files synced/failed, batches created

    **Sync Modes:**
    - `continuous`: Real-time monitoring with configurable polling interval
    - `one_time`: Single bulk import, then sync stops
    - `scheduled`: Polling-based batch imports at fixed intervals

    Args:
        bucket_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SyncCreateRequest): Request to create a bucket sync configuration.

            Establishes automated synchronization between a storage connection and a bucket.
            The sync monitors the source path for changes and ingests files according to
            the specified mode and filters.

            Supported Storage Providers:
                - google_drive: Google Drive and Workspace shared drives
                - s3: Amazon S3 and S3-compatible (MinIO, DigitalOcean Spaces, Wasabi)
                - snowflake: Snowflake data warehouse tables (rows become objects)
                - sharepoint: Microsoft SharePoint and OneDrive for Business
                - tigris: Tigris globally distributed object storage

            Robustness Features (built-in):
                - Dead Letter Queue (DLQ): Failed objects tracked with 3 retries before quarantine
                - Idempotent ingestion: Deduplication via (bucket_id, source_provider,
            source_object_id)
                - Distributed locking: Prevents concurrent execution of same sync config
                - Rate limit handling: Automatic backoff on provider 429 responses
                - Metrics: Duration, files synced/failed, batches created, rate limit hits

            Sync Modes:
                - continuous: Real-time monitoring with polling interval
                - one_time: Single bulk import then stops
                - scheduled: Polling-based batch imports

            Requirements:
                - connection_id: REQUIRED, must be an existing connection
                - source_path: REQUIRED, path must exist in the storage provider
                - sync_mode: OPTIONAL, defaults to 'continuous'
                - All other fields are OPTIONAL with sensible defaults

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bucket_id=bucket_id,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SyncCreateRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Create Sync Configuration

     Create a sync configuration for automated storage ingestion.

    Establishes automated synchronization between an external storage provider
    and a Mixpeek bucket. The sync monitors the source path and ingests files
    according to the specified mode and filters.

    **Supported Providers:** google_drive, s3, snowflake, sharepoint, tigris

    **Built-in Robustness:**
    - Dead Letter Queue (DLQ): Failed objects tracked with 3 retries
    - Idempotent ingestion: Deduplication prevents duplicate objects
    - Distributed locking: Prevents concurrent sync execution
    - Rate limit handling: Automatic backoff on 429 responses
    - Metrics: Duration, files synced/failed, batches created

    **Sync Modes:**
    - `continuous`: Real-time monitoring with configurable polling interval
    - `one_time`: Single bulk import, then sync stops
    - `scheduled`: Polling-based batch imports at fixed intervals

    Args:
        bucket_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SyncCreateRequest): Request to create a bucket sync configuration.

            Establishes automated synchronization between a storage connection and a bucket.
            The sync monitors the source path for changes and ingests files according to
            the specified mode and filters.

            Supported Storage Providers:
                - google_drive: Google Drive and Workspace shared drives
                - s3: Amazon S3 and S3-compatible (MinIO, DigitalOcean Spaces, Wasabi)
                - snowflake: Snowflake data warehouse tables (rows become objects)
                - sharepoint: Microsoft SharePoint and OneDrive for Business
                - tigris: Tigris globally distributed object storage

            Robustness Features (built-in):
                - Dead Letter Queue (DLQ): Failed objects tracked with 3 retries before quarantine
                - Idempotent ingestion: Deduplication via (bucket_id, source_provider,
            source_object_id)
                - Distributed locking: Prevents concurrent execution of same sync config
                - Rate limit handling: Automatic backoff on provider 429 responses
                - Metrics: Duration, files synced/failed, batches created, rate limit hits

            Sync Modes:
                - continuous: Real-time monitoring with polling interval
                - one_time: Single bulk import then stops
                - scheduled: Polling-based batch imports

            Requirements:
                - connection_id: REQUIRED, must be an existing connection
                - source_path: REQUIRED, path must exist in the storage provider
                - sync_mode: OPTIONAL, defaults to 'continuous'
                - All other fields are OPTIONAL with sensible defaults

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            bucket_id=bucket_id,
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
