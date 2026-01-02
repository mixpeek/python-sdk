from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.trigger_collection_request import TriggerCollectionRequest
from ...models.trigger_collection_response import TriggerCollectionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_identifier: str,
    *,
    body: TriggerCollectionRequest | Unset = UNSET,
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
        "url": "/v1/collections/{collection_identifier}/trigger".format(
            collection_identifier=quote(str(collection_identifier), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | TriggerCollectionResponse | None:
    if response.status_code == 202:
        response_202 = TriggerCollectionResponse.from_dict(response.json())

        return response_202

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
) -> Response[ErrorResponse | HTTPValidationError | TriggerCollectionResponse]:
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
    body: TriggerCollectionRequest | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | TriggerCollectionResponse]:
    r"""Trigger Collection Processing

     Process data through a collection - works for both bucket-sourced and collection-sourced
    collections.

        **For bucket-sourced collections:**
        Discovers objects from source bucket(s), creates a batch, and submits for processing.
        Use `include_buckets` to limit which source buckets to process from.

        **For collection-sourced collections:**
        Processes existing documents from upstream collection(s).
        Use `include_collections` to limit which source collections to process from.

        **Filtering:**
        - `source_filters`: Field-level filters using LogicalOperator format
        - Example: `{\"AND\": [{\"field\": \"status\", \"operator\": \"eq\", \"value\": \"pending\"}]}`
        - For specific objects: `{\"AND\": [{\"field\": \"object_id\", \"operator\": \"in\", \"value\":
    [\"obj_1\", \"obj_2\"]}]}`

        **Returns:**
        - batch_id: Track progress via GET /batches/{batch_id}
        - task_id: Monitor via GET /tasks/{task_id}

    Args:
        collection_identifier (str): The ID or name of the collection to trigger
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (TriggerCollectionRequest | Unset): Request to trigger (re)processing through a
            collection.

            **For bucket-sourced collections (tier 0):**
            Discovers objects from source bucket(s) and creates a batch for processing.
            Use `include_buckets` to limit which source buckets to process from.

            **For collection-sourced collections (tier N):**
            Processes existing documents from upstream collection(s).
            Use `include_collections` to limit which source collections to process from.

            Use `source_filters` for field-level filtering on objects or documents.

            **Document Overwrite Behavior:**
            - If source bucket has `unique_key` configured: Documents are UPSERTED (overwrites
            existing)
            - If source bucket has NO `unique_key`: New documents are CREATED (may cause duplicates)

            To enable idempotent re-processing, configure `unique_key` on the source bucket.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | TriggerCollectionResponse]
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
    body: TriggerCollectionRequest | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | TriggerCollectionResponse | None:
    r"""Trigger Collection Processing

     Process data through a collection - works for both bucket-sourced and collection-sourced
    collections.

        **For bucket-sourced collections:**
        Discovers objects from source bucket(s), creates a batch, and submits for processing.
        Use `include_buckets` to limit which source buckets to process from.

        **For collection-sourced collections:**
        Processes existing documents from upstream collection(s).
        Use `include_collections` to limit which source collections to process from.

        **Filtering:**
        - `source_filters`: Field-level filters using LogicalOperator format
        - Example: `{\"AND\": [{\"field\": \"status\", \"operator\": \"eq\", \"value\": \"pending\"}]}`
        - For specific objects: `{\"AND\": [{\"field\": \"object_id\", \"operator\": \"in\", \"value\":
    [\"obj_1\", \"obj_2\"]}]}`

        **Returns:**
        - batch_id: Track progress via GET /batches/{batch_id}
        - task_id: Monitor via GET /tasks/{task_id}

    Args:
        collection_identifier (str): The ID or name of the collection to trigger
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (TriggerCollectionRequest | Unset): Request to trigger (re)processing through a
            collection.

            **For bucket-sourced collections (tier 0):**
            Discovers objects from source bucket(s) and creates a batch for processing.
            Use `include_buckets` to limit which source buckets to process from.

            **For collection-sourced collections (tier N):**
            Processes existing documents from upstream collection(s).
            Use `include_collections` to limit which source collections to process from.

            Use `source_filters` for field-level filtering on objects or documents.

            **Document Overwrite Behavior:**
            - If source bucket has `unique_key` configured: Documents are UPSERTED (overwrites
            existing)
            - If source bucket has NO `unique_key`: New documents are CREATED (may cause duplicates)

            To enable idempotent re-processing, configure `unique_key` on the source bucket.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | TriggerCollectionResponse
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
    body: TriggerCollectionRequest | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | TriggerCollectionResponse]:
    r"""Trigger Collection Processing

     Process data through a collection - works for both bucket-sourced and collection-sourced
    collections.

        **For bucket-sourced collections:**
        Discovers objects from source bucket(s), creates a batch, and submits for processing.
        Use `include_buckets` to limit which source buckets to process from.

        **For collection-sourced collections:**
        Processes existing documents from upstream collection(s).
        Use `include_collections` to limit which source collections to process from.

        **Filtering:**
        - `source_filters`: Field-level filters using LogicalOperator format
        - Example: `{\"AND\": [{\"field\": \"status\", \"operator\": \"eq\", \"value\": \"pending\"}]}`
        - For specific objects: `{\"AND\": [{\"field\": \"object_id\", \"operator\": \"in\", \"value\":
    [\"obj_1\", \"obj_2\"]}]}`

        **Returns:**
        - batch_id: Track progress via GET /batches/{batch_id}
        - task_id: Monitor via GET /tasks/{task_id}

    Args:
        collection_identifier (str): The ID or name of the collection to trigger
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (TriggerCollectionRequest | Unset): Request to trigger (re)processing through a
            collection.

            **For bucket-sourced collections (tier 0):**
            Discovers objects from source bucket(s) and creates a batch for processing.
            Use `include_buckets` to limit which source buckets to process from.

            **For collection-sourced collections (tier N):**
            Processes existing documents from upstream collection(s).
            Use `include_collections` to limit which source collections to process from.

            Use `source_filters` for field-level filtering on objects or documents.

            **Document Overwrite Behavior:**
            - If source bucket has `unique_key` configured: Documents are UPSERTED (overwrites
            existing)
            - If source bucket has NO `unique_key`: New documents are CREATED (may cause duplicates)

            To enable idempotent re-processing, configure `unique_key` on the source bucket.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | TriggerCollectionResponse]
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
    body: TriggerCollectionRequest | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | TriggerCollectionResponse | None:
    r"""Trigger Collection Processing

     Process data through a collection - works for both bucket-sourced and collection-sourced
    collections.

        **For bucket-sourced collections:**
        Discovers objects from source bucket(s), creates a batch, and submits for processing.
        Use `include_buckets` to limit which source buckets to process from.

        **For collection-sourced collections:**
        Processes existing documents from upstream collection(s).
        Use `include_collections` to limit which source collections to process from.

        **Filtering:**
        - `source_filters`: Field-level filters using LogicalOperator format
        - Example: `{\"AND\": [{\"field\": \"status\", \"operator\": \"eq\", \"value\": \"pending\"}]}`
        - For specific objects: `{\"AND\": [{\"field\": \"object_id\", \"operator\": \"in\", \"value\":
    [\"obj_1\", \"obj_2\"]}]}`

        **Returns:**
        - batch_id: Track progress via GET /batches/{batch_id}
        - task_id: Monitor via GET /tasks/{task_id}

    Args:
        collection_identifier (str): The ID or name of the collection to trigger
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (TriggerCollectionRequest | Unset): Request to trigger (re)processing through a
            collection.

            **For bucket-sourced collections (tier 0):**
            Discovers objects from source bucket(s) and creates a batch for processing.
            Use `include_buckets` to limit which source buckets to process from.

            **For collection-sourced collections (tier N):**
            Processes existing documents from upstream collection(s).
            Use `include_collections` to limit which source collections to process from.

            Use `source_filters` for field-level filtering on objects or documents.

            **Document Overwrite Behavior:**
            - If source bucket has `unique_key` configured: Documents are UPSERTED (overwrites
            existing)
            - If source bucket has NO `unique_key`: New documents are CREATED (may cause duplicates)

            To enable idempotent re-processing, configure `unique_key` on the source bucket.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | TriggerCollectionResponse
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
