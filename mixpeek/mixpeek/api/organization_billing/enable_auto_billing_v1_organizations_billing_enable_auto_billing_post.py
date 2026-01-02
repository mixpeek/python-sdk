from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auto_billing_toggle_response import AutoBillingToggleResponse
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
        "method": "post",
        "url": "/v1/organizations/billing/enable-auto-billing",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AutoBillingToggleResponse | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AutoBillingToggleResponse.from_dict(response.json())

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
) -> Response[AutoBillingToggleResponse | ErrorResponse | HTTPValidationError]:
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
) -> Response[AutoBillingToggleResponse | ErrorResponse | HTTPValidationError]:
    r"""Enable Auto Billing

     Enable automatic monthly billing.

    Re-enables automatic billing if it was previously disabled.
    Payment method must already be saved.

    **Requirements:**
    - Admin permission
    - Must have payment method saved

    **Example:**
    ```python
    response = await client.post(\"/v1/organizations/billing/enable-auto-billing\")
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutoBillingToggleResponse | ErrorResponse | HTTPValidationError]
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
) -> AutoBillingToggleResponse | ErrorResponse | HTTPValidationError | None:
    r"""Enable Auto Billing

     Enable automatic monthly billing.

    Re-enables automatic billing if it was previously disabled.
    Payment method must already be saved.

    **Requirements:**
    - Admin permission
    - Must have payment method saved

    **Example:**
    ```python
    response = await client.post(\"/v1/organizations/billing/enable-auto-billing\")
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutoBillingToggleResponse | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> Response[AutoBillingToggleResponse | ErrorResponse | HTTPValidationError]:
    r"""Enable Auto Billing

     Enable automatic monthly billing.

    Re-enables automatic billing if it was previously disabled.
    Payment method must already be saved.

    **Requirements:**
    - Admin permission
    - Must have payment method saved

    **Example:**
    ```python
    response = await client.post(\"/v1/organizations/billing/enable-auto-billing\")
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutoBillingToggleResponse | ErrorResponse | HTTPValidationError]
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
) -> AutoBillingToggleResponse | ErrorResponse | HTTPValidationError | None:
    r"""Enable Auto Billing

     Enable automatic monthly billing.

    Re-enables automatic billing if it was previously disabled.
    Payment method must already be saved.

    **Requirements:**
    - Admin permission
    - Must have payment method saved

    **Example:**
    ```python
    response = await client.post(\"/v1/organizations/billing/enable-auto-billing\")
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutoBillingToggleResponse | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
