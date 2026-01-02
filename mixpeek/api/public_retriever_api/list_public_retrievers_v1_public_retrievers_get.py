from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_public_retrievers_response import ListPublicRetrieversResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    include_inactive: bool | Unset = False,
    search: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params["include_inactive"] = include_inactive

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/public/retrievers/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | ListPublicRetrieversResponse | None:
    if response.status_code == 200:
        response_200 = ListPublicRetrieversResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | ListPublicRetrieversResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    include_inactive: bool | Unset = False,
    search: None | str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListPublicRetrieversResponse]:
    r"""List Public Retrievers

     List all public retrievers with pagination and search.

    This endpoint allows browsing and discovering all published retrievers
    across all organizations. No authentication required.

    **Authentication:**
    - NO authentication required - completely public endpoint
    - Discover retrievers created by all Mixpeek users

    **Pagination:**
    - Default: page=1, page_size=20
    - Maximum page_size: 100
    - Returns total count and total pages

    **Search:**
    - Search across retriever titles and descriptions
    - Case-insensitive regex matching
    - Combine with pagination

    **Filtering:**
    - By default, only active retrievers are shown
    - Set `include_inactive=true` to see all retrievers

    **Response includes:**
    - List of public retrievers with basic info
    - Pagination details (page, page_size, total_count, total_pages)
    - Aggregate statistics (total active, password protected, open)

    **What's NOT exposed:**
    - API keys (except in individual config endpoint)
    - Internal IDs or organization details
    - Full retriever configuration (use template endpoint for that)
    - Password values (only password_protected: true/false)

    **Example:**
    ```bash
    # List all public retrievers (first page)
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/\"

    # Search for video-related retrievers
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/?search=video&page_size=50\"

    # Get page 2 with custom page size
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/?page=2&page_size=50\"
    ```

    **Use Cases:**
    - Browse available public retrievers
    - Discover search patterns and implementations
    - Find retrievers to use as templates
    - Explore what others have built

    Args:
        page (int | Unset): Page number (1-indexed) Default: 1.
        page_size (int | Unset): Results per page Default: 20.
        include_inactive (bool | Unset): Include inactive retrievers in results Default: False.
        search (None | str | Unset): Search query for filtering by title or description

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListPublicRetrieversResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        include_inactive=include_inactive,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    include_inactive: bool | Unset = False,
    search: None | str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListPublicRetrieversResponse | None:
    r"""List Public Retrievers

     List all public retrievers with pagination and search.

    This endpoint allows browsing and discovering all published retrievers
    across all organizations. No authentication required.

    **Authentication:**
    - NO authentication required - completely public endpoint
    - Discover retrievers created by all Mixpeek users

    **Pagination:**
    - Default: page=1, page_size=20
    - Maximum page_size: 100
    - Returns total count and total pages

    **Search:**
    - Search across retriever titles and descriptions
    - Case-insensitive regex matching
    - Combine with pagination

    **Filtering:**
    - By default, only active retrievers are shown
    - Set `include_inactive=true` to see all retrievers

    **Response includes:**
    - List of public retrievers with basic info
    - Pagination details (page, page_size, total_count, total_pages)
    - Aggregate statistics (total active, password protected, open)

    **What's NOT exposed:**
    - API keys (except in individual config endpoint)
    - Internal IDs or organization details
    - Full retriever configuration (use template endpoint for that)
    - Password values (only password_protected: true/false)

    **Example:**
    ```bash
    # List all public retrievers (first page)
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/\"

    # Search for video-related retrievers
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/?search=video&page_size=50\"

    # Get page 2 with custom page size
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/?page=2&page_size=50\"
    ```

    **Use Cases:**
    - Browse available public retrievers
    - Discover search patterns and implementations
    - Find retrievers to use as templates
    - Explore what others have built

    Args:
        page (int | Unset): Page number (1-indexed) Default: 1.
        page_size (int | Unset): Results per page Default: 20.
        include_inactive (bool | Unset): Include inactive retrievers in results Default: False.
        search (None | str | Unset): Search query for filtering by title or description

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListPublicRetrieversResponse
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        include_inactive=include_inactive,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    include_inactive: bool | Unset = False,
    search: None | str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListPublicRetrieversResponse]:
    r"""List Public Retrievers

     List all public retrievers with pagination and search.

    This endpoint allows browsing and discovering all published retrievers
    across all organizations. No authentication required.

    **Authentication:**
    - NO authentication required - completely public endpoint
    - Discover retrievers created by all Mixpeek users

    **Pagination:**
    - Default: page=1, page_size=20
    - Maximum page_size: 100
    - Returns total count and total pages

    **Search:**
    - Search across retriever titles and descriptions
    - Case-insensitive regex matching
    - Combine with pagination

    **Filtering:**
    - By default, only active retrievers are shown
    - Set `include_inactive=true` to see all retrievers

    **Response includes:**
    - List of public retrievers with basic info
    - Pagination details (page, page_size, total_count, total_pages)
    - Aggregate statistics (total active, password protected, open)

    **What's NOT exposed:**
    - API keys (except in individual config endpoint)
    - Internal IDs or organization details
    - Full retriever configuration (use template endpoint for that)
    - Password values (only password_protected: true/false)

    **Example:**
    ```bash
    # List all public retrievers (first page)
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/\"

    # Search for video-related retrievers
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/?search=video&page_size=50\"

    # Get page 2 with custom page size
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/?page=2&page_size=50\"
    ```

    **Use Cases:**
    - Browse available public retrievers
    - Discover search patterns and implementations
    - Find retrievers to use as templates
    - Explore what others have built

    Args:
        page (int | Unset): Page number (1-indexed) Default: 1.
        page_size (int | Unset): Results per page Default: 20.
        include_inactive (bool | Unset): Include inactive retrievers in results Default: False.
        search (None | str | Unset): Search query for filtering by title or description

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListPublicRetrieversResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        include_inactive=include_inactive,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    include_inactive: bool | Unset = False,
    search: None | str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListPublicRetrieversResponse | None:
    r"""List Public Retrievers

     List all public retrievers with pagination and search.

    This endpoint allows browsing and discovering all published retrievers
    across all organizations. No authentication required.

    **Authentication:**
    - NO authentication required - completely public endpoint
    - Discover retrievers created by all Mixpeek users

    **Pagination:**
    - Default: page=1, page_size=20
    - Maximum page_size: 100
    - Returns total count and total pages

    **Search:**
    - Search across retriever titles and descriptions
    - Case-insensitive regex matching
    - Combine with pagination

    **Filtering:**
    - By default, only active retrievers are shown
    - Set `include_inactive=true` to see all retrievers

    **Response includes:**
    - List of public retrievers with basic info
    - Pagination details (page, page_size, total_count, total_pages)
    - Aggregate statistics (total active, password protected, open)

    **What's NOT exposed:**
    - API keys (except in individual config endpoint)
    - Internal IDs or organization details
    - Full retriever configuration (use template endpoint for that)
    - Password values (only password_protected: true/false)

    **Example:**
    ```bash
    # List all public retrievers (first page)
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/\"

    # Search for video-related retrievers
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/?search=video&page_size=50\"

    # Get page 2 with custom page size
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/?page=2&page_size=50\"
    ```

    **Use Cases:**
    - Browse available public retrievers
    - Discover search patterns and implementations
    - Find retrievers to use as templates
    - Explore what others have built

    Args:
        page (int | Unset): Page number (1-indexed) Default: 1.
        page_size (int | Unset): Results per page Default: 20.
        include_inactive (bool | Unset): Include inactive retrievers in results Default: False.
        search (None | str | Unset): Search query for filtering by title or description

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListPublicRetrieversResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            include_inactive=include_inactive,
            search=search,
        )
    ).parsed
