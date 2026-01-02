from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.public_interaction_batch_request import PublicInteractionBatchRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    public_name: str,
    *,
    body: PublicInteractionBatchRequest,
    x_session_id: None | str | Unset = UNSET,
    x_public_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_session_id, Unset):
        headers["X-Session-ID"] = x_session_id

    headers["X-Public-API-Key"] = x_public_api_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/public/retrievers/{public_name}/interactions/batch".format(
            public_name=quote(str(public_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PublicInteractionBatchRequest,
    x_session_id: None | str | Unset = UNSET,
    x_public_api_key: str,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    r""" Track Interaction Batch

     Track multiple interactions in a single request (batching).

    More efficient than sending individual interaction requests.
    Use this for batching viewport visibility, bulk actions, etc.

    **Authentication:**
    - Requires `X-Public-API-Key` header
    - Password NOT required (tracking should work even without auth)

    **Recommended Headers:**
    - `X-Session-ID`: Applied to all interactions in the batch

    **Limits:**
    - Maximum 100 interactions per batch

    **Example:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/video-search/interactions/batch\" \
      -H \"X-Public-API-Key: prk_abc123...\" \
      -H \"X-Session-ID: sess_xyz...\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"interactions\": [
          {
            \"document_id\": \"doc_123\",
            \"interaction_type\": [\"VIEW\"],
            \"position\": 0,
            \"execution_id\": \"exec_abc\"
          },
          {
            \"document_id\": \"doc_456\",
            \"interaction_type\": [\"VIEW\"],
            \"position\": 1,
            \"execution_id\": \"exec_abc\"
          }
        ]
      }'
    ```

    Args:
        public_name (str): Public name of the published retriever
        x_session_id (None | str | Unset):
        x_public_api_key (str):
        body (PublicInteractionBatchRequest): Request to track multiple interactions in batch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        public_name=public_name,
        body=body,
        x_session_id=x_session_id,
        x_public_api_key=x_public_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PublicInteractionBatchRequest,
    x_session_id: None | str | Unset = UNSET,
    x_public_api_key: str,
) -> Any | ErrorResponse | HTTPValidationError | None:
    r""" Track Interaction Batch

     Track multiple interactions in a single request (batching).

    More efficient than sending individual interaction requests.
    Use this for batching viewport visibility, bulk actions, etc.

    **Authentication:**
    - Requires `X-Public-API-Key` header
    - Password NOT required (tracking should work even without auth)

    **Recommended Headers:**
    - `X-Session-ID`: Applied to all interactions in the batch

    **Limits:**
    - Maximum 100 interactions per batch

    **Example:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/video-search/interactions/batch\" \
      -H \"X-Public-API-Key: prk_abc123...\" \
      -H \"X-Session-ID: sess_xyz...\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"interactions\": [
          {
            \"document_id\": \"doc_123\",
            \"interaction_type\": [\"VIEW\"],
            \"position\": 0,
            \"execution_id\": \"exec_abc\"
          },
          {
            \"document_id\": \"doc_456\",
            \"interaction_type\": [\"VIEW\"],
            \"position\": 1,
            \"execution_id\": \"exec_abc\"
          }
        ]
      }'
    ```

    Args:
        public_name (str): Public name of the published retriever
        x_session_id (None | str | Unset):
        x_public_api_key (str):
        body (PublicInteractionBatchRequest): Request to track multiple interactions in batch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
     """

    return sync_detailed(
        public_name=public_name,
        client=client,
        body=body,
        x_session_id=x_session_id,
        x_public_api_key=x_public_api_key,
    ).parsed


async def asyncio_detailed(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PublicInteractionBatchRequest,
    x_session_id: None | str | Unset = UNSET,
    x_public_api_key: str,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    r""" Track Interaction Batch

     Track multiple interactions in a single request (batching).

    More efficient than sending individual interaction requests.
    Use this for batching viewport visibility, bulk actions, etc.

    **Authentication:**
    - Requires `X-Public-API-Key` header
    - Password NOT required (tracking should work even without auth)

    **Recommended Headers:**
    - `X-Session-ID`: Applied to all interactions in the batch

    **Limits:**
    - Maximum 100 interactions per batch

    **Example:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/video-search/interactions/batch\" \
      -H \"X-Public-API-Key: prk_abc123...\" \
      -H \"X-Session-ID: sess_xyz...\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"interactions\": [
          {
            \"document_id\": \"doc_123\",
            \"interaction_type\": [\"VIEW\"],
            \"position\": 0,
            \"execution_id\": \"exec_abc\"
          },
          {
            \"document_id\": \"doc_456\",
            \"interaction_type\": [\"VIEW\"],
            \"position\": 1,
            \"execution_id\": \"exec_abc\"
          }
        ]
      }'
    ```

    Args:
        public_name (str): Public name of the published retriever
        x_session_id (None | str | Unset):
        x_public_api_key (str):
        body (PublicInteractionBatchRequest): Request to track multiple interactions in batch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        public_name=public_name,
        body=body,
        x_session_id=x_session_id,
        x_public_api_key=x_public_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PublicInteractionBatchRequest,
    x_session_id: None | str | Unset = UNSET,
    x_public_api_key: str,
) -> Any | ErrorResponse | HTTPValidationError | None:
    r""" Track Interaction Batch

     Track multiple interactions in a single request (batching).

    More efficient than sending individual interaction requests.
    Use this for batching viewport visibility, bulk actions, etc.

    **Authentication:**
    - Requires `X-Public-API-Key` header
    - Password NOT required (tracking should work even without auth)

    **Recommended Headers:**
    - `X-Session-ID`: Applied to all interactions in the batch

    **Limits:**
    - Maximum 100 interactions per batch

    **Example:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/video-search/interactions/batch\" \
      -H \"X-Public-API-Key: prk_abc123...\" \
      -H \"X-Session-ID: sess_xyz...\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"interactions\": [
          {
            \"document_id\": \"doc_123\",
            \"interaction_type\": [\"VIEW\"],
            \"position\": 0,
            \"execution_id\": \"exec_abc\"
          },
          {
            \"document_id\": \"doc_456\",
            \"interaction_type\": [\"VIEW\"],
            \"position\": 1,
            \"execution_id\": \"exec_abc\"
          }
        ]
      }'
    ```

    Args:
        public_name (str): Public name of the published retriever
        x_session_id (None | str | Unset):
        x_public_api_key (str):
        body (PublicInteractionBatchRequest): Request to track multiple interactions in batch.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
     """

    return (
        await asyncio_detailed(
            public_name=public_name,
            client=client,
            body=body,
            x_session_id=x_session_id,
            x_public_api_key=x_public_api_key,
        )
    ).parsed
