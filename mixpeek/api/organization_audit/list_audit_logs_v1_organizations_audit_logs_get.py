from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_action import AuditAction
from ...models.audit_event_list_response import AuditEventListResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.resource_type import ResourceType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    resource_type: None | ResourceType | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    actor_id: None | str | Unset = UNSET,
    action: AuditAction | None | Unset = UNSET,
    start: None | str | Unset = UNSET,
    end: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    json_resource_type: None | str | Unset
    if isinstance(resource_type, Unset):
        json_resource_type = UNSET
    elif isinstance(resource_type, ResourceType):
        json_resource_type = resource_type.value
    else:
        json_resource_type = resource_type
    params["resource_type"] = json_resource_type

    json_resource_id: None | str | Unset
    if isinstance(resource_id, Unset):
        json_resource_id = UNSET
    else:
        json_resource_id = resource_id
    params["resource_id"] = json_resource_id

    json_actor_id: None | str | Unset
    if isinstance(actor_id, Unset):
        json_actor_id = UNSET
    else:
        json_actor_id = actor_id
    params["actor_id"] = json_actor_id

    json_action: None | str | Unset
    if isinstance(action, Unset):
        json_action = UNSET
    elif isinstance(action, AuditAction):
        json_action = action.value
    else:
        json_action = action
    params["action"] = json_action

    json_start: None | str | Unset
    if isinstance(start, Unset):
        json_start = UNSET
    else:
        json_start = start
    params["start"] = json_start

    json_end: None | str | Unset
    if isinstance(end, Unset):
        json_end = UNSET
    else:
        json_end = end
    params["end"] = json_end

    params["skip"] = skip

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/organizations/audit/logs",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuditEventListResponse | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AuditEventListResponse.from_dict(response.json())

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
) -> Response[AuditEventListResponse | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    resource_type: None | ResourceType | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    actor_id: None | str | Unset = UNSET,
    action: AuditAction | None | Unset = UNSET,
    start: None | str | Unset = UNSET,
    end: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
) -> Response[AuditEventListResponse | ErrorResponse | HTTPValidationError]:
    """List Audit Logs

     List organization audit logs with filtering and pagination.

    Returns audit events for the organization, sorted by timestamp descending.
    Requires ADMIN permission.

    Args:
        resource_type (None | ResourceType | Unset): Filter by resource type
        resource_id (None | str | Unset): Filter by resource ID
        actor_id (None | str | Unset): Filter by actor ID
        action (AuditAction | None | Unset): Filter by action
        start (None | str | Unset): ISO8601 start timestamp
        end (None | str | Unset): ISO8601 end timestamp
        skip (int | Unset): Number of results to skip Default: 0.
        limit (int | Unset): Number of results to return Default: 50.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditEventListResponse | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        resource_type=resource_type,
        resource_id=resource_id,
        actor_id=actor_id,
        action=action,
        start=start,
        end=end,
        skip=skip,
        limit=limit,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    resource_type: None | ResourceType | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    actor_id: None | str | Unset = UNSET,
    action: AuditAction | None | Unset = UNSET,
    start: None | str | Unset = UNSET,
    end: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
) -> AuditEventListResponse | ErrorResponse | HTTPValidationError | None:
    """List Audit Logs

     List organization audit logs with filtering and pagination.

    Returns audit events for the organization, sorted by timestamp descending.
    Requires ADMIN permission.

    Args:
        resource_type (None | ResourceType | Unset): Filter by resource type
        resource_id (None | str | Unset): Filter by resource ID
        actor_id (None | str | Unset): Filter by actor ID
        action (AuditAction | None | Unset): Filter by action
        start (None | str | Unset): ISO8601 start timestamp
        end (None | str | Unset): ISO8601 end timestamp
        skip (int | Unset): Number of results to skip Default: 0.
        limit (int | Unset): Number of results to return Default: 50.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditEventListResponse | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        resource_type=resource_type,
        resource_id=resource_id,
        actor_id=actor_id,
        action=action,
        start=start,
        end=end,
        skip=skip,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    resource_type: None | ResourceType | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    actor_id: None | str | Unset = UNSET,
    action: AuditAction | None | Unset = UNSET,
    start: None | str | Unset = UNSET,
    end: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
) -> Response[AuditEventListResponse | ErrorResponse | HTTPValidationError]:
    """List Audit Logs

     List organization audit logs with filtering and pagination.

    Returns audit events for the organization, sorted by timestamp descending.
    Requires ADMIN permission.

    Args:
        resource_type (None | ResourceType | Unset): Filter by resource type
        resource_id (None | str | Unset): Filter by resource ID
        actor_id (None | str | Unset): Filter by actor ID
        action (AuditAction | None | Unset): Filter by action
        start (None | str | Unset): ISO8601 start timestamp
        end (None | str | Unset): ISO8601 end timestamp
        skip (int | Unset): Number of results to skip Default: 0.
        limit (int | Unset): Number of results to return Default: 50.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditEventListResponse | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        resource_type=resource_type,
        resource_id=resource_id,
        actor_id=actor_id,
        action=action,
        start=start,
        end=end,
        skip=skip,
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    resource_type: None | ResourceType | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    actor_id: None | str | Unset = UNSET,
    action: AuditAction | None | Unset = UNSET,
    start: None | str | Unset = UNSET,
    end: None | str | Unset = UNSET,
    skip: int | Unset = 0,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
) -> AuditEventListResponse | ErrorResponse | HTTPValidationError | None:
    """List Audit Logs

     List organization audit logs with filtering and pagination.

    Returns audit events for the organization, sorted by timestamp descending.
    Requires ADMIN permission.

    Args:
        resource_type (None | ResourceType | Unset): Filter by resource type
        resource_id (None | str | Unset): Filter by resource ID
        actor_id (None | str | Unset): Filter by actor ID
        action (AuditAction | None | Unset): Filter by action
        start (None | str | Unset): ISO8601 start timestamp
        end (None | str | Unset): ISO8601 end timestamp
        skip (int | Unset): Number of results to skip Default: 0.
        limit (int | Unset): Number of results to return Default: 50.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditEventListResponse | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            resource_type=resource_type,
            resource_id=resource_id,
            actor_id=actor_id,
            action=action,
            start=start,
            end=end,
            skip=skip,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
