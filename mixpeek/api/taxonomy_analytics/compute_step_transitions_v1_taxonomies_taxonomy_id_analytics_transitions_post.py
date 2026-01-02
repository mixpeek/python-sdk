from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.step_transition_request import StepTransitionRequest
from ...models.step_transition_response import StepTransitionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    taxonomy_id: str,
    *,
    body: StepTransitionRequest,
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
        "url": "/v1/taxonomies/{taxonomy_id}/analytics/transitions".format(
            taxonomy_id=quote(str(taxonomy_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | StepTransitionResponse | None:
    if response.status_code == 200:
        response_200 = StepTransitionResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | StepTransitionResponse]:
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
    body: StepTransitionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | StepTransitionResponse]:
    r"""Compute step transition analytics

     Analyze how documents progress from one taxonomy step to another.

    This endpoint computes conversion rates, duration statistics, and predictor lifts
    for documents transitioning between taxonomy labels.

    ## Use Cases

    **Email Thread Analysis:**
    - Question: How long from \"inquiry\" to \"closed_won\"?
    - Question: What % of inquiries result in sales?
    - Question: Which sender domains have highest conversion?

    **Content Workflow Tracking:**
    - Question: Conversion rate from \"draft\" to \"published\"?
    - Question: How long does content stay in review?
    - Question: Which authors publish fastest?

    **Safety Compliance Monitoring:**
    - Question: Time from violation detection to resolution?
    - Question: Success rate for remediation efforts?

    ## Requirements

    - Taxonomy must have `step_analytics` configured (or provide `override_step_analytics`)
    - Collection must contain documents enriched with this taxonomy
    - Documents must have timestamp and sequence grouping fields configured

    ## Returns

    **Conversion Metrics:**
    - `count`: Total sequences starting at from_step
    - `converted`: Number reaching to_step
    - `conversion_rate`: Percentage that converted

    **Duration Statistics (if converted > 0):**
    - `mean`, `median`: Average and middle duration
    - `p90`, `p95`: 90th and 95th percentile durations
    - `std_dev`, `min`, `max`: Distribution statistics

    **Top Predictors:**
    - Covariates with highest impact on conversion
    - Lift values (>1.0 = increases conversion, <1.0 = decreases)
    - Statistical significance via minimum support threshold

    ## Example Request

    ```json
    {
        \"collection_id\": \"col_emails\",
        \"taxonomy_id\": \"tax_sales_stages\",
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"max_window_days\": 90,
        \"min_support\": 10
    }
    ```

    ## Example Response

    ```json
    {
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"count\": 1000,
        \"converted\": 350,
        \"conversion_rate\": 0.35,
        \"durations_sec\": {
            \"mean\": 432000.0,
            \"median\": 345600.0,
            \"p50\": 345600.0,
            \"p90\": 691200.0,
            \"p95\": 864000.0
        },
        \"top_predictors\": [
            {
                \"field\": \"Sender Domain\",
                \"value\": \"enterprise.com\",
                \"count\": 150,
                \"conversion_rate\": 0.75,
                \"lift\": 2.14
            }
        ]
    }
    ```

    Args:
        taxonomy_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (StepTransitionRequest): API request model for step transition analytics.

            This model extends the engine query model with API-specific validation
            and documentation.

            Use this to analyze how documents transition from one taxonomy step to another,
            computing conversion rates, durations, and predictor lifts.

            Example:
                ```json
                {
                    "collection_id": "col_emails",
                    "taxonomy_id": "tax_sales_stages",
                    "from_step": "inquiry",
                    "to_step": "closed_won",
                    "max_window_days": 90,
                    "min_support": 10
                }
                ```

            Response includes:
                - Conversion rate (% reaching to_step)
                - Duration statistics (mean, median, p90, p95)
                - Top predictors (covariates with highest lift)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | StepTransitionResponse]
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
    body: StepTransitionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | StepTransitionResponse | None:
    r"""Compute step transition analytics

     Analyze how documents progress from one taxonomy step to another.

    This endpoint computes conversion rates, duration statistics, and predictor lifts
    for documents transitioning between taxonomy labels.

    ## Use Cases

    **Email Thread Analysis:**
    - Question: How long from \"inquiry\" to \"closed_won\"?
    - Question: What % of inquiries result in sales?
    - Question: Which sender domains have highest conversion?

    **Content Workflow Tracking:**
    - Question: Conversion rate from \"draft\" to \"published\"?
    - Question: How long does content stay in review?
    - Question: Which authors publish fastest?

    **Safety Compliance Monitoring:**
    - Question: Time from violation detection to resolution?
    - Question: Success rate for remediation efforts?

    ## Requirements

    - Taxonomy must have `step_analytics` configured (or provide `override_step_analytics`)
    - Collection must contain documents enriched with this taxonomy
    - Documents must have timestamp and sequence grouping fields configured

    ## Returns

    **Conversion Metrics:**
    - `count`: Total sequences starting at from_step
    - `converted`: Number reaching to_step
    - `conversion_rate`: Percentage that converted

    **Duration Statistics (if converted > 0):**
    - `mean`, `median`: Average and middle duration
    - `p90`, `p95`: 90th and 95th percentile durations
    - `std_dev`, `min`, `max`: Distribution statistics

    **Top Predictors:**
    - Covariates with highest impact on conversion
    - Lift values (>1.0 = increases conversion, <1.0 = decreases)
    - Statistical significance via minimum support threshold

    ## Example Request

    ```json
    {
        \"collection_id\": \"col_emails\",
        \"taxonomy_id\": \"tax_sales_stages\",
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"max_window_days\": 90,
        \"min_support\": 10
    }
    ```

    ## Example Response

    ```json
    {
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"count\": 1000,
        \"converted\": 350,
        \"conversion_rate\": 0.35,
        \"durations_sec\": {
            \"mean\": 432000.0,
            \"median\": 345600.0,
            \"p50\": 345600.0,
            \"p90\": 691200.0,
            \"p95\": 864000.0
        },
        \"top_predictors\": [
            {
                \"field\": \"Sender Domain\",
                \"value\": \"enterprise.com\",
                \"count\": 150,
                \"conversion_rate\": 0.75,
                \"lift\": 2.14
            }
        ]
    }
    ```

    Args:
        taxonomy_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (StepTransitionRequest): API request model for step transition analytics.

            This model extends the engine query model with API-specific validation
            and documentation.

            Use this to analyze how documents transition from one taxonomy step to another,
            computing conversion rates, durations, and predictor lifts.

            Example:
                ```json
                {
                    "collection_id": "col_emails",
                    "taxonomy_id": "tax_sales_stages",
                    "from_step": "inquiry",
                    "to_step": "closed_won",
                    "max_window_days": 90,
                    "min_support": 10
                }
                ```

            Response includes:
                - Conversion rate (% reaching to_step)
                - Duration statistics (mean, median, p90, p95)
                - Top predictors (covariates with highest lift)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | StepTransitionResponse
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
    body: StepTransitionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | StepTransitionResponse]:
    r"""Compute step transition analytics

     Analyze how documents progress from one taxonomy step to another.

    This endpoint computes conversion rates, duration statistics, and predictor lifts
    for documents transitioning between taxonomy labels.

    ## Use Cases

    **Email Thread Analysis:**
    - Question: How long from \"inquiry\" to \"closed_won\"?
    - Question: What % of inquiries result in sales?
    - Question: Which sender domains have highest conversion?

    **Content Workflow Tracking:**
    - Question: Conversion rate from \"draft\" to \"published\"?
    - Question: How long does content stay in review?
    - Question: Which authors publish fastest?

    **Safety Compliance Monitoring:**
    - Question: Time from violation detection to resolution?
    - Question: Success rate for remediation efforts?

    ## Requirements

    - Taxonomy must have `step_analytics` configured (or provide `override_step_analytics`)
    - Collection must contain documents enriched with this taxonomy
    - Documents must have timestamp and sequence grouping fields configured

    ## Returns

    **Conversion Metrics:**
    - `count`: Total sequences starting at from_step
    - `converted`: Number reaching to_step
    - `conversion_rate`: Percentage that converted

    **Duration Statistics (if converted > 0):**
    - `mean`, `median`: Average and middle duration
    - `p90`, `p95`: 90th and 95th percentile durations
    - `std_dev`, `min`, `max`: Distribution statistics

    **Top Predictors:**
    - Covariates with highest impact on conversion
    - Lift values (>1.0 = increases conversion, <1.0 = decreases)
    - Statistical significance via minimum support threshold

    ## Example Request

    ```json
    {
        \"collection_id\": \"col_emails\",
        \"taxonomy_id\": \"tax_sales_stages\",
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"max_window_days\": 90,
        \"min_support\": 10
    }
    ```

    ## Example Response

    ```json
    {
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"count\": 1000,
        \"converted\": 350,
        \"conversion_rate\": 0.35,
        \"durations_sec\": {
            \"mean\": 432000.0,
            \"median\": 345600.0,
            \"p50\": 345600.0,
            \"p90\": 691200.0,
            \"p95\": 864000.0
        },
        \"top_predictors\": [
            {
                \"field\": \"Sender Domain\",
                \"value\": \"enterprise.com\",
                \"count\": 150,
                \"conversion_rate\": 0.75,
                \"lift\": 2.14
            }
        ]
    }
    ```

    Args:
        taxonomy_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (StepTransitionRequest): API request model for step transition analytics.

            This model extends the engine query model with API-specific validation
            and documentation.

            Use this to analyze how documents transition from one taxonomy step to another,
            computing conversion rates, durations, and predictor lifts.

            Example:
                ```json
                {
                    "collection_id": "col_emails",
                    "taxonomy_id": "tax_sales_stages",
                    "from_step": "inquiry",
                    "to_step": "closed_won",
                    "max_window_days": 90,
                    "min_support": 10
                }
                ```

            Response includes:
                - Conversion rate (% reaching to_step)
                - Duration statistics (mean, median, p90, p95)
                - Top predictors (covariates with highest lift)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | StepTransitionResponse]
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
    body: StepTransitionRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | StepTransitionResponse | None:
    r"""Compute step transition analytics

     Analyze how documents progress from one taxonomy step to another.

    This endpoint computes conversion rates, duration statistics, and predictor lifts
    for documents transitioning between taxonomy labels.

    ## Use Cases

    **Email Thread Analysis:**
    - Question: How long from \"inquiry\" to \"closed_won\"?
    - Question: What % of inquiries result in sales?
    - Question: Which sender domains have highest conversion?

    **Content Workflow Tracking:**
    - Question: Conversion rate from \"draft\" to \"published\"?
    - Question: How long does content stay in review?
    - Question: Which authors publish fastest?

    **Safety Compliance Monitoring:**
    - Question: Time from violation detection to resolution?
    - Question: Success rate for remediation efforts?

    ## Requirements

    - Taxonomy must have `step_analytics` configured (or provide `override_step_analytics`)
    - Collection must contain documents enriched with this taxonomy
    - Documents must have timestamp and sequence grouping fields configured

    ## Returns

    **Conversion Metrics:**
    - `count`: Total sequences starting at from_step
    - `converted`: Number reaching to_step
    - `conversion_rate`: Percentage that converted

    **Duration Statistics (if converted > 0):**
    - `mean`, `median`: Average and middle duration
    - `p90`, `p95`: 90th and 95th percentile durations
    - `std_dev`, `min`, `max`: Distribution statistics

    **Top Predictors:**
    - Covariates with highest impact on conversion
    - Lift values (>1.0 = increases conversion, <1.0 = decreases)
    - Statistical significance via minimum support threshold

    ## Example Request

    ```json
    {
        \"collection_id\": \"col_emails\",
        \"taxonomy_id\": \"tax_sales_stages\",
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"max_window_days\": 90,
        \"min_support\": 10
    }
    ```

    ## Example Response

    ```json
    {
        \"from_step\": \"inquiry\",
        \"to_step\": \"closed_won\",
        \"count\": 1000,
        \"converted\": 350,
        \"conversion_rate\": 0.35,
        \"durations_sec\": {
            \"mean\": 432000.0,
            \"median\": 345600.0,
            \"p50\": 345600.0,
            \"p90\": 691200.0,
            \"p95\": 864000.0
        },
        \"top_predictors\": [
            {
                \"field\": \"Sender Domain\",
                \"value\": \"enterprise.com\",
                \"count\": 150,
                \"conversion_rate\": 0.75,
                \"lift\": 2.14
            }
        ]
    }
    ```

    Args:
        taxonomy_id (str):
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (StepTransitionRequest): API request model for step transition analytics.

            This model extends the engine query model with API-specific validation
            and documentation.

            Use this to analyze how documents transition from one taxonomy step to another,
            computing conversion rates, durations, and predictor lifts.

            Example:
                ```json
                {
                    "collection_id": "col_emails",
                    "taxonomy_id": "tax_sales_stages",
                    "from_step": "inquiry",
                    "to_step": "closed_won",
                    "max_window_days": 90,
                    "min_support": 10
                }
                ```

            Response includes:
                - Conversion rate (% reaching to_step)
                - Duration statistics (mean, median, p90, p95)
                - Top predictors (covariates with highest lift)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | StepTransitionResponse
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
