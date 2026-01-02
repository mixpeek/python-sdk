from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_objects_request import ListObjectsRequest
from ...models.list_objects_response import ListObjectsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket_identifier: str,
    *,
    body: ListObjectsRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params["include_total"] = include_total

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/buckets/{bucket_identifier}/objects/list".format(
            bucket_identifier=quote(str(bucket_identifier), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | ListObjectsResponse | None:
    if response.status_code == 200:
        response_200 = ListObjectsResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | ListObjectsResponse]:
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
    body: ListObjectsRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListObjectsResponse]:
    """List Objects

     This endpoint lists objects in a bucket with cursor-based pagination, filtering, and sorting.

        **Filtering**: Use dot notation for metadata fields
        - Example: ?metadata.type=video&metadata.status=ready

        **Sorting**: Specify field and direction
        - Example: ?sort_field=metadata.created_at&sort_direction=desc
        - Direction: asc (ascending) or desc (descending), defaults to asc

        **Pagination**: Cursor-based for efficient deep pagination
        - First page: ?limit=100 (omit cursor)
        - Next pages: ?limit=100&cursor={next_cursor}
        - Use next_cursor from response to navigate
        - No limit on pagination depth

        **Total Count**: Optional (expensive operation)
        - Use ?include_total=true to get total count
        - Adds 50-200ms to response time
        - Returns total, page, page_size, total_pages fields in pagination response

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        limit (int | None | Unset):
        offset (int | None | Unset):
        cursor (None | str | Unset):
        include_total (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ListObjectsRequest | Unset): Request model for listing objects in a bucket.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListObjectsResponse]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        body=body,
        limit=limit,
        offset=offset,
        cursor=cursor,
        include_total=include_total,
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
    body: ListObjectsRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListObjectsResponse | None:
    """List Objects

     This endpoint lists objects in a bucket with cursor-based pagination, filtering, and sorting.

        **Filtering**: Use dot notation for metadata fields
        - Example: ?metadata.type=video&metadata.status=ready

        **Sorting**: Specify field and direction
        - Example: ?sort_field=metadata.created_at&sort_direction=desc
        - Direction: asc (ascending) or desc (descending), defaults to asc

        **Pagination**: Cursor-based for efficient deep pagination
        - First page: ?limit=100 (omit cursor)
        - Next pages: ?limit=100&cursor={next_cursor}
        - Use next_cursor from response to navigate
        - No limit on pagination depth

        **Total Count**: Optional (expensive operation)
        - Use ?include_total=true to get total count
        - Adds 50-200ms to response time
        - Returns total, page, page_size, total_pages fields in pagination response

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        limit (int | None | Unset):
        offset (int | None | Unset):
        cursor (None | str | Unset):
        include_total (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ListObjectsRequest | Unset): Request model for listing objects in a bucket.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListObjectsResponse
    """

    return sync_detailed(
        bucket_identifier=bucket_identifier,
        client=client,
        body=body,
        limit=limit,
        offset=offset,
        cursor=cursor,
        include_total=include_total,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    bucket_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: ListObjectsRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListObjectsResponse]:
    """List Objects

     This endpoint lists objects in a bucket with cursor-based pagination, filtering, and sorting.

        **Filtering**: Use dot notation for metadata fields
        - Example: ?metadata.type=video&metadata.status=ready

        **Sorting**: Specify field and direction
        - Example: ?sort_field=metadata.created_at&sort_direction=desc
        - Direction: asc (ascending) or desc (descending), defaults to asc

        **Pagination**: Cursor-based for efficient deep pagination
        - First page: ?limit=100 (omit cursor)
        - Next pages: ?limit=100&cursor={next_cursor}
        - Use next_cursor from response to navigate
        - No limit on pagination depth

        **Total Count**: Optional (expensive operation)
        - Use ?include_total=true to get total count
        - Adds 50-200ms to response time
        - Returns total, page, page_size, total_pages fields in pagination response

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        limit (int | None | Unset):
        offset (int | None | Unset):
        cursor (None | str | Unset):
        include_total (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ListObjectsRequest | Unset): Request model for listing objects in a bucket.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListObjectsResponse]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        body=body,
        limit=limit,
        offset=offset,
        cursor=cursor,
        include_total=include_total,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: ListObjectsRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListObjectsResponse | None:
    """List Objects

     This endpoint lists objects in a bucket with cursor-based pagination, filtering, and sorting.

        **Filtering**: Use dot notation for metadata fields
        - Example: ?metadata.type=video&metadata.status=ready

        **Sorting**: Specify field and direction
        - Example: ?sort_field=metadata.created_at&sort_direction=desc
        - Direction: asc (ascending) or desc (descending), defaults to asc

        **Pagination**: Cursor-based for efficient deep pagination
        - First page: ?limit=100 (omit cursor)
        - Next pages: ?limit=100&cursor={next_cursor}
        - Use next_cursor from response to navigate
        - No limit on pagination depth

        **Total Count**: Optional (expensive operation)
        - Use ?include_total=true to get total count
        - Adds 50-200ms to response time
        - Returns total, page, page_size, total_pages fields in pagination response

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        limit (int | None | Unset):
        offset (int | None | Unset):
        cursor (None | str | Unset):
        include_total (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ListObjectsRequest | Unset): Request model for listing objects in a bucket.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListObjectsResponse
    """

    return (
        await asyncio_detailed(
            bucket_identifier=bucket_identifier,
            client=client,
            body=body,
            limit=limit,
            offset=offset,
            cursor=cursor,
            include_total=include_total,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
