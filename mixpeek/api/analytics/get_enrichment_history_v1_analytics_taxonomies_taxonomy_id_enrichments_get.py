import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    taxonomy_id: str,
    *,
    start_date: datetime.datetime | None | Unset = UNSET,
    end_date: datetime.datetime | None | Unset = UNSET,
    group_by: str | Unset = "day",
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    json_start_date: None | str | Unset
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    elif isinstance(start_date, datetime.datetime):
        json_start_date = start_date.isoformat()
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: None | str | Unset
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    elif isinstance(end_date, datetime.datetime):
        json_end_date = end_date.isoformat()
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date

    params["group_by"] = group_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/taxonomies/{taxonomy_id}/enrichments".format(
            taxonomy_id=quote(str(taxonomy_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
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
    taxonomy_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.datetime | None | Unset = UNSET,
    end_date: datetime.datetime | None | Unset = UNSET,
    group_by: str | Unset = "day",
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Get Enrichment History

     Get enrichment execution history.

    Tracks enrichment operations including:
    - Enrichment success rates
    - Average latency
    - Volume trends

    **Use Cases:**
    - Monitor enrichment performance
    - Track success rates
    - Identify performance issues

    Args:
        taxonomy_id (str):
        start_date (datetime.datetime | None | Unset):
        end_date (datetime.datetime | None | Unset):
        group_by (str | Unset):  Default: 'day'.
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
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        taxonomy_id=taxonomy_id,
        start_date=start_date,
        end_date=end_date,
        group_by=group_by,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    taxonomy_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.datetime | None | Unset = UNSET,
    end_date: datetime.datetime | None | Unset = UNSET,
    group_by: str | Unset = "day",
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Get Enrichment History

     Get enrichment execution history.

    Tracks enrichment operations including:
    - Enrichment success rates
    - Average latency
    - Volume trends

    **Use Cases:**
    - Monitor enrichment performance
    - Track success rates
    - Identify performance issues

    Args:
        taxonomy_id (str):
        start_date (datetime.datetime | None | Unset):
        end_date (datetime.datetime | None | Unset):
        group_by (str | Unset):  Default: 'day'.
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
        ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        taxonomy_id=taxonomy_id,
        client=client,
        start_date=start_date,
        end_date=end_date,
        group_by=group_by,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    taxonomy_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.datetime | None | Unset = UNSET,
    end_date: datetime.datetime | None | Unset = UNSET,
    group_by: str | Unset = "day",
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError]:
    """Get Enrichment History

     Get enrichment execution history.

    Tracks enrichment operations including:
    - Enrichment success rates
    - Average latency
    - Volume trends

    **Use Cases:**
    - Monitor enrichment performance
    - Track success rates
    - Identify performance issues

    Args:
        taxonomy_id (str):
        start_date (datetime.datetime | None | Unset):
        end_date (datetime.datetime | None | Unset):
        group_by (str | Unset):  Default: 'day'.
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
        Response[ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        taxonomy_id=taxonomy_id,
        start_date=start_date,
        end_date=end_date,
        group_by=group_by,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    taxonomy_id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.datetime | None | Unset = UNSET,
    end_date: datetime.datetime | None | Unset = UNSET,
    group_by: str | Unset = "day",
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | None:
    """Get Enrichment History

     Get enrichment execution history.

    Tracks enrichment operations including:
    - Enrichment success rates
    - Average latency
    - Volume trends

    **Use Cases:**
    - Monitor enrichment performance
    - Track success rates
    - Identify performance issues

    Args:
        taxonomy_id (str):
        start_date (datetime.datetime | None | Unset):
        end_date (datetime.datetime | None | Unset):
        group_by (str | Unset):  Default: 'day'.
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
        ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            taxonomy_id=taxonomy_id,
            client=client,
            start_date=start_date,
            end_date=end_date,
            group_by=group_by,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
