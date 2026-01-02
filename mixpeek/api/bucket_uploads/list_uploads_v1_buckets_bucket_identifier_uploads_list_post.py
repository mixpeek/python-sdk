from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_uploads_request import ListUploadsRequest
from ...models.list_uploads_response import ListUploadsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket_identifier: str,
    *,
    body: ListUploadsRequest | Unset = UNSET,
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
        "url": "/v1/buckets/{bucket_identifier}/uploads/list".format(
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
) -> ErrorResponse | HTTPValidationError | ListUploadsResponse | None:
    if response.status_code == 200:
        response_200 = ListUploadsResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | ListUploadsResponse]:
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
    body: ListUploadsRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListUploadsResponse]:
    r"""List Uploads

     List uploads in a bucket with filtering, sorting, search, and pagination.

        **Filtering**: Use LogicalOperator with shorthand syntax
        - Simple: `{\"status\": \"PENDING\", \"metadata.campaign\": \"summer_2024\"}`
        - Complex: `{\"AND\": [{\"field\": \"file_size_bytes\", \"operator\": \"gte\", \"value\":
    1000000}]}`

        **Sorting**: Specify field and direction
        - Example: `{\"field\": \"created_at\", \"direction\": \"desc\"}`

        **Search**: Full-text search across filename and metadata
        - Example: `\"search\": \"video\"`

        **Pagination**: Use limit and offset
        - Example: `\"limit\": 50, \"offset\": 100`

    Args:
        bucket_identifier (str): The unique identifier of the bucket
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
        body (ListUploadsRequest | Unset): Request model for listing uploads with filtering,
            sorting, and search.

            Provides flexible querying capabilities using the same filter/sort framework
            as documents, objects, and other list endpoints.

            Supports:
                - Complex filters using LogicalOperator (AND, OR, NOT)
                - Shorthand filter syntax: {"metadata.campaign": "summer_2024"}
                - Full-text search across filename and metadata
                - Multi-field sorting
                - Pagination with limit/offset

            Examples:
                - List all pending uploads in a bucket
                - Find uploads by metadata campaign
                - Search for uploads by filename pattern
                - Sort by file size or creation date

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListUploadsResponse]
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
    body: ListUploadsRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListUploadsResponse | None:
    r"""List Uploads

     List uploads in a bucket with filtering, sorting, search, and pagination.

        **Filtering**: Use LogicalOperator with shorthand syntax
        - Simple: `{\"status\": \"PENDING\", \"metadata.campaign\": \"summer_2024\"}`
        - Complex: `{\"AND\": [{\"field\": \"file_size_bytes\", \"operator\": \"gte\", \"value\":
    1000000}]}`

        **Sorting**: Specify field and direction
        - Example: `{\"field\": \"created_at\", \"direction\": \"desc\"}`

        **Search**: Full-text search across filename and metadata
        - Example: `\"search\": \"video\"`

        **Pagination**: Use limit and offset
        - Example: `\"limit\": 50, \"offset\": 100`

    Args:
        bucket_identifier (str): The unique identifier of the bucket
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
        body (ListUploadsRequest | Unset): Request model for listing uploads with filtering,
            sorting, and search.

            Provides flexible querying capabilities using the same filter/sort framework
            as documents, objects, and other list endpoints.

            Supports:
                - Complex filters using LogicalOperator (AND, OR, NOT)
                - Shorthand filter syntax: {"metadata.campaign": "summer_2024"}
                - Full-text search across filename and metadata
                - Multi-field sorting
                - Pagination with limit/offset

            Examples:
                - List all pending uploads in a bucket
                - Find uploads by metadata campaign
                - Search for uploads by filename pattern
                - Sort by file size or creation date

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListUploadsResponse
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
    body: ListUploadsRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListUploadsResponse]:
    r"""List Uploads

     List uploads in a bucket with filtering, sorting, search, and pagination.

        **Filtering**: Use LogicalOperator with shorthand syntax
        - Simple: `{\"status\": \"PENDING\", \"metadata.campaign\": \"summer_2024\"}`
        - Complex: `{\"AND\": [{\"field\": \"file_size_bytes\", \"operator\": \"gte\", \"value\":
    1000000}]}`

        **Sorting**: Specify field and direction
        - Example: `{\"field\": \"created_at\", \"direction\": \"desc\"}`

        **Search**: Full-text search across filename and metadata
        - Example: `\"search\": \"video\"`

        **Pagination**: Use limit and offset
        - Example: `\"limit\": 50, \"offset\": 100`

    Args:
        bucket_identifier (str): The unique identifier of the bucket
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
        body (ListUploadsRequest | Unset): Request model for listing uploads with filtering,
            sorting, and search.

            Provides flexible querying capabilities using the same filter/sort framework
            as documents, objects, and other list endpoints.

            Supports:
                - Complex filters using LogicalOperator (AND, OR, NOT)
                - Shorthand filter syntax: {"metadata.campaign": "summer_2024"}
                - Full-text search across filename and metadata
                - Multi-field sorting
                - Pagination with limit/offset

            Examples:
                - List all pending uploads in a bucket
                - Find uploads by metadata campaign
                - Search for uploads by filename pattern
                - Sort by file size or creation date

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListUploadsResponse]
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
    body: ListUploadsRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListUploadsResponse | None:
    r"""List Uploads

     List uploads in a bucket with filtering, sorting, search, and pagination.

        **Filtering**: Use LogicalOperator with shorthand syntax
        - Simple: `{\"status\": \"PENDING\", \"metadata.campaign\": \"summer_2024\"}`
        - Complex: `{\"AND\": [{\"field\": \"file_size_bytes\", \"operator\": \"gte\", \"value\":
    1000000}]}`

        **Sorting**: Specify field and direction
        - Example: `{\"field\": \"created_at\", \"direction\": \"desc\"}`

        **Search**: Full-text search across filename and metadata
        - Example: `\"search\": \"video\"`

        **Pagination**: Use limit and offset
        - Example: `\"limit\": 50, \"offset\": 100`

    Args:
        bucket_identifier (str): The unique identifier of the bucket
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
        body (ListUploadsRequest | Unset): Request model for listing uploads with filtering,
            sorting, and search.

            Provides flexible querying capabilities using the same filter/sort framework
            as documents, objects, and other list endpoints.

            Supports:
                - Complex filters using LogicalOperator (AND, OR, NOT)
                - Shorthand filter syntax: {"metadata.campaign": "summer_2024"}
                - Full-text search across filename and metadata
                - Multi-field sorting
                - Pagination with limit/offset

            Examples:
                - List all pending uploads in a bucket
                - Find uploads by metadata campaign
                - Search for uploads by filename pattern
                - Sort by file size or creation date

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListUploadsResponse
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
