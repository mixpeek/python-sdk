from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_aggregation_request import DocumentAggregationRequest
from ...models.document_aggregation_response import DocumentAggregationResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_identifier: str,
    *,
    body: DocumentAggregationRequest,
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
        "url": "/v1/collections/{collection_identifier}/documents/aggregate".format(
            collection_identifier=quote(str(collection_identifier), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DocumentAggregationResponse | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DocumentAggregationResponse.from_dict(response.json())

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
) -> Response[DocumentAggregationResponse | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: DocumentAggregationRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[DocumentAggregationResponse | ErrorResponse | HTTPValidationError]:
    """Aggregate Documents

     This endpoint performs aggregation operations on documents in a collection.

        **Aggregation Framework**: Provides MongoDB-style aggregation operations:
        - GROUP BY: Group documents by one or more fields
        - Aggregations: COUNT, SUM, AVG, MIN, MAX, COUNT_DISTINCT, etc.
        - Date Operations: Truncate or extract date parts for time-series analysis
        - Filtering: Pre-aggregation filters (WHERE) and post-aggregation filters (HAVING)
        - Sorting & Limiting: Control result ordering and size

        **Use Cases**:
        - Count documents by feature type or collection
        - Calculate daily/monthly processing statistics
        - Analyze feature distributions and confidence scores
        - Generate reports with multiple metrics

        **Note**: This endpoint works with both MongoDB and Qdrant using the same interface.
        The system automatically selects the appropriate aggregation provider based on
        the underlying metadata store.

    Args:
        collection_identifier (str): The unique identifier of the collection.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (DocumentAggregationRequest): Aggregation request for collection documents.

            Extends the base AggregationRequest with document-specific context.
            Inherits all fields from AggregationRequest.

            Requirements:
                - group_by: REQUIRED, fields to group by
                - aggregations: REQUIRED, aggregation operations to perform
                - All other fields from AggregationRequest are available

            Examples:
                - Count documents by feature type
                - Daily processing statistics
                - User-based analytics with filtering

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DocumentAggregationResponse | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        collection_identifier=collection_identifier,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: DocumentAggregationRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> DocumentAggregationResponse | ErrorResponse | HTTPValidationError | None:
    """Aggregate Documents

     This endpoint performs aggregation operations on documents in a collection.

        **Aggregation Framework**: Provides MongoDB-style aggregation operations:
        - GROUP BY: Group documents by one or more fields
        - Aggregations: COUNT, SUM, AVG, MIN, MAX, COUNT_DISTINCT, etc.
        - Date Operations: Truncate or extract date parts for time-series analysis
        - Filtering: Pre-aggregation filters (WHERE) and post-aggregation filters (HAVING)
        - Sorting & Limiting: Control result ordering and size

        **Use Cases**:
        - Count documents by feature type or collection
        - Calculate daily/monthly processing statistics
        - Analyze feature distributions and confidence scores
        - Generate reports with multiple metrics

        **Note**: This endpoint works with both MongoDB and Qdrant using the same interface.
        The system automatically selects the appropriate aggregation provider based on
        the underlying metadata store.

    Args:
        collection_identifier (str): The unique identifier of the collection.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (DocumentAggregationRequest): Aggregation request for collection documents.

            Extends the base AggregationRequest with document-specific context.
            Inherits all fields from AggregationRequest.

            Requirements:
                - group_by: REQUIRED, fields to group by
                - aggregations: REQUIRED, aggregation operations to perform
                - All other fields from AggregationRequest are available

            Examples:
                - Count documents by feature type
                - Daily processing statistics
                - User-based analytics with filtering

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DocumentAggregationResponse | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        collection_identifier=collection_identifier,
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    collection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: DocumentAggregationRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[DocumentAggregationResponse | ErrorResponse | HTTPValidationError]:
    """Aggregate Documents

     This endpoint performs aggregation operations on documents in a collection.

        **Aggregation Framework**: Provides MongoDB-style aggregation operations:
        - GROUP BY: Group documents by one or more fields
        - Aggregations: COUNT, SUM, AVG, MIN, MAX, COUNT_DISTINCT, etc.
        - Date Operations: Truncate or extract date parts for time-series analysis
        - Filtering: Pre-aggregation filters (WHERE) and post-aggregation filters (HAVING)
        - Sorting & Limiting: Control result ordering and size

        **Use Cases**:
        - Count documents by feature type or collection
        - Calculate daily/monthly processing statistics
        - Analyze feature distributions and confidence scores
        - Generate reports with multiple metrics

        **Note**: This endpoint works with both MongoDB and Qdrant using the same interface.
        The system automatically selects the appropriate aggregation provider based on
        the underlying metadata store.

    Args:
        collection_identifier (str): The unique identifier of the collection.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (DocumentAggregationRequest): Aggregation request for collection documents.

            Extends the base AggregationRequest with document-specific context.
            Inherits all fields from AggregationRequest.

            Requirements:
                - group_by: REQUIRED, fields to group by
                - aggregations: REQUIRED, aggregation operations to perform
                - All other fields from AggregationRequest are available

            Examples:
                - Count documents by feature type
                - Daily processing statistics
                - User-based analytics with filtering

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DocumentAggregationResponse | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        collection_identifier=collection_identifier,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: DocumentAggregationRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> DocumentAggregationResponse | ErrorResponse | HTTPValidationError | None:
    """Aggregate Documents

     This endpoint performs aggregation operations on documents in a collection.

        **Aggregation Framework**: Provides MongoDB-style aggregation operations:
        - GROUP BY: Group documents by one or more fields
        - Aggregations: COUNT, SUM, AVG, MIN, MAX, COUNT_DISTINCT, etc.
        - Date Operations: Truncate or extract date parts for time-series analysis
        - Filtering: Pre-aggregation filters (WHERE) and post-aggregation filters (HAVING)
        - Sorting & Limiting: Control result ordering and size

        **Use Cases**:
        - Count documents by feature type or collection
        - Calculate daily/monthly processing statistics
        - Analyze feature distributions and confidence scores
        - Generate reports with multiple metrics

        **Note**: This endpoint works with both MongoDB and Qdrant using the same interface.
        The system automatically selects the appropriate aggregation provider based on
        the underlying metadata store.

    Args:
        collection_identifier (str): The unique identifier of the collection.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (DocumentAggregationRequest): Aggregation request for collection documents.

            Extends the base AggregationRequest with document-specific context.
            Inherits all fields from AggregationRequest.

            Requirements:
                - group_by: REQUIRED, fields to group by
                - aggregations: REQUIRED, aggregation operations to perform
                - All other fields from AggregationRequest are available

            Examples:
                - Count documents by feature type
                - Daily processing statistics
                - User-based analytics with filtering

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DocumentAggregationResponse | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            collection_identifier=collection_identifier,
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
