from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_object_request import CreateObjectRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.object_response import ObjectResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bucket_identifier: str,
    *,
    body: CreateObjectRequest,
    policy: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    json_policy: None | str | Unset
    if isinstance(policy, Unset):
        json_policy = UNSET
    else:
        json_policy = policy
    params["policy"] = json_policy

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/buckets/{bucket_identifier}/objects".format(
            bucket_identifier=quote(str(bucket_identifier), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | ObjectResponse | None:
    if response.status_code == 200:
        response_200 = ObjectResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | ObjectResponse]:
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
    body: CreateObjectRequest,
    policy: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ObjectResponse]:
    """Create Object

     This endpoint creates a new object in the specified bucket.
        The object must conform to the bucket's schema. It does not trigger processing.

        If the bucket has a unique_key configured, the insertion policy determines behavior:
        - insert: Create only. Fail with 409 Conflict if unique key exists.
        - update: Update only. Fail with 404 Not Found if unique key doesn't exist.
        - upsert: Create if new, update if exists (idempotent).

        Policy resolution:
        1. Use ?policy= query parameter if provided
        2. Fall back to bucket's default_policy if configured
        3. Error 400 if neither is specified

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        policy (None | str | Unset): Insertion policy for unique key enforcement. Valid values:
            'insert', 'update', 'upsert'. Only applies if bucket has unique_key configured. Overrides
            bucket's default_policy if provided.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateObjectRequest): Request model for creating a bucket object.

            Objects can be created with blobs from two sources:
            1. Direct data (URLs, base64) - Use CreateBlobRequest.data field
            2. Upload references - Use CreateBlobRequest.upload_id field (from POST
            /buckets/{id}/uploads)

            Upload Reference Workflow:
                For large files or client-side uploads, use the presigned URL workflow:
                1. POST /buckets/{id}/uploads → Returns {upload_id, presigned_url}
                2. User uploads file to presigned_url (client-side)
                3. POST /uploads/{upload_id}/confirm → Validates upload
                4. POST /buckets/{id}/objects with upload_id in blobs (this endpoint)

            Use Cases:
                - Single blob with direct data (simple)
                - Multiple blobs from presigned uploads (recommended for large files)
                - Mix of direct data and upload references
                - Combine multiple uploads into one object

            See Also:
                - CreateBlobRequest for blob field documentation
                - POST /buckets/{id}/uploads for presigned URL generation Example: {'blobs': [{'data':
            {'num_pages': 5, 'title': 'Service Agreement 2024'}, 'key_prefix':
            '/contract-2024/content.pdf', 'metadata': {'author': 'John Doe', 'department': 'Legal'},
            'property': 'content', 'type': 'json'}, {'data': {'filename':
            'https://example.com/images/smartphone-x1.jpg', 'mime_type': 'image/jpeg'}, 'key_prefix':
            '/contract-2024/thumbnail.jpg', 'metadata': {'height': 300, 'width': 200}, 'property':
            'thumbnail', 'type': 'image'}], 'key_prefix': '/documents', 'metadata': {'category':
            'contracts', 'status': 'draft', 'year': 2024}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ObjectResponse]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        body=body,
        policy=policy,
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
    body: CreateObjectRequest,
    policy: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ObjectResponse | None:
    """Create Object

     This endpoint creates a new object in the specified bucket.
        The object must conform to the bucket's schema. It does not trigger processing.

        If the bucket has a unique_key configured, the insertion policy determines behavior:
        - insert: Create only. Fail with 409 Conflict if unique key exists.
        - update: Update only. Fail with 404 Not Found if unique key doesn't exist.
        - upsert: Create if new, update if exists (idempotent).

        Policy resolution:
        1. Use ?policy= query parameter if provided
        2. Fall back to bucket's default_policy if configured
        3. Error 400 if neither is specified

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        policy (None | str | Unset): Insertion policy for unique key enforcement. Valid values:
            'insert', 'update', 'upsert'. Only applies if bucket has unique_key configured. Overrides
            bucket's default_policy if provided.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateObjectRequest): Request model for creating a bucket object.

            Objects can be created with blobs from two sources:
            1. Direct data (URLs, base64) - Use CreateBlobRequest.data field
            2. Upload references - Use CreateBlobRequest.upload_id field (from POST
            /buckets/{id}/uploads)

            Upload Reference Workflow:
                For large files or client-side uploads, use the presigned URL workflow:
                1. POST /buckets/{id}/uploads → Returns {upload_id, presigned_url}
                2. User uploads file to presigned_url (client-side)
                3. POST /uploads/{upload_id}/confirm → Validates upload
                4. POST /buckets/{id}/objects with upload_id in blobs (this endpoint)

            Use Cases:
                - Single blob with direct data (simple)
                - Multiple blobs from presigned uploads (recommended for large files)
                - Mix of direct data and upload references
                - Combine multiple uploads into one object

            See Also:
                - CreateBlobRequest for blob field documentation
                - POST /buckets/{id}/uploads for presigned URL generation Example: {'blobs': [{'data':
            {'num_pages': 5, 'title': 'Service Agreement 2024'}, 'key_prefix':
            '/contract-2024/content.pdf', 'metadata': {'author': 'John Doe', 'department': 'Legal'},
            'property': 'content', 'type': 'json'}, {'data': {'filename':
            'https://example.com/images/smartphone-x1.jpg', 'mime_type': 'image/jpeg'}, 'key_prefix':
            '/contract-2024/thumbnail.jpg', 'metadata': {'height': 300, 'width': 200}, 'property':
            'thumbnail', 'type': 'image'}], 'key_prefix': '/documents', 'metadata': {'category':
            'contracts', 'status': 'draft', 'year': 2024}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ObjectResponse
    """

    return sync_detailed(
        bucket_identifier=bucket_identifier,
        client=client,
        body=body,
        policy=policy,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    bucket_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateObjectRequest,
    policy: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ObjectResponse]:
    """Create Object

     This endpoint creates a new object in the specified bucket.
        The object must conform to the bucket's schema. It does not trigger processing.

        If the bucket has a unique_key configured, the insertion policy determines behavior:
        - insert: Create only. Fail with 409 Conflict if unique key exists.
        - update: Update only. Fail with 404 Not Found if unique key doesn't exist.
        - upsert: Create if new, update if exists (idempotent).

        Policy resolution:
        1. Use ?policy= query parameter if provided
        2. Fall back to bucket's default_policy if configured
        3. Error 400 if neither is specified

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        policy (None | str | Unset): Insertion policy for unique key enforcement. Valid values:
            'insert', 'update', 'upsert'. Only applies if bucket has unique_key configured. Overrides
            bucket's default_policy if provided.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateObjectRequest): Request model for creating a bucket object.

            Objects can be created with blobs from two sources:
            1. Direct data (URLs, base64) - Use CreateBlobRequest.data field
            2. Upload references - Use CreateBlobRequest.upload_id field (from POST
            /buckets/{id}/uploads)

            Upload Reference Workflow:
                For large files or client-side uploads, use the presigned URL workflow:
                1. POST /buckets/{id}/uploads → Returns {upload_id, presigned_url}
                2. User uploads file to presigned_url (client-side)
                3. POST /uploads/{upload_id}/confirm → Validates upload
                4. POST /buckets/{id}/objects with upload_id in blobs (this endpoint)

            Use Cases:
                - Single blob with direct data (simple)
                - Multiple blobs from presigned uploads (recommended for large files)
                - Mix of direct data and upload references
                - Combine multiple uploads into one object

            See Also:
                - CreateBlobRequest for blob field documentation
                - POST /buckets/{id}/uploads for presigned URL generation Example: {'blobs': [{'data':
            {'num_pages': 5, 'title': 'Service Agreement 2024'}, 'key_prefix':
            '/contract-2024/content.pdf', 'metadata': {'author': 'John Doe', 'department': 'Legal'},
            'property': 'content', 'type': 'json'}, {'data': {'filename':
            'https://example.com/images/smartphone-x1.jpg', 'mime_type': 'image/jpeg'}, 'key_prefix':
            '/contract-2024/thumbnail.jpg', 'metadata': {'height': 300, 'width': 200}, 'property':
            'thumbnail', 'type': 'image'}], 'key_prefix': '/documents', 'metadata': {'category':
            'contracts', 'status': 'draft', 'year': 2024}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ObjectResponse]
    """

    kwargs = _get_kwargs(
        bucket_identifier=bucket_identifier,
        body=body,
        policy=policy,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bucket_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateObjectRequest,
    policy: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ObjectResponse | None:
    """Create Object

     This endpoint creates a new object in the specified bucket.
        The object must conform to the bucket's schema. It does not trigger processing.

        If the bucket has a unique_key configured, the insertion policy determines behavior:
        - insert: Create only. Fail with 409 Conflict if unique key exists.
        - update: Update only. Fail with 404 Not Found if unique key doesn't exist.
        - upsert: Create if new, update if exists (idempotent).

        Policy resolution:
        1. Use ?policy= query parameter if provided
        2. Fall back to bucket's default_policy if configured
        3. Error 400 if neither is specified

    Args:
        bucket_identifier (str): The unique identifier of the bucket.
        policy (None | str | Unset): Insertion policy for unique key enforcement. Valid values:
            'insert', 'update', 'upsert'. Only applies if bucket has unique_key configured. Overrides
            bucket's default_policy if provided.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateObjectRequest): Request model for creating a bucket object.

            Objects can be created with blobs from two sources:
            1. Direct data (URLs, base64) - Use CreateBlobRequest.data field
            2. Upload references - Use CreateBlobRequest.upload_id field (from POST
            /buckets/{id}/uploads)

            Upload Reference Workflow:
                For large files or client-side uploads, use the presigned URL workflow:
                1. POST /buckets/{id}/uploads → Returns {upload_id, presigned_url}
                2. User uploads file to presigned_url (client-side)
                3. POST /uploads/{upload_id}/confirm → Validates upload
                4. POST /buckets/{id}/objects with upload_id in blobs (this endpoint)

            Use Cases:
                - Single blob with direct data (simple)
                - Multiple blobs from presigned uploads (recommended for large files)
                - Mix of direct data and upload references
                - Combine multiple uploads into one object

            See Also:
                - CreateBlobRequest for blob field documentation
                - POST /buckets/{id}/uploads for presigned URL generation Example: {'blobs': [{'data':
            {'num_pages': 5, 'title': 'Service Agreement 2024'}, 'key_prefix':
            '/contract-2024/content.pdf', 'metadata': {'author': 'John Doe', 'department': 'Legal'},
            'property': 'content', 'type': 'json'}, {'data': {'filename':
            'https://example.com/images/smartphone-x1.jpg', 'mime_type': 'image/jpeg'}, 'key_prefix':
            '/contract-2024/thumbnail.jpg', 'metadata': {'height': 300, 'width': 200}, 'property':
            'thumbnail', 'type': 'image'}], 'key_prefix': '/documents', 'metadata': {'category':
            'contracts', 'status': 'draft', 'year': 2024}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ObjectResponse
    """

    return (
        await asyncio_detailed(
            bucket_identifier=bucket_identifier,
            client=client,
            body=body,
            policy=policy,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
