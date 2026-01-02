from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_document_lineage_v1_collections_collection_id_documents_document_id_lineage_get_response_get_document_lineage_v1_collections_collection_id_documents_document_id_lineage_get import (
    GetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGetResponseGetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGet,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: str,
    document_id: str,
    *,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collections/{collection_id}/documents/{document_id}/lineage".format(
            collection_id=quote(str(collection_id), safe=""),
            document_id=quote(str(document_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponse
    | GetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGetResponseGetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGet
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = GetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGetResponseGetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGet.from_dict(
            response.json()
        )

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
    | GetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGetResponseGetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGet
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | GetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGetResponseGetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGet
    | HTTPValidationError
]:
    """Get document lineage

     Get the complete processing lineage for a document. Shows the full chain of transformations from the
    root bucket object through all collection processing stages.

    Args:
        collection_id (str): ID of the collection containing the document
        document_id (str): ID of the document to trace
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
        Response[ErrorResponse | GetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGetResponseGetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        document_id=document_id,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> (
    ErrorResponse
    | GetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGetResponseGetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGet
    | HTTPValidationError
    | None
):
    """Get document lineage

     Get the complete processing lineage for a document. Shows the full chain of transformations from the
    root bucket object through all collection processing stages.

    Args:
        collection_id (str): ID of the collection containing the document
        document_id (str): ID of the document to trace
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
        ErrorResponse | GetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGetResponseGetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGet | HTTPValidationError
    """

    return sync_detailed(
        collection_id=collection_id,
        document_id=document_id,
        client=client,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | GetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGetResponseGetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGet
    | HTTPValidationError
]:
    """Get document lineage

     Get the complete processing lineage for a document. Shows the full chain of transformations from the
    root bucket object through all collection processing stages.

    Args:
        collection_id (str): ID of the collection containing the document
        document_id (str): ID of the document to trace
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
        Response[ErrorResponse | GetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGetResponseGetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        document_id=document_id,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> (
    ErrorResponse
    | GetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGetResponseGetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGet
    | HTTPValidationError
    | None
):
    """Get document lineage

     Get the complete processing lineage for a document. Shows the full chain of transformations from the
    root bucket object through all collection processing stages.

    Args:
        collection_id (str): ID of the collection containing the document
        document_id (str): ID of the document to trace
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
        ErrorResponse | GetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGetResponseGetDocumentLineageV1CollectionsCollectionIdDocumentsDocumentIdLineageGet | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            document_id=document_id,
            client=client,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
