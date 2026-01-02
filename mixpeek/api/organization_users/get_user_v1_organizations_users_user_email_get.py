from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_user_v1_organizations_users_user_email_get_response_get_user_v1_organizations_users_user_email_get import (
    GetUserV1OrganizationsUsersUserEmailGetResponseGetUserV1OrganizationsUsersUserEmailGet,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_email: str,
    *,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/organizations/users/{user_email}".format(
            user_email=quote(str(user_email), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponse
    | GetUserV1OrganizationsUsersUserEmailGetResponseGetUserV1OrganizationsUsersUserEmailGet
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = GetUserV1OrganizationsUsersUserEmailGetResponseGetUserV1OrganizationsUsersUserEmailGet.from_dict(
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
    ErrorResponse
    | GetUserV1OrganizationsUsersUserEmailGetResponseGetUserV1OrganizationsUsersUserEmailGet
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_email: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | GetUserV1OrganizationsUsersUserEmailGetResponseGetUserV1OrganizationsUsersUserEmailGet
    | HTTPValidationError
]:
    """Get User

     Return a user by email address.

    Args:
        user_email (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetUserV1OrganizationsUsersUserEmailGetResponseGetUserV1OrganizationsUsersUserEmailGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        user_email=user_email,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_email: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> (
    ErrorResponse
    | GetUserV1OrganizationsUsersUserEmailGetResponseGetUserV1OrganizationsUsersUserEmailGet
    | HTTPValidationError
    | None
):
    """Get User

     Return a user by email address.

    Args:
        user_email (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetUserV1OrganizationsUsersUserEmailGetResponseGetUserV1OrganizationsUsersUserEmailGet | HTTPValidationError
    """

    return sync_detailed(
        user_email=user_email,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    user_email: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | GetUserV1OrganizationsUsersUserEmailGetResponseGetUserV1OrganizationsUsersUserEmailGet
    | HTTPValidationError
]:
    """Get User

     Return a user by email address.

    Args:
        user_email (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetUserV1OrganizationsUsersUserEmailGetResponseGetUserV1OrganizationsUsersUserEmailGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        user_email=user_email,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_email: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> (
    ErrorResponse
    | GetUserV1OrganizationsUsersUserEmailGetResponseGetUserV1OrganizationsUsersUserEmailGet
    | HTTPValidationError
    | None
):
    """Get User

     Return a user by email address.

    Args:
        user_email (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetUserV1OrganizationsUsersUserEmailGetResponseGetUserV1OrganizationsUsersUserEmailGet | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            user_email=user_email,
            client=client,
            authorization=authorization,
        )
    ).parsed
