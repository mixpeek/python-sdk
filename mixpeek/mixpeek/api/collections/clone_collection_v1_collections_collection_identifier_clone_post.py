from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clone_collection_request import CloneCollectionRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_identifier: str,
    *,
    body: CloneCollectionRequest,
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
        "url": "/v1/collections/{collection_identifier}/clone".format(
            collection_identifier=quote(str(collection_identifier), safe=""),
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
    collection_identifier: str,
    *,
    client: AuthenticatedClient | Client,
    body: CloneCollectionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Clone Collection

     Clone a collection with optional modifications.

        **Purpose:**
        Creates a NEW collection (with new ID) based on an existing one. This is the
        recommended way to iterate on collection designs when you need to modify core
        configuration that PATCH doesn't allow (source, feature_extractor, field_passthrough).

        **Clone vs PATCH vs Template:**
        - **PATCH**: Update metadata only (enabled, metadata, taxonomy_applications)
        - **Clone**: Copy and modify core configuration (source, feature_extractor)
        - **Template**: Start from a pre-configured pattern (for new projects)

        **Common Use Cases:**
        - Change feature extractor configuration (model, parameters)
        - Modify field_passthrough to include/exclude fields
        - Switch to different source (bucket or collection)
        - Test modifications before replacing production collection
        - Create variants (e.g., different embedding models)

        **How it works:**
        1. Source collection is copied
        2. You provide a new name (REQUIRED)
        3. Optionally override any other fields
        4. A new collection is created with a new ID
        5. Original collection remains unchanged

    Args:
        collection_identifier (str): Source collection ID or name to clone.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CloneCollectionRequest): Request to clone a collection with optional modifications.

            **Purpose:**
            Cloning creates a NEW collection (with new ID) based on an existing one,
            allowing you to make changes that aren't allowed via PATCH (source,
            feature_extractor, field_passthrough). This is the recommended way to
            iterate on collection designs.

            **Clone vs Template vs Version:**
            - **Clone**: Copy THIS collection and modify it (for iteration/fixes)
            - **Template**: Create collection from a reusable pattern (for new projects)
            - **Version**: (Not implemented) - Use clone instead

            **Use Cases:**
            - Change feature extractor configuration without breaking production
            - Modify field_passthrough to include/exclude fields
            - Switch to different source (bucket or collection)
            - Test modifications before replacing production collection
            - Create variants (e.g., different embedding models)

            **All fields are OPTIONAL:**
            - Omit a field to keep the original value
            - Provide a field to override the original value
            - collection_name is REQUIRED (clones must have unique names)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
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
    body: CloneCollectionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Clone Collection

     Clone a collection with optional modifications.

        **Purpose:**
        Creates a NEW collection (with new ID) based on an existing one. This is the
        recommended way to iterate on collection designs when you need to modify core
        configuration that PATCH doesn't allow (source, feature_extractor, field_passthrough).

        **Clone vs PATCH vs Template:**
        - **PATCH**: Update metadata only (enabled, metadata, taxonomy_applications)
        - **Clone**: Copy and modify core configuration (source, feature_extractor)
        - **Template**: Start from a pre-configured pattern (for new projects)

        **Common Use Cases:**
        - Change feature extractor configuration (model, parameters)
        - Modify field_passthrough to include/exclude fields
        - Switch to different source (bucket or collection)
        - Test modifications before replacing production collection
        - Create variants (e.g., different embedding models)

        **How it works:**
        1. Source collection is copied
        2. You provide a new name (REQUIRED)
        3. Optionally override any other fields
        4. A new collection is created with a new ID
        5. Original collection remains unchanged

    Args:
        collection_identifier (str): Source collection ID or name to clone.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CloneCollectionRequest): Request to clone a collection with optional modifications.

            **Purpose:**
            Cloning creates a NEW collection (with new ID) based on an existing one,
            allowing you to make changes that aren't allowed via PATCH (source,
            feature_extractor, field_passthrough). This is the recommended way to
            iterate on collection designs.

            **Clone vs Template vs Version:**
            - **Clone**: Copy THIS collection and modify it (for iteration/fixes)
            - **Template**: Create collection from a reusable pattern (for new projects)
            - **Version**: (Not implemented) - Use clone instead

            **Use Cases:**
            - Change feature extractor configuration without breaking production
            - Modify field_passthrough to include/exclude fields
            - Switch to different source (bucket or collection)
            - Test modifications before replacing production collection
            - Create variants (e.g., different embedding models)

            **All fields are OPTIONAL:**
            - Omit a field to keep the original value
            - Provide a field to override the original value
            - collection_name is REQUIRED (clones must have unique names)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
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
    body: CloneCollectionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Clone Collection

     Clone a collection with optional modifications.

        **Purpose:**
        Creates a NEW collection (with new ID) based on an existing one. This is the
        recommended way to iterate on collection designs when you need to modify core
        configuration that PATCH doesn't allow (source, feature_extractor, field_passthrough).

        **Clone vs PATCH vs Template:**
        - **PATCH**: Update metadata only (enabled, metadata, taxonomy_applications)
        - **Clone**: Copy and modify core configuration (source, feature_extractor)
        - **Template**: Start from a pre-configured pattern (for new projects)

        **Common Use Cases:**
        - Change feature extractor configuration (model, parameters)
        - Modify field_passthrough to include/exclude fields
        - Switch to different source (bucket or collection)
        - Test modifications before replacing production collection
        - Create variants (e.g., different embedding models)

        **How it works:**
        1. Source collection is copied
        2. You provide a new name (REQUIRED)
        3. Optionally override any other fields
        4. A new collection is created with a new ID
        5. Original collection remains unchanged

    Args:
        collection_identifier (str): Source collection ID or name to clone.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CloneCollectionRequest): Request to clone a collection with optional modifications.

            **Purpose:**
            Cloning creates a NEW collection (with new ID) based on an existing one,
            allowing you to make changes that aren't allowed via PATCH (source,
            feature_extractor, field_passthrough). This is the recommended way to
            iterate on collection designs.

            **Clone vs Template vs Version:**
            - **Clone**: Copy THIS collection and modify it (for iteration/fixes)
            - **Template**: Create collection from a reusable pattern (for new projects)
            - **Version**: (Not implemented) - Use clone instead

            **Use Cases:**
            - Change feature extractor configuration without breaking production
            - Modify field_passthrough to include/exclude fields
            - Switch to different source (bucket or collection)
            - Test modifications before replacing production collection
            - Create variants (e.g., different embedding models)

            **All fields are OPTIONAL:**
            - Omit a field to keep the original value
            - Provide a field to override the original value
            - collection_name is REQUIRED (clones must have unique names)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
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
    body: CloneCollectionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Clone Collection

     Clone a collection with optional modifications.

        **Purpose:**
        Creates a NEW collection (with new ID) based on an existing one. This is the
        recommended way to iterate on collection designs when you need to modify core
        configuration that PATCH doesn't allow (source, feature_extractor, field_passthrough).

        **Clone vs PATCH vs Template:**
        - **PATCH**: Update metadata only (enabled, metadata, taxonomy_applications)
        - **Clone**: Copy and modify core configuration (source, feature_extractor)
        - **Template**: Start from a pre-configured pattern (for new projects)

        **Common Use Cases:**
        - Change feature extractor configuration (model, parameters)
        - Modify field_passthrough to include/exclude fields
        - Switch to different source (bucket or collection)
        - Test modifications before replacing production collection
        - Create variants (e.g., different embedding models)

        **How it works:**
        1. Source collection is copied
        2. You provide a new name (REQUIRED)
        3. Optionally override any other fields
        4. A new collection is created with a new ID
        5. Original collection remains unchanged

    Args:
        collection_identifier (str): Source collection ID or name to clone.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CloneCollectionRequest): Request to clone a collection with optional modifications.

            **Purpose:**
            Cloning creates a NEW collection (with new ID) based on an existing one,
            allowing you to make changes that aren't allowed via PATCH (source,
            feature_extractor, field_passthrough). This is the recommended way to
            iterate on collection designs.

            **Clone vs Template vs Version:**
            - **Clone**: Copy THIS collection and modify it (for iteration/fixes)
            - **Template**: Create collection from a reusable pattern (for new projects)
            - **Version**: (Not implemented) - Use clone instead

            **Use Cases:**
            - Change feature extractor configuration without breaking production
            - Modify field_passthrough to include/exclude fields
            - Switch to different source (bucket or collection)
            - Test modifications before replacing production collection
            - Create variants (e.g., different embedding models)

            **All fields are OPTIONAL:**
            - Omit a field to keep the original value
            - Provide a field to override the original value
            - collection_name is REQUIRED (clones must have unique names)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
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
