from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_users_v1_organizations_users_get_response_list_users_v1_organizations_users_get import (
    ListUsersV1OrganizationsUsersGetResponseListUsersV1OrganizationsUsersGet,
)
from ...models.user_role import UserRole
from ...models.user_status import UserStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    skip: int | Unset = 0,
    limit: int | Unset = 50,
    role: None | Unset | UserRole = UNSET,
    status: None | Unset | UserStatus = UNSET,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["skip"] = skip

    params["limit"] = limit

    json_role: None | str | Unset
    if isinstance(role, Unset):
        json_role = UNSET
    elif isinstance(role, UserRole):
        json_role = role.value
    else:
        json_role = role
    params["role"] = json_role

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, UserStatus):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/organizations/users",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponse
    | HTTPValidationError
    | ListUsersV1OrganizationsUsersGetResponseListUsersV1OrganizationsUsersGet
    | None
):
    if response.status_code == 200:
        response_200 = ListUsersV1OrganizationsUsersGetResponseListUsersV1OrganizationsUsersGet.from_dict(
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
    ErrorResponse | HTTPValidationError | ListUsersV1OrganizationsUsersGetResponseListUsersV1OrganizationsUsersGet
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    skip: int | Unset = 0,
    limit: int | Unset = 50,
    role: None | Unset | UserRole = UNSET,
    status: None | Unset | UserStatus = UNSET,
    authorization: str | Unset = UNSET,
) -> Response[
    ErrorResponse | HTTPValidationError | ListUsersV1OrganizationsUsersGetResponseListUsersV1OrganizationsUsersGet
]:
    """List Users

     List organization users with pagination and optional filters.

    Args:
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.
        role (None | Unset | UserRole):
        status (None | Unset | UserStatus):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListUsersV1OrganizationsUsersGetResponseListUsersV1OrganizationsUsersGet]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        role=role,
        status=status,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    skip: int | Unset = 0,
    limit: int | Unset = 50,
    role: None | Unset | UserRole = UNSET,
    status: None | Unset | UserStatus = UNSET,
    authorization: str | Unset = UNSET,
) -> (
    ErrorResponse
    | HTTPValidationError
    | ListUsersV1OrganizationsUsersGetResponseListUsersV1OrganizationsUsersGet
    | None
):
    """List Users

     List organization users with pagination and optional filters.

    Args:
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.
        role (None | Unset | UserRole):
        status (None | Unset | UserStatus):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListUsersV1OrganizationsUsersGetResponseListUsersV1OrganizationsUsersGet
    """

    return sync_detailed(
        client=client,
        skip=skip,
        limit=limit,
        role=role,
        status=status,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    skip: int | Unset = 0,
    limit: int | Unset = 50,
    role: None | Unset | UserRole = UNSET,
    status: None | Unset | UserStatus = UNSET,
    authorization: str | Unset = UNSET,
) -> Response[
    ErrorResponse | HTTPValidationError | ListUsersV1OrganizationsUsersGetResponseListUsersV1OrganizationsUsersGet
]:
    """List Users

     List organization users with pagination and optional filters.

    Args:
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.
        role (None | Unset | UserRole):
        status (None | Unset | UserStatus):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListUsersV1OrganizationsUsersGetResponseListUsersV1OrganizationsUsersGet]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        role=role,
        status=status,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    skip: int | Unset = 0,
    limit: int | Unset = 50,
    role: None | Unset | UserRole = UNSET,
    status: None | Unset | UserStatus = UNSET,
    authorization: str | Unset = UNSET,
) -> (
    ErrorResponse
    | HTTPValidationError
    | ListUsersV1OrganizationsUsersGetResponseListUsersV1OrganizationsUsersGet
    | None
):
    """List Users

     List organization users with pagination and optional filters.

    Args:
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.
        role (None | Unset | UserRole):
        status (None | Unset | UserStatus):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListUsersV1OrganizationsUsersGetResponseListUsersV1OrganizationsUsersGet
    """

    return (
        await asyncio_detailed(
            client=client,
            skip=skip,
            limit=limit,
            role=role,
            status=status,
            authorization=authorization,
        )
    ).parsed
