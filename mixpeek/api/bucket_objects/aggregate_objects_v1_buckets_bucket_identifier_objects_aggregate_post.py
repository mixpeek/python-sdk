from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.object_aggregation_request import ObjectAggregationRequest
from ...models.object_aggregation_response import ObjectAggregationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket_identifier: str,
    *,
    body: ObjectAggregationRequest,
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
        "url": "/v1/buckets/{bucket_identifier}/objects/aggregate".format(
            bucket_identifier=quote(str(bucket_identifier), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | ObjectAggregationResponse | None:
    if response.status_code == 200:
        response_200 = ObjectAggregationResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | ObjectAggregationResponse]:
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
    body: ObjectAggregationRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ObjectAggregationResponse]:
    """Aggregate Objects

     This endpoint performs aggregation operations on objects in a bucket.

        **Aggregation Framework**: Provides MongoDB-style aggregation operations:
        - GROUP BY: Group objects by one or more fields
        - Aggregations: COUNT, SUM, AVG, MIN, MAX, COUNT_DISTINCT, etc.
        - Date Operations: Truncate or extract date parts for time-series analysis
        - Filtering: Pre-aggregation filters (WHERE) and post-aggregation filters (HAVING)
        - Sorting & Limiting: Control result ordering and size

        **Use Cases**:
        - Count objects by status or category
        - Calculate daily/monthly upload statistics
        - Analyze content distribution and trends
        - Generate reports with multiple metrics

        **Note**: This endpoint works with both MongoDB objects and Qdrant documents
        using the same interface. The system automatically selects the appropriate
        aggregation provider.

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ObjectAggregationRequest): Aggregation request for bucket objects.

            Extends the base AggregationRequest with object-specific context.
            Inherits all fields from AggregationRequest.

            Requirements:
                - group_by: REQUIRED, fields to group by
                - aggregations: REQUIRED, aggregation operations to perform
                - All other fields from AggregationRequest are available

            Examples:
                - Count objects by status
                - Daily upload statistics
                - Category-based analytics with filtering

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ObjectAggregationResponse]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        body=body,
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
    body: ObjectAggregationRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ObjectAggregationResponse | None:
    """Aggregate Objects

     This endpoint performs aggregation operations on objects in a bucket.

        **Aggregation Framework**: Provides MongoDB-style aggregation operations:
        - GROUP BY: Group objects by one or more fields
        - Aggregations: COUNT, SUM, AVG, MIN, MAX, COUNT_DISTINCT, etc.
        - Date Operations: Truncate or extract date parts for time-series analysis
        - Filtering: Pre-aggregation filters (WHERE) and post-aggregation filters (HAVING)
        - Sorting & Limiting: Control result ordering and size

        **Use Cases**:
        - Count objects by status or category
        - Calculate daily/monthly upload statistics
        - Analyze content distribution and trends
        - Generate reports with multiple metrics

        **Note**: This endpoint works with both MongoDB objects and Qdrant documents
        using the same interface. The system automatically selects the appropriate
        aggregation provider.

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ObjectAggregationRequest): Aggregation request for bucket objects.

            Extends the base AggregationRequest with object-specific context.
            Inherits all fields from AggregationRequest.

            Requirements:
                - group_by: REQUIRED, fields to group by
                - aggregations: REQUIRED, aggregation operations to perform
                - All other fields from AggregationRequest are available

            Examples:
                - Count objects by status
                - Daily upload statistics
                - Category-based analytics with filtering

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ObjectAggregationResponse
    """

    return sync_detailed(
        bucket_identifier=bucket_identifier,
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    bucket_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectAggregationRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ObjectAggregationResponse]:
    """Aggregate Objects

     This endpoint performs aggregation operations on objects in a bucket.

        **Aggregation Framework**: Provides MongoDB-style aggregation operations:
        - GROUP BY: Group objects by one or more fields
        - Aggregations: COUNT, SUM, AVG, MIN, MAX, COUNT_DISTINCT, etc.
        - Date Operations: Truncate or extract date parts for time-series analysis
        - Filtering: Pre-aggregation filters (WHERE) and post-aggregation filters (HAVING)
        - Sorting & Limiting: Control result ordering and size

        **Use Cases**:
        - Count objects by status or category
        - Calculate daily/monthly upload statistics
        - Analyze content distribution and trends
        - Generate reports with multiple metrics

        **Note**: This endpoint works with both MongoDB objects and Qdrant documents
        using the same interface. The system automatically selects the appropriate
        aggregation provider.

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ObjectAggregationRequest): Aggregation request for bucket objects.

            Extends the base AggregationRequest with object-specific context.
            Inherits all fields from AggregationRequest.

            Requirements:
                - group_by: REQUIRED, fields to group by
                - aggregations: REQUIRED, aggregation operations to perform
                - All other fields from AggregationRequest are available

            Examples:
                - Count objects by status
                - Daily upload statistics
                - Category-based analytics with filtering

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ObjectAggregationResponse]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: ObjectAggregationRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ObjectAggregationResponse | None:
    """Aggregate Objects

     This endpoint performs aggregation operations on objects in a bucket.

        **Aggregation Framework**: Provides MongoDB-style aggregation operations:
        - GROUP BY: Group objects by one or more fields
        - Aggregations: COUNT, SUM, AVG, MIN, MAX, COUNT_DISTINCT, etc.
        - Date Operations: Truncate or extract date parts for time-series analysis
        - Filtering: Pre-aggregation filters (WHERE) and post-aggregation filters (HAVING)
        - Sorting & Limiting: Control result ordering and size

        **Use Cases**:
        - Count objects by status or category
        - Calculate daily/monthly upload statistics
        - Analyze content distribution and trends
        - Generate reports with multiple metrics

        **Note**: This endpoint works with both MongoDB objects and Qdrant documents
        using the same interface. The system automatically selects the appropriate
        aggregation provider.

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ObjectAggregationRequest): Aggregation request for bucket objects.

            Extends the base AggregationRequest with object-specific context.
            Inherits all fields from AggregationRequest.

            Requirements:
                - group_by: REQUIRED, fields to group by
                - aggregations: REQUIRED, aggregation operations to perform
                - All other fields from AggregationRequest are available

            Examples:
                - Count objects by status
                - Daily upload statistics
                - Category-based analytics with filtering

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ObjectAggregationResponse
    """

    return (
        await asyncio_detailed(
            bucket_identifier=bucket_identifier,
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
