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
    deep: bool | Unset = False,
    metrics: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["deep"] = deep

    params["metrics"] = metrics

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/health",
        "params": params,
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
    *,
    client: AuthenticatedClient | Client,
    deep: bool | Unset = False,
    metrics: bool | Unset = False,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Healthcheck

     Health check endpoint.

    Args:
        deep (bool | Unset):  Default: False.
        metrics (bool | Unset): Include Layer 2 protection metrics Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        deep=deep,
        metrics=metrics,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    deep: bool | Unset = False,
    metrics: bool | Unset = False,
) -> ErrorResponse | HTTPValidationError | None:
    """Healthcheck

     Health check endpoint.

    Args:
        deep (bool | Unset):  Default: False.
        metrics (bool | Unset): Include Layer 2 protection metrics Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        deep=deep,
        metrics=metrics,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    deep: bool | Unset = False,
    metrics: bool | Unset = False,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Healthcheck

     Health check endpoint.

    Args:
        deep (bool | Unset):  Default: False.
        metrics (bool | Unset): Include Layer 2 protection metrics Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        deep=deep,
        metrics=metrics,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    deep: bool | Unset = False,
    metrics: bool | Unset = False,
) -> ErrorResponse | HTTPValidationError | None:
    """Healthcheck

     Health check endpoint.

    Args:
        deep (bool | Unset):  Default: False.
        metrics (bool | Unset): Include Layer 2 protection metrics Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            deep=deep,
            metrics=metrics,
        )
    ).parsed
