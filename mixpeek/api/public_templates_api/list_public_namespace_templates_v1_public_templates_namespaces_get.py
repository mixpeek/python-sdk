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
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_category: None | str | Unset
    if isinstance(category, Unset):
        json_category = UNSET
    else:
        json_category = category
    params["category"] = json_category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/public/templates/namespaces",
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
) -> Response[ErrorResponse | HTTPValidationError | list[BaseTemplateModel]]:
    """List Public Namespace Templates

     List public namespace templates (no authentication required).

    Returns only templates marked as public (is_public=True).

    Args:
        category (None | str | Unset): Filter by category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | list[BaseTemplateModel]]
    """

    kwargs = _get_kwargs(
        category=category,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | list[BaseTemplateModel] | None:
    """List Public Namespace Templates

     List public namespace templates (no authentication required).

    Returns only templates marked as public (is_public=True).

    Args:
        category (None | str | Unset): Filter by category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | list[BaseTemplateModel]
    """

    return sync_detailed(
        client=client,
        category=category,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | list[BaseTemplateModel]]:
    """List Public Namespace Templates

     List public namespace templates (no authentication required).

    Returns only templates marked as public (is_public=True).

    Args:
        category (None | str | Unset): Filter by category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | list[BaseTemplateModel]]
    """

    kwargs = _get_kwargs(
        category=category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | list[BaseTemplateModel] | None:
    """List Public Namespace Templates

     List public namespace templates (no authentication required).

    Returns only templates marked as public (is_public=True).

    Args:
        category (None | str | Unset): Filter by category

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
        )
    ).parsed
