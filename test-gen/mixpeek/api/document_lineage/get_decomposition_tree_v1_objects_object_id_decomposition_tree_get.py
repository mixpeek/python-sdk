from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_decomposition_tree_v1_objects_object_id_decomposition_tree_get_response_get_decomposition_tree_v1_objects_object_id_decomposition_tree_get import (
    GetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGetResponseGetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGet,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_id: str,
    *,
    include_document_ids: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    params["include_document_ids"] = include_document_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/objects/{object_id}/decomposition-tree".format(
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
    | GetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGetResponseGetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGet
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = GetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGetResponseGetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGet.from_dict(
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
    | GetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGetResponseGetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGet
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
    include_document_ids: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | GetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGetResponseGetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGet
    | HTTPValidationError
]:
    """Get decomposition tree visualization

     Get a hierarchical tree structure showing all collections and documents derived from a root object.
    Shows the complete multi-stage processing pipeline.

    Args:
        object_id (str): Root object ID to build decomposition tree for
        include_document_ids (bool | Unset): Include full list of document IDs (can be large)
            Default: False.
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
        Response[ErrorResponse | GetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGetResponseGetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        include_document_ids=include_document_ids,
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
    include_document_ids: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> (
    ErrorResponse
    | GetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGetResponseGetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGet
    | HTTPValidationError
    | None
):
    """Get decomposition tree visualization

     Get a hierarchical tree structure showing all collections and documents derived from a root object.
    Shows the complete multi-stage processing pipeline.

    Args:
        object_id (str): Root object ID to build decomposition tree for
        include_document_ids (bool | Unset): Include full list of document IDs (can be large)
            Default: False.
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
        ErrorResponse | GetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGetResponseGetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGet | HTTPValidationError
    """

    return sync_detailed(
        object_id=object_id,
        client=client,
        include_document_ids=include_document_ids,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_document_ids: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | GetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGetResponseGetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGet
    | HTTPValidationError
]:
    """Get decomposition tree visualization

     Get a hierarchical tree structure showing all collections and documents derived from a root object.
    Shows the complete multi-stage processing pipeline.

    Args:
        object_id (str): Root object ID to build decomposition tree for
        include_document_ids (bool | Unset): Include full list of document IDs (can be large)
            Default: False.
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
        Response[ErrorResponse | GetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGetResponseGetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        include_document_ids=include_document_ids,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_document_ids: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> (
    ErrorResponse
    | GetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGetResponseGetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGet
    | HTTPValidationError
    | None
):
    """Get decomposition tree visualization

     Get a hierarchical tree structure showing all collections and documents derived from a root object.
    Shows the complete multi-stage processing pipeline.

    Args:
        object_id (str): Root object ID to build decomposition tree for
        include_document_ids (bool | Unset): Include full list of document IDs (can be large)
            Default: False.
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
        ErrorResponse | GetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGetResponseGetDecompositionTreeV1ObjectsObjectIdDecompositionTreeGet | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            object_id=object_id,
            client=client,
            include_document_ids=include_document_ids,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
