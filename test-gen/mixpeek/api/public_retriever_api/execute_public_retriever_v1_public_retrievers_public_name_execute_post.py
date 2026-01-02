from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.retriever_execution_request import RetrieverExecutionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    public_name: str,
    *,
    body: RetrieverExecutionRequest,
    return_presigned_urls: bool | Unset = True,
    x_public_api_key: str,
    x_retriever_password: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Public-API-Key"] = x_public_api_key

    if not isinstance(x_retriever_password, Unset):
        headers["X-Retriever-Password"] = x_retriever_password

    params: dict[str, Any] = {}

    params["return_presigned_urls"] = return_presigned_urls

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/public/retrievers/{public_name}/execute".format(
            public_name=quote(str(public_name), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: RetrieverExecutionRequest,
    return_presigned_urls: bool | Unset = True,
    x_public_api_key: str,
    x_retriever_password: None | str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    r""" Execute Public Retriever

     Execute a published retriever (public endpoint).

    **Authentication:**
    - Requires `X-Public-API-Key` header with the retriever's public API key
    - If password-protected, also requires `X-Retriever-Password` header

    **Rate Limiting:**
    - Subject to per-retriever rate limits (per minute/hour/day)
    - May also have IP-based rate limits

    **Response:**
    - Only returns fields specified in `exposed_fields` configuration
    - Internal metadata is stripped from results
    - Includes `execution_id` for interaction tracking
    - Presigned URLs returned by default (return_presigned_urls=true) for media rendering

    **Example:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/video-search/execute\" \
      -H \"X-Public-API-Key: prk_abc123...\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"inputs\": {\"query\": \"red car\"},
        \"pagination\": {\"method\": \"offset\", \"page_number\": 1, \"page_size\": 10}
      }'
    ```

    **Example with return_presigned_urls disabled:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/video-
    search/execute?return_presigned_urls=false\" \
      -H \"X-Public-API-Key: prk_abc123...\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"inputs\": {\"query\": \"red car\"},
        \"pagination\": {\"method\": \"offset\", \"page_number\": 1, \"page_size\": 10}
      }'
    ```

    Args:
        public_name (str): Public name of the published retriever
        return_presigned_urls (bool | Unset): Generate fresh presigned download URLs for all blobs
            with S3 storage. Default: True for public retrievers to enable media rendering. Set to
            False if you only need metadata without URLs. Default: True.
        x_public_api_key (str):
        x_retriever_password (None | str | Unset):
        body (RetrieverExecutionRequest): Request payload for executing a retriever.

            Executes a predefined retriever with runtime inputs. The retriever uses the
            collections it was created with - collection overrides are not supported at
            execution time to ensure feature_uri and schema validation integrity.

            All filtering, pagination, and result shaping is handled by the individual stages
            based on the inputs provided.

            Use Cases:
                - Execute retriever with its configured collections
                - Pass inputs that stages use to determine filtering/pagination behavior

            Design Philosophy:
                - Retrievers are validated at creation time against their collections
                - Feature URIs, input schemas, and stage configs are tightly coupled to collections
                - Filters, limits, and offsets are NOT top-level request fields
                - These are handled by stages when they receive inputs
                - Example: A stage might read {INPUT.top_k} to determine result limit

            Examples:
                Simple query:
                    {"inputs": {"query": "AI", "top_k": 50}}

                Different inputs for stage behavior:
                    {"inputs": {
                        "query": "machine learning",
                        "top_k": 100,
                        "min_score": 0.7,
                        "published_after": "2024-01-01"
                     }}

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        public_name=public_name,
        body=body,
        return_presigned_urls=return_presigned_urls,
        x_public_api_key=x_public_api_key,
        x_retriever_password=x_retriever_password,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: RetrieverExecutionRequest,
    return_presigned_urls: bool | Unset = True,
    x_public_api_key: str,
    x_retriever_password: None | str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    r""" Execute Public Retriever

     Execute a published retriever (public endpoint).

    **Authentication:**
    - Requires `X-Public-API-Key` header with the retriever's public API key
    - If password-protected, also requires `X-Retriever-Password` header

    **Rate Limiting:**
    - Subject to per-retriever rate limits (per minute/hour/day)
    - May also have IP-based rate limits

    **Response:**
    - Only returns fields specified in `exposed_fields` configuration
    - Internal metadata is stripped from results
    - Includes `execution_id` for interaction tracking
    - Presigned URLs returned by default (return_presigned_urls=true) for media rendering

    **Example:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/video-search/execute\" \
      -H \"X-Public-API-Key: prk_abc123...\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"inputs\": {\"query\": \"red car\"},
        \"pagination\": {\"method\": \"offset\", \"page_number\": 1, \"page_size\": 10}
      }'
    ```

    **Example with return_presigned_urls disabled:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/video-
    search/execute?return_presigned_urls=false\" \
      -H \"X-Public-API-Key: prk_abc123...\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"inputs\": {\"query\": \"red car\"},
        \"pagination\": {\"method\": \"offset\", \"page_number\": 1, \"page_size\": 10}
      }'
    ```

    Args:
        public_name (str): Public name of the published retriever
        return_presigned_urls (bool | Unset): Generate fresh presigned download URLs for all blobs
            with S3 storage. Default: True for public retrievers to enable media rendering. Set to
            False if you only need metadata without URLs. Default: True.
        x_public_api_key (str):
        x_retriever_password (None | str | Unset):
        body (RetrieverExecutionRequest): Request payload for executing a retriever.

            Executes a predefined retriever with runtime inputs. The retriever uses the
            collections it was created with - collection overrides are not supported at
            execution time to ensure feature_uri and schema validation integrity.

            All filtering, pagination, and result shaping is handled by the individual stages
            based on the inputs provided.

            Use Cases:
                - Execute retriever with its configured collections
                - Pass inputs that stages use to determine filtering/pagination behavior

            Design Philosophy:
                - Retrievers are validated at creation time against their collections
                - Feature URIs, input schemas, and stage configs are tightly coupled to collections
                - Filters, limits, and offsets are NOT top-level request fields
                - These are handled by stages when they receive inputs
                - Example: A stage might read {INPUT.top_k} to determine result limit

            Examples:
                Simple query:
                    {"inputs": {"query": "AI", "top_k": 50}}

                Different inputs for stage behavior:
                    {"inputs": {
                        "query": "machine learning",
                        "top_k": 100,
                        "min_score": 0.7,
                        "published_after": "2024-01-01"
                     }}

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
     """

    return sync_detailed(
        public_name=public_name,
        client=client,
        body=body,
        return_presigned_urls=return_presigned_urls,
        x_public_api_key=x_public_api_key,
        x_retriever_password=x_retriever_password,
    ).parsed


async def asyncio_detailed(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: RetrieverExecutionRequest,
    return_presigned_urls: bool | Unset = True,
    x_public_api_key: str,
    x_retriever_password: None | str | Unset = UNSET,
) -> Response[Any | ErrorResponse | HTTPValidationError]:
    r""" Execute Public Retriever

     Execute a published retriever (public endpoint).

    **Authentication:**
    - Requires `X-Public-API-Key` header with the retriever's public API key
    - If password-protected, also requires `X-Retriever-Password` header

    **Rate Limiting:**
    - Subject to per-retriever rate limits (per minute/hour/day)
    - May also have IP-based rate limits

    **Response:**
    - Only returns fields specified in `exposed_fields` configuration
    - Internal metadata is stripped from results
    - Includes `execution_id` for interaction tracking
    - Presigned URLs returned by default (return_presigned_urls=true) for media rendering

    **Example:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/video-search/execute\" \
      -H \"X-Public-API-Key: prk_abc123...\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"inputs\": {\"query\": \"red car\"},
        \"pagination\": {\"method\": \"offset\", \"page_number\": 1, \"page_size\": 10}
      }'
    ```

    **Example with return_presigned_urls disabled:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/video-
    search/execute?return_presigned_urls=false\" \
      -H \"X-Public-API-Key: prk_abc123...\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"inputs\": {\"query\": \"red car\"},
        \"pagination\": {\"method\": \"offset\", \"page_number\": 1, \"page_size\": 10}
      }'
    ```

    Args:
        public_name (str): Public name of the published retriever
        return_presigned_urls (bool | Unset): Generate fresh presigned download URLs for all blobs
            with S3 storage. Default: True for public retrievers to enable media rendering. Set to
            False if you only need metadata without URLs. Default: True.
        x_public_api_key (str):
        x_retriever_password (None | str | Unset):
        body (RetrieverExecutionRequest): Request payload for executing a retriever.

            Executes a predefined retriever with runtime inputs. The retriever uses the
            collections it was created with - collection overrides are not supported at
            execution time to ensure feature_uri and schema validation integrity.

            All filtering, pagination, and result shaping is handled by the individual stages
            based on the inputs provided.

            Use Cases:
                - Execute retriever with its configured collections
                - Pass inputs that stages use to determine filtering/pagination behavior

            Design Philosophy:
                - Retrievers are validated at creation time against their collections
                - Feature URIs, input schemas, and stage configs are tightly coupled to collections
                - Filters, limits, and offsets are NOT top-level request fields
                - These are handled by stages when they receive inputs
                - Example: A stage might read {INPUT.top_k} to determine result limit

            Examples:
                Simple query:
                    {"inputs": {"query": "AI", "top_k": 50}}

                Different inputs for stage behavior:
                    {"inputs": {
                        "query": "machine learning",
                        "top_k": 100,
                        "min_score": 0.7,
                        "published_after": "2024-01-01"
                     }}

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        public_name=public_name,
        body=body,
        return_presigned_urls=return_presigned_urls,
        x_public_api_key=x_public_api_key,
        x_retriever_password=x_retriever_password,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: RetrieverExecutionRequest,
    return_presigned_urls: bool | Unset = True,
    x_public_api_key: str,
    x_retriever_password: None | str | Unset = UNSET,
) -> Any | ErrorResponse | HTTPValidationError | None:
    r""" Execute Public Retriever

     Execute a published retriever (public endpoint).

    **Authentication:**
    - Requires `X-Public-API-Key` header with the retriever's public API key
    - If password-protected, also requires `X-Retriever-Password` header

    **Rate Limiting:**
    - Subject to per-retriever rate limits (per minute/hour/day)
    - May also have IP-based rate limits

    **Response:**
    - Only returns fields specified in `exposed_fields` configuration
    - Internal metadata is stripped from results
    - Includes `execution_id` for interaction tracking
    - Presigned URLs returned by default (return_presigned_urls=true) for media rendering

    **Example:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/video-search/execute\" \
      -H \"X-Public-API-Key: prk_abc123...\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"inputs\": {\"query\": \"red car\"},
        \"pagination\": {\"method\": \"offset\", \"page_number\": 1, \"page_size\": 10}
      }'
    ```

    **Example with return_presigned_urls disabled:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/video-
    search/execute?return_presigned_urls=false\" \
      -H \"X-Public-API-Key: prk_abc123...\" \
      -H \"Content-Type: application/json\" \
      -d '{
        \"inputs\": {\"query\": \"red car\"},
        \"pagination\": {\"method\": \"offset\", \"page_number\": 1, \"page_size\": 10}
      }'
    ```

    Args:
        public_name (str): Public name of the published retriever
        return_presigned_urls (bool | Unset): Generate fresh presigned download URLs for all blobs
            with S3 storage. Default: True for public retrievers to enable media rendering. Set to
            False if you only need metadata without URLs. Default: True.
        x_public_api_key (str):
        x_retriever_password (None | str | Unset):
        body (RetrieverExecutionRequest): Request payload for executing a retriever.

            Executes a predefined retriever with runtime inputs. The retriever uses the
            collections it was created with - collection overrides are not supported at
            execution time to ensure feature_uri and schema validation integrity.

            All filtering, pagination, and result shaping is handled by the individual stages
            based on the inputs provided.

            Use Cases:
                - Execute retriever with its configured collections
                - Pass inputs that stages use to determine filtering/pagination behavior

            Design Philosophy:
                - Retrievers are validated at creation time against their collections
                - Feature URIs, input schemas, and stage configs are tightly coupled to collections
                - Filters, limits, and offsets are NOT top-level request fields
                - These are handled by stages when they receive inputs
                - Example: A stage might read {INPUT.top_k} to determine result limit

            Examples:
                Simple query:
                    {"inputs": {"query": "AI", "top_k": 50}}

                Different inputs for stage behavior:
                    {"inputs": {
                        "query": "machine learning",
                        "top_k": 100,
                        "min_score": 0.7,
                        "published_after": "2024-01-01"
                     }}

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError
     """

    return (
        await asyncio_detailed(
            public_name=public_name,
            client=client,
            body=body,
            return_presigned_urls=return_presigned_urls,
            x_public_api_key=x_public_api_key,
            x_retriever_password=x_retriever_password,
        )
    ).parsed
