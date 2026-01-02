from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.spending_caps_response import SpendingCapsResponse
from ...models.update_spending_caps_request import UpdateSpendingCapsRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UpdateSpendingCapsRequest,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/organizations/billing/spending-caps",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | SpendingCapsResponse | None:
    if response.status_code == 200:
        response_200 = SpendingCapsResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | SpendingCapsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSpendingCapsRequest,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | SpendingCapsResponse]:
    r"""Update Spending Caps

     Update spending cap configuration.

    Configure spending limits and alert thresholds to control costs.

    **Features:**
    - **Soft Limit (Budget)**: Triggers alerts but doesn't block API access
    - **Hard Cap**: Blocks API access when reached (requires explicit enable)
    - **Alert Thresholds**: Customize when to receive spending notifications

    **Requirements:**
    - Admin permission
    - Only applies to organizations with auto-billing enabled

    **Example:**
    ```python
    # Set $100 budget with alerts at 75% and 100%
    response = await client.post(
        \"/v1/organizations/billing/spending-caps\",
        json={
            \"monthly_spending_budget\": 10000,  # $100 in cents
            \"spending_alert_thresholds\": [75, 100],
            \"spending_alerts_enabled\": True,
        }
    )

    # Enable hard cap at $500
    response = await client.post(
        \"/v1/organizations/billing/spending-caps\",
        json={
            \"hard_spending_cap\": 50000,  # $500 in cents
            \"hard_cap_enabled\": True,
        }
    )

    # Disable all spending limits
    response = await client.post(
        \"/v1/organizations/billing/spending-caps\",
        json={
            \"monthly_spending_budget\": None,
            \"hard_spending_cap\": None,
            \"hard_cap_enabled\": False,
        }
    )
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (UpdateSpendingCapsRequest): Request to update spending cap configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SpendingCapsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSpendingCapsRequest,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | SpendingCapsResponse | None:
    r"""Update Spending Caps

     Update spending cap configuration.

    Configure spending limits and alert thresholds to control costs.

    **Features:**
    - **Soft Limit (Budget)**: Triggers alerts but doesn't block API access
    - **Hard Cap**: Blocks API access when reached (requires explicit enable)
    - **Alert Thresholds**: Customize when to receive spending notifications

    **Requirements:**
    - Admin permission
    - Only applies to organizations with auto-billing enabled

    **Example:**
    ```python
    # Set $100 budget with alerts at 75% and 100%
    response = await client.post(
        \"/v1/organizations/billing/spending-caps\",
        json={
            \"monthly_spending_budget\": 10000,  # $100 in cents
            \"spending_alert_thresholds\": [75, 100],
            \"spending_alerts_enabled\": True,
        }
    )

    # Enable hard cap at $500
    response = await client.post(
        \"/v1/organizations/billing/spending-caps\",
        json={
            \"hard_spending_cap\": 50000,  # $500 in cents
            \"hard_cap_enabled\": True,
        }
    )

    # Disable all spending limits
    response = await client.post(
        \"/v1/organizations/billing/spending-caps\",
        json={
            \"monthly_spending_budget\": None,
            \"hard_spending_cap\": None,
            \"hard_cap_enabled\": False,
        }
    )
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (UpdateSpendingCapsRequest): Request to update spending cap configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SpendingCapsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSpendingCapsRequest,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | SpendingCapsResponse]:
    r"""Update Spending Caps

     Update spending cap configuration.

    Configure spending limits and alert thresholds to control costs.

    **Features:**
    - **Soft Limit (Budget)**: Triggers alerts but doesn't block API access
    - **Hard Cap**: Blocks API access when reached (requires explicit enable)
    - **Alert Thresholds**: Customize when to receive spending notifications

    **Requirements:**
    - Admin permission
    - Only applies to organizations with auto-billing enabled

    **Example:**
    ```python
    # Set $100 budget with alerts at 75% and 100%
    response = await client.post(
        \"/v1/organizations/billing/spending-caps\",
        json={
            \"monthly_spending_budget\": 10000,  # $100 in cents
            \"spending_alert_thresholds\": [75, 100],
            \"spending_alerts_enabled\": True,
        }
    )

    # Enable hard cap at $500
    response = await client.post(
        \"/v1/organizations/billing/spending-caps\",
        json={
            \"hard_spending_cap\": 50000,  # $500 in cents
            \"hard_cap_enabled\": True,
        }
    )

    # Disable all spending limits
    response = await client.post(
        \"/v1/organizations/billing/spending-caps\",
        json={
            \"monthly_spending_budget\": None,
            \"hard_spending_cap\": None,
            \"hard_cap_enabled\": False,
        }
    )
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (UpdateSpendingCapsRequest): Request to update spending cap configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SpendingCapsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UpdateSpendingCapsRequest,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | SpendingCapsResponse | None:
    r"""Update Spending Caps

     Update spending cap configuration.

    Configure spending limits and alert thresholds to control costs.

    **Features:**
    - **Soft Limit (Budget)**: Triggers alerts but doesn't block API access
    - **Hard Cap**: Blocks API access when reached (requires explicit enable)
    - **Alert Thresholds**: Customize when to receive spending notifications

    **Requirements:**
    - Admin permission
    - Only applies to organizations with auto-billing enabled

    **Example:**
    ```python
    # Set $100 budget with alerts at 75% and 100%
    response = await client.post(
        \"/v1/organizations/billing/spending-caps\",
        json={
            \"monthly_spending_budget\": 10000,  # $100 in cents
            \"spending_alert_thresholds\": [75, 100],
            \"spending_alerts_enabled\": True,
        }
    )

    # Enable hard cap at $500
    response = await client.post(
        \"/v1/organizations/billing/spending-caps\",
        json={
            \"hard_spending_cap\": 50000,  # $500 in cents
            \"hard_cap_enabled\": True,
        }
    )

    # Disable all spending limits
    response = await client.post(
        \"/v1/organizations/billing/spending-caps\",
        json={
            \"monthly_spending_budget\": None,
            \"hard_spending_cap\": None,
            \"hard_cap_enabled\": False,
        }
    )
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (UpdateSpendingCapsRequest): Request to update spending cap configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SpendingCapsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
