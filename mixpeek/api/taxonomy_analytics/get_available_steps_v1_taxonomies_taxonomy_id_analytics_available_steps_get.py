from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.available_steps_response import AvailableStepsResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    taxonomy_id: str,
    *,
    collection_id: str,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    params["collection_id"] = collection_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/taxonomies/{taxonomy_id}/analytics/available-steps".format(
            taxonomy_id=quote(str(taxonomy_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AvailableStepsResponse | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AvailableStepsResponse.from_dict(response.json())

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
) -> Response[AvailableStepsResponse | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    taxonomy_id: str,
    *,
    client: AuthenticatedClient | Client,
    collection_id: str,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[AvailableStepsResponse | ErrorResponse | HTTPValidationError]:
    r"""Get Available Steps

     Get all available steps for a taxonomy and collection.

    This endpoint discovers what steps exist in your analytics data by querying
    the ClickHouse taxonomy_events table. Use this before querying transitions
    or paths to understand what step values you can use.

    **Use Cases:**
    - Discover available steps before querying analytics
    - Validate step names (avoid typos in from_step/to_step)
    - See which steps have the most events
    - Check data freshness (first_seen/last_seen timestamps)

    **Example Usage:**
    ```python
    # 1. Get available steps
    GET /v1/taxonomies/tax_sales/analytics/available-steps?collection_id=col_emails

    # Response:
    {
        \"taxonomy_id\": \"tax_sales\",
        \"collection_id\": \"col_emails\",
        \"total_events\": 5432,
        \"total_sequences\": 1000,
        \"steps\": [
            {\"step_key\": \"inquiry\", \"event_count\": 1000, ...},
            {\"step_key\": \"followup\", \"event_count\": 450, ...},
            {\"step_key\": \"closed_won\", \"event_count\": 350, ...}
        ]
    }

    # 2. Use discovered steps in transition query
    POST /v1/taxonomies/tax_sales/analytics/transitions
    {
        \"collection_id\": \"col_emails\",
        \"from_step\": \"inquiry\",      # From available steps
        \"to_step\": \"closed_won\"      # From available steps
    }
    ```

    Args:
        request: FastAPI request object (contains tenant context)
        taxonomy_id: Taxonomy ID to query
        collection_id: Collection ID for filtering events

    Returns:
        AvailableStepsResponse with all steps sorted by event count (descending)

    Raises:
        NotFoundError: If taxonomy not found
        ValidationError: If unable to query ClickHouse

    Args:
        taxonomy_id (str):
        collection_id (str): Collection ID to analyze
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
        Response[AvailableStepsResponse | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        taxonomy_id=taxonomy_id,
        collection_id=collection_id,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    taxonomy_id: str,
    *,
    client: AuthenticatedClient | Client,
    collection_id: str,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> AvailableStepsResponse | ErrorResponse | HTTPValidationError | None:
    r"""Get Available Steps

     Get all available steps for a taxonomy and collection.

    This endpoint discovers what steps exist in your analytics data by querying
    the ClickHouse taxonomy_events table. Use this before querying transitions
    or paths to understand what step values you can use.

    **Use Cases:**
    - Discover available steps before querying analytics
    - Validate step names (avoid typos in from_step/to_step)
    - See which steps have the most events
    - Check data freshness (first_seen/last_seen timestamps)

    **Example Usage:**
    ```python
    # 1. Get available steps
    GET /v1/taxonomies/tax_sales/analytics/available-steps?collection_id=col_emails

    # Response:
    {
        \"taxonomy_id\": \"tax_sales\",
        \"collection_id\": \"col_emails\",
        \"total_events\": 5432,
        \"total_sequences\": 1000,
        \"steps\": [
            {\"step_key\": \"inquiry\", \"event_count\": 1000, ...},
            {\"step_key\": \"followup\", \"event_count\": 450, ...},
            {\"step_key\": \"closed_won\", \"event_count\": 350, ...}
        ]
    }

    # 2. Use discovered steps in transition query
    POST /v1/taxonomies/tax_sales/analytics/transitions
    {
        \"collection_id\": \"col_emails\",
        \"from_step\": \"inquiry\",      # From available steps
        \"to_step\": \"closed_won\"      # From available steps
    }
    ```

    Args:
        request: FastAPI request object (contains tenant context)
        taxonomy_id: Taxonomy ID to query
        collection_id: Collection ID for filtering events

    Returns:
        AvailableStepsResponse with all steps sorted by event count (descending)

    Raises:
        NotFoundError: If taxonomy not found
        ValidationError: If unable to query ClickHouse

    Args:
        taxonomy_id (str):
        collection_id (str): Collection ID to analyze
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
        AvailableStepsResponse | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        taxonomy_id=taxonomy_id,
        client=client,
        collection_id=collection_id,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    taxonomy_id: str,
    *,
    client: AuthenticatedClient | Client,
    collection_id: str,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[AvailableStepsResponse | ErrorResponse | HTTPValidationError]:
    r"""Get Available Steps

     Get all available steps for a taxonomy and collection.

    This endpoint discovers what steps exist in your analytics data by querying
    the ClickHouse taxonomy_events table. Use this before querying transitions
    or paths to understand what step values you can use.

    **Use Cases:**
    - Discover available steps before querying analytics
    - Validate step names (avoid typos in from_step/to_step)
    - See which steps have the most events
    - Check data freshness (first_seen/last_seen timestamps)

    **Example Usage:**
    ```python
    # 1. Get available steps
    GET /v1/taxonomies/tax_sales/analytics/available-steps?collection_id=col_emails

    # Response:
    {
        \"taxonomy_id\": \"tax_sales\",
        \"collection_id\": \"col_emails\",
        \"total_events\": 5432,
        \"total_sequences\": 1000,
        \"steps\": [
            {\"step_key\": \"inquiry\", \"event_count\": 1000, ...},
            {\"step_key\": \"followup\", \"event_count\": 450, ...},
            {\"step_key\": \"closed_won\", \"event_count\": 350, ...}
        ]
    }

    # 2. Use discovered steps in transition query
    POST /v1/taxonomies/tax_sales/analytics/transitions
    {
        \"collection_id\": \"col_emails\",
        \"from_step\": \"inquiry\",      # From available steps
        \"to_step\": \"closed_won\"      # From available steps
    }
    ```

    Args:
        request: FastAPI request object (contains tenant context)
        taxonomy_id: Taxonomy ID to query
        collection_id: Collection ID for filtering events

    Returns:
        AvailableStepsResponse with all steps sorted by event count (descending)

    Raises:
        NotFoundError: If taxonomy not found
        ValidationError: If unable to query ClickHouse

    Args:
        taxonomy_id (str):
        collection_id (str): Collection ID to analyze
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
        Response[AvailableStepsResponse | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        taxonomy_id=taxonomy_id,
        collection_id=collection_id,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    taxonomy_id: str,
    *,
    client: AuthenticatedClient | Client,
    collection_id: str,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> AvailableStepsResponse | ErrorResponse | HTTPValidationError | None:
    r"""Get Available Steps

     Get all available steps for a taxonomy and collection.

    This endpoint discovers what steps exist in your analytics data by querying
    the ClickHouse taxonomy_events table. Use this before querying transitions
    or paths to understand what step values you can use.

    **Use Cases:**
    - Discover available steps before querying analytics
    - Validate step names (avoid typos in from_step/to_step)
    - See which steps have the most events
    - Check data freshness (first_seen/last_seen timestamps)

    **Example Usage:**
    ```python
    # 1. Get available steps
    GET /v1/taxonomies/tax_sales/analytics/available-steps?collection_id=col_emails

    # Response:
    {
        \"taxonomy_id\": \"tax_sales\",
        \"collection_id\": \"col_emails\",
        \"total_events\": 5432,
        \"total_sequences\": 1000,
        \"steps\": [
            {\"step_key\": \"inquiry\", \"event_count\": 1000, ...},
            {\"step_key\": \"followup\", \"event_count\": 450, ...},
            {\"step_key\": \"closed_won\", \"event_count\": 350, ...}
        ]
    }

    # 2. Use discovered steps in transition query
    POST /v1/taxonomies/tax_sales/analytics/transitions
    {
        \"collection_id\": \"col_emails\",
        \"from_step\": \"inquiry\",      # From available steps
        \"to_step\": \"closed_won\"      # From available steps
    }
    ```

    Args:
        request: FastAPI request object (contains tenant context)
        taxonomy_id: Taxonomy ID to query
        collection_id: Collection ID for filtering events

    Returns:
        AvailableStepsResponse with all steps sorted by event count (descending)

    Raises:
        NotFoundError: If taxonomy not found
        ValidationError: If unable to query ClickHouse

    Args:
        taxonomy_id (str):
        collection_id (str): Collection ID to analyze
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
        AvailableStepsResponse | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            taxonomy_id=taxonomy_id,
            client=client,
            collection_id=collection_id,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
