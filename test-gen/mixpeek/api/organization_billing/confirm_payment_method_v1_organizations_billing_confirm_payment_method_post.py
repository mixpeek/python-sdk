from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.confirm_payment_method_request import ConfirmPaymentMethodRequest
from ...models.confirm_payment_method_response import ConfirmPaymentMethodResponse
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ConfirmPaymentMethodRequest,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/organizations/billing/confirm-payment-method",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConfirmPaymentMethodResponse | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ConfirmPaymentMethodResponse.from_dict(response.json())

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
) -> Response[ConfirmPaymentMethodResponse | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConfirmPaymentMethodRequest,
    authorization: str | Unset = UNSET,
) -> Response[ConfirmPaymentMethodResponse | ErrorResponse | HTTPValidationError]:
    r"""Confirm Payment Method

     Confirm payment method after frontend collects it.

    After Stripe Elements confirms the SetupIntent, call this endpoint
    to attach the payment method to the customer and enable auto-billing.

    **Requirements:**
    - Admin permission
    - Must have called setup-payment-method first

    **Example:**
    ```python
    # After Stripe Elements confirms setup
    response = await client.post(
        \"/v1/organizations/billing/confirm-payment-method\",
        json={\"payment_method_id\": \"pm_1ABC2DEF3GHI\"}
    )
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (ConfirmPaymentMethodRequest): Request to confirm a payment method after collection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmPaymentMethodResponse | ErrorResponse | HTTPValidationError]
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
    body: ConfirmPaymentMethodRequest,
    authorization: str | Unset = UNSET,
) -> ConfirmPaymentMethodResponse | ErrorResponse | HTTPValidationError | None:
    r"""Confirm Payment Method

     Confirm payment method after frontend collects it.

    After Stripe Elements confirms the SetupIntent, call this endpoint
    to attach the payment method to the customer and enable auto-billing.

    **Requirements:**
    - Admin permission
    - Must have called setup-payment-method first

    **Example:**
    ```python
    # After Stripe Elements confirms setup
    response = await client.post(
        \"/v1/organizations/billing/confirm-payment-method\",
        json={\"payment_method_id\": \"pm_1ABC2DEF3GHI\"}
    )
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (ConfirmPaymentMethodRequest): Request to confirm a payment method after collection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmPaymentMethodResponse | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConfirmPaymentMethodRequest,
    authorization: str | Unset = UNSET,
) -> Response[ConfirmPaymentMethodResponse | ErrorResponse | HTTPValidationError]:
    r"""Confirm Payment Method

     Confirm payment method after frontend collects it.

    After Stripe Elements confirms the SetupIntent, call this endpoint
    to attach the payment method to the customer and enable auto-billing.

    **Requirements:**
    - Admin permission
    - Must have called setup-payment-method first

    **Example:**
    ```python
    # After Stripe Elements confirms setup
    response = await client.post(
        \"/v1/organizations/billing/confirm-payment-method\",
        json={\"payment_method_id\": \"pm_1ABC2DEF3GHI\"}
    )
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (ConfirmPaymentMethodRequest): Request to confirm a payment method after collection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmPaymentMethodResponse | ErrorResponse | HTTPValidationError]
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
    body: ConfirmPaymentMethodRequest,
    authorization: str | Unset = UNSET,
) -> ConfirmPaymentMethodResponse | ErrorResponse | HTTPValidationError | None:
    r"""Confirm Payment Method

     Confirm payment method after frontend collects it.

    After Stripe Elements confirms the SetupIntent, call this endpoint
    to attach the payment method to the customer and enable auto-billing.

    **Requirements:**
    - Admin permission
    - Must have called setup-payment-method first

    **Example:**
    ```python
    # After Stripe Elements confirms setup
    response = await client.post(
        \"/v1/organizations/billing/confirm-payment-method\",
        json={\"payment_method_id\": \"pm_1ABC2DEF3GHI\"}
    )
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (ConfirmPaymentMethodRequest): Request to confirm a payment method after collection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmPaymentMethodResponse | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
