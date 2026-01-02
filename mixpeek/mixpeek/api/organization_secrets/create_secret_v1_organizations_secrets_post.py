from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_secret_request import CreateSecretRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.secret_response import SecretResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateSecretRequest,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/organizations/secrets",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | SecretResponse | None:
    if response.status_code == 201:
        response_201 = SecretResponse.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient | Client,
    body: CreateSecretRequest,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | SecretResponse]:
    """Create Secret

     Create a new secret in organization vault.

    **Security**:
    - Secret value is encrypted at rest using Fernet encryption
    - Encrypted using ENCRYPTION_KEY from environment
    - Decrypted value is NEVER returned in API responses
    - Only secret names are exposed in list operations

    **Use Cases**:
    - Store API keys for external services (Stripe, GitHub, etc.)
    - Store authentication tokens for api_call retriever stage
    - Store credentials for third-party integrations

    **Important**:
    - Secret names must be unique within organization
    - Use update endpoint to modify existing secrets
    - Delete and recreate if you forget the value

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (CreateSecretRequest): Request to create a new secret in the organization vault.

            Secrets are encrypted at rest using Fernet encryption and stored in the
            organization document. Use secrets to securely store API keys, tokens,
            and credentials for external services.

            **Use Cases**:
            - Store API keys for Stripe, GitHub, OpenAI, etc.
            - Manage authentication tokens for api_call retriever stage
            - Store credentials for third-party integrations

            **Security**:
            - Secret values are encrypted using ENCRYPTION_KEY from environment
            - Decrypted values are NEVER returned in API responses
            - Only secret names are exposed in list operations
            - Access is logged for audit trail

            **Requirements**:
            - secret_name: REQUIRED, must be unique within organization
            - secret_value: REQUIRED, plaintext value to encrypt

            **Permissions**: Requires ADMIN permission to create secrets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SecretResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSecretRequest,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | SecretResponse | None:
    """Create Secret

     Create a new secret in organization vault.

    **Security**:
    - Secret value is encrypted at rest using Fernet encryption
    - Encrypted using ENCRYPTION_KEY from environment
    - Decrypted value is NEVER returned in API responses
    - Only secret names are exposed in list operations

    **Use Cases**:
    - Store API keys for external services (Stripe, GitHub, etc.)
    - Store authentication tokens for api_call retriever stage
    - Store credentials for third-party integrations

    **Important**:
    - Secret names must be unique within organization
    - Use update endpoint to modify existing secrets
    - Delete and recreate if you forget the value

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (CreateSecretRequest): Request to create a new secret in the organization vault.

            Secrets are encrypted at rest using Fernet encryption and stored in the
            organization document. Use secrets to securely store API keys, tokens,
            and credentials for external services.

            **Use Cases**:
            - Store API keys for Stripe, GitHub, OpenAI, etc.
            - Manage authentication tokens for api_call retriever stage
            - Store credentials for third-party integrations

            **Security**:
            - Secret values are encrypted using ENCRYPTION_KEY from environment
            - Decrypted values are NEVER returned in API responses
            - Only secret names are exposed in list operations
            - Access is logged for audit trail

            **Requirements**:
            - secret_name: REQUIRED, must be unique within organization
            - secret_value: REQUIRED, plaintext value to encrypt

            **Permissions**: Requires ADMIN permission to create secrets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SecretResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSecretRequest,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | SecretResponse]:
    """Create Secret

     Create a new secret in organization vault.

    **Security**:
    - Secret value is encrypted at rest using Fernet encryption
    - Encrypted using ENCRYPTION_KEY from environment
    - Decrypted value is NEVER returned in API responses
    - Only secret names are exposed in list operations

    **Use Cases**:
    - Store API keys for external services (Stripe, GitHub, etc.)
    - Store authentication tokens for api_call retriever stage
    - Store credentials for third-party integrations

    **Important**:
    - Secret names must be unique within organization
    - Use update endpoint to modify existing secrets
    - Delete and recreate if you forget the value

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (CreateSecretRequest): Request to create a new secret in the organization vault.

            Secrets are encrypted at rest using Fernet encryption and stored in the
            organization document. Use secrets to securely store API keys, tokens,
            and credentials for external services.

            **Use Cases**:
            - Store API keys for Stripe, GitHub, OpenAI, etc.
            - Manage authentication tokens for api_call retriever stage
            - Store credentials for third-party integrations

            **Security**:
            - Secret values are encrypted using ENCRYPTION_KEY from environment
            - Decrypted values are NEVER returned in API responses
            - Only secret names are exposed in list operations
            - Access is logged for audit trail

            **Requirements**:
            - secret_name: REQUIRED, must be unique within organization
            - secret_value: REQUIRED, plaintext value to encrypt

            **Permissions**: Requires ADMIN permission to create secrets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SecretResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateSecretRequest,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | SecretResponse | None:
    """Create Secret

     Create a new secret in organization vault.

    **Security**:
    - Secret value is encrypted at rest using Fernet encryption
    - Encrypted using ENCRYPTION_KEY from environment
    - Decrypted value is NEVER returned in API responses
    - Only secret names are exposed in list operations

    **Use Cases**:
    - Store API keys for external services (Stripe, GitHub, etc.)
    - Store authentication tokens for api_call retriever stage
    - Store credentials for third-party integrations

    **Important**:
    - Secret names must be unique within organization
    - Use update endpoint to modify existing secrets
    - Delete and recreate if you forget the value

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (CreateSecretRequest): Request to create a new secret in the organization vault.

            Secrets are encrypted at rest using Fernet encryption and stored in the
            organization document. Use secrets to securely store API keys, tokens,
            and credentials for external services.

            **Use Cases**:
            - Store API keys for Stripe, GitHub, OpenAI, etc.
            - Manage authentication tokens for api_call retriever stage
            - Store credentials for third-party integrations

            **Security**:
            - Secret values are encrypted using ENCRYPTION_KEY from environment
            - Decrypted values are NEVER returned in API responses
            - Only secret names are exposed in list operations
            - Access is logged for audit trail

            **Requirements**:
            - secret_name: REQUIRED, must be unique within organization
            - secret_value: REQUIRED, plaintext value to encrypt

            **Permissions**: Requires ADMIN permission to create secrets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SecretResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
