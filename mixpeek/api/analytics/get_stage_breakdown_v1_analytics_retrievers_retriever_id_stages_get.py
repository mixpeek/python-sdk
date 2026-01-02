from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.stage_breakdown_response import StageBreakdownResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    retriever_id: str,
    *,
    hours: int | Unset = 24,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    params["hours"] = hours

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/retrievers/{retriever_id}/stages".format(
            retriever_id=quote(str(retriever_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | StageBreakdownResponse | None:
    if response.status_code == 200:
        response_200 = StageBreakdownResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | StageBreakdownResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    hours: int | Unset = 24,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | StageBreakdownResponse]:
    r""" Get Stage Breakdown

     Get stage-level performance breakdown.

    Analyzes individual stage performance to identify bottlenecks:
    - Stage execution times
    - Document flow (in/out)
    - Stage-level latency distribution

    **Use Cases:**
    - Identify slow stages in retrieval pipeline
    - Optimize stage ordering
    - Debug pipeline bottlenecks
    - Understand document reduction rates

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/retrievers/ret_abc123/stages?hours=24\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        retriever_id (str):
        hours (int | Unset): Hours of history Default: 24.
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
        Response[ErrorResponse | HTTPValidationError | StageBreakdownResponse]
     """

    kwargs = _get_kwargs(
        retriever_id=retriever_id,
        hours=hours,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    hours: int | Unset = 24,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | StageBreakdownResponse | None:
    r""" Get Stage Breakdown

     Get stage-level performance breakdown.

    Analyzes individual stage performance to identify bottlenecks:
    - Stage execution times
    - Document flow (in/out)
    - Stage-level latency distribution

    **Use Cases:**
    - Identify slow stages in retrieval pipeline
    - Optimize stage ordering
    - Debug pipeline bottlenecks
    - Understand document reduction rates

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/retrievers/ret_abc123/stages?hours=24\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        retriever_id (str):
        hours (int | Unset): Hours of history Default: 24.
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
        ErrorResponse | HTTPValidationError | StageBreakdownResponse
     """

    return sync_detailed(
        retriever_id=retriever_id,
        client=client,
        hours=hours,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    hours: int | Unset = 24,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | StageBreakdownResponse]:
    r""" Get Stage Breakdown

     Get stage-level performance breakdown.

    Analyzes individual stage performance to identify bottlenecks:
    - Stage execution times
    - Document flow (in/out)
    - Stage-level latency distribution

    **Use Cases:**
    - Identify slow stages in retrieval pipeline
    - Optimize stage ordering
    - Debug pipeline bottlenecks
    - Understand document reduction rates

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/retrievers/ret_abc123/stages?hours=24\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        retriever_id (str):
        hours (int | Unset): Hours of history Default: 24.
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
        Response[ErrorResponse | HTTPValidationError | StageBreakdownResponse]
     """

    kwargs = _get_kwargs(
        retriever_id=retriever_id,
        hours=hours,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    hours: int | Unset = 24,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | StageBreakdownResponse | None:
    r""" Get Stage Breakdown

     Get stage-level performance breakdown.

    Analyzes individual stage performance to identify bottlenecks:
    - Stage execution times
    - Document flow (in/out)
    - Stage-level latency distribution

    **Use Cases:**
    - Identify slow stages in retrieval pipeline
    - Optimize stage ordering
    - Debug pipeline bottlenecks
    - Understand document reduction rates

    **Example:**
    ```bash
    curl -X GET \"https://api.mixpeek.com/v1/analytics/retrievers/ret_abc123/stages?hours=24\" \
      -H \"Authorization: Bearer YOUR_API_KEY\" \
      -H \"X-Namespace: your-namespace\"
    ```

    Args:
        retriever_id (str):
        hours (int | Unset): Hours of history Default: 24.
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
        ErrorResponse | HTTPValidationError | StageBreakdownResponse
     """

    return (
        await asyncio_detailed(
            retriever_id=retriever_id,
            client=client,
            hours=hours,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
