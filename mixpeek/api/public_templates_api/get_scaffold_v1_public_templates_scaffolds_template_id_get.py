from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_template_model import BaseTemplateModel
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    template_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/public/templates/scaffolds/{template_id}".format(
            template_id=quote(str(template_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BaseTemplateModel | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BaseTemplateModel.from_dict(response.json())

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
) -> Response[BaseTemplateModel | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[BaseTemplateModel | ErrorResponse | HTTPValidationError]:
    r"""Get Scaffold

     Get scaffold template details (public, no auth required).

    Returns the complete configuration including:
    - Namespace: feature extractors, payload indexes
    - Bucket: name, description, schema
    - Collection: feature extractor config
    - Retriever: stages, input schema

    **To instantiate (requires auth):**
    ```
    POST /v1/templates/scaffolds/{template_id}/instantiate
    {\"namespace_name\": \"my_app\"}
    ```

    Args:
        template_id (str): Scaffold template ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BaseTemplateModel | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> BaseTemplateModel | ErrorResponse | HTTPValidationError | None:
    r"""Get Scaffold

     Get scaffold template details (public, no auth required).

    Returns the complete configuration including:
    - Namespace: feature extractors, payload indexes
    - Bucket: name, description, schema
    - Collection: feature extractor config
    - Retriever: stages, input schema

    **To instantiate (requires auth):**
    ```
    POST /v1/templates/scaffolds/{template_id}/instantiate
    {\"namespace_name\": \"my_app\"}
    ```

    Args:
        template_id (str): Scaffold template ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BaseTemplateModel | ErrorResponse | HTTPValidationError
    """

    return sync_detailed(
        template_id=template_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[BaseTemplateModel | ErrorResponse | HTTPValidationError]:
    r"""Get Scaffold

     Get scaffold template details (public, no auth required).

    Returns the complete configuration including:
    - Namespace: feature extractors, payload indexes
    - Bucket: name, description, schema
    - Collection: feature extractor config
    - Retriever: stages, input schema

    **To instantiate (requires auth):**
    ```
    POST /v1/templates/scaffolds/{template_id}/instantiate
    {\"namespace_name\": \"my_app\"}
    ```

    Args:
        template_id (str): Scaffold template ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BaseTemplateModel | ErrorResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> BaseTemplateModel | ErrorResponse | HTTPValidationError | None:
    r"""Get Scaffold

     Get scaffold template details (public, no auth required).

    Returns the complete configuration including:
    - Namespace: feature extractors, payload indexes
    - Bucket: name, description, schema
    - Collection: feature extractor config
    - Retriever: stages, input schema

    **To instantiate (requires auth):**
    ```
    POST /v1/templates/scaffolds/{template_id}/instantiate
    {\"namespace_name\": \"my_app\"}
    ```

    Args:
        template_id (str): Scaffold template ID

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BaseTemplateModel | ErrorResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            client=client,
        )
    ).parsed
