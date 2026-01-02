from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_extractor_performance_v1_analytics_extractors_performance_get_response_200_item import (
    GetExtractorPerformanceV1AnalyticsExtractorsPerformanceGetResponse200Item,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    extractor_name: None | str | Unset = UNSET,
    hours: int | Unset = 24,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    json_extractor_name: None | str | Unset
    if isinstance(extractor_name, Unset):
        json_extractor_name = UNSET
    else:
        json_extractor_name = extractor_name
    params["extractor_name"] = json_extractor_name

    params["hours"] = hours

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/extractors/performance",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponse
    | HTTPValidationError
    | list[GetExtractorPerformanceV1AnalyticsExtractorsPerformanceGetResponse200Item]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetExtractorPerformanceV1AnalyticsExtractorsPerformanceGetResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
) -> Response[
    ErrorResponse
    | HTTPValidationError
    | list[GetExtractorPerformanceV1AnalyticsExtractorsPerformanceGetResponse200Item]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    extractor_name: None | str | Unset = UNSET,
    hours: int | Unset = 24,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | HTTPValidationError
    | list[GetExtractorPerformanceV1AnalyticsExtractorsPerformanceGetResponse200Item]
]:
    """Get Extractor Performance

     Get feature extraction performance metrics.

    Returns performance metrics for feature extractors including:
    - Total executions per extractor
    - Average duration
    - P95/P99 latencies
    - Success/failure rates

    **Example:**
    ```bash
    GET /v1/analytics/extractors/performance?hours=24
    GET /v1/analytics/extractors/performance?extractor_name=text_extractor&hours=168
    ```

    Args:
        extractor_name (None | str | Unset): Filter by extractor
        hours (int | Unset): Hours of history Default: 24.
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
        Response[ErrorResponse | HTTPValidationError | list[GetExtractorPerformanceV1AnalyticsExtractorsPerformanceGetResponse200Item]]
    """

    kwargs = _get_kwargs(
        extractor_name=extractor_name,
        hours=hours,
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
    extractor_name: None | str | Unset = UNSET,
    hours: int | Unset = 24,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> (
    ErrorResponse
    | HTTPValidationError
    | list[GetExtractorPerformanceV1AnalyticsExtractorsPerformanceGetResponse200Item]
    | None
):
    """Get Extractor Performance

     Get feature extraction performance metrics.

    Returns performance metrics for feature extractors including:
    - Total executions per extractor
    - Average duration
    - P95/P99 latencies
    - Success/failure rates

    **Example:**
    ```bash
    GET /v1/analytics/extractors/performance?hours=24
    GET /v1/analytics/extractors/performance?extractor_name=text_extractor&hours=168
    ```

    Args:
        extractor_name (None | str | Unset): Filter by extractor
        hours (int | Unset): Hours of history Default: 24.
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
        ErrorResponse | HTTPValidationError | list[GetExtractorPerformanceV1AnalyticsExtractorsPerformanceGetResponse200Item]
    """

    return sync_detailed(
        client=client,
        extractor_name=extractor_name,
        hours=hours,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    extractor_name: None | str | Unset = UNSET,
    hours: int | Unset = 24,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | HTTPValidationError
    | list[GetExtractorPerformanceV1AnalyticsExtractorsPerformanceGetResponse200Item]
]:
    """Get Extractor Performance

     Get feature extraction performance metrics.

    Returns performance metrics for feature extractors including:
    - Total executions per extractor
    - Average duration
    - P95/P99 latencies
    - Success/failure rates

    **Example:**
    ```bash
    GET /v1/analytics/extractors/performance?hours=24
    GET /v1/analytics/extractors/performance?extractor_name=text_extractor&hours=168
    ```

    Args:
        extractor_name (None | str | Unset): Filter by extractor
        hours (int | Unset): Hours of history Default: 24.
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
        Response[ErrorResponse | HTTPValidationError | list[GetExtractorPerformanceV1AnalyticsExtractorsPerformanceGetResponse200Item]]
    """

    kwargs = _get_kwargs(
        extractor_name=extractor_name,
        hours=hours,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    extractor_name: None | str | Unset = UNSET,
    hours: int | Unset = 24,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> (
    ErrorResponse
    | HTTPValidationError
    | list[GetExtractorPerformanceV1AnalyticsExtractorsPerformanceGetResponse200Item]
    | None
):
    """Get Extractor Performance

     Get feature extraction performance metrics.

    Returns performance metrics for feature extractors including:
    - Total executions per extractor
    - Average duration
    - P95/P99 latencies
    - Success/failure rates

    **Example:**
    ```bash
    GET /v1/analytics/extractors/performance?hours=24
    GET /v1/analytics/extractors/performance?extractor_name=text_extractor&hours=168
    ```

    Args:
        extractor_name (None | str | Unset): Filter by extractor
        hours (int | Unset): Hours of history Default: 24.
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
        ErrorResponse | HTTPValidationError | list[GetExtractorPerformanceV1AnalyticsExtractorsPerformanceGetResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            extractor_name=extractor_name,
            hours=hours,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
