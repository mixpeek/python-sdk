from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    description: str,
    manifest_name: str | Unset = "generated-manifest",
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["description"] = description

    params["manifest_name"] = manifest_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/manifest/generate",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    description: str,
    manifest_name: str | Unset = "generated-manifest",
    authorization: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    r""" Generate Manifest

     Generate a manifest from natural language description.

        Uses AI to create a valid YAML manifest from a natural language description
        of desired resources. The generated manifest can be reviewed and applied.

        **Example:**
        ```bash
        curl -X POST /v1/manifest/generate \
          -H \"Authorization: Bearer $API_KEY\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"description\": \"I need a bucket of images that feeds into a multimodal extractor and a
    retriever\",
            \"manifest_name\": \"image-search-setup\"
          }'
        ```

        **Response:**
        ```json
        {
          \"manifest\": \"version: '1.0'
    metadata:
      name: image-search-setup
    ...\",
          \"format\": \"yaml\",
          \"manifest_name\": \"image-search-setup\",
          \"description\": \"I need a bucket of images...\"
        }
        ```

        **Next Steps:**
        1. Review the generated manifest
        2. Apply it using POST /v1/manifest/apply

    Args:
        description (str):
        manifest_name (str | Unset):  Default: 'generated-manifest'.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        description=description,
        manifest_name=manifest_name,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    description: str,
    manifest_name: str | Unset = "generated-manifest",
    authorization: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    r""" Generate Manifest

     Generate a manifest from natural language description.

        Uses AI to create a valid YAML manifest from a natural language description
        of desired resources. The generated manifest can be reviewed and applied.

        **Example:**
        ```bash
        curl -X POST /v1/manifest/generate \
          -H \"Authorization: Bearer $API_KEY\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"description\": \"I need a bucket of images that feeds into a multimodal extractor and a
    retriever\",
            \"manifest_name\": \"image-search-setup\"
          }'
        ```

        **Response:**
        ```json
        {
          \"manifest\": \"version: '1.0'
    metadata:
      name: image-search-setup
    ...\",
          \"format\": \"yaml\",
          \"manifest_name\": \"image-search-setup\",
          \"description\": \"I need a bucket of images...\"
        }
        ```

        **Next Steps:**
        1. Review the generated manifest
        2. Apply it using POST /v1/manifest/apply

    Args:
        description (str):
        manifest_name (str | Unset):  Default: 'generated-manifest'.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
     """

    return sync_detailed(
        client=client,
        description=description,
        manifest_name=manifest_name,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    description: str,
    manifest_name: str | Unset = "generated-manifest",
    authorization: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    r""" Generate Manifest

     Generate a manifest from natural language description.

        Uses AI to create a valid YAML manifest from a natural language description
        of desired resources. The generated manifest can be reviewed and applied.

        **Example:**
        ```bash
        curl -X POST /v1/manifest/generate \
          -H \"Authorization: Bearer $API_KEY\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"description\": \"I need a bucket of images that feeds into a multimodal extractor and a
    retriever\",
            \"manifest_name\": \"image-search-setup\"
          }'
        ```

        **Response:**
        ```json
        {
          \"manifest\": \"version: '1.0'
    metadata:
      name: image-search-setup
    ...\",
          \"format\": \"yaml\",
          \"manifest_name\": \"image-search-setup\",
          \"description\": \"I need a bucket of images...\"
        }
        ```

        **Next Steps:**
        1. Review the generated manifest
        2. Apply it using POST /v1/manifest/apply

    Args:
        description (str):
        manifest_name (str | Unset):  Default: 'generated-manifest'.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        description=description,
        manifest_name=manifest_name,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    description: str,
    manifest_name: str | Unset = "generated-manifest",
    authorization: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    r""" Generate Manifest

     Generate a manifest from natural language description.

        Uses AI to create a valid YAML manifest from a natural language description
        of desired resources. The generated manifest can be reviewed and applied.

        **Example:**
        ```bash
        curl -X POST /v1/manifest/generate \
          -H \"Authorization: Bearer $API_KEY\" \
          -H \"Content-Type: application/json\" \
          -d '{
            \"description\": \"I need a bucket of images that feeds into a multimodal extractor and a
    retriever\",
            \"manifest_name\": \"image-search-setup\"
          }'
        ```

        **Response:**
        ```json
        {
          \"manifest\": \"version: '1.0'
    metadata:
      name: image-search-setup
    ...\",
          \"format\": \"yaml\",
          \"manifest_name\": \"image-search-setup\",
          \"description\": \"I need a bucket of images...\"
        }
        ```

        **Next Steps:**
        1. Review the generated manifest
        2. Apply it using POST /v1/manifest/apply

    Args:
        description (str):
        manifest_name (str | Unset):  Default: 'generated-manifest'.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
     """

    return (
        await asyncio_detailed(
            client=client,
            description=description,
            manifest_name=manifest_name,
            authorization=authorization,
        )
    ).parsed
