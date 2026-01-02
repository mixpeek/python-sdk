from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.path_analysis_request import PathAnalysisRequest
from ...models.path_analysis_response import PathAnalysisResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    taxonomy_id: str,
    *,
    body: PathAnalysisRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_namespace, Unset):
        headers["X-Namespace"] = x_namespace

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/taxonomies/{taxonomy_id}/analytics/paths".format(
            taxonomy_id=quote(str(taxonomy_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | PathAnalysisResponse | None:
    if response.status_code == 200:
        response_200 = PathAnalysisResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | PathAnalysisResponse]:
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
    body: PathAnalysisRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | PathAnalysisResponse]:
    r"""Analyze multi-step transition paths

     Discover the most common multi-step paths documents take between two taxonomy steps.

    Unlike the `/transitions` endpoint which only analyzes direct A→B transitions,
    this endpoint reveals the intermediate steps documents actually take.

    ## Use Cases

    **Email Thread Analysis:**
    - Question: What paths do emails take from \"inquiry\" to \"closed_won\"?
    - Discover: Some go inquiry → followup → proposal → closed_won
    - Discover: Others skip steps: inquiry → proposal → closed_won
    - Discover: Fast track: inquiry → closed_won

    **Content Editorial Paths:**
    - Question: Common paths from \"draft\" to \"published\"?
    - Discover: draft → review → edit → review → published
    - Discover: draft → review → published (expedited)
    - Discover: Paths that loop back (draft → review → draft → review)

    **Compliance Resolution Paths:**
    - Question: How do violations get resolved?
    - Discover: violation → investigated → remediated → resolved
    - Discover: violation → false_positive → closed
    - Discover: Escalation paths: violation → escalated → legal_review → resolved

    ## Requirements

    - Taxonomy must have `step_analytics` configured
    - Collection must contain documents with timestamp and sequence_id fields

    ## Returns

    **Completion Metrics:**
    - `total_sequences`: Sequences starting at from_step
    - `completed_sequences`: Number reaching to_step
    - `completion_rate`: Percentage that completed

    **Paths (sorted by frequency):**
    - `path`: Ordered sequence of steps
    - `count`: Number of sequences following this path
    - `percentage`: Percentage of completing sequences
    - `avg_duration_sec`: Average time for this path

    ## Example Request

    ```json
    {
        \"collection_id\": \"col_emails\",
        \"taxonomy_id\": \"tax_sales_stages\",
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"max_path_length\": 10,
        \"min_support\": 5
    }
    ```

    ## Example Response

    ```json
    {
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"total_sequences\": 1000,
        \"completed_sequences\": 350,
        \"completion_rate\": 0.35,
        \"paths\": [
            {
                \"path\": [\"inquiry\", \"followup\", \"proposal\", \"closed_won\"],
                \"count\": 120,
                \"percentage\": 34.3,
                \"avg_duration_sec\": 604800.0
            },
            {
                \"path\": [\"inquiry\", \"proposal\", \"closed_won\"],
                \"count\": 90,
                \"percentage\": 25.7,
                \"avg_duration_sec\": 432000.0
            },
            {
                \"path\": [\"inquiry\", \"closed_won\"],
                \"count\": 70,
                \"percentage\": 20.0,
                \"avg_duration_sec\": 172800.0
            }
        ]
    }
    ```

    ## Path Interpretation

    **Length Analysis:**
    - Shorter paths indicate efficient progression
    - Longer paths may indicate complexity or bottlenecks
    - Loops (repeated steps) indicate rework or revisions

    **Duration Analysis:**
    - Compare avg_duration_sec across paths
    - Shorter paths may not always be faster
    - Identify optimization opportunities

    **Frequency Analysis:**
    - High-percentage paths are \"happy paths\"
    - Low-percentage paths may be edge cases or exceptions
    - Missing expected paths indicate drop-off points

    Args:
        taxonomy_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (PathAnalysisRequest): API request model for multi-step path analysis.

            Discovers the most common sequences of intermediate steps documents take
            when progressing from from_step to to_step.

            Unlike the transitions endpoint which only analyzes direct A→B progressions,
            this endpoint reveals the actual paths taken (e.g., A → X → Y → B).

            Example:
                ```json
                {
                    "collection_id": "col_emails",
                    "taxonomy_id": "tax_sales_stages",
                    "from_step": "inquiry",
                    "to_step": "closed_won",
                    "max_path_length": 10,
                    "min_support": 5
                }
                ```

            Response includes:
                - Most common paths sorted by frequency
                - Count and percentage for each path
                - Average duration per path

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | PathAnalysisResponse]
    """

    kwargs = _get_kwargs(
        taxonomy_id=taxonomy_id,
        body=body,
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
    body: PathAnalysisRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | PathAnalysisResponse | None:
    r"""Analyze multi-step transition paths

     Discover the most common multi-step paths documents take between two taxonomy steps.

    Unlike the `/transitions` endpoint which only analyzes direct A→B transitions,
    this endpoint reveals the intermediate steps documents actually take.

    ## Use Cases

    **Email Thread Analysis:**
    - Question: What paths do emails take from \"inquiry\" to \"closed_won\"?
    - Discover: Some go inquiry → followup → proposal → closed_won
    - Discover: Others skip steps: inquiry → proposal → closed_won
    - Discover: Fast track: inquiry → closed_won

    **Content Editorial Paths:**
    - Question: Common paths from \"draft\" to \"published\"?
    - Discover: draft → review → edit → review → published
    - Discover: draft → review → published (expedited)
    - Discover: Paths that loop back (draft → review → draft → review)

    **Compliance Resolution Paths:**
    - Question: How do violations get resolved?
    - Discover: violation → investigated → remediated → resolved
    - Discover: violation → false_positive → closed
    - Discover: Escalation paths: violation → escalated → legal_review → resolved

    ## Requirements

    - Taxonomy must have `step_analytics` configured
    - Collection must contain documents with timestamp and sequence_id fields

    ## Returns

    **Completion Metrics:**
    - `total_sequences`: Sequences starting at from_step
    - `completed_sequences`: Number reaching to_step
    - `completion_rate`: Percentage that completed

    **Paths (sorted by frequency):**
    - `path`: Ordered sequence of steps
    - `count`: Number of sequences following this path
    - `percentage`: Percentage of completing sequences
    - `avg_duration_sec`: Average time for this path

    ## Example Request

    ```json
    {
        \"collection_id\": \"col_emails\",
        \"taxonomy_id\": \"tax_sales_stages\",
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"max_path_length\": 10,
        \"min_support\": 5
    }
    ```

    ## Example Response

    ```json
    {
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"total_sequences\": 1000,
        \"completed_sequences\": 350,
        \"completion_rate\": 0.35,
        \"paths\": [
            {
                \"path\": [\"inquiry\", \"followup\", \"proposal\", \"closed_won\"],
                \"count\": 120,
                \"percentage\": 34.3,
                \"avg_duration_sec\": 604800.0
            },
            {
                \"path\": [\"inquiry\", \"proposal\", \"closed_won\"],
                \"count\": 90,
                \"percentage\": 25.7,
                \"avg_duration_sec\": 432000.0
            },
            {
                \"path\": [\"inquiry\", \"closed_won\"],
                \"count\": 70,
                \"percentage\": 20.0,
                \"avg_duration_sec\": 172800.0
            }
        ]
    }
    ```

    ## Path Interpretation

    **Length Analysis:**
    - Shorter paths indicate efficient progression
    - Longer paths may indicate complexity or bottlenecks
    - Loops (repeated steps) indicate rework or revisions

    **Duration Analysis:**
    - Compare avg_duration_sec across paths
    - Shorter paths may not always be faster
    - Identify optimization opportunities

    **Frequency Analysis:**
    - High-percentage paths are \"happy paths\"
    - Low-percentage paths may be edge cases or exceptions
    - Missing expected paths indicate drop-off points

    Args:
        taxonomy_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (PathAnalysisRequest): API request model for multi-step path analysis.

            Discovers the most common sequences of intermediate steps documents take
            when progressing from from_step to to_step.

            Unlike the transitions endpoint which only analyzes direct A→B progressions,
            this endpoint reveals the actual paths taken (e.g., A → X → Y → B).

            Example:
                ```json
                {
                    "collection_id": "col_emails",
                    "taxonomy_id": "tax_sales_stages",
                    "from_step": "inquiry",
                    "to_step": "closed_won",
                    "max_path_length": 10,
                    "min_support": 5
                }
                ```

            Response includes:
                - Most common paths sorted by frequency
                - Count and percentage for each path
                - Average duration per path

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | PathAnalysisResponse
    """

    return sync_detailed(
        taxonomy_id=taxonomy_id,
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    taxonomy_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PathAnalysisRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | PathAnalysisResponse]:
    r"""Analyze multi-step transition paths

     Discover the most common multi-step paths documents take between two taxonomy steps.

    Unlike the `/transitions` endpoint which only analyzes direct A→B transitions,
    this endpoint reveals the intermediate steps documents actually take.

    ## Use Cases

    **Email Thread Analysis:**
    - Question: What paths do emails take from \"inquiry\" to \"closed_won\"?
    - Discover: Some go inquiry → followup → proposal → closed_won
    - Discover: Others skip steps: inquiry → proposal → closed_won
    - Discover: Fast track: inquiry → closed_won

    **Content Editorial Paths:**
    - Question: Common paths from \"draft\" to \"published\"?
    - Discover: draft → review → edit → review → published
    - Discover: draft → review → published (expedited)
    - Discover: Paths that loop back (draft → review → draft → review)

    **Compliance Resolution Paths:**
    - Question: How do violations get resolved?
    - Discover: violation → investigated → remediated → resolved
    - Discover: violation → false_positive → closed
    - Discover: Escalation paths: violation → escalated → legal_review → resolved

    ## Requirements

    - Taxonomy must have `step_analytics` configured
    - Collection must contain documents with timestamp and sequence_id fields

    ## Returns

    **Completion Metrics:**
    - `total_sequences`: Sequences starting at from_step
    - `completed_sequences`: Number reaching to_step
    - `completion_rate`: Percentage that completed

    **Paths (sorted by frequency):**
    - `path`: Ordered sequence of steps
    - `count`: Number of sequences following this path
    - `percentage`: Percentage of completing sequences
    - `avg_duration_sec`: Average time for this path

    ## Example Request

    ```json
    {
        \"collection_id\": \"col_emails\",
        \"taxonomy_id\": \"tax_sales_stages\",
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"max_path_length\": 10,
        \"min_support\": 5
    }
    ```

    ## Example Response

    ```json
    {
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"total_sequences\": 1000,
        \"completed_sequences\": 350,
        \"completion_rate\": 0.35,
        \"paths\": [
            {
                \"path\": [\"inquiry\", \"followup\", \"proposal\", \"closed_won\"],
                \"count\": 120,
                \"percentage\": 34.3,
                \"avg_duration_sec\": 604800.0
            },
            {
                \"path\": [\"inquiry\", \"proposal\", \"closed_won\"],
                \"count\": 90,
                \"percentage\": 25.7,
                \"avg_duration_sec\": 432000.0
            },
            {
                \"path\": [\"inquiry\", \"closed_won\"],
                \"count\": 70,
                \"percentage\": 20.0,
                \"avg_duration_sec\": 172800.0
            }
        ]
    }
    ```

    ## Path Interpretation

    **Length Analysis:**
    - Shorter paths indicate efficient progression
    - Longer paths may indicate complexity or bottlenecks
    - Loops (repeated steps) indicate rework or revisions

    **Duration Analysis:**
    - Compare avg_duration_sec across paths
    - Shorter paths may not always be faster
    - Identify optimization opportunities

    **Frequency Analysis:**
    - High-percentage paths are \"happy paths\"
    - Low-percentage paths may be edge cases or exceptions
    - Missing expected paths indicate drop-off points

    Args:
        taxonomy_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (PathAnalysisRequest): API request model for multi-step path analysis.

            Discovers the most common sequences of intermediate steps documents take
            when progressing from from_step to to_step.

            Unlike the transitions endpoint which only analyzes direct A→B progressions,
            this endpoint reveals the actual paths taken (e.g., A → X → Y → B).

            Example:
                ```json
                {
                    "collection_id": "col_emails",
                    "taxonomy_id": "tax_sales_stages",
                    "from_step": "inquiry",
                    "to_step": "closed_won",
                    "max_path_length": 10,
                    "min_support": 5
                }
                ```

            Response includes:
                - Most common paths sorted by frequency
                - Count and percentage for each path
                - Average duration per path

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | PathAnalysisResponse]
    """

    kwargs = _get_kwargs(
        taxonomy_id=taxonomy_id,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    taxonomy_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PathAnalysisRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | PathAnalysisResponse | None:
    r"""Analyze multi-step transition paths

     Discover the most common multi-step paths documents take between two taxonomy steps.

    Unlike the `/transitions` endpoint which only analyzes direct A→B transitions,
    this endpoint reveals the intermediate steps documents actually take.

    ## Use Cases

    **Email Thread Analysis:**
    - Question: What paths do emails take from \"inquiry\" to \"closed_won\"?
    - Discover: Some go inquiry → followup → proposal → closed_won
    - Discover: Others skip steps: inquiry → proposal → closed_won
    - Discover: Fast track: inquiry → closed_won

    **Content Editorial Paths:**
    - Question: Common paths from \"draft\" to \"published\"?
    - Discover: draft → review → edit → review → published
    - Discover: draft → review → published (expedited)
    - Discover: Paths that loop back (draft → review → draft → review)

    **Compliance Resolution Paths:**
    - Question: How do violations get resolved?
    - Discover: violation → investigated → remediated → resolved
    - Discover: violation → false_positive → closed
    - Discover: Escalation paths: violation → escalated → legal_review → resolved

    ## Requirements

    - Taxonomy must have `step_analytics` configured
    - Collection must contain documents with timestamp and sequence_id fields

    ## Returns

    **Completion Metrics:**
    - `total_sequences`: Sequences starting at from_step
    - `completed_sequences`: Number reaching to_step
    - `completion_rate`: Percentage that completed

    **Paths (sorted by frequency):**
    - `path`: Ordered sequence of steps
    - `count`: Number of sequences following this path
    - `percentage`: Percentage of completing sequences
    - `avg_duration_sec`: Average time for this path

    ## Example Request

    ```json
    {
        \"collection_id\": \"col_emails\",
        \"taxonomy_id\": \"tax_sales_stages\",
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"max_path_length\": 10,
        \"min_support\": 5
    }
    ```

    ## Example Response

    ```json
    {
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"total_sequences\": 1000,
        \"completed_sequences\": 350,
        \"completion_rate\": 0.35,
        \"paths\": [
            {
                \"path\": [\"inquiry\", \"followup\", \"proposal\", \"closed_won\"],
                \"count\": 120,
                \"percentage\": 34.3,
                \"avg_duration_sec\": 604800.0
            },
            {
                \"path\": [\"inquiry\", \"proposal\", \"closed_won\"],
                \"count\": 90,
                \"percentage\": 25.7,
                \"avg_duration_sec\": 432000.0
            },
            {
                \"path\": [\"inquiry\", \"closed_won\"],
                \"count\": 70,
                \"percentage\": 20.0,
                \"avg_duration_sec\": 172800.0
            }
        ]
    }
    ```

    ## Path Interpretation

    **Length Analysis:**
    - Shorter paths indicate efficient progression
    - Longer paths may indicate complexity or bottlenecks
    - Loops (repeated steps) indicate rework or revisions

    **Duration Analysis:**
    - Compare avg_duration_sec across paths
    - Shorter paths may not always be faster
    - Identify optimization opportunities

    **Frequency Analysis:**
    - High-percentage paths are \"happy paths\"
    - Low-percentage paths may be edge cases or exceptions
    - Missing expected paths indicate drop-off points

    Args:
        taxonomy_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (PathAnalysisRequest): API request model for multi-step path analysis.

            Discovers the most common sequences of intermediate steps documents take
            when progressing from from_step to to_step.

            Unlike the transitions endpoint which only analyzes direct A→B progressions,
            this endpoint reveals the actual paths taken (e.g., A → X → Y → B).

            Example:
                ```json
                {
                    "collection_id": "col_emails",
                    "taxonomy_id": "tax_sales_stages",
                    "from_step": "inquiry",
                    "to_step": "closed_won",
                    "max_path_length": 10,
                    "min_support": 5
                }
                ```

            Response includes:
                - Most common paths sorted by frequency
                - Count and percentage for each path
                - Average duration per path

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | PathAnalysisResponse
    """

    return (
        await asyncio_detailed(
            taxonomy_id=taxonomy_id,
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
