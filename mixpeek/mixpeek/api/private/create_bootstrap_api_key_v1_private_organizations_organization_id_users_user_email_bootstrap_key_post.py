from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_bootstrap_api_key_v1_private_organizations_organization_id_users_user_email_bootstrap_key_post_response_create_bootstrap_api_key_v1_private_organizations_organization_id_users_user_email_bootstrap_key_post import (
    CreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPostResponseCreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPost,
)
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    organization_id: str,
    user_email: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/private/organizations/{organization_id}/users/{user_email}/bootstrap-key".format(
            organization_id=quote(str(organization_id), safe=""),
            user_email=quote(str(user_email), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPostResponseCreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPost
    | ErrorResponse
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = CreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPostResponseCreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPost.from_dict(
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
    CreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPostResponseCreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPost
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
    organization_id: str,
    user_email: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    CreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPostResponseCreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPost
    | ErrorResponse
    | HTTPValidationError
]:
    r"""Create Bootstrap Api Key

     Create the organization's primary API key (requires MIXPEEK_PRIVATE_KEY).

    🔑 IMPORTANT - Two Different Keys (DO NOT CONFUSE):

    1. MIXPEEK_PRIVATE_KEY (what you use to call THIS endpoint):
       - Static, hardcoded token shared between studio proxy and backend
       - Used ONLY for server-to-server /v1/private/* endpoint calls
       - Never changes, never stored in database
       - Never used by frontend UI
       - Example: xnefritAiaKQiddNL3ZHWEN4cHWLsCkwEycUDLU2wLekQEuf

    2. Organization API Key (what THIS endpoint creates and returns):
       - Created ONCE per organization with ADMIN permissions
       - Used by frontend UI for ALL /v1/* API calls
       - Named \"admin-key\" and stored in database (hashed)
       - Plaintext returned ONCE on creation
       - 🔒 PROTECTED: Users CANNOT delete, rotate, or change permissions on this key
       - Example: sk_kbHvXHAySDUrzrPo2ajwmqBAXJ...

    This endpoint creates an Organization API key (type #2) that the frontend will use.
    It does NOT create, modify, or touch the MIXPEEK_PRIVATE_KEY (type #1).

    ⚠️ The plaintext key is only returned ONCE on creation - store it in localStorage!
    ✅ If called when key exists: Revokes old key and returns a new one (idempotent)

    Args:
        organization_id (str):
        user_email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPostResponseCreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPost | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        user_email=user_email,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    user_email: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    CreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPostResponseCreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPost
    | ErrorResponse
    | HTTPValidationError
    | None
):
    r"""Create Bootstrap Api Key

     Create the organization's primary API key (requires MIXPEEK_PRIVATE_KEY).

    🔑 IMPORTANT - Two Different Keys (DO NOT CONFUSE):

    1. MIXPEEK_PRIVATE_KEY (what you use to call THIS endpoint):
       - Static, hardcoded token shared between studio proxy and backend
       - Used ONLY for server-to-server /v1/private/* endpoint calls
       - Never changes, never stored in database
       - Never used by frontend UI
       - Example: xnefritAiaKQiddNL3ZHWEN4cHWLsCkwEycUDLU2wLekQEuf

    2. Organization API Key (what THIS endpoint creates and returns):
       - Created ONCE per organization with ADMIN permissions
       - Used by frontend UI for ALL /v1/* API calls
       - Named \"admin-key\" and stored in database (hashed)
       - Plaintext returned ONCE on creation
       - 🔒 PROTECTED: Users CANNOT delete, rotate, or change permissions on this key
       - Example: sk_kbHvXHAySDUrzrPo2ajwmqBAXJ...

    This endpoint creates an Organization API key (type #2) that the frontend will use.
    It does NOT create, modify, or touch the MIXPEEK_PRIVATE_KEY (type #1).

    ⚠️ The plaintext key is only returned ONCE on creation - store it in localStorage!
    ✅ If called when key exists: Revokes old key and returns a new one (idempotent)

    Args:
        organization_id (str):
        user_email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPostResponseCreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPost | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        organization_id=organization_id,
        user_email=user_email,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    user_email: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    CreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPostResponseCreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPost
    | ErrorResponse
    | HTTPValidationError
]:
    r"""Create Bootstrap Api Key

     Create the organization's primary API key (requires MIXPEEK_PRIVATE_KEY).

    🔑 IMPORTANT - Two Different Keys (DO NOT CONFUSE):

    1. MIXPEEK_PRIVATE_KEY (what you use to call THIS endpoint):
       - Static, hardcoded token shared between studio proxy and backend
       - Used ONLY for server-to-server /v1/private/* endpoint calls
       - Never changes, never stored in database
       - Never used by frontend UI
       - Example: xnefritAiaKQiddNL3ZHWEN4cHWLsCkwEycUDLU2wLekQEuf

    2. Organization API Key (what THIS endpoint creates and returns):
       - Created ONCE per organization with ADMIN permissions
       - Used by frontend UI for ALL /v1/* API calls
       - Named \"admin-key\" and stored in database (hashed)
       - Plaintext returned ONCE on creation
       - 🔒 PROTECTED: Users CANNOT delete, rotate, or change permissions on this key
       - Example: sk_kbHvXHAySDUrzrPo2ajwmqBAXJ...

    This endpoint creates an Organization API key (type #2) that the frontend will use.
    It does NOT create, modify, or touch the MIXPEEK_PRIVATE_KEY (type #1).

    ⚠️ The plaintext key is only returned ONCE on creation - store it in localStorage!
    ✅ If called when key exists: Revokes old key and returns a new one (idempotent)

    Args:
        organization_id (str):
        user_email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPostResponseCreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPost | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        user_email=user_email,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    user_email: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    CreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPostResponseCreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPost
    | ErrorResponse
    | HTTPValidationError
    | None
):
    r"""Create Bootstrap Api Key

     Create the organization's primary API key (requires MIXPEEK_PRIVATE_KEY).

    🔑 IMPORTANT - Two Different Keys (DO NOT CONFUSE):

    1. MIXPEEK_PRIVATE_KEY (what you use to call THIS endpoint):
       - Static, hardcoded token shared between studio proxy and backend
       - Used ONLY for server-to-server /v1/private/* endpoint calls
       - Never changes, never stored in database
       - Never used by frontend UI
       - Example: xnefritAiaKQiddNL3ZHWEN4cHWLsCkwEycUDLU2wLekQEuf

    2. Organization API Key (what THIS endpoint creates and returns):
       - Created ONCE per organization with ADMIN permissions
       - Used by frontend UI for ALL /v1/* API calls
       - Named \"admin-key\" and stored in database (hashed)
       - Plaintext returned ONCE on creation
       - 🔒 PROTECTED: Users CANNOT delete, rotate, or change permissions on this key
       - Example: sk_kbHvXHAySDUrzrPo2ajwmqBAXJ...

    This endpoint creates an Organization API key (type #2) that the frontend will use.
    It does NOT create, modify, or touch the MIXPEEK_PRIVATE_KEY (type #1).

    ⚠️ The plaintext key is only returned ONCE on creation - store it in localStorage!
    ✅ If called when key exists: Revokes old key and returns a new one (idempotent)

    Args:
        organization_id (str):
        user_email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPostResponseCreateBootstrapApiKeyV1PrivateOrganizationsOrganizationIdUsersUserEmailBootstrapKeyPost | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            user_email=user_email,
            client=client,
        )
    ).parsed
