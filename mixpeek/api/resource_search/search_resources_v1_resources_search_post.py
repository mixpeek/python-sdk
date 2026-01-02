from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.search_request import SearchRequest
from ...models.search_response import SearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchRequest,
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
        "url": "/v1/resources/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | SearchResponse | None:
    if response.status_code == 200:
        response_200 = SearchResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | SearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | SearchResponse]:
    """Search Resources

     Search across all resource names and IDs within your namespace.

        This endpoint performs a case-insensitive search across:
        - Buckets (bucket_name, bucket_id)
        - Collections (collection_name, collection_id)
        - Retrievers (retriever_name, retriever_id)
        - Taxonomies (taxonomy_name, taxonomy_id)
        - Clusters (cluster_name, cluster_id)
        - Namespaces (namespace_name, namespace_id)

        Results are sorted by relevance (exact matches first) and creation time (newest first).
        Use the resource_types parameter to filter searches to specific resource types.
        Pagination is supported via limit and offset parameters.

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SearchRequest): Request model for searching across resource names and IDs.

            Search is performed across all resource types within the authenticated namespace.
            The search is case-insensitive and supports partial matching on both names and IDs.

            Use Cases:
                - Find resources by partial name match
                - Locate resources by ID prefix
                - Filter search to specific resource types
                - Paginate through large result sets

            Requirements:
                - query: REQUIRED - Search term (minimum 1 character)
                - resource_types: OPTIONAL - Filter by specific types
                - limit: OPTIONAL - Results per page (1-100, default 20)
                - offset: OPTIONAL - Pagination offset (default 0)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SearchResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | SearchResponse | None:
    """Search Resources

     Search across all resource names and IDs within your namespace.

        This endpoint performs a case-insensitive search across:
        - Buckets (bucket_name, bucket_id)
        - Collections (collection_name, collection_id)
        - Retrievers (retriever_name, retriever_id)
        - Taxonomies (taxonomy_name, taxonomy_id)
        - Clusters (cluster_name, cluster_id)
        - Namespaces (namespace_name, namespace_id)

        Results are sorted by relevance (exact matches first) and creation time (newest first).
        Use the resource_types parameter to filter searches to specific resource types.
        Pagination is supported via limit and offset parameters.

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SearchRequest): Request model for searching across resource names and IDs.

            Search is performed across all resource types within the authenticated namespace.
            The search is case-insensitive and supports partial matching on both names and IDs.

            Use Cases:
                - Find resources by partial name match
                - Locate resources by ID prefix
                - Filter search to specific resource types
                - Paginate through large result sets

            Requirements:
                - query: REQUIRED - Search term (minimum 1 character)
                - resource_types: OPTIONAL - Filter by specific types
                - limit: OPTIONAL - Results per page (1-100, default 20)
                - offset: OPTIONAL - Pagination offset (default 0)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SearchResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | SearchResponse]:
    """Search Resources

     Search across all resource names and IDs within your namespace.

        This endpoint performs a case-insensitive search across:
        - Buckets (bucket_name, bucket_id)
        - Collections (collection_name, collection_id)
        - Retrievers (retriever_name, retriever_id)
        - Taxonomies (taxonomy_name, taxonomy_id)
        - Clusters (cluster_name, cluster_id)
        - Namespaces (namespace_name, namespace_id)

        Results are sorted by relevance (exact matches first) and creation time (newest first).
        Use the resource_types parameter to filter searches to specific resource types.
        Pagination is supported via limit and offset parameters.

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SearchRequest): Request model for searching across resource names and IDs.

            Search is performed across all resource types within the authenticated namespace.
            The search is case-insensitive and supports partial matching on both names and IDs.

            Use Cases:
                - Find resources by partial name match
                - Locate resources by ID prefix
                - Filter search to specific resource types
                - Paginate through large result sets

            Requirements:
                - query: REQUIRED - Search term (minimum 1 character)
                - resource_types: OPTIONAL - Filter by specific types
                - limit: OPTIONAL - Results per page (1-100, default 20)
                - offset: OPTIONAL - Pagination offset (default 0)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SearchResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | SearchResponse | None:
    """Search Resources

     Search across all resource names and IDs within your namespace.

        This endpoint performs a case-insensitive search across:
        - Buckets (bucket_name, bucket_id)
        - Collections (collection_name, collection_id)
        - Retrievers (retriever_name, retriever_id)
        - Taxonomies (taxonomy_name, taxonomy_id)
        - Clusters (cluster_name, cluster_id)
        - Namespaces (namespace_name, namespace_id)

        Results are sorted by relevance (exact matches first) and creation time (newest first).
        Use the resource_types parameter to filter searches to specific resource types.
        Pagination is supported via limit and offset parameters.

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SearchRequest): Request model for searching across resource names and IDs.

            Search is performed across all resource types within the authenticated namespace.
            The search is case-insensitive and supports partial matching on both names and IDs.

            Use Cases:
                - Find resources by partial name match
                - Locate resources by ID prefix
                - Filter search to specific resource types
                - Paginate through large result sets

            Requirements:
                - query: REQUIRED - Search term (minimum 1 character)
                - resource_types: OPTIONAL - Filter by specific types
                - limit: OPTIONAL - Results per page (1-100, default 20)
                - offset: OPTIONAL - Pagination offset (default 0)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SearchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
