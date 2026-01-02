from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.verify_password_request import VerifyPasswordRequest
from ...models.verify_password_response import VerifyPasswordResponse
from ...types import Response


def _get_kwargs(
    public_name: str,
    *,
    body: VerifyPasswordRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/public/retrievers/{public_name}/verify".format(
            public_name=quote(str(public_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | VerifyPasswordResponse | None:
    if response.status_code == 200:
        response_200 = VerifyPasswordResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | VerifyPasswordResponse]:
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
    body: VerifyPasswordRequest,
) -> Response[ErrorResponse | HTTPValidationError | VerifyPasswordResponse]:
    r""" Verify Password

     Verify password for a password-protected retriever.

    Allows the frontend to check if a password is valid before attempting to execute
    a password-protected retriever. Returns the public API key if the password is valid.

    **Authentication:**
    - NO authentication required - this endpoint is public
    - The password is verified against the retriever's configured password

    **Use Case:**
    1. Frontend detects that a retriever is password-protected (from /config endpoint)
    2. User enters password in the UI
    3. Frontend calls this endpoint to verify the password
    4. If valid, frontend receives the public_api_key to use for subsequent requests

    **Response:**
    - `valid`: Whether the password is correct
    - `public_api_key`: The API key to use for execute/interact endpoints (only if valid)

    **Example:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/private-search/verify\" \
      -H \"Content-Type: application/json\" \
      -d '{\"password\": \"secret123\"}'
    ```

    **Response if valid:**
    ```json
    {
      \"valid\": true,
      \"public_api_key\": \"prk_abc123...\"
    }
    ```

    **Response if invalid:**
    ```json
    {
      \"valid\": false,
      \"public_api_key\": null
    }
    ```

    Args:
        public_name (str): Public name of the published retriever
        body (VerifyPasswordRequest): Request to verify password for a password-protected
            retriever.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | VerifyPasswordResponse]
     """

    kwargs = _get_kwargs(
        public_name=public_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: VerifyPasswordRequest,
) -> ErrorResponse | HTTPValidationError | VerifyPasswordResponse | None:
    r""" Verify Password

     Verify password for a password-protected retriever.

    Allows the frontend to check if a password is valid before attempting to execute
    a password-protected retriever. Returns the public API key if the password is valid.

    **Authentication:**
    - NO authentication required - this endpoint is public
    - The password is verified against the retriever's configured password

    **Use Case:**
    1. Frontend detects that a retriever is password-protected (from /config endpoint)
    2. User enters password in the UI
    3. Frontend calls this endpoint to verify the password
    4. If valid, frontend receives the public_api_key to use for subsequent requests

    **Response:**
    - `valid`: Whether the password is correct
    - `public_api_key`: The API key to use for execute/interact endpoints (only if valid)

    **Example:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/private-search/verify\" \
      -H \"Content-Type: application/json\" \
      -d '{\"password\": \"secret123\"}'
    ```

    **Response if valid:**
    ```json
    {
      \"valid\": true,
      \"public_api_key\": \"prk_abc123...\"
    }
    ```

    **Response if invalid:**
    ```json
    {
      \"valid\": false,
      \"public_api_key\": null
    }
    ```

    Args:
        public_name (str): Public name of the published retriever
        body (VerifyPasswordRequest): Request to verify password for a password-protected
            retriever.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | VerifyPasswordResponse
     """

    return sync_detailed(
        public_name=public_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: VerifyPasswordRequest,
) -> Response[ErrorResponse | HTTPValidationError | VerifyPasswordResponse]:
    r""" Verify Password

     Verify password for a password-protected retriever.

    Allows the frontend to check if a password is valid before attempting to execute
    a password-protected retriever. Returns the public API key if the password is valid.

    **Authentication:**
    - NO authentication required - this endpoint is public
    - The password is verified against the retriever's configured password

    **Use Case:**
    1. Frontend detects that a retriever is password-protected (from /config endpoint)
    2. User enters password in the UI
    3. Frontend calls this endpoint to verify the password
    4. If valid, frontend receives the public_api_key to use for subsequent requests

    **Response:**
    - `valid`: Whether the password is correct
    - `public_api_key`: The API key to use for execute/interact endpoints (only if valid)

    **Example:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/private-search/verify\" \
      -H \"Content-Type: application/json\" \
      -d '{\"password\": \"secret123\"}'
    ```

    **Response if valid:**
    ```json
    {
      \"valid\": true,
      \"public_api_key\": \"prk_abc123...\"
    }
    ```

    **Response if invalid:**
    ```json
    {
      \"valid\": false,
      \"public_api_key\": null
    }
    ```

    Args:
        public_name (str): Public name of the published retriever
        body (VerifyPasswordRequest): Request to verify password for a password-protected
            retriever.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | VerifyPasswordResponse]
     """

    kwargs = _get_kwargs(
        public_name=public_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    public_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: VerifyPasswordRequest,
) -> ErrorResponse | HTTPValidationError | VerifyPasswordResponse | None:
    r""" Verify Password

     Verify password for a password-protected retriever.

    Allows the frontend to check if a password is valid before attempting to execute
    a password-protected retriever. Returns the public API key if the password is valid.

    **Authentication:**
    - NO authentication required - this endpoint is public
    - The password is verified against the retriever's configured password

    **Use Case:**
    1. Frontend detects that a retriever is password-protected (from /config endpoint)
    2. User enters password in the UI
    3. Frontend calls this endpoint to verify the password
    4. If valid, frontend receives the public_api_key to use for subsequent requests

    **Response:**
    - `valid`: Whether the password is correct
    - `public_api_key`: The API key to use for execute/interact endpoints (only if valid)

    **Example:**
    ```bash
    curl -X POST \"https://api.mixpeek.com/v1/public/retrievers/private-search/verify\" \
      -H \"Content-Type: application/json\" \
      -d '{\"password\": \"secret123\"}'
    ```

    **Response if valid:**
    ```json
    {
      \"valid\": true,
      \"public_api_key\": \"prk_abc123...\"
    }
    ```

    **Response if invalid:**
    ```json
    {
      \"valid\": false,
      \"public_api_key\": null
    }
    ```

    Args:
        public_name (str): Public name of the published retriever
        body (VerifyPasswordRequest): Request to verify password for a password-protected
            retriever.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | VerifyPasswordResponse
     """

    return (
        await asyncio_detailed(
            public_name=public_name,
            client=client,
            body=body,
        )
    ).parsed
