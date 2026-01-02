from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket_identifier: str,
    upload_id: str,
    *,
    return_presigned_urls: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    params["return_presigned_urls"] = return_presigned_urls

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/buckets/{bucket_identifier}/uploads/{upload_id}".format(
            bucket_identifier=quote(str(bucket_identifier), safe=""),
            upload_id=quote(str(upload_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bucket_identifier: str,
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,
    return_presigned_urls: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    """Get Upload

     Retrieve an upload by its ID.

        Use this to check upload status, get S3 key, or retrieve created object_id after confirmation.

        **Presigned URLs**: Set `return_presigned_urls=true` query parameter to generate fresh presigned
    download URLs (default: false).
        The presigned URLs expire after 1 hour and allow direct download from S3.

    Args:
        bucket_identifier (str): The unique identifier of the bucket
        upload_id (str): The unique identifier of the upload
        return_presigned_urls (bool | Unset): Generate fresh presigned download URLs for all blobs
            with S3 storage Default: False.
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
        Response[Any | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        upload_id=upload_id,
        return_presigned_urls=return_presigned_urls,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bucket_identifier: str,
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,
    return_presigned_urls: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    """Get Upload

     Retrieve an upload by its ID.

        Use this to check upload status, get S3 key, or retrieve created object_id after confirmation.

        **Presigned URLs**: Set `return_presigned_urls=true` query parameter to generate fresh presigned
    download URLs (default: false).
        The presigned URLs expire after 1 hour and allow direct download from S3.

    Args:
        bucket_identifier (str): The unique identifier of the bucket
        upload_id (str): The unique identifier of the upload
        return_presigned_urls (bool | Unset): Generate fresh presigned download URLs for all blobs
            with S3 storage Default: False.
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
        Any | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        bucket_identifier=bucket_identifier,
        upload_id=upload_id,
        client=client,
        return_presigned_urls=return_presigned_urls,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    bucket_identifier: str,
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,
    return_presigned_urls: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    """Get Upload

     Retrieve an upload by its ID.

        Use this to check upload status, get S3 key, or retrieve created object_id after confirmation.

        **Presigned URLs**: Set `return_presigned_urls=true` query parameter to generate fresh presigned
    download URLs (default: false).
        The presigned URLs expire after 1 hour and allow direct download from S3.

    Args:
        bucket_identifier (str): The unique identifier of the bucket
        upload_id (str): The unique identifier of the upload
        return_presigned_urls (bool | Unset): Generate fresh presigned download URLs for all blobs
            with S3 storage Default: False.
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
        Response[Any | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        upload_id=upload_id,
        return_presigned_urls=return_presigned_urls,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket_identifier: str,
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,
    return_presigned_urls: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    """Get Upload

     Retrieve an upload by its ID.

        Use this to check upload status, get S3 key, or retrieve created object_id after confirmation.

        **Presigned URLs**: Set `return_presigned_urls=true` query parameter to generate fresh presigned
    download URLs (default: false).
        The presigned URLs expire after 1 hour and allow direct download from S3.

    Args:
        bucket_identifier (str): The unique identifier of the bucket
        upload_id (str): The unique identifier of the upload
        return_presigned_urls (bool | Unset): Generate fresh presigned download URLs for all blobs
            with S3 storage Default: False.
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
        Any | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            bucket_identifier=bucket_identifier,
            upload_id=upload_id,
            client=client,
            return_presigned_urls=return_presigned_urls,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
