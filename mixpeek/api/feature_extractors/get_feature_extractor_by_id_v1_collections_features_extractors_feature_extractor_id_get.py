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
    feature_extractor_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collections/features/extractors/{feature_extractor_id}".format(
            feature_extractor_id=quote(str(feature_extractor_id), safe=""),
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
    feature_extractor_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Get Feature Extractor by Name

     Get detailed information about a specific feature extractor by its name

    Args:
        feature_extractor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        feature_extractor_id=feature_extractor_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    feature_extractor_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | HTTPValidationError | None:
    """Get Feature Extractor by Name

     Get detailed information about a specific feature extractor by its name

    Args:
        feature_extractor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        feature_extractor_id=feature_extractor_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    feature_extractor_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Get Feature Extractor by Name

     Get detailed information about a specific feature extractor by its name

    Args:
        feature_extractor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        feature_extractor_id=feature_extractor_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    feature_extractor_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ErrorResponse | HTTPValidationError | None:
    """Get Feature Extractor by Name

     Get detailed information about a specific feature extractor by its name

    Args:
        feature_extractor_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            feature_extractor_id=feature_extractor_id,
            client=client,
        )
    ).parsed
