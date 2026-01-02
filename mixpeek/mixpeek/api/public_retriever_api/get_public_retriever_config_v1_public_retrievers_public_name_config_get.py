from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    public_name: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/public/retrievers/{public_name}/config".format(
            public_name=quote(str(public_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | None:
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
) -> Response[ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | HTTPValidationError]:
    r"""Get Public Retriever Config

     Get display configuration for public page rendering.

    Returns the UI configuration needed to render the public search interface.
    Used by the frontend app at apps.mixpeek.com to dynamically build the UI.

    **Authentication:**
    - NO authentication required - this endpoint is public
    - Anyone can access the config if they know the public_name
    - The config includes the public_api_key needed for execute/interact endpoints

    **Response includes:**
    - Display config (logo, theme, components, field rendering)
    - Title and description
    - Password protection status
    - Public API key for subsequent authenticated requests

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/video-search/config\"
    ```

    Args:
        public_name (str): Public name of the published retriever

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        public_name=public_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | HTTPValidationError | None:
    r"""Get Public Retriever Config

     Get display configuration for public page rendering.

    Returns the UI configuration needed to render the public search interface.
    Used by the frontend app at apps.mixpeek.com to dynamically build the UI.

    **Authentication:**
    - NO authentication required - this endpoint is public
    - Anyone can access the config if they know the public_name
    - The config includes the public_api_key needed for execute/interact endpoints

    **Response includes:**
    - Display config (logo, theme, components, field rendering)
    - Title and description
    - Password protection status
    - Public API key for subsequent authenticated requests

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/video-search/config\"
    ```

    Args:
        public_name (str): Public name of the published retriever

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        public_name=public_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | HTTPValidationError]:
    r"""Get Public Retriever Config

     Get display configuration for public page rendering.

    Returns the UI configuration needed to render the public search interface.
    Used by the frontend app at apps.mixpeek.com to dynamically build the UI.

    **Authentication:**
    - NO authentication required - this endpoint is public
    - Anyone can access the config if they know the public_name
    - The config includes the public_api_key needed for execute/interact endpoints

    **Response includes:**
    - Display config (logo, theme, components, field rendering)
    - Title and description
    - Password protection status
    - Public API key for subsequent authenticated requests

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/video-search/config\"
    ```

    Args:
        public_name (str): Public name of the published retriever

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        public_name=public_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | HTTPValidationError | None:
    r"""Get Public Retriever Config

     Get display configuration for public page rendering.

    Returns the UI configuration needed to render the public search interface.
    Used by the frontend app at apps.mixpeek.com to dynamically build the UI.

    **Authentication:**
    - NO authentication required - this endpoint is public
    - Anyone can access the config if they know the public_name
    - The config includes the public_api_key needed for execute/interact endpoints

    **Response includes:**
    - Display config (logo, theme, components, field rendering)
    - Title and description
    - Password protection status
    - Public API key for subsequent authenticated requests

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/video-search/config\"
    ```

    Args:
        public_name (str): Public name of the published retriever

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            public_name=public_name,
            client=client,
        )
    ).parsed
