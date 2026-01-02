from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_tasks_request import ListTasksRequest
from ...models.list_tasks_response import ListTasksResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ListTasksRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_offset: int | None | Unset
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params["include_total"] = include_total

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/tasks/list",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | ListTasksResponse | None:
    if response.status_code == 200:
        response_200 = ListTasksResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | ListTasksResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListTasksRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListTasksResponse]:
    r"""List Tasks

     List tasks with optional filtering, sorting, and pagination.

        **Filter Options**:
        - `status`: Filter by specific status (PENDING, IN_PROGRESS, COMPLETED, FAILED, etc.)
        - `task_type`: Filter by task type

        **Examples**:
        - All tasks: `{}`
        - Failed tasks only: `{\"status\": \"FAILED\"}`
        - Pending batches: `{\"status\": \"PENDING\", \"task_type\":
    \"API_BUCKETS_UPLOADS_BATCH_CONFIRM\"}`
        - In-progress tasks: `{\"status\": \"IN_PROGRESS\"}`

    Args:
        limit (int | None | Unset):
        offset (int | None | Unset):
        cursor (None | str | Unset):
        include_total (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (ListTasksRequest | Unset): Request model for listing tasks.

            Filter tasks by status, type, or other criteria.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListTasksResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        limit=limit,
        offset=offset,
        cursor=cursor,
        include_total=include_total,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ListTasksRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListTasksResponse | None:
    r"""List Tasks

     List tasks with optional filtering, sorting, and pagination.

        **Filter Options**:
        - `status`: Filter by specific status (PENDING, IN_PROGRESS, COMPLETED, FAILED, etc.)
        - `task_type`: Filter by task type

        **Examples**:
        - All tasks: `{}`
        - Failed tasks only: `{\"status\": \"FAILED\"}`
        - Pending batches: `{\"status\": \"PENDING\", \"task_type\":
    \"API_BUCKETS_UPLOADS_BATCH_CONFIRM\"}`
        - In-progress tasks: `{\"status\": \"IN_PROGRESS\"}`

    Args:
        limit (int | None | Unset):
        offset (int | None | Unset):
        cursor (None | str | Unset):
        include_total (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (ListTasksRequest | Unset): Request model for listing tasks.

            Filter tasks by status, type, or other criteria.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListTasksResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        limit=limit,
        offset=offset,
        cursor=cursor,
        include_total=include_total,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListTasksRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ListTasksResponse]:
    r"""List Tasks

     List tasks with optional filtering, sorting, and pagination.

        **Filter Options**:
        - `status`: Filter by specific status (PENDING, IN_PROGRESS, COMPLETED, FAILED, etc.)
        - `task_type`: Filter by task type

        **Examples**:
        - All tasks: `{}`
        - Failed tasks only: `{\"status\": \"FAILED\"}`
        - Pending batches: `{\"status\": \"PENDING\", \"task_type\":
    \"API_BUCKETS_UPLOADS_BATCH_CONFIRM\"}`
        - In-progress tasks: `{\"status\": \"IN_PROGRESS\"}`

    Args:
        limit (int | None | Unset):
        offset (int | None | Unset):
        cursor (None | str | Unset):
        include_total (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (ListTasksRequest | Unset): Request model for listing tasks.

            Filter tasks by status, type, or other criteria.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListTasksResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        limit=limit,
        offset=offset,
        cursor=cursor,
        include_total=include_total,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ListTasksRequest | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    offset: int | None | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    include_total: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ListTasksResponse | None:
    r"""List Tasks

     List tasks with optional filtering, sorting, and pagination.

        **Filter Options**:
        - `status`: Filter by specific status (PENDING, IN_PROGRESS, COMPLETED, FAILED, etc.)
        - `task_type`: Filter by task type

        **Examples**:
        - All tasks: `{}`
        - Failed tasks only: `{\"status\": \"FAILED\"}`
        - Pending batches: `{\"status\": \"PENDING\", \"task_type\":
    \"API_BUCKETS_UPLOADS_BATCH_CONFIRM\"}`
        - In-progress tasks: `{\"status\": \"IN_PROGRESS\"}`

    Args:
        limit (int | None | Unset):
        offset (int | None | Unset):
        cursor (None | str | Unset):
        include_total (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (ListTasksRequest | Unset): Request model for listing tasks.

            Filter tasks by status, type, or other criteria.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListTasksResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            limit=limit,
            offset=offset,
            cursor=cursor,
            include_total=include_total,
            authorization=authorization,
        )
    ).parsed
