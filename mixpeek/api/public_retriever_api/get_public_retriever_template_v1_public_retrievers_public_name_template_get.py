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
        "url": "/v1/public/retrievers/{public_name}/template".format(
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
    r""" Get Public Retriever Template

     Get retriever configuration as a reusable template.

    Returns the published retriever's configuration in a format that can be
    directly used to create your own retriever. This is perfect for discovering
    patterns and adapting them to your own data.

    **Authentication:**
    - NO authentication required - this endpoint is completely public
    - Anyone can get the template if they know the public_name

    **Use Case:**
    1. Browse public retrievers to find patterns you like
    2. GET this endpoint to get the full configuration
    3. Copy the config and modify for your needs (especially `collection_identifiers`)
    4. POST to `/v1/retrievers` to create your own retriever
    5. Optionally publish it with the same display_config

    **What's included:**
    - Retriever configuration (stages, input_schema, budget_limits)
    - Display configuration (for publishing with similar UI)
    - Original metadata for reference

    **What you need to change:**
    - `collection_identifiers`: Replace with your own collection IDs
    - `retriever_name`: Give it a unique name
    - Optionally modify stages, inputs, display_config as needed

    **Example:**
    ```bash
    # 1. Get the template
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/video-search/template\"

    # 2. Modify the response and create your own retriever
    curl -X POST \"https://api.mixpeek.com/v1/retrievers\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"retriever_name\": \"my_video_search\",
        \"collection_identifiers\": [\"my_videos\"],
        \"stages\": [...],  # From template
        \"input_schema\": {...},  # From template
        \"budget_limits\": {...},  # From template
        \"display_config\": {...}  # From template (optional)
      }'
    ```

    **Response includes:**
    - All retriever configuration fields
    - Display config for publishing (optional to use)
    - Source reference (where this template came from)

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
    r""" Get Public Retriever Template

     Get retriever configuration as a reusable template.

    Returns the published retriever's configuration in a format that can be
    directly used to create your own retriever. This is perfect for discovering
    patterns and adapting them to your own data.

    **Authentication:**
    - NO authentication required - this endpoint is completely public
    - Anyone can get the template if they know the public_name

    **Use Case:**
    1. Browse public retrievers to find patterns you like
    2. GET this endpoint to get the full configuration
    3. Copy the config and modify for your needs (especially `collection_identifiers`)
    4. POST to `/v1/retrievers` to create your own retriever
    5. Optionally publish it with the same display_config

    **What's included:**
    - Retriever configuration (stages, input_schema, budget_limits)
    - Display configuration (for publishing with similar UI)
    - Original metadata for reference

    **What you need to change:**
    - `collection_identifiers`: Replace with your own collection IDs
    - `retriever_name`: Give it a unique name
    - Optionally modify stages, inputs, display_config as needed

    **Example:**
    ```bash
    # 1. Get the template
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/video-search/template\"

    # 2. Modify the response and create your own retriever
    curl -X POST \"https://api.mixpeek.com/v1/retrievers\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"retriever_name\": \"my_video_search\",
        \"collection_identifiers\": [\"my_videos\"],
        \"stages\": [...],  # From template
        \"input_schema\": {...},  # From template
        \"budget_limits\": {...},  # From template
        \"display_config\": {...}  # From template (optional)
      }'
    ```

    **Response includes:**
    - All retriever configuration fields
    - Display config for publishing (optional to use)
    - Source reference (where this template came from)

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
    r""" Get Public Retriever Template

     Get retriever configuration as a reusable template.

    Returns the published retriever's configuration in a format that can be
    directly used to create your own retriever. This is perfect for discovering
    patterns and adapting them to your own data.

    **Authentication:**
    - NO authentication required - this endpoint is completely public
    - Anyone can get the template if they know the public_name

    **Use Case:**
    1. Browse public retrievers to find patterns you like
    2. GET this endpoint to get the full configuration
    3. Copy the config and modify for your needs (especially `collection_identifiers`)
    4. POST to `/v1/retrievers` to create your own retriever
    5. Optionally publish it with the same display_config

    **What's included:**
    - Retriever configuration (stages, input_schema, budget_limits)
    - Display configuration (for publishing with similar UI)
    - Original metadata for reference

    **What you need to change:**
    - `collection_identifiers`: Replace with your own collection IDs
    - `retriever_name`: Give it a unique name
    - Optionally modify stages, inputs, display_config as needed

    **Example:**
    ```bash
    # 1. Get the template
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/video-search/template\"

    # 2. Modify the response and create your own retriever
    curl -X POST \"https://api.mixpeek.com/v1/retrievers\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"retriever_name\": \"my_video_search\",
        \"collection_identifiers\": [\"my_videos\"],
        \"stages\": [...],  # From template
        \"input_schema\": {...},  # From template
        \"budget_limits\": {...},  # From template
        \"display_config\": {...}  # From template (optional)
      }'
    ```

    **Response includes:**
    - All retriever configuration fields
    - Display config for publishing (optional to use)
    - Source reference (where this template came from)

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
    r""" Get Public Retriever Template

     Get retriever configuration as a reusable template.

    Returns the published retriever's configuration in a format that can be
    directly used to create your own retriever. This is perfect for discovering
    patterns and adapting them to your own data.

    **Authentication:**
    - NO authentication required - this endpoint is completely public
    - Anyone can get the template if they know the public_name

    **Use Case:**
    1. Browse public retrievers to find patterns you like
    2. GET this endpoint to get the full configuration
    3. Copy the config and modify for your needs (especially `collection_identifiers`)
    4. POST to `/v1/retrievers` to create your own retriever
    5. Optionally publish it with the same display_config

    **What's included:**
    - Retriever configuration (stages, input_schema, budget_limits)
    - Display configuration (for publishing with similar UI)
    - Original metadata for reference

    **What you need to change:**
    - `collection_identifiers`: Replace with your own collection IDs
    - `retriever_name`: Give it a unique name
    - Optionally modify stages, inputs, display_config as needed

    **Example:**
    ```bash
    # 1. Get the template
    curl -X GET \"https://api.mixpeek.com/v1/public/retrievers/video-search/template\"

    # 2. Modify the response and create your own retriever
    curl -X POST \"https://api.mixpeek.com/v1/retrievers\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"retriever_name\": \"my_video_search\",
        \"collection_identifiers\": [\"my_videos\"],
        \"stages\": [...],  # From template
        \"input_schema\": {...},  # From template
        \"budget_limits\": {...},  # From template
        \"display_config\": {...}  # From template (optional)
      }'
    ```

    **Response includes:**
    - All retriever configuration fields
    - Display config for publishing (optional to use)
    - Source reference (where this template came from)

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
