from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.submit_feedback_request import SubmitFeedbackRequest
from ...models.submit_feedback_response import SubmitFeedbackResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    session_id: str,
    *,
    body: SubmitFeedbackRequest,
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
        "url": "/v1/agents/sessions/{session_id}/feedback".format(
            session_id=quote(str(session_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | SubmitFeedbackResponse | None:
    if response.status_code == 200:
        response_200 = SubmitFeedbackResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | SubmitFeedbackResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitFeedbackRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | SubmitFeedbackResponse]:
    r""" Submit Feedback

     Submit feedback on an assistant message.

    When positive feedback is received, the conversation exchange is stored
    to memory for future context. When negative feedback is received, the
    exchange is NOT stored. This enables learning from quality interactions.

    Args:
        request: FastAPI request with tenant context
        session_id: Session identifier
        payload: Feedback request

    Returns:
        SubmitFeedbackResponse with feedback status

    Raises:
        NotFoundError: If session or message not found

    Example:
        ```bash
        curl -X POST http://localhost:8000/v1/agents/sessions/ses_abc123/feedback \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"message_id\": \"msg_xyz789\",
            \"rating\": \"positive\",
            \"feedback_text\": \"Very helpful response!\"
          }'
        ```

    Args:
        session_id (str): Session ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SubmitFeedbackRequest): Request payload for submitting feedback on a message.

            Attributes:
                message_id: The assistant message ID to provide feedback for
                rating: Feedback rating (positive or negative)
                feedback_text: Optional additional feedback text

            Example:
                ```python
                request = SubmitFeedbackRequest(
                    message_id="msg_abc123",
                    rating="positive",
                    feedback_text="This was very helpful!"
                )
                ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SubmitFeedbackResponse]
     """

    kwargs = _get_kwargs(
        session_id=session_id,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitFeedbackRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | SubmitFeedbackResponse | None:
    r""" Submit Feedback

     Submit feedback on an assistant message.

    When positive feedback is received, the conversation exchange is stored
    to memory for future context. When negative feedback is received, the
    exchange is NOT stored. This enables learning from quality interactions.

    Args:
        request: FastAPI request with tenant context
        session_id: Session identifier
        payload: Feedback request

    Returns:
        SubmitFeedbackResponse with feedback status

    Raises:
        NotFoundError: If session or message not found

    Example:
        ```bash
        curl -X POST http://localhost:8000/v1/agents/sessions/ses_abc123/feedback \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"message_id\": \"msg_xyz789\",
            \"rating\": \"positive\",
            \"feedback_text\": \"Very helpful response!\"
          }'
        ```

    Args:
        session_id (str): Session ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SubmitFeedbackRequest): Request payload for submitting feedback on a message.

            Attributes:
                message_id: The assistant message ID to provide feedback for
                rating: Feedback rating (positive or negative)
                feedback_text: Optional additional feedback text

            Example:
                ```python
                request = SubmitFeedbackRequest(
                    message_id="msg_abc123",
                    rating="positive",
                    feedback_text="This was very helpful!"
                )
                ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SubmitFeedbackResponse
     """

    return sync_detailed(
        session_id=session_id,
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitFeedbackRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | SubmitFeedbackResponse]:
    r""" Submit Feedback

     Submit feedback on an assistant message.

    When positive feedback is received, the conversation exchange is stored
    to memory for future context. When negative feedback is received, the
    exchange is NOT stored. This enables learning from quality interactions.

    Args:
        request: FastAPI request with tenant context
        session_id: Session identifier
        payload: Feedback request

    Returns:
        SubmitFeedbackResponse with feedback status

    Raises:
        NotFoundError: If session or message not found

    Example:
        ```bash
        curl -X POST http://localhost:8000/v1/agents/sessions/ses_abc123/feedback \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"message_id\": \"msg_xyz789\",
            \"rating\": \"positive\",
            \"feedback_text\": \"Very helpful response!\"
          }'
        ```

    Args:
        session_id (str): Session ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SubmitFeedbackRequest): Request payload for submitting feedback on a message.

            Attributes:
                message_id: The assistant message ID to provide feedback for
                rating: Feedback rating (positive or negative)
                feedback_text: Optional additional feedback text

            Example:
                ```python
                request = SubmitFeedbackRequest(
                    message_id="msg_abc123",
                    rating="positive",
                    feedback_text="This was very helpful!"
                )
                ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SubmitFeedbackResponse]
     """

    kwargs = _get_kwargs(
        session_id=session_id,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitFeedbackRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | SubmitFeedbackResponse | None:
    r""" Submit Feedback

     Submit feedback on an assistant message.

    When positive feedback is received, the conversation exchange is stored
    to memory for future context. When negative feedback is received, the
    exchange is NOT stored. This enables learning from quality interactions.

    Args:
        request: FastAPI request with tenant context
        session_id: Session identifier
        payload: Feedback request

    Returns:
        SubmitFeedbackResponse with feedback status

    Raises:
        NotFoundError: If session or message not found

    Example:
        ```bash
        curl -X POST http://localhost:8000/v1/agents/sessions/ses_abc123/feedback \
          -H \"Authorization: Bearer {api_key}\" \
          -H \"X-Namespace: {namespace_id}\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"message_id\": \"msg_xyz789\",
            \"rating\": \"positive\",
            \"feedback_text\": \"Very helpful response!\"
          }'
        ```

    Args:
        session_id (str): Session ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (SubmitFeedbackRequest): Request payload for submitting feedback on a message.

            Attributes:
                message_id: The assistant message ID to provide feedback for
                rating: Feedback rating (positive or negative)
                feedback_text: Optional additional feedback text

            Example:
                ```python
                request = SubmitFeedbackRequest(
                    message_id="msg_abc123",
                    rating="positive",
                    feedback_text="This was very helpful!"
                )
                ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SubmitFeedbackResponse
     """

    return (
        await asyncio_detailed(
            session_id=session_id,
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
