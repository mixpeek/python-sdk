from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.evaluation_list_response import EvaluationListResponse
from ...models.evaluation_status import EvaluationStatus
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    retriever_id: str,
    *,
    status: EvaluationStatus | None | Unset = UNSET,
    dataset_name: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    params: dict[str, Any] = {}

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, EvaluationStatus):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    json_dataset_name: None | str | Unset
    if isinstance(dataset_name, Unset):
        json_dataset_name = UNSET
    else:
        json_dataset_name = dataset_name
    params["dataset_name"] = json_dataset_name

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/retrievers/{retriever_id}/evaluations".format(
            retriever_id=quote(str(retriever_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | EvaluationListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EvaluationListResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | EvaluationListResponse | HTTPValidationError]:
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
    status: EvaluationStatus | None | Unset = UNSET,
    dataset_name: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | EvaluationListResponse | HTTPValidationError]:
    """List evaluations

     List all evaluations for a retriever with optional filters

    Args:
        retriever_id (str):
        status (EvaluationStatus | None | Unset): Filter by status (pending, in_progress,
            completed, failed)
        dataset_name (None | str | Unset): Filter by dataset name
        page (int | Unset): Page number (1-indexed) Default: 1.
        page_size (int | Unset): Items per page Default: 20.
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
        Response[ErrorResponse | EvaluationListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        retriever_id=retriever_id,
        status=status,
        dataset_name=dataset_name,
        page=page,
        page_size=page_size,
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
    status: EvaluationStatus | None | Unset = UNSET,
    dataset_name: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | EvaluationListResponse | HTTPValidationError | None:
    """List evaluations

     List all evaluations for a retriever with optional filters

    Args:
        retriever_id (str):
        status (EvaluationStatus | None | Unset): Filter by status (pending, in_progress,
            completed, failed)
        dataset_name (None | str | Unset): Filter by dataset name
        page (int | Unset): Page number (1-indexed) Default: 1.
        page_size (int | Unset): Items per page Default: 20.
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
        ErrorResponse | EvaluationListResponse | HTTPValidationError
    """

    return sync_detailed(
        retriever_id=retriever_id,
        client=client,
        status=status,
        dataset_name=dataset_name,
        page=page,
        page_size=page_size,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: EvaluationStatus | None | Unset = UNSET,
    dataset_name: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | EvaluationListResponse | HTTPValidationError]:
    """List evaluations

     List all evaluations for a retriever with optional filters

    Args:
        retriever_id (str):
        status (EvaluationStatus | None | Unset): Filter by status (pending, in_progress,
            completed, failed)
        dataset_name (None | str | Unset): Filter by dataset name
        page (int | Unset): Page number (1-indexed) Default: 1.
        page_size (int | Unset): Items per page Default: 20.
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
        Response[ErrorResponse | EvaluationListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        retriever_id=retriever_id,
        status=status,
        dataset_name=dataset_name,
        page=page,
        page_size=page_size,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    status: EvaluationStatus | None | Unset = UNSET,
    dataset_name: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | EvaluationListResponse | HTTPValidationError | None:
    """List evaluations

     List all evaluations for a retriever with optional filters

    Args:
        retriever_id (str):
        status (EvaluationStatus | None | Unset): Filter by status (pending, in_progress,
            completed, failed)
        dataset_name (None | str | Unset): Filter by dataset name
        page (int | Unset): Page number (1-indexed) Default: 1.
        page_size (int | Unset): Items per page Default: 20.
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
        ErrorResponse | EvaluationListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            retriever_id=retriever_id,
            client=client,
            status=status,
            dataset_name=dataset_name,
            page=page,
            page_size=page_size,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
