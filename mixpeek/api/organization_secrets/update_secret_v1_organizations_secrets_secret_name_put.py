from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.secret_response import SecretResponse
from ...models.update_secret_request import UpdateSecretRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    secret_name: str,
    *,
    body: UpdateSecretRequest,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/organizations/secrets/{secret_name}".format(
            secret_name=quote(str(secret_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | SecretResponse | None:
    if response.status_code == 200:
        response_200 = SecretResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | SecretResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    secret_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSecretRequest,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | SecretResponse]:
    """Update Secret

     Update an existing secret in organization vault.

    **Security**:
    - Replaces existing encrypted value with new encrypted value
    - Old value is permanently overwritten
    - No history or audit trail of previous values

    **Use Cases**:
    - Rotate API keys periodically
    - Update expired tokens
    - Change credentials after security incident

    Args:
        secret_name (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (UpdateSecretRequest): Request to update an existing secret in the organization
            vault.

            Updates the encrypted value of an existing secret. The old value is
            permanently overwritten with no history or rollback capability.

            **Use Cases**:
            - Rotate API keys periodically for security
            - Update expired tokens
            - Change credentials after security incident
            - Switch from test to production keys

            **Security**:
            - Old value is permanently overwritten (no history)
            - New value is encrypted before storage
            - No rollback or undo capability
            - Update is logged for audit trail

            **Requirements**:
            - secret_value: REQUIRED, new plaintext value
            - Secret must already exist (use POST to create)

            **Permissions**: Requires ADMIN permission to update secrets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SecretResponse]
    """

    kwargs = _get_kwargs(
        secret_name=secret_name,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    secret_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSecretRequest,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | SecretResponse | None:
    """Update Secret

     Update an existing secret in organization vault.

    **Security**:
    - Replaces existing encrypted value with new encrypted value
    - Old value is permanently overwritten
    - No history or audit trail of previous values

    **Use Cases**:
    - Rotate API keys periodically
    - Update expired tokens
    - Change credentials after security incident

    Args:
        secret_name (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (UpdateSecretRequest): Request to update an existing secret in the organization
            vault.

            Updates the encrypted value of an existing secret. The old value is
            permanently overwritten with no history or rollback capability.

            **Use Cases**:
            - Rotate API keys periodically for security
            - Update expired tokens
            - Change credentials after security incident
            - Switch from test to production keys

            **Security**:
            - Old value is permanently overwritten (no history)
            - New value is encrypted before storage
            - No rollback or undo capability
            - Update is logged for audit trail

            **Requirements**:
            - secret_value: REQUIRED, new plaintext value
            - Secret must already exist (use POST to create)

            **Permissions**: Requires ADMIN permission to update secrets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SecretResponse
    """

    return sync_detailed(
        secret_name=secret_name,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    secret_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSecretRequest,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | SecretResponse]:
    """Update Secret

     Update an existing secret in organization vault.

    **Security**:
    - Replaces existing encrypted value with new encrypted value
    - Old value is permanently overwritten
    - No history or audit trail of previous values

    **Use Cases**:
    - Rotate API keys periodically
    - Update expired tokens
    - Change credentials after security incident

    Args:
        secret_name (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (UpdateSecretRequest): Request to update an existing secret in the organization
            vault.

            Updates the encrypted value of an existing secret. The old value is
            permanently overwritten with no history or rollback capability.

            **Use Cases**:
            - Rotate API keys periodically for security
            - Update expired tokens
            - Change credentials after security incident
            - Switch from test to production keys

            **Security**:
            - Old value is permanently overwritten (no history)
            - New value is encrypted before storage
            - No rollback or undo capability
            - Update is logged for audit trail

            **Requirements**:
            - secret_value: REQUIRED, new plaintext value
            - Secret must already exist (use POST to create)

            **Permissions**: Requires ADMIN permission to update secrets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SecretResponse]
    """

    kwargs = _get_kwargs(
        secret_name=secret_name,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    secret_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSecretRequest,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | SecretResponse | None:
    """Update Secret

     Update an existing secret in organization vault.

    **Security**:
    - Replaces existing encrypted value with new encrypted value
    - Old value is permanently overwritten
    - No history or audit trail of previous values

    **Use Cases**:
    - Rotate API keys periodically
    - Update expired tokens
    - Change credentials after security incident

    Args:
        secret_name (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (UpdateSecretRequest): Request to update an existing secret in the organization
            vault.

            Updates the encrypted value of an existing secret. The old value is
            permanently overwritten with no history or rollback capability.

            **Use Cases**:
            - Rotate API keys periodically for security
            - Update expired tokens
            - Change credentials after security incident
            - Switch from test to production keys

            **Security**:
            - Old value is permanently overwritten (no history)
            - New value is encrypted before storage
            - No rollback or undo capability
            - Update is logged for audit trail

            **Requirements**:
            - secret_value: REQUIRED, new plaintext value
            - Secret must already exist (use POST to create)

            **Permissions**: Requires ADMIN permission to update secrets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SecretResponse
    """

    return (
        await asyncio_detailed(
            secret_name=secret_name,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
