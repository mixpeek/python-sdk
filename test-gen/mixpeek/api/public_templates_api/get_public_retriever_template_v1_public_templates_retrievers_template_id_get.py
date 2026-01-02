from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_template_model import BaseTemplateModel
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    template_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/public/templates/retrievers/{template_id}".format(
            template_id=quote(str(template_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BaseTemplateModel | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BaseTemplateModel.from_dict(response.json())

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
) -> Response[BaseTemplateModel | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[BaseTemplateModel | ErrorResponse | HTTPValidationError]:
    """Get Public Retriever Template

     Get public retriever template details (no authentication required).

    Returns template only if marked as public.

    Args:
        template_id (str): Template ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BaseTemplateModel | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> BaseTemplateModel | ErrorResponse | HTTPValidationError | None:
    """Get Public Retriever Template

     Get public retriever template details (no authentication required).

    Returns template only if marked as public.

    Args:
        template_id (str): Template ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BaseTemplateModel | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        template_id=template_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[BaseTemplateModel | ErrorResponse | HTTPValidationError]:
    """Get Public Retriever Template

     Get public retriever template details (no authentication required).

    Returns template only if marked as public.

    Args:
        template_id (str): Template ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BaseTemplateModel | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> BaseTemplateModel | ErrorResponse | HTTPValidationError | None:
    """Get Public Retriever Template

     Get public retriever template details (no authentication required).

    Returns template only if marked as public.

    Args:
        template_id (str): Template ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BaseTemplateModel | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            client=client,
        )
    ).parsed
