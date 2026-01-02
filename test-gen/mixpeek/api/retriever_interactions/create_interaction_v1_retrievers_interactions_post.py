from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.interaction_response import InteractionResponse
from ...models.search_interaction import SearchInteraction
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchInteraction,
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
        "url": "/v1/retrievers/interactions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | InteractionResponse | None:
    if response.status_code == 200:
        response_200 = InteractionResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | InteractionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchInteraction,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | InteractionResponse]:
    """Create Interaction

     Record a search interaction (view, click, feedback, etc.).

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SearchInteraction): Records a user interaction with a search result.

            This model captures user behavior signals that can be used to improve retrieval quality.
            Each interaction represents a user action (click, view, feedback) on a specific document
            returned by a retriever.

            Use Cases:
                - Track which search results users actually click on
                - Collect explicit feedback (thumbs up/down) on result quality
                - Monitor engagement metrics (time spent viewing, sharing)
                - Identify problematic queries (zero results, immediate refinements)
                - Power Learning to Rank models with real user behavior

            Requirements:
                - feature_id: REQUIRED - The document/feature that was interacted with
                - interaction_type: REQUIRED - Type(s) of interaction that occurred
                - position: REQUIRED - Where in results list the interaction occurred (for LTR)
                - query_snapshot: HIGHLY RECOMMENDED - Query input for training optimization
                - document_score: HIGHLY RECOMMENDED - Initial score for LTR training
                - result_set_size: OPTIONAL - Total results shown (for context)
                - metadata: OPTIONAL - Additional context about the interaction
                - user_id: OPTIONAL - For personalization and user-specific metrics
                - session_id: OPTIONAL - For tracking multi-query sessions
                - execution_id: OPTIONAL - Link to full execution context
                - retriever_id: OPTIONAL - For multi-retriever analytics

            Related Concepts:
                - Retrievers: Interactions measure retriever performance
                - Evaluations: Interactions provide real-world complement to offline evaluation
                - Learning to Rank: Interactions train ranking models

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | InteractionResponse]
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
    body: SearchInteraction,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | InteractionResponse | None:
    """Create Interaction

     Record a search interaction (view, click, feedback, etc.).

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SearchInteraction): Records a user interaction with a search result.

            This model captures user behavior signals that can be used to improve retrieval quality.
            Each interaction represents a user action (click, view, feedback) on a specific document
            returned by a retriever.

            Use Cases:
                - Track which search results users actually click on
                - Collect explicit feedback (thumbs up/down) on result quality
                - Monitor engagement metrics (time spent viewing, sharing)
                - Identify problematic queries (zero results, immediate refinements)
                - Power Learning to Rank models with real user behavior

            Requirements:
                - feature_id: REQUIRED - The document/feature that was interacted with
                - interaction_type: REQUIRED - Type(s) of interaction that occurred
                - position: REQUIRED - Where in results list the interaction occurred (for LTR)
                - query_snapshot: HIGHLY RECOMMENDED - Query input for training optimization
                - document_score: HIGHLY RECOMMENDED - Initial score for LTR training
                - result_set_size: OPTIONAL - Total results shown (for context)
                - metadata: OPTIONAL - Additional context about the interaction
                - user_id: OPTIONAL - For personalization and user-specific metrics
                - session_id: OPTIONAL - For tracking multi-query sessions
                - execution_id: OPTIONAL - Link to full execution context
                - retriever_id: OPTIONAL - For multi-retriever analytics

            Related Concepts:
                - Retrievers: Interactions measure retriever performance
                - Evaluations: Interactions provide real-world complement to offline evaluation
                - Learning to Rank: Interactions train ranking models

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | InteractionResponse
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
    body: SearchInteraction,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | InteractionResponse]:
    """Create Interaction

     Record a search interaction (view, click, feedback, etc.).

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SearchInteraction): Records a user interaction with a search result.

            This model captures user behavior signals that can be used to improve retrieval quality.
            Each interaction represents a user action (click, view, feedback) on a specific document
            returned by a retriever.

            Use Cases:
                - Track which search results users actually click on
                - Collect explicit feedback (thumbs up/down) on result quality
                - Monitor engagement metrics (time spent viewing, sharing)
                - Identify problematic queries (zero results, immediate refinements)
                - Power Learning to Rank models with real user behavior

            Requirements:
                - feature_id: REQUIRED - The document/feature that was interacted with
                - interaction_type: REQUIRED - Type(s) of interaction that occurred
                - position: REQUIRED - Where in results list the interaction occurred (for LTR)
                - query_snapshot: HIGHLY RECOMMENDED - Query input for training optimization
                - document_score: HIGHLY RECOMMENDED - Initial score for LTR training
                - result_set_size: OPTIONAL - Total results shown (for context)
                - metadata: OPTIONAL - Additional context about the interaction
                - user_id: OPTIONAL - For personalization and user-specific metrics
                - session_id: OPTIONAL - For tracking multi-query sessions
                - execution_id: OPTIONAL - Link to full execution context
                - retriever_id: OPTIONAL - For multi-retriever analytics

            Related Concepts:
                - Retrievers: Interactions measure retriever performance
                - Evaluations: Interactions provide real-world complement to offline evaluation
                - Learning to Rank: Interactions train ranking models

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | InteractionResponse]
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
    body: SearchInteraction,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | InteractionResponse | None:
    """Create Interaction

     Record a search interaction (view, click, feedback, etc.).

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SearchInteraction): Records a user interaction with a search result.

            This model captures user behavior signals that can be used to improve retrieval quality.
            Each interaction represents a user action (click, view, feedback) on a specific document
            returned by a retriever.

            Use Cases:
                - Track which search results users actually click on
                - Collect explicit feedback (thumbs up/down) on result quality
                - Monitor engagement metrics (time spent viewing, sharing)
                - Identify problematic queries (zero results, immediate refinements)
                - Power Learning to Rank models with real user behavior

            Requirements:
                - feature_id: REQUIRED - The document/feature that was interacted with
                - interaction_type: REQUIRED - Type(s) of interaction that occurred
                - position: REQUIRED - Where in results list the interaction occurred (for LTR)
                - query_snapshot: HIGHLY RECOMMENDED - Query input for training optimization
                - document_score: HIGHLY RECOMMENDED - Initial score for LTR training
                - result_set_size: OPTIONAL - Total results shown (for context)
                - metadata: OPTIONAL - Additional context about the interaction
                - user_id: OPTIONAL - For personalization and user-specific metrics
                - session_id: OPTIONAL - For tracking multi-query sessions
                - execution_id: OPTIONAL - Link to full execution context
                - retriever_id: OPTIONAL - For multi-retriever analytics

            Related Concepts:
                - Retrievers: Interactions measure retriever performance
                - Evaluations: Interactions provide real-world complement to offline evaluation
                - Learning to Rank: Interactions train ranking models

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | InteractionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
