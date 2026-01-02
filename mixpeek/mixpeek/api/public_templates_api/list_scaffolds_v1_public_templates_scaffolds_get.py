from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_template_model import BaseTemplateModel
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: None | str | Unset = UNSET,
    is_active: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_category: None | str | Unset
    if isinstance(category, Unset):
        json_category = UNSET
    else:
        json_category = category
    params["category"] = json_category

    params["is_active"] = is_active

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/public/templates/scaffolds",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | list[BaseTemplateModel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BaseTemplateModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[ErrorResponse | HTTPValidationError | list[BaseTemplateModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    is_active: bool | Unset = True,
) -> Response[ErrorResponse | HTTPValidationError | list[BaseTemplateModel]]:
    r"""List Scaffolds

     List available scaffold templates (public, no auth required).

    Scaffolds are pre-configured templates that create complete infrastructure:
    - Namespace with feature extractors
    - Bucket with data schema
    - Collection with processing config
    - Retriever with search pipeline

    **Categories:**
    - `media` - Video, image, podcast search
    - `documents` - Document Q&A, RAG
    - `ecommerce` - Product catalog search

    **To instantiate (requires auth):**
    ```
    POST /v1/templates/scaffolds/{template_id}/instantiate
    {\"namespace_name\": \"my_app\"}
    ```

    Args:
        category (None | str | Unset): Filter by category (media, documents, ecommerce)
        is_active (bool | Unset): Only show active templates Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | list[BaseTemplateModel]]
    """

    kwargs = _get_kwargs(
        category=category,
        is_active=is_active,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    is_active: bool | Unset = True,
) -> ErrorResponse | HTTPValidationError | list[BaseTemplateModel] | None:
    r"""List Scaffolds

     List available scaffold templates (public, no auth required).

    Scaffolds are pre-configured templates that create complete infrastructure:
    - Namespace with feature extractors
    - Bucket with data schema
    - Collection with processing config
    - Retriever with search pipeline

    **Categories:**
    - `media` - Video, image, podcast search
    - `documents` - Document Q&A, RAG
    - `ecommerce` - Product catalog search

    **To instantiate (requires auth):**
    ```
    POST /v1/templates/scaffolds/{template_id}/instantiate
    {\"namespace_name\": \"my_app\"}
    ```

    Args:
        category (None | str | Unset): Filter by category (media, documents, ecommerce)
        is_active (bool | Unset): Only show active templates Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | list[BaseTemplateModel]
    """

    return sync_detailed(
        client=client,
        category=category,
        is_active=is_active,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    is_active: bool | Unset = True,
) -> Response[ErrorResponse | HTTPValidationError | list[BaseTemplateModel]]:
    r"""List Scaffolds

     List available scaffold templates (public, no auth required).

    Scaffolds are pre-configured templates that create complete infrastructure:
    - Namespace with feature extractors
    - Bucket with data schema
    - Collection with processing config
    - Retriever with search pipeline

    **Categories:**
    - `media` - Video, image, podcast search
    - `documents` - Document Q&A, RAG
    - `ecommerce` - Product catalog search

    **To instantiate (requires auth):**
    ```
    POST /v1/templates/scaffolds/{template_id}/instantiate
    {\"namespace_name\": \"my_app\"}
    ```

    Args:
        category (None | str | Unset): Filter by category (media, documents, ecommerce)
        is_active (bool | Unset): Only show active templates Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | list[BaseTemplateModel]]
    """

    kwargs = _get_kwargs(
        category=category,
        is_active=is_active,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    is_active: bool | Unset = True,
) -> ErrorResponse | HTTPValidationError | list[BaseTemplateModel] | None:
    r"""List Scaffolds

     List available scaffold templates (public, no auth required).

    Scaffolds are pre-configured templates that create complete infrastructure:
    - Namespace with feature extractors
    - Bucket with data schema
    - Collection with processing config
    - Retriever with search pipeline

    **Categories:**
    - `media` - Video, image, podcast search
    - `documents` - Document Q&A, RAG
    - `ecommerce` - Product catalog search

    **To instantiate (requires auth):**
    ```
    POST /v1/templates/scaffolds/{template_id}/instantiate
    {\"namespace_name\": \"my_app\"}
    ```

    Args:
        category (None | str | Unset): Filter by category (media, documents, ecommerce)
        is_active (bool | Unset): Only show active templates Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | list[BaseTemplateModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            is_active=is_active,
        )
    ).parsed
