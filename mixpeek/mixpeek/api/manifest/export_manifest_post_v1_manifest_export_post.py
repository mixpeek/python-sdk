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
    body: list[str] | None | Unset = UNSET,
    manifest_name: str | Unset = "exported-manifest",
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["manifest_name"] = manifest_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/manifest/export",
        "params": params,
    }

    if isinstance(body, list):
        _kwargs["json"] = body

    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

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
    body: list[str] | None | Unset = UNSET,
    manifest_name: str | Unset = "exported-manifest",
    authorization: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    r""" Export Manifest Post

     Export current resources to a YAML manifest (POST version for agent tools).

    Same as GET /export but accepts parameters in JSON body instead of query params.
    Used by agent tools and programmatic API clients.

    **Example:**
    ```bash
    curl -X POST /v1/manifest/export \
      -H \"Authorization: Bearer $API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{\"namespace_ids\": [\"ns_abc123\"], \"manifest_name\": \"my-setup\"}'
    ```

    Args:
        manifest_name (str | Unset):  Default: 'exported-manifest'.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        body=body,
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
    body: list[str] | None | Unset = UNSET,
    manifest_name: str | Unset = "exported-manifest",
    authorization: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    r""" Export Manifest Post

     Export current resources to a YAML manifest (POST version for agent tools).

    Same as GET /export but accepts parameters in JSON body instead of query params.
    Used by agent tools and programmatic API clients.

    **Example:**
    ```bash
    curl -X POST /v1/manifest/export \
      -H \"Authorization: Bearer $API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{\"namespace_ids\": [\"ns_abc123\"], \"manifest_name\": \"my-setup\"}'
    ```

    Args:
        manifest_name (str | Unset):  Default: 'exported-manifest'.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
     """

    return sync_detailed(
        client=client,
        body=body,
        manifest_name=manifest_name,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[str] | None | Unset = UNSET,
    manifest_name: str | Unset = "exported-manifest",
    authorization: str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    r""" Export Manifest Post

     Export current resources to a YAML manifest (POST version for agent tools).

    Same as GET /export but accepts parameters in JSON body instead of query params.
    Used by agent tools and programmatic API clients.

    **Example:**
    ```bash
    curl -X POST /v1/manifest/export \
      -H \"Authorization: Bearer $API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{\"namespace_ids\": [\"ns_abc123\"], \"manifest_name\": \"my-setup\"}'
    ```

    Args:
        manifest_name (str | Unset):  Default: 'exported-manifest'.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        body=body,
        manifest_name=manifest_name,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[str] | None | Unset = UNSET,
    manifest_name: str | Unset = "exported-manifest",
    authorization: str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    r""" Export Manifest Post

     Export current resources to a YAML manifest (POST version for agent tools).

    Same as GET /export but accepts parameters in JSON body instead of query params.
    Used by agent tools and programmatic API clients.

    **Example:**
    ```bash
    curl -X POST /v1/manifest/export \
      -H \"Authorization: Bearer $API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{\"namespace_ids\": [\"ns_abc123\"], \"manifest_name\": \"my-setup\"}'
    ```

    Args:
        manifest_name (str | Unset):  Default: 'exported-manifest'.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (list[str] | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
     """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            manifest_name=manifest_name,
            authorization=authorization,
        )
    ).parsed
