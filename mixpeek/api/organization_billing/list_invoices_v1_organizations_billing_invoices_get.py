from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.invoice_list_response import InvoiceListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 10,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/organizations/billing/invoices",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | InvoiceListResponse | None:
    if response.status_code == 200:
        response_200 = InvoiceListResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | InvoiceListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | InvoiceListResponse]:
    r"""List Invoices

     List monthly invoices.

    Returns paginated list of monthly invoices with links to
    Stripe-hosted invoice pages.

    **Query Parameters:**
    - `limit`: Number of invoices (1-100, default 10)

    **Requirements:**
    - Read permission

    **Example:**
    ```python
    response = await client.get(\"/v1/organizations/billing/invoices?limit=10\")
    for invoice in response[\"invoices\"]:
        print(f\"{invoice['billing_month']}: ${invoice['amount_paid']/100}\")
    ```

    Args:
        limit (int | Unset): Number of invoices to return Default: 10.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | InvoiceListResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | InvoiceListResponse | None:
    r"""List Invoices

     List monthly invoices.

    Returns paginated list of monthly invoices with links to
    Stripe-hosted invoice pages.

    **Query Parameters:**
    - `limit`: Number of invoices (1-100, default 10)

    **Requirements:**
    - Read permission

    **Example:**
    ```python
    response = await client.get(\"/v1/organizations/billing/invoices?limit=10\")
    for invoice in response[\"invoices\"]:
        print(f\"{invoice['billing_month']}: ${invoice['amount_paid']/100}\")
    ```

    Args:
        limit (int | Unset): Number of invoices to return Default: 10.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | InvoiceListResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | InvoiceListResponse]:
    r"""List Invoices

     List monthly invoices.

    Returns paginated list of monthly invoices with links to
    Stripe-hosted invoice pages.

    **Query Parameters:**
    - `limit`: Number of invoices (1-100, default 10)

    **Requirements:**
    - Read permission

    **Example:**
    ```python
    response = await client.get(\"/v1/organizations/billing/invoices?limit=10\")
    for invoice in response[\"invoices\"]:
        print(f\"{invoice['billing_month']}: ${invoice['amount_paid']/100}\")
    ```

    Args:
        limit (int | Unset): Number of invoices to return Default: 10.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | InvoiceListResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | InvoiceListResponse | None:
    r"""List Invoices

     List monthly invoices.

    Returns paginated list of monthly invoices with links to
    Stripe-hosted invoice pages.

    **Query Parameters:**
    - `limit`: Number of invoices (1-100, default 10)

    **Requirements:**
    - Read permission

    **Example:**
    ```python
    response = await client.get(\"/v1/organizations/billing/invoices?limit=10\")
    for invoice in response[\"invoices\"]:
        print(f\"{invoice['billing_month']}: ${invoice['amount_paid']/100}\")
    ```

    Args:
        limit (int | Unset): Number of invoices to return Default: 10.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | InvoiceListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
