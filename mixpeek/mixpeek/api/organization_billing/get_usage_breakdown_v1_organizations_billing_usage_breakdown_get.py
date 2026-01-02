from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.usage_breakdown_response import UsageBreakdownResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    billing_month: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    json_billing_month: None | str | Unset
    if isinstance(billing_month, Unset):
        json_billing_month = UNSET
    else:
        json_billing_month = billing_month
    params["billing_month"] = json_billing_month

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/organizations/billing/usage/breakdown",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | UsageBreakdownResponse | None:
    if response.status_code == 200:
        response_200 = UsageBreakdownResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | UsageBreakdownResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    billing_month: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | UsageBreakdownResponse]:
    r"""Get Usage Breakdown

     Get detailed usage breakdown.

    Returns usage breakdown by operation type and extractor
    for the specified billing period.

    **Query Parameters:**
    - `billing_month`: Month to query (YYYY-MM format, defaults to current)

    **Requirements:**
    - Read permission

    **Example:**
    ```python
    # Current month
    response = await client.get(\"/v1/organizations/billing/usage/breakdown\")

    # Specific month
    response = await client.get(
        \"/v1/organizations/billing/usage/breakdown\",
        params={\"billing_month\": \"2025-11\"}
    )
    ```

    Args:
        billing_month (None | str | Unset): Billing month in YYYY-MM format (defaults to current
            month)
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | UsageBreakdownResponse]
    """

    kwargs = _get_kwargs(
        billing_month=billing_month,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    billing_month: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | UsageBreakdownResponse | None:
    r"""Get Usage Breakdown

     Get detailed usage breakdown.

    Returns usage breakdown by operation type and extractor
    for the specified billing period.

    **Query Parameters:**
    - `billing_month`: Month to query (YYYY-MM format, defaults to current)

    **Requirements:**
    - Read permission

    **Example:**
    ```python
    # Current month
    response = await client.get(\"/v1/organizations/billing/usage/breakdown\")

    # Specific month
    response = await client.get(
        \"/v1/organizations/billing/usage/breakdown\",
        params={\"billing_month\": \"2025-11\"}
    )
    ```

    Args:
        billing_month (None | str | Unset): Billing month in YYYY-MM format (defaults to current
            month)
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | UsageBreakdownResponse
    """

    return sync_detailed(
        client=client,
        billing_month=billing_month,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    billing_month: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | UsageBreakdownResponse]:
    r"""Get Usage Breakdown

     Get detailed usage breakdown.

    Returns usage breakdown by operation type and extractor
    for the specified billing period.

    **Query Parameters:**
    - `billing_month`: Month to query (YYYY-MM format, defaults to current)

    **Requirements:**
    - Read permission

    **Example:**
    ```python
    # Current month
    response = await client.get(\"/v1/organizations/billing/usage/breakdown\")

    # Specific month
    response = await client.get(
        \"/v1/organizations/billing/usage/breakdown\",
        params={\"billing_month\": \"2025-11\"}
    )
    ```

    Args:
        billing_month (None | str | Unset): Billing month in YYYY-MM format (defaults to current
            month)
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | UsageBreakdownResponse]
    """

    kwargs = _get_kwargs(
        billing_month=billing_month,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    billing_month: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | UsageBreakdownResponse | None:
    r"""Get Usage Breakdown

     Get detailed usage breakdown.

    Returns usage breakdown by operation type and extractor
    for the specified billing period.

    **Query Parameters:**
    - `billing_month`: Month to query (YYYY-MM format, defaults to current)

    **Requirements:**
    - Read permission

    **Example:**
    ```python
    # Current month
    response = await client.get(\"/v1/organizations/billing/usage/breakdown\")

    # Specific month
    response = await client.get(
        \"/v1/organizations/billing/usage/breakdown\",
        params={\"billing_month\": \"2025-11\"}
    )
    ```

    Args:
        billing_month (None | str | Unset): Billing month in YYYY-MM format (defaults to current
            month)
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | UsageBreakdownResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            billing_month=billing_month,
            authorization=authorization,
        )
    ).parsed
