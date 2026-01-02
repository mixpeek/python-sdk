from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.patch_taxonomy_request import PatchTaxonomyRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    taxonomy_identifier: str,
    *,
    body: PatchTaxonomyRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/taxonomies/{taxonomy_identifier}".format(
            taxonomy_identifier=quote(str(taxonomy_identifier), safe=""),
        ),
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
    taxonomy_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchTaxonomyRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Partially Update Taxonomy

     Update a taxonomy's metadata.

        **Metadata Only Updates:**
        This endpoint allows updating ONLY metadata fields. Core taxonomy logic is immutable
        to ensure consistency for join history and dependent resources.

        **Fields You CAN Update:**
        - taxonomy_name: Rename the taxonomy
        - description: Update documentation
        - metadata: Update custom metadata

        **Fields You CANNOT Update:**
        - config: Taxonomy configuration (retriever_id, input_mappings, collections)
        - taxonomy_type: Type (flat vs hierarchical)

        **Need to Modify Core Logic?**
        Use POST /{taxonomy_identifier}/clone instead to modify configuration,
        retriever_id, input_mappings, or collections.

    Args:
        taxonomy_identifier (str): Taxonomy ID or name
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (PatchTaxonomyRequest): Request to update a taxonomy's metadata.

            **IMPORTANT: Partial Updates with Controlled Mutability**

            This endpoint allows updating ONLY metadata fields. Core taxonomy logic is immutable
            to ensure consistency for join history and dependent resources.

            **✅ Fields You CAN Update (Metadata Only):**
            - `taxonomy_name`: Rename the taxonomy
            - `description`: Update documentation
            - `metadata`: Update custom metadata fields

            **❌ Fields You CANNOT Update (Immutable Core Logic):**
            - `config`: Taxonomy configuration (retriever_id, input_mappings, collections, hierarchy)
            - `taxonomy_type`: Type (flat vs hierarchical)
            - `retriever_id`: Associated retriever
            - `input_mappings`: Field mappings
            - `enrichment_fields`: Enrichment configuration

            **Need to Modify Core Logic?**
            Use POST /taxonomies/{taxonomy_id}/clone instead. Cloning creates a new taxonomy
            with a new ID, allowing you to:
            - Change retriever or input mappings
            - Modify enrichment fields
            - Update collection configuration
            - Change taxonomy hierarchy

            **Behavior:**
            - All fields are OPTIONAL - provide only what you want to update
            - Empty updates (no fields provided) will be rejected with 400 error
            - Original taxonomy remains unchanged (no destructive operations)

            **Why This Design?**
            - Join history is tied to specific taxonomy configuration
            - Changing retriever would invalidate previous joins
            - Version tracking enables auditing and rollback

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        taxonomy_identifier=taxonomy_identifier,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    taxonomy_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchTaxonomyRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Partially Update Taxonomy

     Update a taxonomy's metadata.

        **Metadata Only Updates:**
        This endpoint allows updating ONLY metadata fields. Core taxonomy logic is immutable
        to ensure consistency for join history and dependent resources.

        **Fields You CAN Update:**
        - taxonomy_name: Rename the taxonomy
        - description: Update documentation
        - metadata: Update custom metadata

        **Fields You CANNOT Update:**
        - config: Taxonomy configuration (retriever_id, input_mappings, collections)
        - taxonomy_type: Type (flat vs hierarchical)

        **Need to Modify Core Logic?**
        Use POST /{taxonomy_identifier}/clone instead to modify configuration,
        retriever_id, input_mappings, or collections.

    Args:
        taxonomy_identifier (str): Taxonomy ID or name
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (PatchTaxonomyRequest): Request to update a taxonomy's metadata.

            **IMPORTANT: Partial Updates with Controlled Mutability**

            This endpoint allows updating ONLY metadata fields. Core taxonomy logic is immutable
            to ensure consistency for join history and dependent resources.

            **✅ Fields You CAN Update (Metadata Only):**
            - `taxonomy_name`: Rename the taxonomy
            - `description`: Update documentation
            - `metadata`: Update custom metadata fields

            **❌ Fields You CANNOT Update (Immutable Core Logic):**
            - `config`: Taxonomy configuration (retriever_id, input_mappings, collections, hierarchy)
            - `taxonomy_type`: Type (flat vs hierarchical)
            - `retriever_id`: Associated retriever
            - `input_mappings`: Field mappings
            - `enrichment_fields`: Enrichment configuration

            **Need to Modify Core Logic?**
            Use POST /taxonomies/{taxonomy_id}/clone instead. Cloning creates a new taxonomy
            with a new ID, allowing you to:
            - Change retriever or input mappings
            - Modify enrichment fields
            - Update collection configuration
            - Change taxonomy hierarchy

            **Behavior:**
            - All fields are OPTIONAL - provide only what you want to update
            - Empty updates (no fields provided) will be rejected with 400 error
            - Original taxonomy remains unchanged (no destructive operations)

            **Why This Design?**
            - Join history is tied to specific taxonomy configuration
            - Changing retriever would invalidate previous joins
            - Version tracking enables auditing and rollback

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        taxonomy_identifier=taxonomy_identifier,
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    taxonomy_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchTaxonomyRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Partially Update Taxonomy

     Update a taxonomy's metadata.

        **Metadata Only Updates:**
        This endpoint allows updating ONLY metadata fields. Core taxonomy logic is immutable
        to ensure consistency for join history and dependent resources.

        **Fields You CAN Update:**
        - taxonomy_name: Rename the taxonomy
        - description: Update documentation
        - metadata: Update custom metadata

        **Fields You CANNOT Update:**
        - config: Taxonomy configuration (retriever_id, input_mappings, collections)
        - taxonomy_type: Type (flat vs hierarchical)

        **Need to Modify Core Logic?**
        Use POST /{taxonomy_identifier}/clone instead to modify configuration,
        retriever_id, input_mappings, or collections.

    Args:
        taxonomy_identifier (str): Taxonomy ID or name
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (PatchTaxonomyRequest): Request to update a taxonomy's metadata.

            **IMPORTANT: Partial Updates with Controlled Mutability**

            This endpoint allows updating ONLY metadata fields. Core taxonomy logic is immutable
            to ensure consistency for join history and dependent resources.

            **✅ Fields You CAN Update (Metadata Only):**
            - `taxonomy_name`: Rename the taxonomy
            - `description`: Update documentation
            - `metadata`: Update custom metadata fields

            **❌ Fields You CANNOT Update (Immutable Core Logic):**
            - `config`: Taxonomy configuration (retriever_id, input_mappings, collections, hierarchy)
            - `taxonomy_type`: Type (flat vs hierarchical)
            - `retriever_id`: Associated retriever
            - `input_mappings`: Field mappings
            - `enrichment_fields`: Enrichment configuration

            **Need to Modify Core Logic?**
            Use POST /taxonomies/{taxonomy_id}/clone instead. Cloning creates a new taxonomy
            with a new ID, allowing you to:
            - Change retriever or input mappings
            - Modify enrichment fields
            - Update collection configuration
            - Change taxonomy hierarchy

            **Behavior:**
            - All fields are OPTIONAL - provide only what you want to update
            - Empty updates (no fields provided) will be rejected with 400 error
            - Original taxonomy remains unchanged (no destructive operations)

            **Why This Design?**
            - Join history is tied to specific taxonomy configuration
            - Changing retriever would invalidate previous joins
            - Version tracking enables auditing and rollback

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        taxonomy_identifier=taxonomy_identifier,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    taxonomy_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchTaxonomyRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Partially Update Taxonomy

     Update a taxonomy's metadata.

        **Metadata Only Updates:**
        This endpoint allows updating ONLY metadata fields. Core taxonomy logic is immutable
        to ensure consistency for join history and dependent resources.

        **Fields You CAN Update:**
        - taxonomy_name: Rename the taxonomy
        - description: Update documentation
        - metadata: Update custom metadata

        **Fields You CANNOT Update:**
        - config: Taxonomy configuration (retriever_id, input_mappings, collections)
        - taxonomy_type: Type (flat vs hierarchical)

        **Need to Modify Core Logic?**
        Use POST /{taxonomy_identifier}/clone instead to modify configuration,
        retriever_id, input_mappings, or collections.

    Args:
        taxonomy_identifier (str): Taxonomy ID or name
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (PatchTaxonomyRequest): Request to update a taxonomy's metadata.

            **IMPORTANT: Partial Updates with Controlled Mutability**

            This endpoint allows updating ONLY metadata fields. Core taxonomy logic is immutable
            to ensure consistency for join history and dependent resources.

            **✅ Fields You CAN Update (Metadata Only):**
            - `taxonomy_name`: Rename the taxonomy
            - `description`: Update documentation
            - `metadata`: Update custom metadata fields

            **❌ Fields You CANNOT Update (Immutable Core Logic):**
            - `config`: Taxonomy configuration (retriever_id, input_mappings, collections, hierarchy)
            - `taxonomy_type`: Type (flat vs hierarchical)
            - `retriever_id`: Associated retriever
            - `input_mappings`: Field mappings
            - `enrichment_fields`: Enrichment configuration

            **Need to Modify Core Logic?**
            Use POST /taxonomies/{taxonomy_id}/clone instead. Cloning creates a new taxonomy
            with a new ID, allowing you to:
            - Change retriever or input mappings
            - Modify enrichment fields
            - Update collection configuration
            - Change taxonomy hierarchy

            **Behavior:**
            - All fields are OPTIONAL - provide only what you want to update
            - Empty updates (no fields provided) will be rejected with 400 error
            - Original taxonomy remains unchanged (no destructive operations)

            **Why This Design?**
            - Join history is tied to specific taxonomy configuration
            - Changing retriever would invalidate previous joins
            - Version tracking enables auditing and rollback

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            taxonomy_identifier=taxonomy_identifier,
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
