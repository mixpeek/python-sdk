from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_interaction_v1_retrievers_interactions_interaction_id_delete_response_delete_interaction_v1_retrievers_interactions_interaction_id_delete import (
    DeleteInteractionV1RetrieversInteractionsInteractionIdDeleteResponseDeleteInteractionV1RetrieversInteractionsInteractionIdDelete,
)
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    interaction_id: str,
    *,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/retrievers/interactions/{interaction_id}".format(
            interaction_id=quote(str(interaction_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteInteractionV1RetrieversInteractionsInteractionIdDeleteResponseDeleteInteractionV1RetrieversInteractionsInteractionIdDelete
    | ErrorResponse
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = DeleteInteractionV1RetrieversInteractionsInteractionIdDeleteResponseDeleteInteractionV1RetrieversInteractionsInteractionIdDelete.from_dict(
            response.json()
        )

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
) -> Response[
    DeleteInteractionV1RetrieversInteractionsInteractionIdDeleteResponseDeleteInteractionV1RetrieversInteractionsInteractionIdDelete
    | ErrorResponse
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    interaction_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[
    DeleteInteractionV1RetrieversInteractionsInteractionIdDeleteResponseDeleteInteractionV1RetrieversInteractionsInteractionIdDelete
    | ErrorResponse
    | HTTPValidationError
]:
    """Delete Interaction

     Delete a specific interaction (idempotent - succeeds even if already deleted).

    Args:
        interaction_id (str):
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
        Response[DeleteInteractionV1RetrieversInteractionsInteractionIdDeleteResponseDeleteInteractionV1RetrieversInteractionsInteractionIdDelete | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        interaction_id=interaction_id,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    interaction_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> (
    DeleteInteractionV1RetrieversInteractionsInteractionIdDeleteResponseDeleteInteractionV1RetrieversInteractionsInteractionIdDelete
    | ErrorResponse
    | HTTPValidationError
    | None
):
    """Delete Interaction

     Delete a specific interaction (idempotent - succeeds even if already deleted).

    Args:
        interaction_id (str):
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
        DeleteInteractionV1RetrieversInteractionsInteractionIdDeleteResponseDeleteInteractionV1RetrieversInteractionsInteractionIdDelete | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        interaction_id=interaction_id,
        client=client,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    interaction_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[
    DeleteInteractionV1RetrieversInteractionsInteractionIdDeleteResponseDeleteInteractionV1RetrieversInteractionsInteractionIdDelete
    | ErrorResponse
    | HTTPValidationError
]:
    """Delete Interaction

     Delete a specific interaction (idempotent - succeeds even if already deleted).

    Args:
        interaction_id (str):
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
        Response[DeleteInteractionV1RetrieversInteractionsInteractionIdDeleteResponseDeleteInteractionV1RetrieversInteractionsInteractionIdDelete | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        interaction_id=interaction_id,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    interaction_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> (
    DeleteInteractionV1RetrieversInteractionsInteractionIdDeleteResponseDeleteInteractionV1RetrieversInteractionsInteractionIdDelete
    | ErrorResponse
    | HTTPValidationError
    | None
):
    """Delete Interaction

     Delete a specific interaction (idempotent - succeeds even if already deleted).

    Args:
        interaction_id (str):
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
        DeleteInteractionV1RetrieversInteractionsInteractionIdDeleteResponseDeleteInteractionV1RetrieversInteractionsInteractionIdDelete | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            interaction_id=interaction_id,
            client=client,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
