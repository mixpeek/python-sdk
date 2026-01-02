from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_org_usage_v1_organizations_usage_get_response_get_org_usage_v1_organizations_usage_get import (
    GetOrgUsageV1OrganizationsUsageGetResponseGetOrgUsageV1OrganizationsUsageGet,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: None | str | Unset = UNSET,
    end: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    json_start: None | str | Unset
    if isinstance(start, Unset):
        json_start = UNSET
    else:
        json_start = start
    params["start"] = json_start

    json_end: None | str | Unset
    if isinstance(end, Unset):
        json_end = UNSET
    else:
        json_end = end
    params["end"] = json_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/organizations/usage",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponse
    | GetOrgUsageV1OrganizationsUsageGetResponseGetOrgUsageV1OrganizationsUsageGet
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = GetOrgUsageV1OrganizationsUsageGetResponseGetOrgUsageV1OrganizationsUsageGet.from_dict(
            response.json()
        )

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
) -> Response[
    ErrorResponse | GetOrgUsageV1OrganizationsUsageGetResponseGetOrgUsageV1OrganizationsUsageGet | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: None | str | Unset = UNSET,
    end: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> Response[
    ErrorResponse | GetOrgUsageV1OrganizationsUsageGetResponseGetOrgUsageV1OrganizationsUsageGet | HTTPValidationError
]:
    """Get Org Usage

     Return aggregated usage for the organization.

    Args:
        start (None | str | Unset): ISO8601 start timestamp
        end (None | str | Unset): ISO8601 end timestamp
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetOrgUsageV1OrganizationsUsageGetResponseGetOrgUsageV1OrganizationsUsageGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start: None | str | Unset = UNSET,
    end: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> (
    ErrorResponse
    | GetOrgUsageV1OrganizationsUsageGetResponseGetOrgUsageV1OrganizationsUsageGet
    | HTTPValidationError
    | None
):
    """Get Org Usage

     Return aggregated usage for the organization.

    Args:
        start (None | str | Unset): ISO8601 start timestamp
        end (None | str | Unset): ISO8601 end timestamp
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetOrgUsageV1OrganizationsUsageGetResponseGetOrgUsageV1OrganizationsUsageGet | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: None | str | Unset = UNSET,
    end: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> Response[
    ErrorResponse | GetOrgUsageV1OrganizationsUsageGetResponseGetOrgUsageV1OrganizationsUsageGet | HTTPValidationError
]:
    """Get Org Usage

     Return aggregated usage for the organization.

    Args:
        start (None | str | Unset): ISO8601 start timestamp
        end (None | str | Unset): ISO8601 end timestamp
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | GetOrgUsageV1OrganizationsUsageGetResponseGetOrgUsageV1OrganizationsUsageGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: None | str | Unset = UNSET,
    end: None | str | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> (
    ErrorResponse
    | GetOrgUsageV1OrganizationsUsageGetResponseGetOrgUsageV1OrganizationsUsageGet
    | HTTPValidationError
    | None
):
    """Get Org Usage

     Return aggregated usage for the organization.

    Args:
        start (None | str | Unset): ISO8601 start timestamp
        end (None | str | Unset): ISO8601 end timestamp
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | GetOrgUsageV1OrganizationsUsageGetResponseGetOrgUsageV1OrganizationsUsageGet | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
            authorization=authorization,
        )
    ).parsed
