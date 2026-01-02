from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clone_taxonomy_request import CloneTaxonomyRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    taxonomy_identifier: str,
    *,
    body: CloneTaxonomyRequest,
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
        "url": "/v1/taxonomies/{taxonomy_identifier}/clone".format(
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
    body: CloneTaxonomyRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Clone Taxonomy

     Clone a taxonomy with optional modifications.

        **Purpose:**
        Creates a NEW taxonomy (with new ID) based on an existing one. This is the
        recommended way to iterate on taxonomy designs when you need to modify core
        logic that PATCH doesn't allow (config, retriever_id, input_mappings).

        **Clone vs PATCH vs Template:**
        - **PATCH**: Update metadata only (name, description, metadata)
        - **Clone**: Copy and modify core logic (config, retriever, collections)
        - **Template**: Start from a pre-configured pattern (for new projects)

        **Common Use Cases:**
        - Fix configuration errors without losing join history
        - Change retriever or input mappings
        - Modify enrichment fields or collection configuration
        - Test modifications before replacing production taxonomy
        - Create variants for different datasets

        **How it works:**
        1. Source taxonomy is copied
        2. You provide a new name (REQUIRED)
        3. Optionally override any other fields (description, config)
        4. A new taxonomy is created with a new ID
        5. Original taxonomy remains unchanged

    Args:
        taxonomy_identifier (str): Source taxonomy ID or name to clone.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CloneTaxonomyRequest): Request to clone a taxonomy with optional modifications.

            **Purpose:**
            Cloning creates a NEW taxonomy (with new ID) based on an existing one,
            allowing you to make changes that aren't allowed via PATCH (config,
            retriever_id, collections). This is the recommended way to iterate on
            taxonomy designs.

            **Clone vs Template vs Version:**
            - **Clone**: Copy THIS taxonomy and modify it (for iteration/fixes)
            - **Template**: Create taxonomy from a reusable pattern (for new projects)
            - **Version**: (Not implemented) - Use clone instead

            **Use Cases:**
            - Fix configuration errors without losing join history
            - Change retriever or input mappings
            - Change target collections
            - Test modifications before replacing production taxonomy
            - Create variants for different datasets

            **All fields are OPTIONAL:**
            - Omit a field to keep the original value
            - Provide a field to override the original value
            - taxonomy_name is REQUIRED (clones must have unique names)

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
    body: CloneTaxonomyRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Clone Taxonomy

     Clone a taxonomy with optional modifications.

        **Purpose:**
        Creates a NEW taxonomy (with new ID) based on an existing one. This is the
        recommended way to iterate on taxonomy designs when you need to modify core
        logic that PATCH doesn't allow (config, retriever_id, input_mappings).

        **Clone vs PATCH vs Template:**
        - **PATCH**: Update metadata only (name, description, metadata)
        - **Clone**: Copy and modify core logic (config, retriever, collections)
        - **Template**: Start from a pre-configured pattern (for new projects)

        **Common Use Cases:**
        - Fix configuration errors without losing join history
        - Change retriever or input mappings
        - Modify enrichment fields or collection configuration
        - Test modifications before replacing production taxonomy
        - Create variants for different datasets

        **How it works:**
        1. Source taxonomy is copied
        2. You provide a new name (REQUIRED)
        3. Optionally override any other fields (description, config)
        4. A new taxonomy is created with a new ID
        5. Original taxonomy remains unchanged

    Args:
        taxonomy_identifier (str): Source taxonomy ID or name to clone.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CloneTaxonomyRequest): Request to clone a taxonomy with optional modifications.

            **Purpose:**
            Cloning creates a NEW taxonomy (with new ID) based on an existing one,
            allowing you to make changes that aren't allowed via PATCH (config,
            retriever_id, collections). This is the recommended way to iterate on
            taxonomy designs.

            **Clone vs Template vs Version:**
            - **Clone**: Copy THIS taxonomy and modify it (for iteration/fixes)
            - **Template**: Create taxonomy from a reusable pattern (for new projects)
            - **Version**: (Not implemented) - Use clone instead

            **Use Cases:**
            - Fix configuration errors without losing join history
            - Change retriever or input mappings
            - Change target collections
            - Test modifications before replacing production taxonomy
            - Create variants for different datasets

            **All fields are OPTIONAL:**
            - Omit a field to keep the original value
            - Provide a field to override the original value
            - taxonomy_name is REQUIRED (clones must have unique names)

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
    body: CloneTaxonomyRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Clone Taxonomy

     Clone a taxonomy with optional modifications.

        **Purpose:**
        Creates a NEW taxonomy (with new ID) based on an existing one. This is the
        recommended way to iterate on taxonomy designs when you need to modify core
        logic that PATCH doesn't allow (config, retriever_id, input_mappings).

        **Clone vs PATCH vs Template:**
        - **PATCH**: Update metadata only (name, description, metadata)
        - **Clone**: Copy and modify core logic (config, retriever, collections)
        - **Template**: Start from a pre-configured pattern (for new projects)

        **Common Use Cases:**
        - Fix configuration errors without losing join history
        - Change retriever or input mappings
        - Modify enrichment fields or collection configuration
        - Test modifications before replacing production taxonomy
        - Create variants for different datasets

        **How it works:**
        1. Source taxonomy is copied
        2. You provide a new name (REQUIRED)
        3. Optionally override any other fields (description, config)
        4. A new taxonomy is created with a new ID
        5. Original taxonomy remains unchanged

    Args:
        taxonomy_identifier (str): Source taxonomy ID or name to clone.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CloneTaxonomyRequest): Request to clone a taxonomy with optional modifications.

            **Purpose:**
            Cloning creates a NEW taxonomy (with new ID) based on an existing one,
            allowing you to make changes that aren't allowed via PATCH (config,
            retriever_id, collections). This is the recommended way to iterate on
            taxonomy designs.

            **Clone vs Template vs Version:**
            - **Clone**: Copy THIS taxonomy and modify it (for iteration/fixes)
            - **Template**: Create taxonomy from a reusable pattern (for new projects)
            - **Version**: (Not implemented) - Use clone instead

            **Use Cases:**
            - Fix configuration errors without losing join history
            - Change retriever or input mappings
            - Change target collections
            - Test modifications before replacing production taxonomy
            - Create variants for different datasets

            **All fields are OPTIONAL:**
            - Omit a field to keep the original value
            - Provide a field to override the original value
            - taxonomy_name is REQUIRED (clones must have unique names)

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
    body: CloneTaxonomyRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Clone Taxonomy

     Clone a taxonomy with optional modifications.

        **Purpose:**
        Creates a NEW taxonomy (with new ID) based on an existing one. This is the
        recommended way to iterate on taxonomy designs when you need to modify core
        logic that PATCH doesn't allow (config, retriever_id, input_mappings).

        **Clone vs PATCH vs Template:**
        - **PATCH**: Update metadata only (name, description, metadata)
        - **Clone**: Copy and modify core logic (config, retriever, collections)
        - **Template**: Start from a pre-configured pattern (for new projects)

        **Common Use Cases:**
        - Fix configuration errors without losing join history
        - Change retriever or input mappings
        - Modify enrichment fields or collection configuration
        - Test modifications before replacing production taxonomy
        - Create variants for different datasets

        **How it works:**
        1. Source taxonomy is copied
        2. You provide a new name (REQUIRED)
        3. Optionally override any other fields (description, config)
        4. A new taxonomy is created with a new ID
        5. Original taxonomy remains unchanged

    Args:
        taxonomy_identifier (str): Source taxonomy ID or name to clone.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CloneTaxonomyRequest): Request to clone a taxonomy with optional modifications.

            **Purpose:**
            Cloning creates a NEW taxonomy (with new ID) based on an existing one,
            allowing you to make changes that aren't allowed via PATCH (config,
            retriever_id, collections). This is the recommended way to iterate on
            taxonomy designs.

            **Clone vs Template vs Version:**
            - **Clone**: Copy THIS taxonomy and modify it (for iteration/fixes)
            - **Template**: Create taxonomy from a reusable pattern (for new projects)
            - **Version**: (Not implemented) - Use clone instead

            **Use Cases:**
            - Fix configuration errors without losing join history
            - Change retriever or input mappings
            - Change target collections
            - Test modifications before replacing production taxonomy
            - Create variants for different datasets

            **All fields are OPTIONAL:**
            - Omit a field to keep the original value
            - Provide a field to override the original value
            - taxonomy_name is REQUIRED (clones must have unique names)

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
