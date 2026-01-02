from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.setup_payment_method_response import SetupPaymentMethodResponse
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
        "url": "/v1/organizations/billing/setup-payment-method",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | SetupPaymentMethodResponse | None:
    if response.status_code == 200:
        response_200 = SetupPaymentMethodResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | SetupPaymentMethodResponse]:
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
) -> Response[ErrorResponse | HTTPValidationError | SetupPaymentMethodResponse]:
    r"""Setup Payment Method

     Initialize payment method setup flow.

    Creates a Stripe SetupIntent for collecting payment method without charging.
    The client_secret should be used with Stripe Elements on the frontend.

    **Flow:**
    1. Frontend calls this endpoint
    2. Backend creates Stripe Customer (if needed) and SetupIntent
    3. Frontend uses client_secret with Stripe Elements
    4. User enters card details
    5. Frontend calls confirm-payment-method endpoint

    **Requirements:**
    - Admin permission (only org admins can set up payment methods)

    **Example:**
    ```python
    response = await client.post(\"/v1/organizations/billing/setup-payment-method\")
    client_secret = response[\"client_secret\"]
    # Use client_secret with Stripe Elements
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SetupPaymentMethodResponse]
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
) -> ErrorResponse | HTTPValidationError | SetupPaymentMethodResponse | None:
    r"""Setup Payment Method

     Initialize payment method setup flow.

    Creates a Stripe SetupIntent for collecting payment method without charging.
    The client_secret should be used with Stripe Elements on the frontend.

    **Flow:**
    1. Frontend calls this endpoint
    2. Backend creates Stripe Customer (if needed) and SetupIntent
    3. Frontend uses client_secret with Stripe Elements
    4. User enters card details
    5. Frontend calls confirm-payment-method endpoint

    **Requirements:**
    - Admin permission (only org admins can set up payment methods)

    **Example:**
    ```python
    response = await client.post(\"/v1/organizations/billing/setup-payment-method\")
    client_secret = response[\"client_secret\"]
    # Use client_secret with Stripe Elements
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SetupPaymentMethodResponse
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | SetupPaymentMethodResponse]:
    r"""Setup Payment Method

     Initialize payment method setup flow.

    Creates a Stripe SetupIntent for collecting payment method without charging.
    The client_secret should be used with Stripe Elements on the frontend.

    **Flow:**
    1. Frontend calls this endpoint
    2. Backend creates Stripe Customer (if needed) and SetupIntent
    3. Frontend uses client_secret with Stripe Elements
    4. User enters card details
    5. Frontend calls confirm-payment-method endpoint

    **Requirements:**
    - Admin permission (only org admins can set up payment methods)

    **Example:**
    ```python
    response = await client.post(\"/v1/organizations/billing/setup-payment-method\")
    client_secret = response[\"client_secret\"]
    # Use client_secret with Stripe Elements
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | SetupPaymentMethodResponse]
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
) -> ErrorResponse | HTTPValidationError | SetupPaymentMethodResponse | None:
    r"""Setup Payment Method

     Initialize payment method setup flow.

    Creates a Stripe SetupIntent for collecting payment method without charging.
    The client_secret should be used with Stripe Elements on the frontend.

    **Flow:**
    1. Frontend calls this endpoint
    2. Backend creates Stripe Customer (if needed) and SetupIntent
    3. Frontend uses client_secret with Stripe Elements
    4. User enters card details
    5. Frontend calls confirm-payment-method endpoint

    **Requirements:**
    - Admin permission (only org admins can set up payment methods)

    **Example:**
    ```python
    response = await client.post(\"/v1/organizations/billing/setup-payment-method\")
    client_secret = response[\"client_secret\"]
    # Use client_secret with Stripe Elements
    ```

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | SetupPaymentMethodResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
