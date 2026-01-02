from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clone_retriever_request import CloneRetrieverRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    retriever_id: str,
    *,
    body: CloneRetrieverRequest,
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
        "url": "/v1/retrievers/{retriever_id}/clone".format(
            retriever_id=quote(str(retriever_id), safe=""),
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
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CloneRetrieverRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    r"""Clone Retriever

     Clone a retriever with optional modifications.

    **Purpose:**
    Creates a NEW retriever (with new ID) based on an existing one. This is the
    recommended way to iterate on retriever designs when you need to modify core
    logic that PATCH doesn't allow (stages, input_schema, collections).

    **Clone vs PATCH vs Template:**
    - **PATCH**: Update metadata only (name, description, tags, display_config)
    - **Clone**: Copy and modify core logic (stages, input_schema, collections)
    - **Template**: Start from a pre-configured pattern (for new projects)

    **Common Use Cases:**
    - Fix a typo in a stage name
    - Add or remove stages
    - Change target collections
    - Create variants (e.g., \"strict\" vs \"relaxed\" versions)
    - Test modifications before replacing production retriever

    **How it works:**
    1. Source retriever is copied
    2. You provide a new name (REQUIRED)
    3. Optionally override any other fields
    4. A new retriever is created with a new ID
    5. Original retriever remains unchanged

    **All fields except retriever_name are OPTIONAL:**
    - Omit a field to copy from source
    - Provide a field to override the source value

    Args:
        retriever_id (str): Source retriever ID or name to clone.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CloneRetrieverRequest): Request to clone a retriever with optional modifications.

            **Purpose:**
            Cloning creates a NEW retriever (with new ID) based on an existing one,
            allowing you to make changes that aren't allowed via PATCH (stages,
            input_schema, collections). This is the recommended way to iterate on
            retriever designs.

            **Clone vs Template vs Version:**
            - **Clone**: Copy THIS retriever and modify it (for iteration/fixes)
            - **Template**: Create retriever from a reusable pattern (for new projects)
            - **Version**: (Not implemented) - Use clone instead

            **Use Cases:**
            - Fix a typo in a stage name without losing execution history
            - Add/remove stages while keeping the original intact
            - Change collections while preserving the original retriever
            - Test modifications before replacing production retriever
            - Create variants (e.g., "strict" vs "relaxed" versions)

            **All fields are OPTIONAL:**
            - Omit a field to keep the original value
            - Provide a field to override the original value
            - retriever_name is REQUIRED (clones must have unique names)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        retriever_id=retriever_id,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CloneRetrieverRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    r"""Clone Retriever

     Clone a retriever with optional modifications.

    **Purpose:**
    Creates a NEW retriever (with new ID) based on an existing one. This is the
    recommended way to iterate on retriever designs when you need to modify core
    logic that PATCH doesn't allow (stages, input_schema, collections).

    **Clone vs PATCH vs Template:**
    - **PATCH**: Update metadata only (name, description, tags, display_config)
    - **Clone**: Copy and modify core logic (stages, input_schema, collections)
    - **Template**: Start from a pre-configured pattern (for new projects)

    **Common Use Cases:**
    - Fix a typo in a stage name
    - Add or remove stages
    - Change target collections
    - Create variants (e.g., \"strict\" vs \"relaxed\" versions)
    - Test modifications before replacing production retriever

    **How it works:**
    1. Source retriever is copied
    2. You provide a new name (REQUIRED)
    3. Optionally override any other fields
    4. A new retriever is created with a new ID
    5. Original retriever remains unchanged

    **All fields except retriever_name are OPTIONAL:**
    - Omit a field to copy from source
    - Provide a field to override the source value

    Args:
        retriever_id (str): Source retriever ID or name to clone.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CloneRetrieverRequest): Request to clone a retriever with optional modifications.

            **Purpose:**
            Cloning creates a NEW retriever (with new ID) based on an existing one,
            allowing you to make changes that aren't allowed via PATCH (stages,
            input_schema, collections). This is the recommended way to iterate on
            retriever designs.

            **Clone vs Template vs Version:**
            - **Clone**: Copy THIS retriever and modify it (for iteration/fixes)
            - **Template**: Create retriever from a reusable pattern (for new projects)
            - **Version**: (Not implemented) - Use clone instead

            **Use Cases:**
            - Fix a typo in a stage name without losing execution history
            - Add/remove stages while keeping the original intact
            - Change collections while preserving the original retriever
            - Test modifications before replacing production retriever
            - Create variants (e.g., "strict" vs "relaxed" versions)

            **All fields are OPTIONAL:**
            - Omit a field to keep the original value
            - Provide a field to override the original value
            - retriever_name is REQUIRED (clones must have unique names)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        retriever_id=retriever_id,
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CloneRetrieverRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    r"""Clone Retriever

     Clone a retriever with optional modifications.

    **Purpose:**
    Creates a NEW retriever (with new ID) based on an existing one. This is the
    recommended way to iterate on retriever designs when you need to modify core
    logic that PATCH doesn't allow (stages, input_schema, collections).

    **Clone vs PATCH vs Template:**
    - **PATCH**: Update metadata only (name, description, tags, display_config)
    - **Clone**: Copy and modify core logic (stages, input_schema, collections)
    - **Template**: Start from a pre-configured pattern (for new projects)

    **Common Use Cases:**
    - Fix a typo in a stage name
    - Add or remove stages
    - Change target collections
    - Create variants (e.g., \"strict\" vs \"relaxed\" versions)
    - Test modifications before replacing production retriever

    **How it works:**
    1. Source retriever is copied
    2. You provide a new name (REQUIRED)
    3. Optionally override any other fields
    4. A new retriever is created with a new ID
    5. Original retriever remains unchanged

    **All fields except retriever_name are OPTIONAL:**
    - Omit a field to copy from source
    - Provide a field to override the source value

    Args:
        retriever_id (str): Source retriever ID or name to clone.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CloneRetrieverRequest): Request to clone a retriever with optional modifications.

            **Purpose:**
            Cloning creates a NEW retriever (with new ID) based on an existing one,
            allowing you to make changes that aren't allowed via PATCH (stages,
            input_schema, collections). This is the recommended way to iterate on
            retriever designs.

            **Clone vs Template vs Version:**
            - **Clone**: Copy THIS retriever and modify it (for iteration/fixes)
            - **Template**: Create retriever from a reusable pattern (for new projects)
            - **Version**: (Not implemented) - Use clone instead

            **Use Cases:**
            - Fix a typo in a stage name without losing execution history
            - Add/remove stages while keeping the original intact
            - Change collections while preserving the original retriever
            - Test modifications before replacing production retriever
            - Create variants (e.g., "strict" vs "relaxed" versions)

            **All fields are OPTIONAL:**
            - Omit a field to keep the original value
            - Provide a field to override the original value
            - retriever_name is REQUIRED (clones must have unique names)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        retriever_id=retriever_id,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CloneRetrieverRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    r"""Clone Retriever

     Clone a retriever with optional modifications.

    **Purpose:**
    Creates a NEW retriever (with new ID) based on an existing one. This is the
    recommended way to iterate on retriever designs when you need to modify core
    logic that PATCH doesn't allow (stages, input_schema, collections).

    **Clone vs PATCH vs Template:**
    - **PATCH**: Update metadata only (name, description, tags, display_config)
    - **Clone**: Copy and modify core logic (stages, input_schema, collections)
    - **Template**: Start from a pre-configured pattern (for new projects)

    **Common Use Cases:**
    - Fix a typo in a stage name
    - Add or remove stages
    - Change target collections
    - Create variants (e.g., \"strict\" vs \"relaxed\" versions)
    - Test modifications before replacing production retriever

    **How it works:**
    1. Source retriever is copied
    2. You provide a new name (REQUIRED)
    3. Optionally override any other fields
    4. A new retriever is created with a new ID
    5. Original retriever remains unchanged

    **All fields except retriever_name are OPTIONAL:**
    - Omit a field to copy from source
    - Provide a field to override the source value

    Args:
        retriever_id (str): Source retriever ID or name to clone.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CloneRetrieverRequest): Request to clone a retriever with optional modifications.

            **Purpose:**
            Cloning creates a NEW retriever (with new ID) based on an existing one,
            allowing you to make changes that aren't allowed via PATCH (stages,
            input_schema, collections). This is the recommended way to iterate on
            retriever designs.

            **Clone vs Template vs Version:**
            - **Clone**: Copy THIS retriever and modify it (for iteration/fixes)
            - **Template**: Create retriever from a reusable pattern (for new projects)
            - **Version**: (Not implemented) - Use clone instead

            **Use Cases:**
            - Fix a typo in a stage name without losing execution history
            - Add/remove stages while keeping the original intact
            - Change collections while preserving the original retriever
            - Test modifications before replacing production retriever
            - Create variants (e.g., "strict" vs "relaxed" versions)

            **All fields are OPTIONAL:**
            - Omit a field to keep the original value
            - Provide a field to override the original value
            - retriever_name is REQUIRED (clones must have unique names)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            retriever_id=retriever_id,
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
