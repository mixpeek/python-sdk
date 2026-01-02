from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.apply_result import ApplyResult
from ...models.body_apply_manifest_v1_manifest_apply_post import BodyApplyManifestV1ManifestApplyPost
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyApplyManifestV1ManifestApplyPost,
    dry_run: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["dry_run"] = dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/manifest/apply",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApplyResult | ErrorResponse | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = ApplyResult.from_dict(response.json())

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
) -> Response[ApplyResult | ErrorResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyApplyManifestV1ManifestApplyPost,
    dry_run: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> Response[ApplyResult | ErrorResponse | HTTPValidationError]:
    r""" Apply Manifest

     Apply a YAML manifest to create resources.

    Creates all resources defined in the manifest file in dependency order.
    Fails if any resource already exists (create-only mode).
    Performs automatic rollback if any resource creation fails.

    **Features:**
    - Topological sorting ensures resources are created in correct dependency order
    - Secret references (`${{ secrets.NAME }}`) are resolved from organization secrets
    - Atomic operation: rolls back all created resources if any creation fails
    - Dry run mode validates the manifest without making changes

    **Example:**
    ```bash
    curl -X POST /v1/manifest/apply \
      -H \"Authorization: Bearer $API_KEY\" \
      -H \"X-Namespace-Id: ns_xxx\" \
      -F \"manifest_file=@mixpeek.yaml\"
    ```

    **Example manifest:**
    ```yaml
    version: \"1.0\"
    metadata:
      name: \"my-environment\"

    namespaces:
      - name: video_search
        feature_extractors:
          - name: multimodal_extractor
            version: v1

    buckets:
      - name: raw_videos
        namespace: video_search
        schema:
          properties:
            video: { type: video }
    ```

    Args:
        dry_run (bool | Unset): Validate only, don't create resources Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (BodyApplyManifestV1ManifestApplyPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplyResult | ErrorResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        body=body,
        dry_run=dry_run,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BodyApplyManifestV1ManifestApplyPost,
    dry_run: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> ApplyResult | ErrorResponse | HTTPValidationError | None:
    r""" Apply Manifest

     Apply a YAML manifest to create resources.

    Creates all resources defined in the manifest file in dependency order.
    Fails if any resource already exists (create-only mode).
    Performs automatic rollback if any resource creation fails.

    **Features:**
    - Topological sorting ensures resources are created in correct dependency order
    - Secret references (`${{ secrets.NAME }}`) are resolved from organization secrets
    - Atomic operation: rolls back all created resources if any creation fails
    - Dry run mode validates the manifest without making changes

    **Example:**
    ```bash
    curl -X POST /v1/manifest/apply \
      -H \"Authorization: Bearer $API_KEY\" \
      -H \"X-Namespace-Id: ns_xxx\" \
      -F \"manifest_file=@mixpeek.yaml\"
    ```

    **Example manifest:**
    ```yaml
    version: \"1.0\"
    metadata:
      name: \"my-environment\"

    namespaces:
      - name: video_search
        feature_extractors:
          - name: multimodal_extractor
            version: v1

    buckets:
      - name: raw_videos
        namespace: video_search
        schema:
          properties:
            video: { type: video }
    ```

    Args:
        dry_run (bool | Unset): Validate only, don't create resources Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (BodyApplyManifestV1ManifestApplyPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplyResult | ErrorResponse | HTTPValidationError
     """

    return sync_detailed(
        client=client,
        body=body,
        dry_run=dry_run,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyApplyManifestV1ManifestApplyPost,
    dry_run: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> Response[ApplyResult | ErrorResponse | HTTPValidationError]:
    r""" Apply Manifest

     Apply a YAML manifest to create resources.

    Creates all resources defined in the manifest file in dependency order.
    Fails if any resource already exists (create-only mode).
    Performs automatic rollback if any resource creation fails.

    **Features:**
    - Topological sorting ensures resources are created in correct dependency order
    - Secret references (`${{ secrets.NAME }}`) are resolved from organization secrets
    - Atomic operation: rolls back all created resources if any creation fails
    - Dry run mode validates the manifest without making changes

    **Example:**
    ```bash
    curl -X POST /v1/manifest/apply \
      -H \"Authorization: Bearer $API_KEY\" \
      -H \"X-Namespace-Id: ns_xxx\" \
      -F \"manifest_file=@mixpeek.yaml\"
    ```

    **Example manifest:**
    ```yaml
    version: \"1.0\"
    metadata:
      name: \"my-environment\"

    namespaces:
      - name: video_search
        feature_extractors:
          - name: multimodal_extractor
            version: v1

    buckets:
      - name: raw_videos
        namespace: video_search
        schema:
          properties:
            video: { type: video }
    ```

    Args:
        dry_run (bool | Unset): Validate only, don't create resources Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (BodyApplyManifestV1ManifestApplyPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplyResult | ErrorResponse | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        body=body,
        dry_run=dry_run,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BodyApplyManifestV1ManifestApplyPost,
    dry_run: bool | Unset = False,
    authorization: str | Unset = UNSET,
) -> ApplyResult | ErrorResponse | HTTPValidationError | None:
    r""" Apply Manifest

     Apply a YAML manifest to create resources.

    Creates all resources defined in the manifest file in dependency order.
    Fails if any resource already exists (create-only mode).
    Performs automatic rollback if any resource creation fails.

    **Features:**
    - Topological sorting ensures resources are created in correct dependency order
    - Secret references (`${{ secrets.NAME }}`) are resolved from organization secrets
    - Atomic operation: rolls back all created resources if any creation fails
    - Dry run mode validates the manifest without making changes

    **Example:**
    ```bash
    curl -X POST /v1/manifest/apply \
      -H \"Authorization: Bearer $API_KEY\" \
      -H \"X-Namespace-Id: ns_xxx\" \
      -F \"manifest_file=@mixpeek.yaml\"
    ```

    **Example manifest:**
    ```yaml
    version: \"1.0\"
    metadata:
      name: \"my-environment\"

    namespaces:
      - name: video_search
        feature_extractors:
          - name: multimodal_extractor
            version: v1

    buckets:
      - name: raw_videos
        namespace: video_search
        schema:
          properties:
            video: { type: video }
    ```

    Args:
        dry_run (bool | Unset): Validate only, don't create resources Default: False.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        body (BodyApplyManifestV1ManifestApplyPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplyResult | ErrorResponse | HTTPValidationError
     """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            dry_run=dry_run,
            authorization=authorization,
        )
    ).parsed
