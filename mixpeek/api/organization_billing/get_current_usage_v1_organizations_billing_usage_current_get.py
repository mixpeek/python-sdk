from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.current_usage_response import CurrentUsageResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/organizations/billing/usage/current",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CurrentUsageResponse | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CurrentUsageResponse.from_dict(response.json())

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
) -> Response[CurrentUsageResponse | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> Response[CurrentUsageResponse | ErrorResponse | HTTPValidationError]:
    r"""Get Current Usage

     Get current month usage.

    Returns credit consumption for the current billing period,
    estimated cost, and next invoice date.

    **Requirements:**
    - Read permission

    **Example:**
    ```python
    response = await client.get(\"/v1/organizations/billing/usage/current\")
    print(f\"Usage: {response['current_month_usage']} credits\")
    print(f\"Estimated cost: ${response['estimated_cost_usd']}\")
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CurrentUsageResponse | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> CurrentUsageResponse | ErrorResponse | HTTPValidationError | None:
    r"""Get Current Usage

     Get current month usage.

    Returns credit consumption for the current billing period,
    estimated cost, and next invoice date.

    **Requirements:**
    - Read permission

    **Example:**
    ```python
    response = await client.get(\"/v1/organizations/billing/usage/current\")
    print(f\"Usage: {response['current_month_usage']} credits\")
    print(f\"Estimated cost: ${response['estimated_cost_usd']}\")
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CurrentUsageResponse | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> Response[CurrentUsageResponse | ErrorResponse | HTTPValidationError]:
    r"""Get Current Usage

     Get current month usage.

    Returns credit consumption for the current billing period,
    estimated cost, and next invoice date.

    **Requirements:**
    - Read permission

    **Example:**
    ```python
    response = await client.get(\"/v1/organizations/billing/usage/current\")
    print(f\"Usage: {response['current_month_usage']} credits\")
    print(f\"Estimated cost: ${response['estimated_cost_usd']}\")
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CurrentUsageResponse | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> CurrentUsageResponse | ErrorResponse | HTTPValidationError | None:
    r"""Get Current Usage

     Get current month usage.

    Returns credit consumption for the current billing period,
    estimated cost, and next invoice date.

    **Requirements:**
    - Read permission

    **Example:**
    ```python
    response = await client.get(\"/v1/organizations/billing/usage/current\")
    print(f\"Usage: {response['current_month_usage']} credits\")
    print(f\"Estimated cost: ${response['estimated_cost_usd']}\")
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CurrentUsageResponse | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
