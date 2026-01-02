from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detect_intent_request import DetectIntentRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.intent_classification import IntentClassification
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DetectIntentRequest,
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
        "url": "/v1/agents/sessions/intent/detect",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | IntentClassification | None:
    if response.status_code == 200:
        response_200 = IntentClassification.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | IntentClassification]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DetectIntentRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | IntentClassification]:
    r""" Detect Intent

     Detect user intent from natural language request.

    This endpoint analyzes a user's request to determine whether they want to:
    - Execute queries on existing data (execution mode)
    - Create new resources/infrastructure (setup mode)
    - Or if the request is ambiguous and needs clarification

    It performs keyword analysis and checks existing collections to provide
    intelligent classification and recommendations.

    Args:
        request: FastAPI request with tenant context
        payload: Intent detection request with user's input

    Returns:
        IntentClassification with detected intent and recommendations

    Example:
        ```bash
        curl -X POST http://localhost:8000/v1/agents/intent/detect \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"user_request\": \"I want to search videos by faces\",
            \"include_collection_analysis\": true
          }'
        ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (DetectIntentRequest): Request to detect intent from user input.

            Attributes:
                user_request: The user's natural language request to analyze
                include_collection_analysis: Whether to analyze existing collections

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | IntentClassification]
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
    body: DetectIntentRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | IntentClassification | None:
    r""" Detect Intent

     Detect user intent from natural language request.

    This endpoint analyzes a user's request to determine whether they want to:
    - Execute queries on existing data (execution mode)
    - Create new resources/infrastructure (setup mode)
    - Or if the request is ambiguous and needs clarification

    It performs keyword analysis and checks existing collections to provide
    intelligent classification and recommendations.

    Args:
        request: FastAPI request with tenant context
        payload: Intent detection request with user's input

    Returns:
        IntentClassification with detected intent and recommendations

    Example:
        ```bash
        curl -X POST http://localhost:8000/v1/agents/intent/detect \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"user_request\": \"I want to search videos by faces\",
            \"include_collection_analysis\": true
          }'
        ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (DetectIntentRequest): Request to detect intent from user input.

            Attributes:
                user_request: The user's natural language request to analyze
                include_collection_analysis: Whether to analyze existing collections

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | IntentClassification
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
    body: DetectIntentRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | IntentClassification]:
    r""" Detect Intent

     Detect user intent from natural language request.

    This endpoint analyzes a user's request to determine whether they want to:
    - Execute queries on existing data (execution mode)
    - Create new resources/infrastructure (setup mode)
    - Or if the request is ambiguous and needs clarification

    It performs keyword analysis and checks existing collections to provide
    intelligent classification and recommendations.

    Args:
        request: FastAPI request with tenant context
        payload: Intent detection request with user's input

    Returns:
        IntentClassification with detected intent and recommendations

    Example:
        ```bash
        curl -X POST http://localhost:8000/v1/agents/intent/detect \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"user_request\": \"I want to search videos by faces\",
            \"include_collection_analysis\": true
          }'
        ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (DetectIntentRequest): Request to detect intent from user input.

            Attributes:
                user_request: The user's natural language request to analyze
                include_collection_analysis: Whether to analyze existing collections

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | IntentClassification]
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
    body: DetectIntentRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | IntentClassification | None:
    r""" Detect Intent

     Detect user intent from natural language request.

    This endpoint analyzes a user's request to determine whether they want to:
    - Execute queries on existing data (execution mode)
    - Create new resources/infrastructure (setup mode)
    - Or if the request is ambiguous and needs clarification

    It performs keyword analysis and checks existing collections to provide
    intelligent classification and recommendations.

    Args:
        request: FastAPI request with tenant context
        payload: Intent detection request with user's input

    Returns:
        IntentClassification with detected intent and recommendations

    Example:
        ```bash
        curl -X POST http://localhost:8000/v1/agents/intent/detect \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"user_request\": \"I want to search videos by faces\",
            \"include_collection_analysis\": true
          }'
        ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (DetectIntentRequest): Request to detect intent from user input.

            Attributes:
                user_request: The user's natural language request to analyze
                include_collection_analysis: Whether to analyze existing collections

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | IntentClassification
     """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
