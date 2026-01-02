from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.instantiate_scaffold_request import InstantiateScaffoldRequest
from ...models.instantiated_scaffold_response import InstantiatedScaffoldResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    template_id: str,
    *,
    body: InstantiateScaffoldRequest,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/templates/scaffolds/{template_id}/instantiate".format(
            template_id=quote(str(template_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | InstantiatedScaffoldResponse | None:
    if response.status_code == 201:
        response_201 = InstantiatedScaffoldResponse.from_dict(response.json())

        return response_201

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
) -> Response[ErrorResponse | HTTPValidationError | InstantiatedScaffoldResponse]:
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
    body: InstantiateScaffoldRequest,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | InstantiatedScaffoldResponse]:
    r"""Instantiate Scaffold Template

     Create complete infrastructure from scaffold template.

    Creates all resources atomically:
    1. **Namespace** with configured feature extractors
    2. **Bucket** with schema for your data structure
    3. **Collection** linked to bucket with feature config
    4. **Retriever** with search pipeline stages

    All resources are empty, ready for data upload.

    **Next Steps:**
    1. Upload data: `POST /v1/buckets/{bucket_id}/objects`
    2. Process batch: `POST /v1/collections/{collection_id}/batches`
    3. Search: `POST /v1/retrievers/{retriever_id}/retrieve`

    **Example Request:**
    ```json
    {
        \"namespace_name\": \"my_video_app\",
        \"namespace_description\": \"Video search application\"
    }
    ```

    Args:
        template_id (str): Scaffold template ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (InstantiateScaffoldRequest): Request to instantiate a scaffold template.

            Only namespace_name is required. Other names use scaffold defaults.

            Options:
                include_sample_data: If true, clone from demo namespace with sample data.
                                    If false (default), create empty resources.

            Example:
                # Empty scaffold
                {"namespace_name": "my_app"}

                # With sample data
                {"namespace_name": "my_app", "include_sample_data": true}

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | InstantiatedScaffoldResponse]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InstantiateScaffoldRequest,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | InstantiatedScaffoldResponse | None:
    r"""Instantiate Scaffold Template

     Create complete infrastructure from scaffold template.

    Creates all resources atomically:
    1. **Namespace** with configured feature extractors
    2. **Bucket** with schema for your data structure
    3. **Collection** linked to bucket with feature config
    4. **Retriever** with search pipeline stages

    All resources are empty, ready for data upload.

    **Next Steps:**
    1. Upload data: `POST /v1/buckets/{bucket_id}/objects`
    2. Process batch: `POST /v1/collections/{collection_id}/batches`
    3. Search: `POST /v1/retrievers/{retriever_id}/retrieve`

    **Example Request:**
    ```json
    {
        \"namespace_name\": \"my_video_app\",
        \"namespace_description\": \"Video search application\"
    }
    ```

    Args:
        template_id (str): Scaffold template ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (InstantiateScaffoldRequest): Request to instantiate a scaffold template.

            Only namespace_name is required. Other names use scaffold defaults.

            Options:
                include_sample_data: If true, clone from demo namespace with sample data.
                                    If false (default), create empty resources.

            Example:
                # Empty scaffold
                {"namespace_name": "my_app"}

                # With sample data
                {"namespace_name": "my_app", "include_sample_data": true}

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | InstantiatedScaffoldResponse
    """

    return sync_detailed(
        template_id=template_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InstantiateScaffoldRequest,
    authorization: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | InstantiatedScaffoldResponse]:
    r"""Instantiate Scaffold Template

     Create complete infrastructure from scaffold template.

    Creates all resources atomically:
    1. **Namespace** with configured feature extractors
    2. **Bucket** with schema for your data structure
    3. **Collection** linked to bucket with feature config
    4. **Retriever** with search pipeline stages

    All resources are empty, ready for data upload.

    **Next Steps:**
    1. Upload data: `POST /v1/buckets/{bucket_id}/objects`
    2. Process batch: `POST /v1/collections/{collection_id}/batches`
    3. Search: `POST /v1/retrievers/{retriever_id}/retrieve`

    **Example Request:**
    ```json
    {
        \"namespace_name\": \"my_video_app\",
        \"namespace_description\": \"Video search application\"
    }
    ```

    Args:
        template_id (str): Scaffold template ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (InstantiateScaffoldRequest): Request to instantiate a scaffold template.

            Only namespace_name is required. Other names use scaffold defaults.

            Options:
                include_sample_data: If true, clone from demo namespace with sample data.
                                    If false (default), create empty resources.

            Example:
                # Empty scaffold
                {"namespace_name": "my_app"}

                # With sample data
                {"namespace_name": "my_app", "include_sample_data": true}

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | InstantiatedScaffoldResponse]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InstantiateScaffoldRequest,
    authorization: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | InstantiatedScaffoldResponse | None:
    r"""Instantiate Scaffold Template

     Create complete infrastructure from scaffold template.

    Creates all resources atomically:
    1. **Namespace** with configured feature extractors
    2. **Bucket** with schema for your data structure
    3. **Collection** linked to bucket with feature config
    4. **Retriever** with search pipeline stages

    All resources are empty, ready for data upload.

    **Next Steps:**
    1. Upload data: `POST /v1/buckets/{bucket_id}/objects`
    2. Process batch: `POST /v1/collections/{collection_id}/batches`
    3. Search: `POST /v1/retrievers/{retriever_id}/retrieve`

    **Example Request:**
    ```json
    {
        \"namespace_name\": \"my_video_app\",
        \"namespace_description\": \"Video search application\"
    }
    ```

    Args:
        template_id (str): Scaffold template ID
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (InstantiateScaffoldRequest): Request to instantiate a scaffold template.

            Only namespace_name is required. Other names use scaffold defaults.

            Options:
                include_sample_data: If true, clone from demo namespace with sample data.
                                    If false (default), create empty resources.

            Example:
                # Empty scaffold
                {"namespace_name": "my_app"}

                # With sample data
                {"namespace_name": "my_app", "include_sample_data": true}

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | InstantiatedScaffoldResponse
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
