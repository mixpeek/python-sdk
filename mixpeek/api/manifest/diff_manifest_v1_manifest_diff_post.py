from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_diff_manifest_v1_manifest_diff_post import BodyDiffManifestV1ManifestDiffPost
from ...models.diff_result import DiffResult
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyDiffManifestV1ManifestDiffPost,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/manifest/diff",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DiffResult | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DiffResult.from_dict(response.json())

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
) -> Response[DiffResult | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyDiffManifestV1ManifestDiffPost,
    authorization: str | Unset = UNSET,
) -> Response[DiffResult | ErrorResponse | HTTPValidationError]:
    r""" Diff Manifest

     Compare a manifest file with current state.

    Shows resources that would be:
    - **Created**: In manifest but not in system
    - **In system only**: In system but not in manifest
    - **Different**: In both but with configuration differences

    This is useful for understanding what changes would occur
    before applying a manifest.

    **Example:**
    ```bash
    curl -X POST /v1/manifest/diff \
      -H \"Authorization: Bearer $API_KEY\" \
      -F \"manifest_file=@mixpeek.yaml\"
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (BodyDiffManifestV1ManifestDiffPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiffResult | ErrorResponse | HTTPValidationError]
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
    body: BodyDiffManifestV1ManifestDiffPost,
    authorization: str | Unset = UNSET,
) -> DiffResult | ErrorResponse | HTTPValidationError | None:
    r""" Diff Manifest

     Compare a manifest file with current state.

    Shows resources that would be:
    - **Created**: In manifest but not in system
    - **In system only**: In system but not in manifest
    - **Different**: In both but with configuration differences

    This is useful for understanding what changes would occur
    before applying a manifest.

    **Example:**
    ```bash
    curl -X POST /v1/manifest/diff \
      -H \"Authorization: Bearer $API_KEY\" \
      -F \"manifest_file=@mixpeek.yaml\"
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (BodyDiffManifestV1ManifestDiffPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiffResult | ErrorResponse | HTTPValidationError
     """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyDiffManifestV1ManifestDiffPost,
    authorization: str | Unset = UNSET,
) -> Response[DiffResult | ErrorResponse | HTTPValidationError]:
    r""" Diff Manifest

     Compare a manifest file with current state.

    Shows resources that would be:
    - **Created**: In manifest but not in system
    - **In system only**: In system but not in manifest
    - **Different**: In both but with configuration differences

    This is useful for understanding what changes would occur
    before applying a manifest.

    **Example:**
    ```bash
    curl -X POST /v1/manifest/diff \
      -H \"Authorization: Bearer $API_KEY\" \
      -F \"manifest_file=@mixpeek.yaml\"
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (BodyDiffManifestV1ManifestDiffPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiffResult | ErrorResponse | HTTPValidationError]
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
    body: BodyDiffManifestV1ManifestDiffPost,
    authorization: str | Unset = UNSET,
) -> DiffResult | ErrorResponse | HTTPValidationError | None:
    r""" Diff Manifest

     Compare a manifest file with current state.

    Shows resources that would be:
    - **Created**: In manifest but not in system
    - **In system only**: In system but not in manifest
    - **Different**: In both but with configuration differences

    This is useful for understanding what changes would occur
    before applying a manifest.

    **Example:**
    ```bash
    curl -X POST /v1/manifest/diff \
      -H \"Authorization: Bearer $API_KEY\" \
      -F \"manifest_file=@mixpeek.yaml\"
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (BodyDiffManifestV1ManifestDiffPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiffResult | ErrorResponse | HTTPValidationError
     """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
