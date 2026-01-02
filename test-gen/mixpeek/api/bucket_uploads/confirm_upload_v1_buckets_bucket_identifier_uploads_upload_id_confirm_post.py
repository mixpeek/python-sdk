from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.confirm_upload_request import ConfirmUploadRequest
from ...models.confirm_upload_response import ConfirmUploadResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket_identifier: str,
    upload_id: str,
    *,
    body: ConfirmUploadRequest,
    async_: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    params["async"] = async_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/buckets/{bucket_identifier}/uploads/{upload_id}/confirm".format(
            bucket_identifier=quote(str(bucket_identifier), safe=""),
            upload_id=quote(str(upload_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConfirmUploadResponse | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ConfirmUploadResponse.from_dict(response.json())

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
) -> Response[ConfirmUploadResponse | ErrorResponse | HTTPValidationError]:
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
    body: ConfirmUploadRequest,
    async_: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ConfirmUploadResponse | ErrorResponse | HTTPValidationError]:
    """Confirm Upload

     Verify S3 upload completion and create bucket object.

        After uploading to S3 using the presigned URL, call this endpoint to:
        1. Verify the file exists in S3
        2. Validate ETag and file size (if provided)
        3. Create bucket object (default, unless create_object_on_confirm=false)
        4. Update upload status to COMPLETED

        **Sync vs Async**:
        - Files < 100MB: Processed synchronously (~100ms)
        - Files >= 100MB or async=true: Processed asynchronously (returns task_id)

        **Duplicate Detection**:
        - If file hash matches existing upload, marks as duplicate
        - References original object_id if available

    Args:
        bucket_identifier (str): The unique identifier of the bucket
        upload_id (str): The unique identifier of the upload
        async_ (bool | Unset): Process confirmation asynchronously (recommended for files >=
            100MB) Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ConfirmUploadRequest): Request to confirm S3 upload completion and create bucket
            object.

            ⚠️  THIS ENDPOINT IS REQUIRED AFTER UPLOADING TO S3!

            S3 presigned URLs have no callback mechanism - the API cannot detect when
            your upload completes. You MUST call this endpoint to finalize the upload.

            Why confirmation is required:
                - S3 doesn't notify us when uploads complete
                - We need to verify the file actually exists in S3
                - We need to create the bucket object
                - We need to update quotas and tracking

            The system will:
            1. Verify the S3 object exists (HeadObject call)
            2. Validate ETag matches (if provided) - RECOMMENDED for integrity
            3. Validate file size matches (if provided)
            4. Create bucket object (default, unless create_object_on_confirm=false)
            5. Update upload status to COMPLETED

            If you don't call confirm:
                - Upload stays in PENDING status
                - No bucket object is created
                - File is orphaned in S3

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmUploadResponse | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        upload_id=upload_id,
        body=body,
        async_=async_,
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
    body: ConfirmUploadRequest,
    async_: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ConfirmUploadResponse | ErrorResponse | HTTPValidationError | None:
    """Confirm Upload

     Verify S3 upload completion and create bucket object.

        After uploading to S3 using the presigned URL, call this endpoint to:
        1. Verify the file exists in S3
        2. Validate ETag and file size (if provided)
        3. Create bucket object (default, unless create_object_on_confirm=false)
        4. Update upload status to COMPLETED

        **Sync vs Async**:
        - Files < 100MB: Processed synchronously (~100ms)
        - Files >= 100MB or async=true: Processed asynchronously (returns task_id)

        **Duplicate Detection**:
        - If file hash matches existing upload, marks as duplicate
        - References original object_id if available

    Args:
        bucket_identifier (str): The unique identifier of the bucket
        upload_id (str): The unique identifier of the upload
        async_ (bool | Unset): Process confirmation asynchronously (recommended for files >=
            100MB) Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ConfirmUploadRequest): Request to confirm S3 upload completion and create bucket
            object.

            ⚠️  THIS ENDPOINT IS REQUIRED AFTER UPLOADING TO S3!

            S3 presigned URLs have no callback mechanism - the API cannot detect when
            your upload completes. You MUST call this endpoint to finalize the upload.

            Why confirmation is required:
                - S3 doesn't notify us when uploads complete
                - We need to verify the file actually exists in S3
                - We need to create the bucket object
                - We need to update quotas and tracking

            The system will:
            1. Verify the S3 object exists (HeadObject call)
            2. Validate ETag matches (if provided) - RECOMMENDED for integrity
            3. Validate file size matches (if provided)
            4. Create bucket object (default, unless create_object_on_confirm=false)
            5. Update upload status to COMPLETED

            If you don't call confirm:
                - Upload stays in PENDING status
                - No bucket object is created
                - File is orphaned in S3

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmUploadResponse | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        bucket_identifier=bucket_identifier,
        upload_id=upload_id,
        client=client,
        body=body,
        async_=async_,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    bucket_identifier: str,
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConfirmUploadRequest,
    async_: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ConfirmUploadResponse | ErrorResponse | HTTPValidationError]:
    """Confirm Upload

     Verify S3 upload completion and create bucket object.

        After uploading to S3 using the presigned URL, call this endpoint to:
        1. Verify the file exists in S3
        2. Validate ETag and file size (if provided)
        3. Create bucket object (default, unless create_object_on_confirm=false)
        4. Update upload status to COMPLETED

        **Sync vs Async**:
        - Files < 100MB: Processed synchronously (~100ms)
        - Files >= 100MB or async=true: Processed asynchronously (returns task_id)

        **Duplicate Detection**:
        - If file hash matches existing upload, marks as duplicate
        - References original object_id if available

    Args:
        bucket_identifier (str): The unique identifier of the bucket
        upload_id (str): The unique identifier of the upload
        async_ (bool | Unset): Process confirmation asynchronously (recommended for files >=
            100MB) Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ConfirmUploadRequest): Request to confirm S3 upload completion and create bucket
            object.

            ⚠️  THIS ENDPOINT IS REQUIRED AFTER UPLOADING TO S3!

            S3 presigned URLs have no callback mechanism - the API cannot detect when
            your upload completes. You MUST call this endpoint to finalize the upload.

            Why confirmation is required:
                - S3 doesn't notify us when uploads complete
                - We need to verify the file actually exists in S3
                - We need to create the bucket object
                - We need to update quotas and tracking

            The system will:
            1. Verify the S3 object exists (HeadObject call)
            2. Validate ETag matches (if provided) - RECOMMENDED for integrity
            3. Validate file size matches (if provided)
            4. Create bucket object (default, unless create_object_on_confirm=false)
            5. Update upload status to COMPLETED

            If you don't call confirm:
                - Upload stays in PENDING status
                - No bucket object is created
                - File is orphaned in S3

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmUploadResponse | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        upload_id=upload_id,
        body=body,
        async_=async_,
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
    body: ConfirmUploadRequest,
    async_: bool | Unset = False,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ConfirmUploadResponse | ErrorResponse | HTTPValidationError | None:
    """Confirm Upload

     Verify S3 upload completion and create bucket object.

        After uploading to S3 using the presigned URL, call this endpoint to:
        1. Verify the file exists in S3
        2. Validate ETag and file size (if provided)
        3. Create bucket object (default, unless create_object_on_confirm=false)
        4. Update upload status to COMPLETED

        **Sync vs Async**:
        - Files < 100MB: Processed synchronously (~100ms)
        - Files >= 100MB or async=true: Processed asynchronously (returns task_id)

        **Duplicate Detection**:
        - If file hash matches existing upload, marks as duplicate
        - References original object_id if available

    Args:
        bucket_identifier (str): The unique identifier of the bucket
        upload_id (str): The unique identifier of the upload
        async_ (bool | Unset): Process confirmation asynchronously (recommended for files >=
            100MB) Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ConfirmUploadRequest): Request to confirm S3 upload completion and create bucket
            object.

            ⚠️  THIS ENDPOINT IS REQUIRED AFTER UPLOADING TO S3!

            S3 presigned URLs have no callback mechanism - the API cannot detect when
            your upload completes. You MUST call this endpoint to finalize the upload.

            Why confirmation is required:
                - S3 doesn't notify us when uploads complete
                - We need to verify the file actually exists in S3
                - We need to create the bucket object
                - We need to update quotas and tracking

            The system will:
            1. Verify the S3 object exists (HeadObject call)
            2. Validate ETag matches (if provided) - RECOMMENDED for integrity
            3. Validate file size matches (if provided)
            4. Create bucket object (default, unless create_object_on_confirm=false)
            5. Update upload status to COMPLETED

            If you don't call confirm:
                - Upload stays in PENDING status
                - No bucket object is created
                - File is orphaned in S3

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmUploadResponse | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            bucket_identifier=bucket_identifier,
            upload_id=upload_id,
            client=client,
            body=body,
            async_=async_,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
