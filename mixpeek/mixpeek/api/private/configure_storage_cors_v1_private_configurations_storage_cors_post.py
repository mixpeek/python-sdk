from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.configure_cors_request import ConfigureCORSRequest
from ...models.cors_configuration_response import CORSConfigurationResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: ConfigureCORSRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/private/configurations/storage/cors",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CORSConfigurationResponse | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CORSConfigurationResponse.from_dict(response.json())

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
) -> Response[CORSConfigurationResponse | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConfigureCORSRequest,
) -> Response[CORSConfigurationResponse | ErrorResponse | HTTPValidationError]:
    """Configure CORS for Object Storage

     Configure CORS (Cross-Origin Resource Sharing) on the object storage bucket.

        **Why is this needed?**
        When using presigned URLs for browser-based uploads, browsers enforce CORS policies.
        Without proper CORS configuration, uploads from the frontend will fail with CORS errors.

        **When to use this:**
        - During initial setup of the Mixpeek platform
        - When adding new frontend domains (development, staging, production)
        - When troubleshooting browser upload failures

        **Important notes:**
        - This is an admin-only operation (requires admin API key)
        - CORS is configured on the entire object storage bucket (not per-namespace)
        - Changes take effect immediately but may be cached by browsers
        - This works for any object storage provider (S3, LocalStack, GCS)

        **Common use cases:**
        1. Local development: Configure localhost origins
        2. Production: Configure production domain origins
        3. Multi-environment: Configure multiple origins for dev/staging/prod

    Args:
        body (ConfigureCORSRequest): Request model for configuring CORS on object storage.

            This allows administrators to configure CORS policies on the object storage
            bucket to enable browser-based uploads using presigned URLs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CORSConfigurationResponse | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ConfigureCORSRequest,
) -> CORSConfigurationResponse | ErrorResponse | HTTPValidationError | None:
    """Configure CORS for Object Storage

     Configure CORS (Cross-Origin Resource Sharing) on the object storage bucket.

        **Why is this needed?**
        When using presigned URLs for browser-based uploads, browsers enforce CORS policies.
        Without proper CORS configuration, uploads from the frontend will fail with CORS errors.

        **When to use this:**
        - During initial setup of the Mixpeek platform
        - When adding new frontend domains (development, staging, production)
        - When troubleshooting browser upload failures

        **Important notes:**
        - This is an admin-only operation (requires admin API key)
        - CORS is configured on the entire object storage bucket (not per-namespace)
        - Changes take effect immediately but may be cached by browsers
        - This works for any object storage provider (S3, LocalStack, GCS)

        **Common use cases:**
        1. Local development: Configure localhost origins
        2. Production: Configure production domain origins
        3. Multi-environment: Configure multiple origins for dev/staging/prod

    Args:
        body (ConfigureCORSRequest): Request model for configuring CORS on object storage.

            This allows administrators to configure CORS policies on the object storage
            bucket to enable browser-based uploads using presigned URLs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CORSConfigurationResponse | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConfigureCORSRequest,
) -> Response[CORSConfigurationResponse | ErrorResponse | HTTPValidationError]:
    """Configure CORS for Object Storage

     Configure CORS (Cross-Origin Resource Sharing) on the object storage bucket.

        **Why is this needed?**
        When using presigned URLs for browser-based uploads, browsers enforce CORS policies.
        Without proper CORS configuration, uploads from the frontend will fail with CORS errors.

        **When to use this:**
        - During initial setup of the Mixpeek platform
        - When adding new frontend domains (development, staging, production)
        - When troubleshooting browser upload failures

        **Important notes:**
        - This is an admin-only operation (requires admin API key)
        - CORS is configured on the entire object storage bucket (not per-namespace)
        - Changes take effect immediately but may be cached by browsers
        - This works for any object storage provider (S3, LocalStack, GCS)

        **Common use cases:**
        1. Local development: Configure localhost origins
        2. Production: Configure production domain origins
        3. Multi-environment: Configure multiple origins for dev/staging/prod

    Args:
        body (ConfigureCORSRequest): Request model for configuring CORS on object storage.

            This allows administrators to configure CORS policies on the object storage
            bucket to enable browser-based uploads using presigned URLs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CORSConfigurationResponse | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ConfigureCORSRequest,
) -> CORSConfigurationResponse | ErrorResponse | HTTPValidationError | None:
    """Configure CORS for Object Storage

     Configure CORS (Cross-Origin Resource Sharing) on the object storage bucket.

        **Why is this needed?**
        When using presigned URLs for browser-based uploads, browsers enforce CORS policies.
        Without proper CORS configuration, uploads from the frontend will fail with CORS errors.

        **When to use this:**
        - During initial setup of the Mixpeek platform
        - When adding new frontend domains (development, staging, production)
        - When troubleshooting browser upload failures

        **Important notes:**
        - This is an admin-only operation (requires admin API key)
        - CORS is configured on the entire object storage bucket (not per-namespace)
        - Changes take effect immediately but may be cached by browsers
        - This works for any object storage provider (S3, LocalStack, GCS)

        **Common use cases:**
        1. Local development: Configure localhost origins
        2. Production: Configure production domain origins
        3. Multi-environment: Configure multiple origins for dev/staging/prod

    Args:
        body (ConfigureCORSRequest): Request model for configuring CORS on object storage.

            This allows administrators to configure CORS policies on the object storage
            bucket to enable browser-based uploads using presigned URLs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CORSConfigurationResponse | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
