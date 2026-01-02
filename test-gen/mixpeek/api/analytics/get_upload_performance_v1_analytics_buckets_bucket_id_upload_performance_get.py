from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.upload_performance_response import UploadPerformanceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket_id: str,
    *,
    hours: int | Unset = 24,
    group_by: str | Unset = "hour",
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    params["hours"] = hours

    params["group_by"] = group_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/buckets/{bucket_id}/upload-performance".format(
            bucket_id=quote(str(bucket_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | UploadPerformanceResponse | None:
    if response.status_code == 200:
        response_200 = UploadPerformanceResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | UploadPerformanceResponse]:
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
    hours: int | Unset = 24,
    group_by: str | Unset = "hour",
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | UploadPerformanceResponse]:
    r""" Get Upload Performance

     Get upload performance metrics.

    Analyzes upload operations including:
    - Upload latency (P50, P95, P99)
    - Throughput (MB/s)
    - Error rates

    **Use Cases:**
    - Monitor upload performance
    - Identify performance degradations
    - Optimize upload strategies
    - Debug upload issues

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/buckets/bkt_abc123/upload-performance?hours=24\"
    \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        bucket_id (str):
        hours (int | Unset): Hours of history Default: 24.
        group_by (str | Unset): Time grouping: hour, day Default: 'hour'.
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
        Response[ErrorResponse | HTTPValidationError | UploadPerformanceResponse]
     """

    kwargs = _get_kwargs(
        bucket_id=bucket_id,
        hours=hours,
        group_by=group_by,
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
    hours: int | Unset = 24,
    group_by: str | Unset = "hour",
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | UploadPerformanceResponse | None:
    r""" Get Upload Performance

     Get upload performance metrics.

    Analyzes upload operations including:
    - Upload latency (P50, P95, P99)
    - Throughput (MB/s)
    - Error rates

    **Use Cases:**
    - Monitor upload performance
    - Identify performance degradations
    - Optimize upload strategies
    - Debug upload issues

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/buckets/bkt_abc123/upload-performance?hours=24\"
    \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        bucket_id (str):
        hours (int | Unset): Hours of history Default: 24.
        group_by (str | Unset): Time grouping: hour, day Default: 'hour'.
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
        ErrorResponse | HTTPValidationError | UploadPerformanceResponse
     """

    return sync_detailed(
        bucket_id=bucket_id,
        client=client,
        hours=hours,
        group_by=group_by,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    bucket_id: str,
    *,
    client: AuthenticatedClient | Client,
    hours: int | Unset = 24,
    group_by: str | Unset = "hour",
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | UploadPerformanceResponse]:
    r""" Get Upload Performance

     Get upload performance metrics.

    Analyzes upload operations including:
    - Upload latency (P50, P95, P99)
    - Throughput (MB/s)
    - Error rates

    **Use Cases:**
    - Monitor upload performance
    - Identify performance degradations
    - Optimize upload strategies
    - Debug upload issues

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/buckets/bkt_abc123/upload-performance?hours=24\"
    \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        bucket_id (str):
        hours (int | Unset): Hours of history Default: 24.
        group_by (str | Unset): Time grouping: hour, day Default: 'hour'.
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
        Response[ErrorResponse | HTTPValidationError | UploadPerformanceResponse]
     """

    kwargs = _get_kwargs(
        bucket_id=bucket_id,
        hours=hours,
        group_by=group_by,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket_id: str,
    *,
    client: AuthenticatedClient | Client,
    hours: int | Unset = 24,
    group_by: str | Unset = "hour",
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | UploadPerformanceResponse | None:
    r""" Get Upload Performance

     Get upload performance metrics.

    Analyzes upload operations including:
    - Upload latency (P50, P95, P99)
    - Throughput (MB/s)
    - Error rates

    **Use Cases:**
    - Monitor upload performance
    - Identify performance degradations
    - Optimize upload strategies
    - Debug upload issues

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/buckets/bkt_abc123/upload-performance?hours=24\"
    \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        bucket_id (str):
        hours (int | Unset): Hours of history Default: 24.
        group_by (str | Unset): Time grouping: hour, day Default: 'hour'.
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
        ErrorResponse | HTTPValidationError | UploadPerformanceResponse
     """

    return (
        await asyncio_detailed(
            bucket_id=bucket_id,
            client=client,
            hours=hours,
            group_by=group_by,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
