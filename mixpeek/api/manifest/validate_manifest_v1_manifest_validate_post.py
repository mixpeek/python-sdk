from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_validate_manifest_v1_manifest_validate_post import BodyValidateManifestV1ManifestValidatePost
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.validate_result import ValidateResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyValidateManifestV1ManifestValidatePost,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/manifest/validate",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | ValidateResult | None:
    if response.status_code == 200:
        response_200 = ValidateResult.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | ValidateResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyValidateManifestV1ManifestValidatePost,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ValidateResult]:
    r""" Validate Manifest

     Validate a YAML manifest without applying.

    Checks:
    - YAML syntax validity
    - Schema validation against manifest models
    - Cross-resource reference validation
    - Dependency resolution (no circular dependencies)
    - Secret reference existence

    Returns detailed validation results including:
    - Resource counts by type
    - Missing secrets that need to be configured
    - Validation errors and warnings

    **Example:**
    ```bash
    curl -X POST /v1/manifest/validate \
      -H \"Authorization: Bearer $API_KEY\" \
      -F \"manifest_file=@mixpeek.yaml\"
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (BodyValidateManifestV1ManifestValidatePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ValidateResult]
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
    body: BodyValidateManifestV1ManifestValidatePost,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ValidateResult | None:
    r""" Validate Manifest

     Validate a YAML manifest without applying.

    Checks:
    - YAML syntax validity
    - Schema validation against manifest models
    - Cross-resource reference validation
    - Dependency resolution (no circular dependencies)
    - Secret reference existence

    Returns detailed validation results including:
    - Resource counts by type
    - Missing secrets that need to be configured
    - Validation errors and warnings

    **Example:**
    ```bash
    curl -X POST /v1/manifest/validate \
      -H \"Authorization: Bearer $API_KEY\" \
      -F \"manifest_file=@mixpeek.yaml\"
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (BodyValidateManifestV1ManifestValidatePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ValidateResult
     """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyValidateManifestV1ManifestValidatePost,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | ValidateResult]:
    r""" Validate Manifest

     Validate a YAML manifest without applying.

    Checks:
    - YAML syntax validity
    - Schema validation against manifest models
    - Cross-resource reference validation
    - Dependency resolution (no circular dependencies)
    - Secret reference existence

    Returns detailed validation results including:
    - Resource counts by type
    - Missing secrets that need to be configured
    - Validation errors and warnings

    **Example:**
    ```bash
    curl -X POST /v1/manifest/validate \
      -H \"Authorization: Bearer $API_KEY\" \
      -F \"manifest_file=@mixpeek.yaml\"
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (BodyValidateManifestV1ManifestValidatePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | ValidateResult]
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
    body: BodyValidateManifestV1ManifestValidatePost,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | ValidateResult | None:
    r""" Validate Manifest

     Validate a YAML manifest without applying.

    Checks:
    - YAML syntax validity
    - Schema validation against manifest models
    - Cross-resource reference validation
    - Dependency resolution (no circular dependencies)
    - Secret reference existence

    Returns detailed validation results including:
    - Resource counts by type
    - Missing secrets that need to be configured
    - Validation errors and warnings

    **Example:**
    ```bash
    curl -X POST /v1/manifest/validate \
      -H \"Authorization: Bearer $API_KEY\" \
      -F \"manifest_file=@mixpeek.yaml\"
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (BodyValidateManifestV1ManifestValidatePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | ValidateResult
     """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
