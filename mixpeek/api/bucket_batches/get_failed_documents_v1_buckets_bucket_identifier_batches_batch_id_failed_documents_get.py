from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_failed_documents_v1_buckets_bucket_identifier_batches_batch_id_failed_documents_get_response_get_failed_documents_v1_buckets_bucket_identifier_batches_batch_id_failed_documents_get import (
    GetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGetResponseGetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGet,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket_identifier: str,
    batch_id: str,
    *,
    tier_num: int | None | Unset = UNSET,
    collection_id: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    json_tier_num: int | None | Unset
    if isinstance(tier_num, Unset):
        json_tier_num = UNSET
    else:
        json_tier_num = tier_num
    params["tier_num"] = json_tier_num

    json_collection_id: None | str | Unset
    if isinstance(collection_id, Unset):
        json_collection_id = UNSET
    else:
        json_collection_id = collection_id
    params["collection_id"] = json_collection_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/buckets/{bucket_identifier}/batches/{batch_id}/failed-documents".format(
            bucket_identifier=quote(str(bucket_identifier), safe=""),
            batch_id=quote(str(batch_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponse
    | GetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGetResponseGetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGet
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = GetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGetResponseGetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGet.from_dict(
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
    | GetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGetResponseGetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGet
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bucket_identifier: str,
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
    tier_num: int | None | Unset = UNSET,
    collection_id: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | GetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGetResponseGetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGet
    | HTTPValidationError
]:
    """Get Failed Documents for Batch

     Retrieve failed documents for a batch, optionally filtered by tier or collection.

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        batch_id (str): The unique identifier of the batch.
        tier_num (int | None | Unset):
        collection_id (None | str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
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
        Response[ErrorResponse | GetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGetResponseGetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        batch_id=batch_id,
        tier_num=tier_num,
        collection_id=collection_id,
        limit=limit,
        offset=offset,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bucket_identifier: str,
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
    tier_num: int | None | Unset = UNSET,
    collection_id: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> (
    ErrorResponse
    | GetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGetResponseGetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGet
    | HTTPValidationError
    | None
):
    """Get Failed Documents for Batch

     Retrieve failed documents for a batch, optionally filtered by tier or collection.

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        batch_id (str): The unique identifier of the batch.
        tier_num (int | None | Unset):
        collection_id (None | str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
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
        ErrorResponse | GetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGetResponseGetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGet | HTTPValidationError
    """

    return sync_detailed(
        bucket_identifier=bucket_identifier,
        batch_id=batch_id,
        client=client,
        tier_num=tier_num,
        collection_id=collection_id,
        limit=limit,
        offset=offset,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    bucket_identifier: str,
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
    tier_num: int | None | Unset = UNSET,
    collection_id: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | GetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGetResponseGetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGet
    | HTTPValidationError
]:
    """Get Failed Documents for Batch

     Retrieve failed documents for a batch, optionally filtered by tier or collection.

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        batch_id (str): The unique identifier of the batch.
        tier_num (int | None | Unset):
        collection_id (None | str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
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
        Response[ErrorResponse | GetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGetResponseGetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        batch_id=batch_id,
        tier_num=tier_num,
        collection_id=collection_id,
        limit=limit,
        offset=offset,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket_identifier: str,
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
    tier_num: int | None | Unset = UNSET,
    collection_id: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> (
    ErrorResponse
    | GetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGetResponseGetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGet
    | HTTPValidationError
    | None
):
    """Get Failed Documents for Batch

     Retrieve failed documents for a batch, optionally filtered by tier or collection.

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        batch_id (str): The unique identifier of the batch.
        tier_num (int | None | Unset):
        collection_id (None | str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.
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
        ErrorResponse | GetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGetResponseGetFailedDocumentsV1BucketsBucketIdentifierBatchesBatchIdFailedDocumentsGet | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            bucket_identifier=bucket_identifier,
            batch_id=batch_id,
            client=client,
            tier_num=tier_num,
            collection_id=collection_id,
            limit=limit,
            offset=offset,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
