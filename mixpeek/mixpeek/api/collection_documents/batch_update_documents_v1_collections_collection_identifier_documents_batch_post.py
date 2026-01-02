from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_update_documents_request import BatchUpdateDocumentsRequest
from ...models.batch_update_documents_response import BatchUpdateDocumentsResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_identifier: str,
    *,
    body: BatchUpdateDocumentsRequest,
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
        "url": "/v1/collections/{collection_identifier}/documents/batch".format(
            collection_identifier=quote(str(collection_identifier), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BatchUpdateDocumentsResponse | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BatchUpdateDocumentsResponse.from_dict(response.json())

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
) -> Response[BatchUpdateDocumentsResponse | ErrorResponse | HTTPValidationError]:
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
    body: BatchUpdateDocumentsRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[BatchUpdateDocumentsResponse | ErrorResponse | HTTPValidationError]:
    r"""Batch Update Documents

     Batch update multiple documents by explicit IDs or filters.

    Supports TWO modes:
    1. Explicit IDs mode: Provide 'updates' array with document_id + update_data for each document
       - Each document can have DIFFERENT update_data
       - Returns detailed per-document results

    2. Filter mode: Provide 'filters' + 'update_data' to update all matching documents
       - All documents receive the SAME update_data
       - Returns total count only

    Key Features:
    - Update any document field except vectors (metadata, internal_metadata, source_blobs, etc.)
    - Maximum 1000 documents per batch in explicit mode
    - Per-document success/failure reporting in explicit mode
    - Validates documents exist in the specified collection

    Examples:
        Explicit IDs mode:
        ```json
        {
            \"updates\": [
                {\"document_id\": \"doc_123\", \"update_data\": {\"metadata\": {\"status\":
    \"processed\"}}},
                {\"document_id\": \"doc_456\", \"update_data\": {\"metadata\": {\"status\":
    \"archived\"}}}
            ]
        }
        ```

        Filter mode:
        ```json
        {
            \"filters\": {\"must\": [{\"key\": \"metadata.status\", \"value\": \"pending\"}]},
            \"update_data\": {\"metadata\": {\"status\": \"processed\"}}
        }
        ```

    Args:
        collection_identifier (str): The ID of the collection to update documents in.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (BatchUpdateDocumentsRequest): Request model for batch updating multiple documents by
            explicit IDs or filters.

            Supports TWO modes:
            1. Explicit IDs mode: Provide 'updates' array with document_id + update_data for each
            2. Filter mode: Provide 'filters' + 'update_data' to update all matching documents

            Key difference from BulkUpdateDocumentsRequest:
            - Batch (this): Can apply DIFFERENT updates to SPECIFIC documents by ID
            - Bulk: Applies SAME update to ALL documents matching filters

            Use Cases:
                - Update 5 specific documents with different metadata values
                - Update documents by IDs with per-document update control
                - Combine with filters for targeted batch updates

            Requirements:
                - EITHER 'updates' (explicit mode) OR 'filters' + 'update_data' (filter mode)
                - NOT BOTH modes simultaneously

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchUpdateDocumentsResponse | ErrorResponse | HTTPValidationError]
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
    body: BatchUpdateDocumentsRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> BatchUpdateDocumentsResponse | ErrorResponse | HTTPValidationError | None:
    r"""Batch Update Documents

     Batch update multiple documents by explicit IDs or filters.

    Supports TWO modes:
    1. Explicit IDs mode: Provide 'updates' array with document_id + update_data for each document
       - Each document can have DIFFERENT update_data
       - Returns detailed per-document results

    2. Filter mode: Provide 'filters' + 'update_data' to update all matching documents
       - All documents receive the SAME update_data
       - Returns total count only

    Key Features:
    - Update any document field except vectors (metadata, internal_metadata, source_blobs, etc.)
    - Maximum 1000 documents per batch in explicit mode
    - Per-document success/failure reporting in explicit mode
    - Validates documents exist in the specified collection

    Examples:
        Explicit IDs mode:
        ```json
        {
            \"updates\": [
                {\"document_id\": \"doc_123\", \"update_data\": {\"metadata\": {\"status\":
    \"processed\"}}},
                {\"document_id\": \"doc_456\", \"update_data\": {\"metadata\": {\"status\":
    \"archived\"}}}
            ]
        }
        ```

        Filter mode:
        ```json
        {
            \"filters\": {\"must\": [{\"key\": \"metadata.status\", \"value\": \"pending\"}]},
            \"update_data\": {\"metadata\": {\"status\": \"processed\"}}
        }
        ```

    Args:
        collection_identifier (str): The ID of the collection to update documents in.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (BatchUpdateDocumentsRequest): Request model for batch updating multiple documents by
            explicit IDs or filters.

            Supports TWO modes:
            1. Explicit IDs mode: Provide 'updates' array with document_id + update_data for each
            2. Filter mode: Provide 'filters' + 'update_data' to update all matching documents

            Key difference from BulkUpdateDocumentsRequest:
            - Batch (this): Can apply DIFFERENT updates to SPECIFIC documents by ID
            - Bulk: Applies SAME update to ALL documents matching filters

            Use Cases:
                - Update 5 specific documents with different metadata values
                - Update documents by IDs with per-document update control
                - Combine with filters for targeted batch updates

            Requirements:
                - EITHER 'updates' (explicit mode) OR 'filters' + 'update_data' (filter mode)
                - NOT BOTH modes simultaneously

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchUpdateDocumentsResponse | ErrorResponse | HTTPValidationError
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
    body: BatchUpdateDocumentsRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[BatchUpdateDocumentsResponse | ErrorResponse | HTTPValidationError]:
    r"""Batch Update Documents

     Batch update multiple documents by explicit IDs or filters.

    Supports TWO modes:
    1. Explicit IDs mode: Provide 'updates' array with document_id + update_data for each document
       - Each document can have DIFFERENT update_data
       - Returns detailed per-document results

    2. Filter mode: Provide 'filters' + 'update_data' to update all matching documents
       - All documents receive the SAME update_data
       - Returns total count only

    Key Features:
    - Update any document field except vectors (metadata, internal_metadata, source_blobs, etc.)
    - Maximum 1000 documents per batch in explicit mode
    - Per-document success/failure reporting in explicit mode
    - Validates documents exist in the specified collection

    Examples:
        Explicit IDs mode:
        ```json
        {
            \"updates\": [
                {\"document_id\": \"doc_123\", \"update_data\": {\"metadata\": {\"status\":
    \"processed\"}}},
                {\"document_id\": \"doc_456\", \"update_data\": {\"metadata\": {\"status\":
    \"archived\"}}}
            ]
        }
        ```

        Filter mode:
        ```json
        {
            \"filters\": {\"must\": [{\"key\": \"metadata.status\", \"value\": \"pending\"}]},
            \"update_data\": {\"metadata\": {\"status\": \"processed\"}}
        }
        ```

    Args:
        collection_identifier (str): The ID of the collection to update documents in.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (BatchUpdateDocumentsRequest): Request model for batch updating multiple documents by
            explicit IDs or filters.

            Supports TWO modes:
            1. Explicit IDs mode: Provide 'updates' array with document_id + update_data for each
            2. Filter mode: Provide 'filters' + 'update_data' to update all matching documents

            Key difference from BulkUpdateDocumentsRequest:
            - Batch (this): Can apply DIFFERENT updates to SPECIFIC documents by ID
            - Bulk: Applies SAME update to ALL documents matching filters

            Use Cases:
                - Update 5 specific documents with different metadata values
                - Update documents by IDs with per-document update control
                - Combine with filters for targeted batch updates

            Requirements:
                - EITHER 'updates' (explicit mode) OR 'filters' + 'update_data' (filter mode)
                - NOT BOTH modes simultaneously

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchUpdateDocumentsResponse | ErrorResponse | HTTPValidationError]
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
    body: BatchUpdateDocumentsRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> BatchUpdateDocumentsResponse | ErrorResponse | HTTPValidationError | None:
    r"""Batch Update Documents

     Batch update multiple documents by explicit IDs or filters.

    Supports TWO modes:
    1. Explicit IDs mode: Provide 'updates' array with document_id + update_data for each document
       - Each document can have DIFFERENT update_data
       - Returns detailed per-document results

    2. Filter mode: Provide 'filters' + 'update_data' to update all matching documents
       - All documents receive the SAME update_data
       - Returns total count only

    Key Features:
    - Update any document field except vectors (metadata, internal_metadata, source_blobs, etc.)
    - Maximum 1000 documents per batch in explicit mode
    - Per-document success/failure reporting in explicit mode
    - Validates documents exist in the specified collection

    Examples:
        Explicit IDs mode:
        ```json
        {
            \"updates\": [
                {\"document_id\": \"doc_123\", \"update_data\": {\"metadata\": {\"status\":
    \"processed\"}}},
                {\"document_id\": \"doc_456\", \"update_data\": {\"metadata\": {\"status\":
    \"archived\"}}}
            ]
        }
        ```

        Filter mode:
        ```json
        {
            \"filters\": {\"must\": [{\"key\": \"metadata.status\", \"value\": \"pending\"}]},
            \"update_data\": {\"metadata\": {\"status\": \"processed\"}}
        }
        ```

    Args:
        collection_identifier (str): The ID of the collection to update documents in.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (BatchUpdateDocumentsRequest): Request model for batch updating multiple documents by
            explicit IDs or filters.

            Supports TWO modes:
            1. Explicit IDs mode: Provide 'updates' array with document_id + update_data for each
            2. Filter mode: Provide 'filters' + 'update_data' to update all matching documents

            Key difference from BulkUpdateDocumentsRequest:
            - Batch (this): Can apply DIFFERENT updates to SPECIFIC documents by ID
            - Bulk: Applies SAME update to ALL documents matching filters

            Use Cases:
                - Update 5 specific documents with different metadata values
                - Update documents by IDs with per-document update control
                - Combine with filters for targeted batch updates

            Requirements:
                - EITHER 'updates' (explicit mode) OR 'filters' + 'update_data' (filter mode)
                - NOT BOTH modes simultaneously

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchUpdateDocumentsResponse | ErrorResponse | HTTPValidationError
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
