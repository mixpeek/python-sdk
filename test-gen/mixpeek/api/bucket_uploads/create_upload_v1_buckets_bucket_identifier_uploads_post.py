from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_upload_request import CreateUploadRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.upload_response import UploadResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket_identifier: str,
    *,
    body: CreateUploadRequest,
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
        "url": "/v1/buckets/{bucket_identifier}/uploads".format(
            bucket_identifier=quote(str(bucket_identifier), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | UploadResponse | None:
    if response.status_code == 200:
        response_200 = UploadResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | UploadResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bucket_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateUploadRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | UploadResponse]:
    """Create Upload

     Generate a presigned URL for direct S3 upload.

        This endpoint validates all requirements BEFORE generating the presigned URL,
        ensuring immediate feedback if something is wrong (bucket inactive, quota exceeded, etc.).

        **Duplicate Detection (Enabled by Default)**:
        - If `file_hash` provided and `skip_duplicates=true`: Checks for existing upload
        - If duplicate found: Returns existing upload (200 OK) with `is_duplicate=true`
        - If new file: Returns presigned URL (201 Created) with `is_duplicate=false`

        **Two-Step Flow**:
        1. Call this endpoint → Get presigned URL
        2. PUT file to presigned URL → Upload directly to S3
        3. Call confirm endpoint → Verify upload and create object

    Args:
        bucket_identifier (str): The unique identifier of the bucket
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateUploadRequest): Request to generate a presigned URL for direct S3 upload.

            ⚠️  ⚠️  ⚠️  THIS IS THE PRESIGNED URL SYSTEM ⚠️  ⚠️  ⚠️

            This endpoint (POST /buckets/{id}/uploads) is the COMPLETE presigned URL system.
            It handles:
            - ✅ Presigned URL generation (S3 PUT URLs)
            - ✅ Upload tracking and status management
            - ✅ Validation (quotas, file size, content type, schema)
            - ✅ Duplicate detection
            - ✅ Auto object creation on confirmation
            - ✅ Returns upload_id for later reference

            DO NOT CREATE A NEW PRESIGNED UPLOAD ENDPOINT!
            If you need presigned URLs, use this existing system.

            If you think you need a new endpoint:
            1. Check if this system already does it (it probably does)
            2. Extend this system instead of creating redundancy
            3. See api/buckets/uploads/services.py for implementation

            Integration Points:
            - Object creation: Use upload_id in CreateBlobRequest.upload_id field
            - See: shared/buckets/objects/blobs/models.py::CreateBlobRequest
            - See: api/buckets/objects/canonicalization.py::resolve_upload_reference()

            Workflow:
            1. POST /buckets/{id}/uploads → Returns presigned_url + upload_id
            2. PUT presigned_url with file content (client uploads directly to S3)
            3. POST /uploads/{upload_id}/confirm → REQUIRED to finalize upload
            4. Object is created automatically (default behavior)

            ⚠️  IMPORTANT: Step 3 (confirm) is REQUIRED!
            S3 presigned URLs have no callback mechanism - the API cannot detect when
            your upload to S3 completes. You MUST call the confirm endpoint to:
            - Verify the file exists in S3
            - Validate integrity (ETag/size)
            - Create the bucket object
            - Mark upload as COMPLETED

            If you don't confirm:
            - Upload stays in PENDING status forever
            - No object is created
            - File exists in S3 but is orphaned
            - Presigned URL expires (default: 1 hour)

            Use Cases:
                - Simple: Upload → confirm → object created automatically (default)
                - Advanced: Upload multiple files with create_object_on_confirm=false,
                  then POST /buckets/{id}/objects with all upload_ids to create one object

            Requirements:
                - filename: REQUIRED, will be validated (no path traversal)
                - content_type: REQUIRED, must be valid MIME type
                - bucket_id: Comes from URL path parameter, not request body
                - All other fields: OPTIONAL with sensible defaults

            Note:
                The bucket_id comes from the URL path (/v1/buckets/{bucket_id}/uploads),
                not from the request body. The bucket is validated before generating presigned URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | UploadResponse]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
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
    *,
    client: AuthenticatedClient | Client,
    body: CreateUploadRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | UploadResponse | None:
    """Create Upload

     Generate a presigned URL for direct S3 upload.

        This endpoint validates all requirements BEFORE generating the presigned URL,
        ensuring immediate feedback if something is wrong (bucket inactive, quota exceeded, etc.).

        **Duplicate Detection (Enabled by Default)**:
        - If `file_hash` provided and `skip_duplicates=true`: Checks for existing upload
        - If duplicate found: Returns existing upload (200 OK) with `is_duplicate=true`
        - If new file: Returns presigned URL (201 Created) with `is_duplicate=false`

        **Two-Step Flow**:
        1. Call this endpoint → Get presigned URL
        2. PUT file to presigned URL → Upload directly to S3
        3. Call confirm endpoint → Verify upload and create object

    Args:
        bucket_identifier (str): The unique identifier of the bucket
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateUploadRequest): Request to generate a presigned URL for direct S3 upload.

            ⚠️  ⚠️  ⚠️  THIS IS THE PRESIGNED URL SYSTEM ⚠️  ⚠️  ⚠️

            This endpoint (POST /buckets/{id}/uploads) is the COMPLETE presigned URL system.
            It handles:
            - ✅ Presigned URL generation (S3 PUT URLs)
            - ✅ Upload tracking and status management
            - ✅ Validation (quotas, file size, content type, schema)
            - ✅ Duplicate detection
            - ✅ Auto object creation on confirmation
            - ✅ Returns upload_id for later reference

            DO NOT CREATE A NEW PRESIGNED UPLOAD ENDPOINT!
            If you need presigned URLs, use this existing system.

            If you think you need a new endpoint:
            1. Check if this system already does it (it probably does)
            2. Extend this system instead of creating redundancy
            3. See api/buckets/uploads/services.py for implementation

            Integration Points:
            - Object creation: Use upload_id in CreateBlobRequest.upload_id field
            - See: shared/buckets/objects/blobs/models.py::CreateBlobRequest
            - See: api/buckets/objects/canonicalization.py::resolve_upload_reference()

            Workflow:
            1. POST /buckets/{id}/uploads → Returns presigned_url + upload_id
            2. PUT presigned_url with file content (client uploads directly to S3)
            3. POST /uploads/{upload_id}/confirm → REQUIRED to finalize upload
            4. Object is created automatically (default behavior)

            ⚠️  IMPORTANT: Step 3 (confirm) is REQUIRED!
            S3 presigned URLs have no callback mechanism - the API cannot detect when
            your upload to S3 completes. You MUST call the confirm endpoint to:
            - Verify the file exists in S3
            - Validate integrity (ETag/size)
            - Create the bucket object
            - Mark upload as COMPLETED

            If you don't confirm:
            - Upload stays in PENDING status forever
            - No object is created
            - File exists in S3 but is orphaned
            - Presigned URL expires (default: 1 hour)

            Use Cases:
                - Simple: Upload → confirm → object created automatically (default)
                - Advanced: Upload multiple files with create_object_on_confirm=false,
                  then POST /buckets/{id}/objects with all upload_ids to create one object

            Requirements:
                - filename: REQUIRED, will be validated (no path traversal)
                - content_type: REQUIRED, must be valid MIME type
                - bucket_id: Comes from URL path parameter, not request body
                - All other fields: OPTIONAL with sensible defaults

            Note:
                The bucket_id comes from the URL path (/v1/buckets/{bucket_id}/uploads),
                not from the request body. The bucket is validated before generating presigned URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | UploadResponse
    """

    return sync_detailed(
        bucket_identifier=bucket_identifier,
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    bucket_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateUploadRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | UploadResponse]:
    """Create Upload

     Generate a presigned URL for direct S3 upload.

        This endpoint validates all requirements BEFORE generating the presigned URL,
        ensuring immediate feedback if something is wrong (bucket inactive, quota exceeded, etc.).

        **Duplicate Detection (Enabled by Default)**:
        - If `file_hash` provided and `skip_duplicates=true`: Checks for existing upload
        - If duplicate found: Returns existing upload (200 OK) with `is_duplicate=true`
        - If new file: Returns presigned URL (201 Created) with `is_duplicate=false`

        **Two-Step Flow**:
        1. Call this endpoint → Get presigned URL
        2. PUT file to presigned URL → Upload directly to S3
        3. Call confirm endpoint → Verify upload and create object

    Args:
        bucket_identifier (str): The unique identifier of the bucket
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateUploadRequest): Request to generate a presigned URL for direct S3 upload.

            ⚠️  ⚠️  ⚠️  THIS IS THE PRESIGNED URL SYSTEM ⚠️  ⚠️  ⚠️

            This endpoint (POST /buckets/{id}/uploads) is the COMPLETE presigned URL system.
            It handles:
            - ✅ Presigned URL generation (S3 PUT URLs)
            - ✅ Upload tracking and status management
            - ✅ Validation (quotas, file size, content type, schema)
            - ✅ Duplicate detection
            - ✅ Auto object creation on confirmation
            - ✅ Returns upload_id for later reference

            DO NOT CREATE A NEW PRESIGNED UPLOAD ENDPOINT!
            If you need presigned URLs, use this existing system.

            If you think you need a new endpoint:
            1. Check if this system already does it (it probably does)
            2. Extend this system instead of creating redundancy
            3. See api/buckets/uploads/services.py for implementation

            Integration Points:
            - Object creation: Use upload_id in CreateBlobRequest.upload_id field
            - See: shared/buckets/objects/blobs/models.py::CreateBlobRequest
            - See: api/buckets/objects/canonicalization.py::resolve_upload_reference()

            Workflow:
            1. POST /buckets/{id}/uploads → Returns presigned_url + upload_id
            2. PUT presigned_url with file content (client uploads directly to S3)
            3. POST /uploads/{upload_id}/confirm → REQUIRED to finalize upload
            4. Object is created automatically (default behavior)

            ⚠️  IMPORTANT: Step 3 (confirm) is REQUIRED!
            S3 presigned URLs have no callback mechanism - the API cannot detect when
            your upload to S3 completes. You MUST call the confirm endpoint to:
            - Verify the file exists in S3
            - Validate integrity (ETag/size)
            - Create the bucket object
            - Mark upload as COMPLETED

            If you don't confirm:
            - Upload stays in PENDING status forever
            - No object is created
            - File exists in S3 but is orphaned
            - Presigned URL expires (default: 1 hour)

            Use Cases:
                - Simple: Upload → confirm → object created automatically (default)
                - Advanced: Upload multiple files with create_object_on_confirm=false,
                  then POST /buckets/{id}/objects with all upload_ids to create one object

            Requirements:
                - filename: REQUIRED, will be validated (no path traversal)
                - content_type: REQUIRED, must be valid MIME type
                - bucket_id: Comes from URL path parameter, not request body
                - All other fields: OPTIONAL with sensible defaults

            Note:
                The bucket_id comes from the URL path (/v1/buckets/{bucket_id}/uploads),
                not from the request body. The bucket is validated before generating presigned URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | UploadResponse]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateUploadRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | UploadResponse | None:
    """Create Upload

     Generate a presigned URL for direct S3 upload.

        This endpoint validates all requirements BEFORE generating the presigned URL,
        ensuring immediate feedback if something is wrong (bucket inactive, quota exceeded, etc.).

        **Duplicate Detection (Enabled by Default)**:
        - If `file_hash` provided and `skip_duplicates=true`: Checks for existing upload
        - If duplicate found: Returns existing upload (200 OK) with `is_duplicate=true`
        - If new file: Returns presigned URL (201 Created) with `is_duplicate=false`

        **Two-Step Flow**:
        1. Call this endpoint → Get presigned URL
        2. PUT file to presigned URL → Upload directly to S3
        3. Call confirm endpoint → Verify upload and create object

    Args:
        bucket_identifier (str): The unique identifier of the bucket
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateUploadRequest): Request to generate a presigned URL for direct S3 upload.

            ⚠️  ⚠️  ⚠️  THIS IS THE PRESIGNED URL SYSTEM ⚠️  ⚠️  ⚠️

            This endpoint (POST /buckets/{id}/uploads) is the COMPLETE presigned URL system.
            It handles:
            - ✅ Presigned URL generation (S3 PUT URLs)
            - ✅ Upload tracking and status management
            - ✅ Validation (quotas, file size, content type, schema)
            - ✅ Duplicate detection
            - ✅ Auto object creation on confirmation
            - ✅ Returns upload_id for later reference

            DO NOT CREATE A NEW PRESIGNED UPLOAD ENDPOINT!
            If you need presigned URLs, use this existing system.

            If you think you need a new endpoint:
            1. Check if this system already does it (it probably does)
            2. Extend this system instead of creating redundancy
            3. See api/buckets/uploads/services.py for implementation

            Integration Points:
            - Object creation: Use upload_id in CreateBlobRequest.upload_id field
            - See: shared/buckets/objects/blobs/models.py::CreateBlobRequest
            - See: api/buckets/objects/canonicalization.py::resolve_upload_reference()

            Workflow:
            1. POST /buckets/{id}/uploads → Returns presigned_url + upload_id
            2. PUT presigned_url with file content (client uploads directly to S3)
            3. POST /uploads/{upload_id}/confirm → REQUIRED to finalize upload
            4. Object is created automatically (default behavior)

            ⚠️  IMPORTANT: Step 3 (confirm) is REQUIRED!
            S3 presigned URLs have no callback mechanism - the API cannot detect when
            your upload to S3 completes. You MUST call the confirm endpoint to:
            - Verify the file exists in S3
            - Validate integrity (ETag/size)
            - Create the bucket object
            - Mark upload as COMPLETED

            If you don't confirm:
            - Upload stays in PENDING status forever
            - No object is created
            - File exists in S3 but is orphaned
            - Presigned URL expires (default: 1 hour)

            Use Cases:
                - Simple: Upload → confirm → object created automatically (default)
                - Advanced: Upload multiple files with create_object_on_confirm=false,
                  then POST /buckets/{id}/objects with all upload_ids to create one object

            Requirements:
                - filename: REQUIRED, will be validated (no path traversal)
                - content_type: REQUIRED, must be valid MIME type
                - bucket_id: Comes from URL path parameter, not request body
                - All other fields: OPTIONAL with sensible defaults

            Note:
                The bucket_id comes from the URL path (/v1/buckets/{bucket_id}/uploads),
                not from the request body. The bucket is validated before generating presigned URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | UploadResponse
    """

    return (
        await asyncio_detailed(
            bucket_identifier=bucket_identifier,
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
