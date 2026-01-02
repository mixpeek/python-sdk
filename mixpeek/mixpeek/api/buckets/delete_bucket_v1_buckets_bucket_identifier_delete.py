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
    bucket_identifier: str,
    *,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/buckets/{bucket_identifier}".format(
            bucket_identifier=quote(str(bucket_identifier), safe=""),
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
    bucket_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    """Delete Bucket

     This endpoint deletes a bucket and all its resources including:
        - S3 objects and blobs
        - Running Ray jobs (cancels active batch processing jobs)
        - Batch processing artifacts
        - Upload files
        - Unique key lookups
        - MongoDB metadata

        The deletion is performed **asynchronously** via a background task.
        Returns immediately with a task_id that can be polled via GET /v1/tasks/{task_id}.

        **Response**:
        - `task_id`: Use this to poll deletion status via GET /v1/tasks/{task_id}
        - `status`: Initial status (PENDING)
        - `bucket_id`: The bucket being deleted
        - `bucket_name`: Name of the bucket
        - `object_count`: Number of objects that will be deleted

        **Polling**:
        Poll GET /v1/tasks/{task_id} until status is COMPLETED or FAILED.
        Use exponential backoff (start 1s, max 30s).

    Args:
        bucket_identifier (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bucket_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    """Delete Bucket

     This endpoint deletes a bucket and all its resources including:
        - S3 objects and blobs
        - Running Ray jobs (cancels active batch processing jobs)
        - Batch processing artifacts
        - Upload files
        - Unique key lookups
        - MongoDB metadata

        The deletion is performed **asynchronously** via a background task.
        Returns immediately with a task_id that can be polled via GET /v1/tasks/{task_id}.

        **Response**:
        - `task_id`: Use this to poll deletion status via GET /v1/tasks/{task_id}
        - `status`: Initial status (PENDING)
        - `bucket_id`: The bucket being deleted
        - `bucket_name`: Name of the bucket
        - `object_count`: Number of objects that will be deleted

        **Polling**:
        Poll GET /v1/tasks/{task_id} until status is COMPLETED or FAILED.
        Use exponential backoff (start 1s, max 30s).

    Args:
        bucket_identifier (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        bucket_identifier=bucket_identifier,
        client=client,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    bucket_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    """Delete Bucket

     This endpoint deletes a bucket and all its resources including:
        - S3 objects and blobs
        - Running Ray jobs (cancels active batch processing jobs)
        - Batch processing artifacts
        - Upload files
        - Unique key lookups
        - MongoDB metadata

        The deletion is performed **asynchronously** via a background task.
        Returns immediately with a task_id that can be polled via GET /v1/tasks/{task_id}.

        **Response**:
        - `task_id`: Use this to poll deletion status via GET /v1/tasks/{task_id}
        - `status`: Initial status (PENDING)
        - `bucket_id`: The bucket being deleted
        - `bucket_name`: Name of the bucket
        - `object_count`: Number of objects that will be deleted

        **Polling**:
        Poll GET /v1/tasks/{task_id} until status is COMPLETED or FAILED.
        Use exponential backoff (start 1s, max 30s).

    Args:
        bucket_identifier (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    """Delete Bucket

     This endpoint deletes a bucket and all its resources including:
        - S3 objects and blobs
        - Running Ray jobs (cancels active batch processing jobs)
        - Batch processing artifacts
        - Upload files
        - Unique key lookups
        - MongoDB metadata

        The deletion is performed **asynchronously** via a background task.
        Returns immediately with a task_id that can be polled via GET /v1/tasks/{task_id}.

        **Response**:
        - `task_id`: Use this to poll deletion status via GET /v1/tasks/{task_id}
        - `status`: Initial status (PENDING)
        - `bucket_id`: The bucket being deleted
        - `bucket_name`: Name of the bucket
        - `object_count`: Number of objects that will be deleted

        **Polling**:
        Poll GET /v1/tasks/{task_id} until status is COMPLETED or FAILED.
        Use exponential backoff (start 1s, max 30s).

    Args:
        bucket_identifier (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            bucket_identifier=bucket_identifier,
            client=client,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
