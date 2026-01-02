from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.most_queried_fields_response import MostQueriedFieldsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: int | Unset = 30,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    params["days"] = days

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/namespaces/fields/most-queried",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | MostQueriedFieldsResponse | None:
    if response.status_code == 200:
        response_200 = MostQueriedFieldsResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | MostQueriedFieldsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | MostQueriedFieldsResponse]:
    r""" Get Most Queried Fields

     Get most frequently queried metadata fields.

    Identifies which metadata fields are accessed most often in retriever queries,
    helping prioritize index creation and understand query patterns.

    **Use Cases:**
    - Identify fields that need indexing
    - Understand common query patterns
    - Prioritize optimization efforts
    - Plan database schema improvements

    **Response Includes:**
    - Field name and usage frequency
    - Average and P95 latency metrics
    - Total unique fields analyzed

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/namespaces/fields/most-queried?days=30&limit=20\"
    \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        days (int | Unset): Days of history to analyze Default: 30.
        limit (int | Unset): Maximum fields to return Default: 50.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | MostQueriedFieldsResponse]
     """

    kwargs = _get_kwargs(
        days=days,
        limit=limit,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | MostQueriedFieldsResponse | None:
    r""" Get Most Queried Fields

     Get most frequently queried metadata fields.

    Identifies which metadata fields are accessed most often in retriever queries,
    helping prioritize index creation and understand query patterns.

    **Use Cases:**
    - Identify fields that need indexing
    - Understand common query patterns
    - Prioritize optimization efforts
    - Plan database schema improvements

    **Response Includes:**
    - Field name and usage frequency
    - Average and P95 latency metrics
    - Total unique fields analyzed

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/namespaces/fields/most-queried?days=30&limit=20\"
    \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        days (int | Unset): Days of history to analyze Default: 30.
        limit (int | Unset): Maximum fields to return Default: 50.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | MostQueriedFieldsResponse
     """

    return sync_detailed(
        client=client,
        days=days,
        limit=limit,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | MostQueriedFieldsResponse]:
    r""" Get Most Queried Fields

     Get most frequently queried metadata fields.

    Identifies which metadata fields are accessed most often in retriever queries,
    helping prioritize index creation and understand query patterns.

    **Use Cases:**
    - Identify fields that need indexing
    - Understand common query patterns
    - Prioritize optimization efforts
    - Plan database schema improvements

    **Response Includes:**
    - Field name and usage frequency
    - Average and P95 latency metrics
    - Total unique fields analyzed

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/namespaces/fields/most-queried?days=30&limit=20\"
    \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        days (int | Unset): Days of history to analyze Default: 30.
        limit (int | Unset): Maximum fields to return Default: 50.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | MostQueriedFieldsResponse]
     """

    kwargs = _get_kwargs(
        days=days,
        limit=limit,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    limit: int | Unset = 50,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | MostQueriedFieldsResponse | None:
    r""" Get Most Queried Fields

     Get most frequently queried metadata fields.

    Identifies which metadata fields are accessed most often in retriever queries,
    helping prioritize index creation and understand query patterns.

    **Use Cases:**
    - Identify fields that need indexing
    - Understand common query patterns
    - Prioritize optimization efforts
    - Plan database schema improvements

    **Response Includes:**
    - Field name and usage frequency
    - Average and P95 latency metrics
    - Total unique fields analyzed

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/namespaces/fields/most-queried?days=30&limit=20\"
    \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        days (int | Unset): Days of history to analyze Default: 30.
        limit (int | Unset): Maximum fields to return Default: 50.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | MostQueriedFieldsResponse
     """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
            limit=limit,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
