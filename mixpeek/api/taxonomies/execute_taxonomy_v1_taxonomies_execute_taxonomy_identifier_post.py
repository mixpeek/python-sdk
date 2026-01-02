from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.execute_taxonomy_request import ExecuteTaxonomyRequest
from ...models.execute_taxonomy_v1_taxonomies_execute_taxonomy_identifier_post_body_type_1 import (
    ExecuteTaxonomyV1TaxonomiesExecuteTaxonomyIdentifierPostBodyType1,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.join_response import JoinResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    taxonomy_identifier: str,
    *,
    body: ExecuteTaxonomyRequest | ExecuteTaxonomyV1TaxonomiesExecuteTaxonomyIdentifierPostBodyType1,
    version: int | None | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    json_version: int | None | Unset
    if isinstance(version, Unset):
        json_version = UNSET
    else:
        json_version = version
    params["version"] = json_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/taxonomies/execute/{taxonomy_identifier}".format(
            taxonomy_identifier=quote(str(taxonomy_identifier), safe=""),
        ),
        "params": params,
    }

    if isinstance(body, ExecuteTaxonomyRequest):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | JoinResponse | None:
    if response.status_code == 200:
        response_200 = JoinResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | JoinResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    taxonomy_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExecuteTaxonomyRequest | ExecuteTaxonomyV1TaxonomiesExecuteTaxonomyIdentifierPostBodyType1,
    version: int | None | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | JoinResponse]:
    """Test taxonomy configuration (validation only)

     ⚠️ VALIDATION ENDPOINT ONLY - Not for production enrichment!

    This endpoint validates taxonomy configuration with 1-5 sample documents.
    Results are returned immediately and NOT persisted to any collection.

    ❌ DO NOT USE FOR:
    - Enriching entire collections (use taxonomy_applications instead)
    - Batch processing documents (automatic during ingestion)
    - Persisting enriched documents (use retriever pipelines instead)

    ✅ USE THIS FOR:
    - Testing taxonomy configuration is correct
    - Validating retriever finds matching taxonomy nodes
    - Checking enrichment fields are properly applied
    - Development/debugging taxonomy setup

    📚 FOR PRODUCTION ENRICHMENT:

    Automatic (during ingestion):
      1. Create taxonomy: POST /taxonomies
      2. Attach to collection: PUT /collections/{id} with taxonomy_applications field
      3. Ingest documents: Documents are automatically enriched by engine

    On-the-fly (during retrieval):
      1. Add taxonomy_join stage to retriever pipeline
      2. Execute retriever: GET /retrievers/{id}/execute
      3. Results include enriched documents (not persisted)

    See API documentation for Collections and Retrievers for details.

    Args:
        taxonomy_identifier (str): Taxonomy ID or name to validate
        version (int | None | Unset): Optional taxonomy version (defaults to latest)
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ExecuteTaxonomyRequest |
            ExecuteTaxonomyV1TaxonomiesExecuteTaxonomyIdentifierPostBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | JoinResponse]
    """

    kwargs = _get_kwargs(
        taxonomy_identifier=taxonomy_identifier,
        body=body,
        version=version,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    taxonomy_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExecuteTaxonomyRequest | ExecuteTaxonomyV1TaxonomiesExecuteTaxonomyIdentifierPostBodyType1,
    version: int | None | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | JoinResponse | None:
    """Test taxonomy configuration (validation only)

     ⚠️ VALIDATION ENDPOINT ONLY - Not for production enrichment!

    This endpoint validates taxonomy configuration with 1-5 sample documents.
    Results are returned immediately and NOT persisted to any collection.

    ❌ DO NOT USE FOR:
    - Enriching entire collections (use taxonomy_applications instead)
    - Batch processing documents (automatic during ingestion)
    - Persisting enriched documents (use retriever pipelines instead)

    ✅ USE THIS FOR:
    - Testing taxonomy configuration is correct
    - Validating retriever finds matching taxonomy nodes
    - Checking enrichment fields are properly applied
    - Development/debugging taxonomy setup

    📚 FOR PRODUCTION ENRICHMENT:

    Automatic (during ingestion):
      1. Create taxonomy: POST /taxonomies
      2. Attach to collection: PUT /collections/{id} with taxonomy_applications field
      3. Ingest documents: Documents are automatically enriched by engine

    On-the-fly (during retrieval):
      1. Add taxonomy_join stage to retriever pipeline
      2. Execute retriever: GET /retrievers/{id}/execute
      3. Results include enriched documents (not persisted)

    See API documentation for Collections and Retrievers for details.

    Args:
        taxonomy_identifier (str): Taxonomy ID or name to validate
        version (int | None | Unset): Optional taxonomy version (defaults to latest)
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ExecuteTaxonomyRequest |
            ExecuteTaxonomyV1TaxonomiesExecuteTaxonomyIdentifierPostBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | JoinResponse
    """

    return sync_detailed(
        taxonomy_identifier=taxonomy_identifier,
        client=client,
        body=body,
        version=version,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    taxonomy_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExecuteTaxonomyRequest | ExecuteTaxonomyV1TaxonomiesExecuteTaxonomyIdentifierPostBodyType1,
    version: int | None | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | JoinResponse]:
    """Test taxonomy configuration (validation only)

     ⚠️ VALIDATION ENDPOINT ONLY - Not for production enrichment!

    This endpoint validates taxonomy configuration with 1-5 sample documents.
    Results are returned immediately and NOT persisted to any collection.

    ❌ DO NOT USE FOR:
    - Enriching entire collections (use taxonomy_applications instead)
    - Batch processing documents (automatic during ingestion)
    - Persisting enriched documents (use retriever pipelines instead)

    ✅ USE THIS FOR:
    - Testing taxonomy configuration is correct
    - Validating retriever finds matching taxonomy nodes
    - Checking enrichment fields are properly applied
    - Development/debugging taxonomy setup

    📚 FOR PRODUCTION ENRICHMENT:

    Automatic (during ingestion):
      1. Create taxonomy: POST /taxonomies
      2. Attach to collection: PUT /collections/{id} with taxonomy_applications field
      3. Ingest documents: Documents are automatically enriched by engine

    On-the-fly (during retrieval):
      1. Add taxonomy_join stage to retriever pipeline
      2. Execute retriever: GET /retrievers/{id}/execute
      3. Results include enriched documents (not persisted)

    See API documentation for Collections and Retrievers for details.

    Args:
        taxonomy_identifier (str): Taxonomy ID or name to validate
        version (int | None | Unset): Optional taxonomy version (defaults to latest)
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ExecuteTaxonomyRequest |
            ExecuteTaxonomyV1TaxonomiesExecuteTaxonomyIdentifierPostBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | JoinResponse]
    """

    kwargs = _get_kwargs(
        taxonomy_identifier=taxonomy_identifier,
        body=body,
        version=version,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    taxonomy_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExecuteTaxonomyRequest | ExecuteTaxonomyV1TaxonomiesExecuteTaxonomyIdentifierPostBodyType1,
    version: int | None | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | JoinResponse | None:
    """Test taxonomy configuration (validation only)

     ⚠️ VALIDATION ENDPOINT ONLY - Not for production enrichment!

    This endpoint validates taxonomy configuration with 1-5 sample documents.
    Results are returned immediately and NOT persisted to any collection.

    ❌ DO NOT USE FOR:
    - Enriching entire collections (use taxonomy_applications instead)
    - Batch processing documents (automatic during ingestion)
    - Persisting enriched documents (use retriever pipelines instead)

    ✅ USE THIS FOR:
    - Testing taxonomy configuration is correct
    - Validating retriever finds matching taxonomy nodes
    - Checking enrichment fields are properly applied
    - Development/debugging taxonomy setup

    📚 FOR PRODUCTION ENRICHMENT:

    Automatic (during ingestion):
      1. Create taxonomy: POST /taxonomies
      2. Attach to collection: PUT /collections/{id} with taxonomy_applications field
      3. Ingest documents: Documents are automatically enriched by engine

    On-the-fly (during retrieval):
      1. Add taxonomy_join stage to retriever pipeline
      2. Execute retriever: GET /retrievers/{id}/execute
      3. Results include enriched documents (not persisted)

    See API documentation for Collections and Retrievers for details.

    Args:
        taxonomy_identifier (str): Taxonomy ID or name to validate
        version (int | None | Unset): Optional taxonomy version (defaults to latest)
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ExecuteTaxonomyRequest |
            ExecuteTaxonomyV1TaxonomiesExecuteTaxonomyIdentifierPostBodyType1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | JoinResponse
    """

    return (
        await asyncio_detailed(
            taxonomy_identifier=taxonomy_identifier,
            client=client,
            body=body,
            version=version,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
