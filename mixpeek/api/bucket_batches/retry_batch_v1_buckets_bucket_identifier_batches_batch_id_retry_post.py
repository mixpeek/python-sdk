from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.retry_batch_request import RetryBatchRequest
from ...models.retry_batch_v1_buckets_bucket_identifier_batches_batch_id_retry_post_response_retry_batch_v1_buckets_bucket_identifier_batches_batch_id_retry_post import (
    RetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPostResponseRetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPost,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket_identifier: str,
    batch_id: str,
    *,
    body: RetryBatchRequest,
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
        "url": "/v1/buckets/{bucket_identifier}/batches/{batch_id}/retry".format(
            bucket_identifier=quote(str(bucket_identifier), safe=""),
            batch_id=quote(str(batch_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponse
    | HTTPValidationError
    | RetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPostResponseRetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPost
    | None
):
    if response.status_code == 200:
        response_200 = RetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPostResponseRetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPost.from_dict(
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
    | HTTPValidationError
    | RetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPostResponseRetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPost
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
    body: RetryBatchRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | HTTPValidationError
    | RetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPostResponseRetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPost
]:
    """Retry Failed Documents

     Retry failed documents in a batch with intelligent filtering by error type and tier.

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        batch_id (str): The unique identifier of the batch.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (RetryBatchRequest): Request to retry failed documents in a batch.

            Allows selective retry of failed documents with intelligent filtering by error type
            and tier. Retries use exponential backoff and respect max retry limits.

            Use Cases:
                - Retry only transient errors after resolving temporary infrastructure issues
                - Retry specific processing tiers that failed
                - Retry all failed documents regardless of error type (force retry)

            Requirements:
                - retry_mode: REQUIRED. Determines which documents to retry
                - tier_nums: OPTIONAL. Only retry failures from specific tiers (empty = all tiers)
                - max_retry_count: OPTIONAL. Skip documents that have been retried this many times

            Behavior:
                - 'transient_only': Retries only transient errors (network, timeout, rate limit)
                - 'all': Retries both transient and permanent errors
                - Documents beyond max_retry_count are excluded from retry
                - Each retry increments the document's retry_count

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | RetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPostResponseRetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPost]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        batch_id=batch_id,
        body=body,
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
    body: RetryBatchRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> (
    ErrorResponse
    | HTTPValidationError
    | RetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPostResponseRetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPost
    | None
):
    """Retry Failed Documents

     Retry failed documents in a batch with intelligent filtering by error type and tier.

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        batch_id (str): The unique identifier of the batch.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (RetryBatchRequest): Request to retry failed documents in a batch.

            Allows selective retry of failed documents with intelligent filtering by error type
            and tier. Retries use exponential backoff and respect max retry limits.

            Use Cases:
                - Retry only transient errors after resolving temporary infrastructure issues
                - Retry specific processing tiers that failed
                - Retry all failed documents regardless of error type (force retry)

            Requirements:
                - retry_mode: REQUIRED. Determines which documents to retry
                - tier_nums: OPTIONAL. Only retry failures from specific tiers (empty = all tiers)
                - max_retry_count: OPTIONAL. Skip documents that have been retried this many times

            Behavior:
                - 'transient_only': Retries only transient errors (network, timeout, rate limit)
                - 'all': Retries both transient and permanent errors
                - Documents beyond max_retry_count are excluded from retry
                - Each retry increments the document's retry_count

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | RetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPostResponseRetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPost
    """

    return sync_detailed(
        bucket_identifier=bucket_identifier,
        batch_id=batch_id,
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    bucket_identifier: str,
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RetryBatchRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | HTTPValidationError
    | RetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPostResponseRetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPost
]:
    """Retry Failed Documents

     Retry failed documents in a batch with intelligent filtering by error type and tier.

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        batch_id (str): The unique identifier of the batch.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (RetryBatchRequest): Request to retry failed documents in a batch.

            Allows selective retry of failed documents with intelligent filtering by error type
            and tier. Retries use exponential backoff and respect max retry limits.

            Use Cases:
                - Retry only transient errors after resolving temporary infrastructure issues
                - Retry specific processing tiers that failed
                - Retry all failed documents regardless of error type (force retry)

            Requirements:
                - retry_mode: REQUIRED. Determines which documents to retry
                - tier_nums: OPTIONAL. Only retry failures from specific tiers (empty = all tiers)
                - max_retry_count: OPTIONAL. Skip documents that have been retried this many times

            Behavior:
                - 'transient_only': Retries only transient errors (network, timeout, rate limit)
                - 'all': Retries both transient and permanent errors
                - Documents beyond max_retry_count are excluded from retry
                - Each retry increments the document's retry_count

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | RetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPostResponseRetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPost]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        batch_id=batch_id,
        body=body,
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
    body: RetryBatchRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> (
    ErrorResponse
    | HTTPValidationError
    | RetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPostResponseRetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPost
    | None
):
    """Retry Failed Documents

     Retry failed documents in a batch with intelligent filtering by error type and tier.

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        batch_id (str): The unique identifier of the batch.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (RetryBatchRequest): Request to retry failed documents in a batch.

            Allows selective retry of failed documents with intelligent filtering by error type
            and tier. Retries use exponential backoff and respect max retry limits.

            Use Cases:
                - Retry only transient errors after resolving temporary infrastructure issues
                - Retry specific processing tiers that failed
                - Retry all failed documents regardless of error type (force retry)

            Requirements:
                - retry_mode: REQUIRED. Determines which documents to retry
                - tier_nums: OPTIONAL. Only retry failures from specific tiers (empty = all tiers)
                - max_retry_count: OPTIONAL. Skip documents that have been retried this many times

            Behavior:
                - 'transient_only': Retries only transient errors (network, timeout, rate limit)
                - 'all': Retries both transient and permanent errors
                - Documents beyond max_retry_count are excluded from retry
                - Each retry increments the document's retry_count

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | RetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPostResponseRetryBatchV1BucketsBucketIdentifierBatchesBatchIdRetryPost
    """

    return (
        await asyncio_detailed(
            bucket_identifier=bucket_identifier,
            batch_id=batch_id,
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
