from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_cluster_executions_request import ListClusterExecutionsRequest
from ...models.list_cluster_executions_response import ListClusterExecutionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cluster_id: str,
    *,
    body: ListClusterExecutionsRequest | Unset = UNSET,
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
        "url": "/v1/clusters/{cluster_id}/executions/list".format(
            cluster_id=quote(str(cluster_id), safe=""),
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
) -> ErrorResponse | HTTPValidationError | ListClusterExecutionsResponse | None:
    if response.status_code == 200:
        response_200 = ListClusterExecutionsResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | ListClusterExecutionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ListClusterExecutionsRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListClusterExecutionsResponse]:
    """List Cluster Execution History

     List execution history for a cluster with pagination, filtering, sorting, and search.

        Returns all historical executions for the specified cluster, including:
        - Execution status (pending, processing, completed, failed)
        - Clustering metrics (silhouette score, Davies-Bouldin index, etc.)
        - Number of clusters found and documents processed
        - Execution timestamps and duration
        - Centroid information

        Supports:
        - **Filtering**: Filter by status, date range, metrics, etc.
        - **Sorting**: Sort by created_at, execution time, metrics
        - **Search**: Full-text search across execution metadata
        - **Pagination**: Limit and offset for large result sets

        Use cases:
        - View all past executions for a cluster
        - Compare metrics across runs
        - Track execution history over time
        - Debug failed executions
        - Analyze clustering performance trends

    Args:
        cluster_id (str): Cluster ID
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
        body (ListClusterExecutionsRequest | Unset): Request parameters for listing and filtering
            cluster execution history.

            Provides flexible querying of historical clustering executions with filtering,
            sorting, and search capabilities. Use to build execution history UIs, compare
            runs over time, and analyze clustering performance trends.

            Use Cases:
                - Display execution history table with sorting and filtering
                - Find failed executions for debugging
                - Compare metrics across successful runs
                - Search executions by date range or status
                - Build execution timeline visualization

            Query Behavior:
                - Empty request {} returns all executions sorted by created_at (newest first)
                - Filters, sort, and search can be combined for complex queries
                - Results are paginated (use page/page_size query params)

            Note:
                All fields are OPTIONAL. Omit for default behavior (all executions, newest first).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListClusterExecutionsResponse]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
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
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ListClusterExecutionsRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListClusterExecutionsResponse | None:
    """List Cluster Execution History

     List execution history for a cluster with pagination, filtering, sorting, and search.

        Returns all historical executions for the specified cluster, including:
        - Execution status (pending, processing, completed, failed)
        - Clustering metrics (silhouette score, Davies-Bouldin index, etc.)
        - Number of clusters found and documents processed
        - Execution timestamps and duration
        - Centroid information

        Supports:
        - **Filtering**: Filter by status, date range, metrics, etc.
        - **Sorting**: Sort by created_at, execution time, metrics
        - **Search**: Full-text search across execution metadata
        - **Pagination**: Limit and offset for large result sets

        Use cases:
        - View all past executions for a cluster
        - Compare metrics across runs
        - Track execution history over time
        - Debug failed executions
        - Analyze clustering performance trends

    Args:
        cluster_id (str): Cluster ID
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
        body (ListClusterExecutionsRequest | Unset): Request parameters for listing and filtering
            cluster execution history.

            Provides flexible querying of historical clustering executions with filtering,
            sorting, and search capabilities. Use to build execution history UIs, compare
            runs over time, and analyze clustering performance trends.

            Use Cases:
                - Display execution history table with sorting and filtering
                - Find failed executions for debugging
                - Compare metrics across successful runs
                - Search executions by date range or status
                - Build execution timeline visualization

            Query Behavior:
                - Empty request {} returns all executions sorted by created_at (newest first)
                - Filters, sort, and search can be combined for complex queries
                - Results are paginated (use page/page_size query params)

            Note:
                All fields are OPTIONAL. Omit for default behavior (all executions, newest first).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListClusterExecutionsResponse
    """

    return sync_detailed(
        cluster_id=cluster_id,
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
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ListClusterExecutionsRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListClusterExecutionsResponse]:
    """List Cluster Execution History

     List execution history for a cluster with pagination, filtering, sorting, and search.

        Returns all historical executions for the specified cluster, including:
        - Execution status (pending, processing, completed, failed)
        - Clustering metrics (silhouette score, Davies-Bouldin index, etc.)
        - Number of clusters found and documents processed
        - Execution timestamps and duration
        - Centroid information

        Supports:
        - **Filtering**: Filter by status, date range, metrics, etc.
        - **Sorting**: Sort by created_at, execution time, metrics
        - **Search**: Full-text search across execution metadata
        - **Pagination**: Limit and offset for large result sets

        Use cases:
        - View all past executions for a cluster
        - Compare metrics across runs
        - Track execution history over time
        - Debug failed executions
        - Analyze clustering performance trends

    Args:
        cluster_id (str): Cluster ID
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
        body (ListClusterExecutionsRequest | Unset): Request parameters for listing and filtering
            cluster execution history.

            Provides flexible querying of historical clustering executions with filtering,
            sorting, and search capabilities. Use to build execution history UIs, compare
            runs over time, and analyze clustering performance trends.

            Use Cases:
                - Display execution history table with sorting and filtering
                - Find failed executions for debugging
                - Compare metrics across successful runs
                - Search executions by date range or status
                - Build execution timeline visualization

            Query Behavior:
                - Empty request {} returns all executions sorted by created_at (newest first)
                - Filters, sort, and search can be combined for complex queries
                - Results are paginated (use page/page_size query params)

            Note:
                All fields are OPTIONAL. Omit for default behavior (all executions, newest first).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListClusterExecutionsResponse]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
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
    cluster_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ListClusterExecutionsRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListClusterExecutionsResponse | None:
    """List Cluster Execution History

     List execution history for a cluster with pagination, filtering, sorting, and search.

        Returns all historical executions for the specified cluster, including:
        - Execution status (pending, processing, completed, failed)
        - Clustering metrics (silhouette score, Davies-Bouldin index, etc.)
        - Number of clusters found and documents processed
        - Execution timestamps and duration
        - Centroid information

        Supports:
        - **Filtering**: Filter by status, date range, metrics, etc.
        - **Sorting**: Sort by created_at, execution time, metrics
        - **Search**: Full-text search across execution metadata
        - **Pagination**: Limit and offset for large result sets

        Use cases:
        - View all past executions for a cluster
        - Compare metrics across runs
        - Track execution history over time
        - Debug failed executions
        - Analyze clustering performance trends

    Args:
        cluster_id (str): Cluster ID
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
        body (ListClusterExecutionsRequest | Unset): Request parameters for listing and filtering
            cluster execution history.

            Provides flexible querying of historical clustering executions with filtering,
            sorting, and search capabilities. Use to build execution history UIs, compare
            runs over time, and analyze clustering performance trends.

            Use Cases:
                - Display execution history table with sorting and filtering
                - Find failed executions for debugging
                - Compare metrics across successful runs
                - Search executions by date range or status
                - Build execution timeline visualization

            Query Behavior:
                - Empty request {} returns all executions sorted by created_at (newest first)
                - Filters, sort, and search can be combined for complex queries
                - Results are paginated (use page/page_size query params)

            Note:
                All fields are OPTIONAL. Omit for default behavior (all executions, newest first).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListClusterExecutionsResponse
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
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
