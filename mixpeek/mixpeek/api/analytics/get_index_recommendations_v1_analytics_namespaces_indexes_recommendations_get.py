from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.index_recommendations_response import IndexRecommendationsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: int | Unset = 30,
    min_usage_count: int | Unset = 5,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    params["days"] = days

    params["min_usage_count"] = min_usage_count

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/namespaces/indexes/recommendations",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | IndexRecommendationsResponse | None:
    if response.status_code == 200:
        response_200 = IndexRecommendationsResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | IndexRecommendationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    min_usage_count: int | Unset = 5,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | IndexRecommendationsResponse]:
    r""" Get Index Recommendations

     Get comprehensive MongoDB index recommendations.

    Analyzes query patterns and generates prioritized index recommendations
    with ready-to-use MongoDB commands.

    **Use Cases:**
    - Get actionable index suggestions
    - Prioritize database optimization
    - Copy/paste index creation commands
    - Track optimization opportunities

    **Recommendation Levels:**
    - **HIGH PRIORITY**: >100 queries, >300ms avg OR >10 very slow queries
    - **MEDIUM PRIORITY**: >50 queries, >200ms avg OR >20 slow queries
    - **LOW PRIORITY**: >10 queries but acceptable performance
    - **NO ACTION**: Low usage, no optimization needed

    **Response Includes:**
    - Prioritized recommendations
    - Usage and latency statistics
    - MongoDB index creation commands
    - Summary by priority level

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/namespaces/indexes/recommendations\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        days (int | Unset): Days of history to analyze Default: 30.
        min_usage_count (int | Unset): Minimum queries to consider Default: 5.
        limit (int | Unset): Maximum recommendations to return Default: 50.
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
        Response[ErrorResponse | HTTPValidationError | IndexRecommendationsResponse]
     """

    kwargs = _get_kwargs(
        days=days,
        min_usage_count=min_usage_count,
        limit=limit,
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
    days: int | Unset = 30,
    min_usage_count: int | Unset = 5,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | IndexRecommendationsResponse | None:
    r""" Get Index Recommendations

     Get comprehensive MongoDB index recommendations.

    Analyzes query patterns and generates prioritized index recommendations
    with ready-to-use MongoDB commands.

    **Use Cases:**
    - Get actionable index suggestions
    - Prioritize database optimization
    - Copy/paste index creation commands
    - Track optimization opportunities

    **Recommendation Levels:**
    - **HIGH PRIORITY**: >100 queries, >300ms avg OR >10 very slow queries
    - **MEDIUM PRIORITY**: >50 queries, >200ms avg OR >20 slow queries
    - **LOW PRIORITY**: >10 queries but acceptable performance
    - **NO ACTION**: Low usage, no optimization needed

    **Response Includes:**
    - Prioritized recommendations
    - Usage and latency statistics
    - MongoDB index creation commands
    - Summary by priority level

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/namespaces/indexes/recommendations\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        days (int | Unset): Days of history to analyze Default: 30.
        min_usage_count (int | Unset): Minimum queries to consider Default: 5.
        limit (int | Unset): Maximum recommendations to return Default: 50.
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
        ErrorResponse | HTTPValidationError | IndexRecommendationsResponse
     """

    return sync_detailed(
        client=client,
        days=days,
        min_usage_count=min_usage_count,
        limit=limit,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    min_usage_count: int | Unset = 5,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | IndexRecommendationsResponse]:
    r""" Get Index Recommendations

     Get comprehensive MongoDB index recommendations.

    Analyzes query patterns and generates prioritized index recommendations
    with ready-to-use MongoDB commands.

    **Use Cases:**
    - Get actionable index suggestions
    - Prioritize database optimization
    - Copy/paste index creation commands
    - Track optimization opportunities

    **Recommendation Levels:**
    - **HIGH PRIORITY**: >100 queries, >300ms avg OR >10 very slow queries
    - **MEDIUM PRIORITY**: >50 queries, >200ms avg OR >20 slow queries
    - **LOW PRIORITY**: >10 queries but acceptable performance
    - **NO ACTION**: Low usage, no optimization needed

    **Response Includes:**
    - Prioritized recommendations
    - Usage and latency statistics
    - MongoDB index creation commands
    - Summary by priority level

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/namespaces/indexes/recommendations\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        days (int | Unset): Days of history to analyze Default: 30.
        min_usage_count (int | Unset): Minimum queries to consider Default: 5.
        limit (int | Unset): Maximum recommendations to return Default: 50.
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
        Response[ErrorResponse | HTTPValidationError | IndexRecommendationsResponse]
     """

    kwargs = _get_kwargs(
        days=days,
        min_usage_count=min_usage_count,
        limit=limit,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    min_usage_count: int | Unset = 5,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | IndexRecommendationsResponse | None:
    r""" Get Index Recommendations

     Get comprehensive MongoDB index recommendations.

    Analyzes query patterns and generates prioritized index recommendations
    with ready-to-use MongoDB commands.

    **Use Cases:**
    - Get actionable index suggestions
    - Prioritize database optimization
    - Copy/paste index creation commands
    - Track optimization opportunities

    **Recommendation Levels:**
    - **HIGH PRIORITY**: >100 queries, >300ms avg OR >10 very slow queries
    - **MEDIUM PRIORITY**: >50 queries, >200ms avg OR >20 slow queries
    - **LOW PRIORITY**: >10 queries but acceptable performance
    - **NO ACTION**: Low usage, no optimization needed

    **Response Includes:**
    - Prioritized recommendations
    - Usage and latency statistics
    - MongoDB index creation commands
    - Summary by priority level

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/namespaces/indexes/recommendations\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        days (int | Unset): Days of history to analyze Default: 30.
        min_usage_count (int | Unset): Minimum queries to consider Default: 5.
        limit (int | Unset): Maximum recommendations to return Default: 50.
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
        ErrorResponse | HTTPValidationError | IndexRecommendationsResponse
     """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
            min_usage_count=min_usage_count,
            limit=limit,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
