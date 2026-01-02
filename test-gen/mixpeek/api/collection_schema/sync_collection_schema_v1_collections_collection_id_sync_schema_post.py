from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.schema_sync_request import SchemaSyncRequest
from ...models.schema_sync_response import SchemaSyncResponse
from ...models.schema_sync_skipped_response import SchemaSyncSkippedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: str,
    *,
    body: SchemaSyncRequest | Unset = UNSET,
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
        "url": "/v1/collections/{collection_id}/sync-schema".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | SchemaSyncResponse | SchemaSyncSkippedResponse | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> SchemaSyncResponse | SchemaSyncSkippedResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = SchemaSyncResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = SchemaSyncSkippedResponse.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | SchemaSyncResponse | SchemaSyncSkippedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SchemaSyncRequest | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | SchemaSyncResponse | SchemaSyncSkippedResponse]:
    """Sync Collection Schema

     Sample documents from Qdrant and automatically discover new fields to add to the collection's
    output_schema.

        This endpoint:
        - Samples N documents from the collection (default: 1000)
        - Discovers all fields present in actual documents
        - Merges discovered fields into the collection's output_schema (additive only)
        - Optionally cascades schema updates to downstream collections
        - Respects debounce window (max once per 5 minutes, unless force=true)

        The sync operation is additive only - it never removes or changes existing field types.

        Use this endpoint to:
        - Manually trigger schema discovery after data ingestion
        - Force an immediate schema sync (bypassing debounce)
        - Update schemas with new fields discovered in documents

    Args:
        collection_id (str): Collection ID to sync schema for
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SchemaSyncRequest | Unset): Request to sync a collection's schema by sampling
            documents.

            Used by:
            - Manual API calls from users
            - Automatic triggers from BatchJobPoller

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SchemaSyncResponse | SchemaSyncSkippedResponse]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SchemaSyncRequest | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | SchemaSyncResponse | SchemaSyncSkippedResponse | None:
    """Sync Collection Schema

     Sample documents from Qdrant and automatically discover new fields to add to the collection's
    output_schema.

        This endpoint:
        - Samples N documents from the collection (default: 1000)
        - Discovers all fields present in actual documents
        - Merges discovered fields into the collection's output_schema (additive only)
        - Optionally cascades schema updates to downstream collections
        - Respects debounce window (max once per 5 minutes, unless force=true)

        The sync operation is additive only - it never removes or changes existing field types.

        Use this endpoint to:
        - Manually trigger schema discovery after data ingestion
        - Force an immediate schema sync (bypassing debounce)
        - Update schemas with new fields discovered in documents

    Args:
        collection_id (str): Collection ID to sync schema for
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SchemaSyncRequest | Unset): Request to sync a collection's schema by sampling
            documents.

            Used by:
            - Manual API calls from users
            - Automatic triggers from BatchJobPoller

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SchemaSyncResponse | SchemaSyncSkippedResponse
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SchemaSyncRequest | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | SchemaSyncResponse | SchemaSyncSkippedResponse]:
    """Sync Collection Schema

     Sample documents from Qdrant and automatically discover new fields to add to the collection's
    output_schema.

        This endpoint:
        - Samples N documents from the collection (default: 1000)
        - Discovers all fields present in actual documents
        - Merges discovered fields into the collection's output_schema (additive only)
        - Optionally cascades schema updates to downstream collections
        - Respects debounce window (max once per 5 minutes, unless force=true)

        The sync operation is additive only - it never removes or changes existing field types.

        Use this endpoint to:
        - Manually trigger schema discovery after data ingestion
        - Force an immediate schema sync (bypassing debounce)
        - Update schemas with new fields discovered in documents

    Args:
        collection_id (str): Collection ID to sync schema for
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SchemaSyncRequest | Unset): Request to sync a collection's schema by sampling
            documents.

            Used by:
            - Manual API calls from users
            - Automatic triggers from BatchJobPoller

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SchemaSyncResponse | SchemaSyncSkippedResponse]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SchemaSyncRequest | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | SchemaSyncResponse | SchemaSyncSkippedResponse | None:
    """Sync Collection Schema

     Sample documents from Qdrant and automatically discover new fields to add to the collection's
    output_schema.

        This endpoint:
        - Samples N documents from the collection (default: 1000)
        - Discovers all fields present in actual documents
        - Merges discovered fields into the collection's output_schema (additive only)
        - Optionally cascades schema updates to downstream collections
        - Respects debounce window (max once per 5 minutes, unless force=true)

        The sync operation is additive only - it never removes or changes existing field types.

        Use this endpoint to:
        - Manually trigger schema discovery after data ingestion
        - Force an immediate schema sync (bypassing debounce)
        - Update schemas with new fields discovered in documents

    Args:
        collection_id (str): Collection ID to sync schema for
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SchemaSyncRequest | Unset): Request to sync a collection's schema by sampling
            documents.

            Used by:
            - Manual API calls from users
            - Automatic triggers from BatchJobPoller

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SchemaSyncResponse | SchemaSyncSkippedResponse
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
