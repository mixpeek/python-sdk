from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.list_api_keys_v1_organizations_users_user_email_api_keys_get_response_list_api_keys_v1_organizations_users_user_email_api_keys_get import (
    ListApiKeysV1OrganizationsUsersUserEmailApiKeysGetResponseListApiKeysV1OrganizationsUsersUserEmailApiKeysGet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_email: str,
    *,
    include_revoked: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["include_revoked"] = include_revoked

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/organizations/users/{user_email}/api-keys".format(
            user_email=quote(str(user_email), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponse
    | HTTPValidationError
    | ListApiKeysV1OrganizationsUsersUserEmailApiKeysGetResponseListApiKeysV1OrganizationsUsersUserEmailApiKeysGet
    | None
):
    if response.status_code == 200:
        response_200 = ListApiKeysV1OrganizationsUsersUserEmailApiKeysGetResponseListApiKeysV1OrganizationsUsersUserEmailApiKeysGet.from_dict(
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
    | HTTPValidationError
    | ListApiKeysV1OrganizationsUsersUserEmailApiKeysGetResponseListApiKeysV1OrganizationsUsersUserEmailApiKeysGet
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
    include_revoked: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | HTTPValidationError
    | ListApiKeysV1OrganizationsUsersUserEmailApiKeysGetResponseListApiKeysV1OrganizationsUsersUserEmailApiKeysGet
]:
    """List Api Keys

     List API keys for a user.

    Args:
        user_email (str):
        include_revoked (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListApiKeysV1OrganizationsUsersUserEmailApiKeysGetResponseListApiKeysV1OrganizationsUsersUserEmailApiKeysGet]
    """

    kwargs = _get_kwargs(
        user_email=user_email,
        include_revoked=include_revoked,
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
    include_revoked: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> (
    ErrorResponse
    | HTTPValidationError
    | ListApiKeysV1OrganizationsUsersUserEmailApiKeysGetResponseListApiKeysV1OrganizationsUsersUserEmailApiKeysGet
    | None
):
    """List Api Keys

     List API keys for a user.

    Args:
        user_email (str):
        include_revoked (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListApiKeysV1OrganizationsUsersUserEmailApiKeysGetResponseListApiKeysV1OrganizationsUsersUserEmailApiKeysGet
    """

    return sync_detailed(
        user_email=user_email,
        client=client,
        include_revoked=include_revoked,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    user_email: str,
    *,
    client: AuthenticatedClient | Client,
    include_revoked: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> Response[
    ErrorResponse
    | HTTPValidationError
    | ListApiKeysV1OrganizationsUsersUserEmailApiKeysGetResponseListApiKeysV1OrganizationsUsersUserEmailApiKeysGet
]:
    """List Api Keys

     List API keys for a user.

    Args:
        user_email (str):
        include_revoked (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ListApiKeysV1OrganizationsUsersUserEmailApiKeysGetResponseListApiKeysV1OrganizationsUsersUserEmailApiKeysGet]
    """

    kwargs = _get_kwargs(
        user_email=user_email,
        include_revoked=include_revoked,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_email: str,
    *,
    client: AuthenticatedClient | Client,
    include_revoked: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> (
    ErrorResponse
    | HTTPValidationError
    | ListApiKeysV1OrganizationsUsersUserEmailApiKeysGetResponseListApiKeysV1OrganizationsUsersUserEmailApiKeysGet
    | None
):
    """List Api Keys

     List API keys for a user.

    Args:
        user_email (str):
        include_revoked (bool | Unset):  Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ListApiKeysV1OrganizationsUsersUserEmailApiKeysGetResponseListApiKeysV1OrganizationsUsersUserEmailApiKeysGet
    """

    return (
        await asyncio_detailed(
            user_email=user_email,
            client=client,
            include_revoked=include_revoked,
            authorization=authorization,
        )
    ).parsed
