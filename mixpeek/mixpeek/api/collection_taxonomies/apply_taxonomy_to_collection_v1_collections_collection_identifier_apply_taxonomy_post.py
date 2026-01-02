from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.apply_taxonomy_request import ApplyTaxonomyRequest
from ...models.apply_taxonomy_response import ApplyTaxonomyResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_identifier: str,
    *,
    body: ApplyTaxonomyRequest,
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
        "url": "/v1/collections/{collection_identifier}/apply-taxonomy".format(
            collection_identifier=quote(str(collection_identifier), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApplyTaxonomyResponse | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ApplyTaxonomyResponse.from_dict(response.json())

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
) -> Response[ApplyTaxonomyResponse | ErrorResponse | HTTPValidationError]:
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
    body: ApplyTaxonomyRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ApplyTaxonomyResponse | ErrorResponse | HTTPValidationError]:
    """Apply Taxonomy to Existing Documents

     Apply a taxonomy to all existing documents in a collection retroactively.

    This endpoint triggers distributed Ray processing to enrich existing documents
    with taxonomy data. Unlike automatic materialization (which happens during ingestion),
    this endpoint allows you to:

    1. **Backfill enrichment** for documents ingested before the taxonomy was created
    2. **Re-apply taxonomy** after configuration changes
    3. **Process specific subsets** using scroll_filters

    ⚙️ **Processing Details:**
    - Uses Ray datasets with map_batches for parallel processing
    - Scales horizontally across Ray cluster
    - Non-blocking: Returns immediately with task_id
    - Monitor progress via Tasks API

    ⚠️ **Prerequisites:**
    - Taxonomy must exist and be valid
    - Taxonomy must be in collection's taxonomy_applications list
    - Collection must contain documents

    📊 **Performance:**
    - ~1000-5000 docs/second depending on cluster size
    - Parallel processing across multiple Ray workers
    - Batch size and parallelism configurable

    🔍 **Use Cases:**
    - Backfill: Apply new taxonomy to historical data
    - Re-enrichment: Update after taxonomy changes
    - Selective: Process filtered document subsets

    See Collections API and Taxonomies API documentation for details.

    Args:
        collection_identifier (str): Collection ID or name to apply taxonomy to
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ApplyTaxonomyRequest): Request to apply a taxonomy to an existing collection.

            This endpoint triggers retroactive taxonomy materialization on
            all documents in a collection using distributed Ray processing.

            Use Cases:
                - Apply taxonomy to documents that were ingested before the taxonomy was created
                - Re-apply taxonomy after taxonomy configuration changes
                - Backfill enrichment data for existing collections

            Requirements:
                - taxonomy_id: REQUIRED - Must be an existing, valid taxonomy
                - The taxonomy must already be attached to the collection via taxonomy_applications
                - Documents must exist in the collection

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplyTaxonomyResponse | ErrorResponse | HTTPValidationError]
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
    body: ApplyTaxonomyRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ApplyTaxonomyResponse | ErrorResponse | HTTPValidationError | None:
    """Apply Taxonomy to Existing Documents

     Apply a taxonomy to all existing documents in a collection retroactively.

    This endpoint triggers distributed Ray processing to enrich existing documents
    with taxonomy data. Unlike automatic materialization (which happens during ingestion),
    this endpoint allows you to:

    1. **Backfill enrichment** for documents ingested before the taxonomy was created
    2. **Re-apply taxonomy** after configuration changes
    3. **Process specific subsets** using scroll_filters

    ⚙️ **Processing Details:**
    - Uses Ray datasets with map_batches for parallel processing
    - Scales horizontally across Ray cluster
    - Non-blocking: Returns immediately with task_id
    - Monitor progress via Tasks API

    ⚠️ **Prerequisites:**
    - Taxonomy must exist and be valid
    - Taxonomy must be in collection's taxonomy_applications list
    - Collection must contain documents

    📊 **Performance:**
    - ~1000-5000 docs/second depending on cluster size
    - Parallel processing across multiple Ray workers
    - Batch size and parallelism configurable

    🔍 **Use Cases:**
    - Backfill: Apply new taxonomy to historical data
    - Re-enrichment: Update after taxonomy changes
    - Selective: Process filtered document subsets

    See Collections API and Taxonomies API documentation for details.

    Args:
        collection_identifier (str): Collection ID or name to apply taxonomy to
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ApplyTaxonomyRequest): Request to apply a taxonomy to an existing collection.

            This endpoint triggers retroactive taxonomy materialization on
            all documents in a collection using distributed Ray processing.

            Use Cases:
                - Apply taxonomy to documents that were ingested before the taxonomy was created
                - Re-apply taxonomy after taxonomy configuration changes
                - Backfill enrichment data for existing collections

            Requirements:
                - taxonomy_id: REQUIRED - Must be an existing, valid taxonomy
                - The taxonomy must already be attached to the collection via taxonomy_applications
                - Documents must exist in the collection

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplyTaxonomyResponse | ErrorResponse | HTTPValidationError
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
    body: ApplyTaxonomyRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ApplyTaxonomyResponse | ErrorResponse | HTTPValidationError]:
    """Apply Taxonomy to Existing Documents

     Apply a taxonomy to all existing documents in a collection retroactively.

    This endpoint triggers distributed Ray processing to enrich existing documents
    with taxonomy data. Unlike automatic materialization (which happens during ingestion),
    this endpoint allows you to:

    1. **Backfill enrichment** for documents ingested before the taxonomy was created
    2. **Re-apply taxonomy** after configuration changes
    3. **Process specific subsets** using scroll_filters

    ⚙️ **Processing Details:**
    - Uses Ray datasets with map_batches for parallel processing
    - Scales horizontally across Ray cluster
    - Non-blocking: Returns immediately with task_id
    - Monitor progress via Tasks API

    ⚠️ **Prerequisites:**
    - Taxonomy must exist and be valid
    - Taxonomy must be in collection's taxonomy_applications list
    - Collection must contain documents

    📊 **Performance:**
    - ~1000-5000 docs/second depending on cluster size
    - Parallel processing across multiple Ray workers
    - Batch size and parallelism configurable

    🔍 **Use Cases:**
    - Backfill: Apply new taxonomy to historical data
    - Re-enrichment: Update after taxonomy changes
    - Selective: Process filtered document subsets

    See Collections API and Taxonomies API documentation for details.

    Args:
        collection_identifier (str): Collection ID or name to apply taxonomy to
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ApplyTaxonomyRequest): Request to apply a taxonomy to an existing collection.

            This endpoint triggers retroactive taxonomy materialization on
            all documents in a collection using distributed Ray processing.

            Use Cases:
                - Apply taxonomy to documents that were ingested before the taxonomy was created
                - Re-apply taxonomy after taxonomy configuration changes
                - Backfill enrichment data for existing collections

            Requirements:
                - taxonomy_id: REQUIRED - Must be an existing, valid taxonomy
                - The taxonomy must already be attached to the collection via taxonomy_applications
                - Documents must exist in the collection

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplyTaxonomyResponse | ErrorResponse | HTTPValidationError]
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
    body: ApplyTaxonomyRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ApplyTaxonomyResponse | ErrorResponse | HTTPValidationError | None:
    """Apply Taxonomy to Existing Documents

     Apply a taxonomy to all existing documents in a collection retroactively.

    This endpoint triggers distributed Ray processing to enrich existing documents
    with taxonomy data. Unlike automatic materialization (which happens during ingestion),
    this endpoint allows you to:

    1. **Backfill enrichment** for documents ingested before the taxonomy was created
    2. **Re-apply taxonomy** after configuration changes
    3. **Process specific subsets** using scroll_filters

    ⚙️ **Processing Details:**
    - Uses Ray datasets with map_batches for parallel processing
    - Scales horizontally across Ray cluster
    - Non-blocking: Returns immediately with task_id
    - Monitor progress via Tasks API

    ⚠️ **Prerequisites:**
    - Taxonomy must exist and be valid
    - Taxonomy must be in collection's taxonomy_applications list
    - Collection must contain documents

    📊 **Performance:**
    - ~1000-5000 docs/second depending on cluster size
    - Parallel processing across multiple Ray workers
    - Batch size and parallelism configurable

    🔍 **Use Cases:**
    - Backfill: Apply new taxonomy to historical data
    - Re-enrichment: Update after taxonomy changes
    - Selective: Process filtered document subsets

    See Collections API and Taxonomies API documentation for details.

    Args:
        collection_identifier (str): Collection ID or name to apply taxonomy to
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ApplyTaxonomyRequest): Request to apply a taxonomy to an existing collection.

            This endpoint triggers retroactive taxonomy materialization on
            all documents in a collection using distributed Ray processing.

            Use Cases:
                - Apply taxonomy to documents that were ingested before the taxonomy was created
                - Re-apply taxonomy after taxonomy configuration changes
                - Backfill enrichment data for existing collections

            Requirements:
                - taxonomy_id: REQUIRED - Must be an existing, valid taxonomy
                - The taxonomy must already be attached to the collection via taxonomy_applications
                - Documents must exist in the collection

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplyTaxonomyResponse | ErrorResponse | HTTPValidationError
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
