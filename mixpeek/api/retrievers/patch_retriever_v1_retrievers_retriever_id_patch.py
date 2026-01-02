from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.patch_retriever_request import PatchRetrieverRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    retriever_id: str,
    *,
    body: PatchRetrieverRequest,
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
        "url": "/v1/retrievers/{retriever_id}".format(
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
    body: PatchRetrieverRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Patch Retriever

     Update a retriever's metadata.

    Only metadata fields can be updated:
    - name: Rename the retriever
    - description: Update the description
    - tags: Update tags for organization
    - display_config: Update display configuration

    Core logic (input_schema, stages, collection_ids) is immutable.
    To modify core logic, use POST /{retriever_id}/clone instead.

    Args:
        retriever_id (str): Retriever ID or name.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (PatchRetrieverRequest): Request to update a retriever's metadata.

            **IMPORTANT: Partial Updates with Controlled Mutability**

            This endpoint allows updating ONLY metadata fields. Core retriever logic is immutable
            to ensure consistency for dependent resources (taxonomies, cached results, etc.).

            **✅ Fields You CAN Update (Metadata Only):**
            - `retriever_name`: Rename the retriever
            - `description`: Update documentation
            - `tags`: Update organization tags
            - `display_config`: Update display configuration for publishing

            **❌ Fields You CANNOT Update (Immutable Core Logic):**
            - `input_schema`: Input field definitions (breaks dependent taxonomies)
            - `stages`: Retriever stages and configurations (changes matching behavior)
            - `collection_ids`: Target collections (changes data sources)
            - `budget_limits`: Budget constraints (affects execution behavior)

            **Need to Modify Core Logic?**
            Use POST /retrievers/{retriever_id}/clone instead. Cloning creates a new retriever
            with a new ID, allowing you to:
            - Fix typos in stage names
            - Add or remove stages
            - Change target collections
            - Modify input schema or budget limits

            **Behavior:**
            - All fields are OPTIONAL - provide only what you want to update
            - Version number automatically increments on each update
            - Empty updates (no fields provided) will be rejected with 400 error
            - Original retriever remains unchanged (no destructive operations)

            **Why This Design?**
            - Taxonomies reference retrievers by ID and expect consistent behavior
            - Cached results remain valid after metadata-only changes
            - Version tracking enables auditing and rollback
            - Published retrievers maintain stable behavior for consumers

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
    body: PatchRetrieverRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Patch Retriever

     Update a retriever's metadata.

    Only metadata fields can be updated:
    - name: Rename the retriever
    - description: Update the description
    - tags: Update tags for organization
    - display_config: Update display configuration

    Core logic (input_schema, stages, collection_ids) is immutable.
    To modify core logic, use POST /{retriever_id}/clone instead.

    Args:
        retriever_id (str): Retriever ID or name.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (PatchRetrieverRequest): Request to update a retriever's metadata.

            **IMPORTANT: Partial Updates with Controlled Mutability**

            This endpoint allows updating ONLY metadata fields. Core retriever logic is immutable
            to ensure consistency for dependent resources (taxonomies, cached results, etc.).

            **✅ Fields You CAN Update (Metadata Only):**
            - `retriever_name`: Rename the retriever
            - `description`: Update documentation
            - `tags`: Update organization tags
            - `display_config`: Update display configuration for publishing

            **❌ Fields You CANNOT Update (Immutable Core Logic):**
            - `input_schema`: Input field definitions (breaks dependent taxonomies)
            - `stages`: Retriever stages and configurations (changes matching behavior)
            - `collection_ids`: Target collections (changes data sources)
            - `budget_limits`: Budget constraints (affects execution behavior)

            **Need to Modify Core Logic?**
            Use POST /retrievers/{retriever_id}/clone instead. Cloning creates a new retriever
            with a new ID, allowing you to:
            - Fix typos in stage names
            - Add or remove stages
            - Change target collections
            - Modify input schema or budget limits

            **Behavior:**
            - All fields are OPTIONAL - provide only what you want to update
            - Version number automatically increments on each update
            - Empty updates (no fields provided) will be rejected with 400 error
            - Original retriever remains unchanged (no destructive operations)

            **Why This Design?**
            - Taxonomies reference retrievers by ID and expect consistent behavior
            - Cached results remain valid after metadata-only changes
            - Version tracking enables auditing and rollback
            - Published retrievers maintain stable behavior for consumers

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
    body: PatchRetrieverRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Patch Retriever

     Update a retriever's metadata.

    Only metadata fields can be updated:
    - name: Rename the retriever
    - description: Update the description
    - tags: Update tags for organization
    - display_config: Update display configuration

    Core logic (input_schema, stages, collection_ids) is immutable.
    To modify core logic, use POST /{retriever_id}/clone instead.

    Args:
        retriever_id (str): Retriever ID or name.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (PatchRetrieverRequest): Request to update a retriever's metadata.

            **IMPORTANT: Partial Updates with Controlled Mutability**

            This endpoint allows updating ONLY metadata fields. Core retriever logic is immutable
            to ensure consistency for dependent resources (taxonomies, cached results, etc.).

            **✅ Fields You CAN Update (Metadata Only):**
            - `retriever_name`: Rename the retriever
            - `description`: Update documentation
            - `tags`: Update organization tags
            - `display_config`: Update display configuration for publishing

            **❌ Fields You CANNOT Update (Immutable Core Logic):**
            - `input_schema`: Input field definitions (breaks dependent taxonomies)
            - `stages`: Retriever stages and configurations (changes matching behavior)
            - `collection_ids`: Target collections (changes data sources)
            - `budget_limits`: Budget constraints (affects execution behavior)

            **Need to Modify Core Logic?**
            Use POST /retrievers/{retriever_id}/clone instead. Cloning creates a new retriever
            with a new ID, allowing you to:
            - Fix typos in stage names
            - Add or remove stages
            - Change target collections
            - Modify input schema or budget limits

            **Behavior:**
            - All fields are OPTIONAL - provide only what you want to update
            - Version number automatically increments on each update
            - Empty updates (no fields provided) will be rejected with 400 error
            - Original retriever remains unchanged (no destructive operations)

            **Why This Design?**
            - Taxonomies reference retrievers by ID and expect consistent behavior
            - Cached results remain valid after metadata-only changes
            - Version tracking enables auditing and rollback
            - Published retrievers maintain stable behavior for consumers

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
    body: PatchRetrieverRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Patch Retriever

     Update a retriever's metadata.

    Only metadata fields can be updated:
    - name: Rename the retriever
    - description: Update the description
    - tags: Update tags for organization
    - display_config: Update display configuration

    Core logic (input_schema, stages, collection_ids) is immutable.
    To modify core logic, use POST /{retriever_id}/clone instead.

    Args:
        retriever_id (str): Retriever ID or name.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (PatchRetrieverRequest): Request to update a retriever's metadata.

            **IMPORTANT: Partial Updates with Controlled Mutability**

            This endpoint allows updating ONLY metadata fields. Core retriever logic is immutable
            to ensure consistency for dependent resources (taxonomies, cached results, etc.).

            **✅ Fields You CAN Update (Metadata Only):**
            - `retriever_name`: Rename the retriever
            - `description`: Update documentation
            - `tags`: Update organization tags
            - `display_config`: Update display configuration for publishing

            **❌ Fields You CANNOT Update (Immutable Core Logic):**
            - `input_schema`: Input field definitions (breaks dependent taxonomies)
            - `stages`: Retriever stages and configurations (changes matching behavior)
            - `collection_ids`: Target collections (changes data sources)
            - `budget_limits`: Budget constraints (affects execution behavior)

            **Need to Modify Core Logic?**
            Use POST /retrievers/{retriever_id}/clone instead. Cloning creates a new retriever
            with a new ID, allowing you to:
            - Fix typos in stage names
            - Add or remove stages
            - Change target collections
            - Modify input schema or budget limits

            **Behavior:**
            - All fields are OPTIONAL - provide only what you want to update
            - Version number automatically increments on each update
            - Empty updates (no fields provided) will be rejected with 400 error
            - Original retriever remains unchanged (no destructive operations)

            **Why This Design?**
            - Taxonomies reference retrievers by ID and expect consistent behavior
            - Cached results remain valid after metadata-only changes
            - Version tracking enables auditing and rollback
            - Published retrievers maintain stable behavior for consumers

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
