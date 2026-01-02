from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_documents_by_object_v1_objects_object_id_documents_get_response_get_documents_by_object_v1_objects_object_id_documents_get import (
    GetDocumentsByObjectV1ObjectsObjectIdDocumentsGetResponseGetDocumentsByObjectV1ObjectsObjectIdDocumentsGet,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_id: str,
    *,
    collection_ids: list[str] | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    json_collection_ids: list[str] | Unset = UNSET
    if not isinstance(collection_ids, Unset):
        json_collection_ids = collection_ids

    params["collection_ids"] = json_collection_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/objects/{object_id}/documents".format(
            object_id=quote(str(object_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponse
    | GetDocumentsByObjectV1ObjectsObjectIdDocumentsGetResponseGetDocumentsByObjectV1ObjectsObjectIdDocumentsGet
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = GetDocumentsByObjectV1ObjectsObjectIdDocumentsGetResponseGetDocumentsByObjectV1ObjectsObjectIdDocumentsGet.from_dict(
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
    | GetDocumentsByObjectV1ObjectsObjectIdDocumentsGetResponseGetDocumentsByObjectV1ObjectsObjectIdDocumentsGet
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    collection_ids: list[str] | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | GetDocumentsByObjectV1ObjectsObjectIdDocumentsGetResponseGetDocumentsByObjectV1ObjectsObjectIdDocumentsGet
    | HTTPValidationError
]:
    """Get all documents derived from an object

     Get all documents created from a specific root object. Useful for finding all processing outputs
    across multiple collections.

    Args:
        object_id (str): Root object ID to find all derived documents
        collection_ids (list[str] | Unset): Optional: Filter to specific collections
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
        Response[ErrorResponse | GetDocumentsByObjectV1ObjectsObjectIdDocumentsGetResponseGetDocumentsByObjectV1ObjectsObjectIdDocumentsGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        collection_ids=collection_ids,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    collection_ids: list[str] | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> (
    ErrorResponse
    | GetDocumentsByObjectV1ObjectsObjectIdDocumentsGetResponseGetDocumentsByObjectV1ObjectsObjectIdDocumentsGet
    | HTTPValidationError
    | None
):
    """Get all documents derived from an object

     Get all documents created from a specific root object. Useful for finding all processing outputs
    across multiple collections.

    Args:
        object_id (str): Root object ID to find all derived documents
        collection_ids (list[str] | Unset): Optional: Filter to specific collections
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
        ErrorResponse | GetDocumentsByObjectV1ObjectsObjectIdDocumentsGetResponseGetDocumentsByObjectV1ObjectsObjectIdDocumentsGet | HTTPValidationError
    """

    return sync_detailed(
        object_id=object_id,
        client=client,
        collection_ids=collection_ids,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    collection_ids: list[str] | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | GetDocumentsByObjectV1ObjectsObjectIdDocumentsGetResponseGetDocumentsByObjectV1ObjectsObjectIdDocumentsGet
    | HTTPValidationError
]:
    """Get all documents derived from an object

     Get all documents created from a specific root object. Useful for finding all processing outputs
    across multiple collections.

    Args:
        object_id (str): Root object ID to find all derived documents
        collection_ids (list[str] | Unset): Optional: Filter to specific collections
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
        Response[ErrorResponse | GetDocumentsByObjectV1ObjectsObjectIdDocumentsGetResponseGetDocumentsByObjectV1ObjectsObjectIdDocumentsGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        collection_ids=collection_ids,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    collection_ids: list[str] | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> (
    ErrorResponse
    | GetDocumentsByObjectV1ObjectsObjectIdDocumentsGetResponseGetDocumentsByObjectV1ObjectsObjectIdDocumentsGet
    | HTTPValidationError
    | None
):
    """Get all documents derived from an object

     Get all documents created from a specific root object. Useful for finding all processing outputs
    across multiple collections.

    Args:
        object_id (str): Root object ID to find all derived documents
        collection_ids (list[str] | Unset): Optional: Filter to specific collections
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
        ErrorResponse | GetDocumentsByObjectV1ObjectsObjectIdDocumentsGetResponseGetDocumentsByObjectV1ObjectsObjectIdDocumentsGet | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            object_id=object_id,
            client=client,
            collection_ids=collection_ids,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
