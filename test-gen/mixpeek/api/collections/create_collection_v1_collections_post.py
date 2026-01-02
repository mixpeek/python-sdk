from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_collection_request import CreateCollectionRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateCollectionRequest,
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
        "url": "/v1/collections",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | None:
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
) -> Response[ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCollectionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Create Collection

     This endpoint allows you to create a new collection.

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateCollectionRequest): Request model for creating a new collection.

            Collections process data from buckets or other collections using a single feature
            extractor.

            KEY ARCHITECTURAL CHANGE: Each collection has EXACTLY ONE feature extractor.
            - Use field_passthrough to include additional source fields in output documents
            - Multiple extractors = multiple collections
            - This simplifies processing and makes output schema deterministic

            CRITICAL: To use input_mappings:
            1. Your source bucket MUST have a bucket_schema defined
            2. The input_mappings reference fields from that bucket_schema
            3. The system validates that mapped fields exist in the source schema

            Example workflow:
            1. Create bucket with schema: { "properties": { "image": {"type": "image"}, "title":
            {"type": "string"} } }
            2. Upload objects conforming to that schema
            3. Create collection with:
               - input_mappings: { "image": "image" }
               - field_passthrough: [{"source_path": "title"}]
            4. Output documents will have both extractor outputs AND passthrough fields

            Schema Computation:
            - output_schema is computed IMMEDIATELY when collection is created
            - output_schema = field_passthrough fields + extractor output fields
            - No waiting for documents to be processed!

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCollectionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Create Collection

     This endpoint allows you to create a new collection.

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateCollectionRequest): Request model for creating a new collection.

            Collections process data from buckets or other collections using a single feature
            extractor.

            KEY ARCHITECTURAL CHANGE: Each collection has EXACTLY ONE feature extractor.
            - Use field_passthrough to include additional source fields in output documents
            - Multiple extractors = multiple collections
            - This simplifies processing and makes output schema deterministic

            CRITICAL: To use input_mappings:
            1. Your source bucket MUST have a bucket_schema defined
            2. The input_mappings reference fields from that bucket_schema
            3. The system validates that mapped fields exist in the source schema

            Example workflow:
            1. Create bucket with schema: { "properties": { "image": {"type": "image"}, "title":
            {"type": "string"} } }
            2. Upload objects conforming to that schema
            3. Create collection with:
               - input_mappings: { "image": "image" }
               - field_passthrough: [{"source_path": "title"}]
            4. Output documents will have both extractor outputs AND passthrough fields

            Schema Computation:
            - output_schema is computed IMMEDIATELY when collection is created
            - output_schema = field_passthrough fields + extractor output fields
            - No waiting for documents to be processed!

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCollectionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Create Collection

     This endpoint allows you to create a new collection.

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateCollectionRequest): Request model for creating a new collection.

            Collections process data from buckets or other collections using a single feature
            extractor.

            KEY ARCHITECTURAL CHANGE: Each collection has EXACTLY ONE feature extractor.
            - Use field_passthrough to include additional source fields in output documents
            - Multiple extractors = multiple collections
            - This simplifies processing and makes output schema deterministic

            CRITICAL: To use input_mappings:
            1. Your source bucket MUST have a bucket_schema defined
            2. The input_mappings reference fields from that bucket_schema
            3. The system validates that mapped fields exist in the source schema

            Example workflow:
            1. Create bucket with schema: { "properties": { "image": {"type": "image"}, "title":
            {"type": "string"} } }
            2. Upload objects conforming to that schema
            3. Create collection with:
               - input_mappings: { "image": "image" }
               - field_passthrough: [{"source_path": "title"}]
            4. Output documents will have both extractor outputs AND passthrough fields

            Schema Computation:
            - output_schema is computed IMMEDIATELY when collection is created
            - output_schema = field_passthrough fields + extractor output fields
            - No waiting for documents to be processed!

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateCollectionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Create Collection

     This endpoint allows you to create a new collection.

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateCollectionRequest): Request model for creating a new collection.

            Collections process data from buckets or other collections using a single feature
            extractor.

            KEY ARCHITECTURAL CHANGE: Each collection has EXACTLY ONE feature extractor.
            - Use field_passthrough to include additional source fields in output documents
            - Multiple extractors = multiple collections
            - This simplifies processing and makes output schema deterministic

            CRITICAL: To use input_mappings:
            1. Your source bucket MUST have a bucket_schema defined
            2. The input_mappings reference fields from that bucket_schema
            3. The system validates that mapped fields exist in the source schema

            Example workflow:
            1. Create bucket with schema: { "properties": { "image": {"type": "image"}, "title":
            {"type": "string"} } }
            2. Upload objects conforming to that schema
            3. Create collection with:
               - input_mappings: { "image": "image" }
               - field_passthrough: [{"source_path": "title"}]
            4. Output documents will have both extractor outputs AND passthrough fields

            Schema Computation:
            - output_schema is computed IMMEDIATELY when collection is created
            - output_schema = field_passthrough fields + extractor output fields
            - No waiting for documents to be processed!

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
