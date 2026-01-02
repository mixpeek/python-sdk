from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.explain_retriever_request import ExplainRetrieverRequest
from ...models.explain_retriever_response import ExplainRetrieverResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    retriever_id: str,
    *,
    body: ExplainRetrieverRequest,
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
        "url": "/v1/retrievers/{retriever_id}/execute/explain".format(
            retriever_id=quote(str(retriever_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ExplainRetrieverResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ExplainRetrieverResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | ExplainRetrieverResponse | HTTPValidationError]:
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
    body: ExplainRetrieverRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | ExplainRetrieverResponse | HTTPValidationError]:
    r"""Explain Retriever Execution Plan

     Get a detailed execution plan for a retriever without actually executing it. Similar to MongoDB's
    explain plan or SQL's EXPLAIN command, this endpoint helps you understand performance
    characteristics, identify bottlenecks, estimate costs, and troubleshoot retrieval issues before
    running expensive queries.

    **What This Returns:**
    - Stage-by-stage execution plan (AFTER automatic optimizations)
    - Estimated costs (credits + time per stage)
    - Document flow projections (input/output counts per stage)
    - Efficiency metrics (selectivity ratios, cache likelihood)
    - Bottleneck identification (slowest/most expensive stages)
    - Optimization details (transformations applied by the optimizer)
    - Performance warnings and improvement suggestions


    **Key Features:**
    - **Cost Estimation**: See how many credits and milliseconds each stage will consume
    - **Bottleneck Detection**: Identify which stages dominate execution time
    - **Optimization Transparency**: Understand how your pipeline was optimized
    - **Cache Analysis**: See which stages are likely to hit cache
    - **Accuracy Troubleshooting**: Analyze stage efficiency and document flow
    - **Latency Analysis**: Break down estimated duration by stage


    **Important:** The execution_plan shows OPTIMIZED stages (after automatic transformations like
    filter push-down, stage fusion, and grouping optimization). Check optimization_details to understand
    what changed from your original configuration.


    **Use Cases:**
    - Debug slow retrievers by identifying bottleneck stages
    - Estimate costs before running expensive queries
    - Understand how the optimizer transformed your pipeline
    - Troubleshoot accuracy issues by analyzing stage selectivity
    - Compare different retriever configurations
    - Plan budget allocation for production workloads


    **Example Response:**
    ```json
    {
      \"retriever_id\": \"ret_abc123\",
      \"retriever_name\": \"product_search\",
      \"execution_plan\": [
        {
          \"stage_index\": 0,
          \"stage_name\": \"attribute_filter\",
          \"stage_type\": \"filter\",
          \"estimated_input\": 10000,
          \"estimated_output\": 5000,
          \"estimated_efficiency\": 0.5,
          \"estimated_cost_credits\": 0.01,
          \"estimated_duration_ms\": 20,
          \"cache_likely\": true,
          \"optimization_notes\": [\"Pushed down from stage 2\"],
          \"warnings\": []
        },
        {
          \"stage_index\": 1,
          \"stage_name\": \"semantic_search\",
          \"stage_type\": \"filter\",
          \"estimated_input\": 5000,
          \"estimated_output\": 100,
          \"estimated_efficiency\": 0.02,
          \"estimated_cost_credits\": 0.5,
          \"estimated_duration_ms\": 200,
          \"cache_likely\": false,
          \"optimization_notes\": [],
          \"warnings\": [\"High cost stage - consider reducing limit\"]
        }
      ],
      \"estimated_cost\": {
        \"total_credits\": 0.51,
        \"total_duration_ms\": 220
      },
      \"bottleneck_stages\": [\"semantic_search\"],
      \"optimization_applied\": true,
      \"optimization_details\": {
        \"original_stage_count\": 3,
        \"optimized_stage_count\": 2,
        \"optimization_time_ms\": 8.2,
        \"stage_reduction_pct\": 33.3,
        \"decisions\": [
          {
            \"rule_type\": \"push_down_filters\",
            \"applied\": true,
            \"reason\": \"Moved attribute_filter before semantic_search to reduce search scope\"
          }
        ]
      },
      \"optimization_suggestions\": [
        {
          \"type\": \"reduce_limit\",
          \"stage\": \"semantic_search\",
          \"message\": \"Consider reducing limit to improve latency\"
        }
      ]
    }
    ```

    Args:
        retriever_id (str): Retriever ID or name to explain. The execution plan will show the
            OPTIMIZED version after automatic transformations.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ExplainRetrieverRequest): Request to get execution plan for a retriever.

            Provides optional hypothetical inputs to tailor the execution plan estimation.
            The explain endpoint analyzes your retriever configuration and returns cost/latency
            estimates without actually executing the query.

            Use Cases:
                - See how plan changes with different input values
                - Estimate costs for different query patterns
                - Understand impact of parameter changes (e.g., top_k)
                - Test stage behavior with representative inputs

            Behavior:
                - If inputs are provided, they're used for tailored estimation
                - If inputs are not provided, default/representative values are used
                - Inputs do NOT need to match your input_schema exactly
                - No actual retrieval is performed (explain is analysis only)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ExplainRetrieverResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        retriever_id=retriever_id,
        body=body,
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
    body: ExplainRetrieverRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | ExplainRetrieverResponse | HTTPValidationError | None:
    r"""Explain Retriever Execution Plan

     Get a detailed execution plan for a retriever without actually executing it. Similar to MongoDB's
    explain plan or SQL's EXPLAIN command, this endpoint helps you understand performance
    characteristics, identify bottlenecks, estimate costs, and troubleshoot retrieval issues before
    running expensive queries.

    **What This Returns:**
    - Stage-by-stage execution plan (AFTER automatic optimizations)
    - Estimated costs (credits + time per stage)
    - Document flow projections (input/output counts per stage)
    - Efficiency metrics (selectivity ratios, cache likelihood)
    - Bottleneck identification (slowest/most expensive stages)
    - Optimization details (transformations applied by the optimizer)
    - Performance warnings and improvement suggestions


    **Key Features:**
    - **Cost Estimation**: See how many credits and milliseconds each stage will consume
    - **Bottleneck Detection**: Identify which stages dominate execution time
    - **Optimization Transparency**: Understand how your pipeline was optimized
    - **Cache Analysis**: See which stages are likely to hit cache
    - **Accuracy Troubleshooting**: Analyze stage efficiency and document flow
    - **Latency Analysis**: Break down estimated duration by stage


    **Important:** The execution_plan shows OPTIMIZED stages (after automatic transformations like
    filter push-down, stage fusion, and grouping optimization). Check optimization_details to understand
    what changed from your original configuration.


    **Use Cases:**
    - Debug slow retrievers by identifying bottleneck stages
    - Estimate costs before running expensive queries
    - Understand how the optimizer transformed your pipeline
    - Troubleshoot accuracy issues by analyzing stage selectivity
    - Compare different retriever configurations
    - Plan budget allocation for production workloads


    **Example Response:**
    ```json
    {
      \"retriever_id\": \"ret_abc123\",
      \"retriever_name\": \"product_search\",
      \"execution_plan\": [
        {
          \"stage_index\": 0,
          \"stage_name\": \"attribute_filter\",
          \"stage_type\": \"filter\",
          \"estimated_input\": 10000,
          \"estimated_output\": 5000,
          \"estimated_efficiency\": 0.5,
          \"estimated_cost_credits\": 0.01,
          \"estimated_duration_ms\": 20,
          \"cache_likely\": true,
          \"optimization_notes\": [\"Pushed down from stage 2\"],
          \"warnings\": []
        },
        {
          \"stage_index\": 1,
          \"stage_name\": \"semantic_search\",
          \"stage_type\": \"filter\",
          \"estimated_input\": 5000,
          \"estimated_output\": 100,
          \"estimated_efficiency\": 0.02,
          \"estimated_cost_credits\": 0.5,
          \"estimated_duration_ms\": 200,
          \"cache_likely\": false,
          \"optimization_notes\": [],
          \"warnings\": [\"High cost stage - consider reducing limit\"]
        }
      ],
      \"estimated_cost\": {
        \"total_credits\": 0.51,
        \"total_duration_ms\": 220
      },
      \"bottleneck_stages\": [\"semantic_search\"],
      \"optimization_applied\": true,
      \"optimization_details\": {
        \"original_stage_count\": 3,
        \"optimized_stage_count\": 2,
        \"optimization_time_ms\": 8.2,
        \"stage_reduction_pct\": 33.3,
        \"decisions\": [
          {
            \"rule_type\": \"push_down_filters\",
            \"applied\": true,
            \"reason\": \"Moved attribute_filter before semantic_search to reduce search scope\"
          }
        ]
      },
      \"optimization_suggestions\": [
        {
          \"type\": \"reduce_limit\",
          \"stage\": \"semantic_search\",
          \"message\": \"Consider reducing limit to improve latency\"
        }
      ]
    }
    ```

    Args:
        retriever_id (str): Retriever ID or name to explain. The execution plan will show the
            OPTIMIZED version after automatic transformations.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ExplainRetrieverRequest): Request to get execution plan for a retriever.

            Provides optional hypothetical inputs to tailor the execution plan estimation.
            The explain endpoint analyzes your retriever configuration and returns cost/latency
            estimates without actually executing the query.

            Use Cases:
                - See how plan changes with different input values
                - Estimate costs for different query patterns
                - Understand impact of parameter changes (e.g., top_k)
                - Test stage behavior with representative inputs

            Behavior:
                - If inputs are provided, they're used for tailored estimation
                - If inputs are not provided, default/representative values are used
                - Inputs do NOT need to match your input_schema exactly
                - No actual retrieval is performed (explain is analysis only)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ExplainRetrieverResponse | HTTPValidationError
    """

    return sync_detailed(
        retriever_id=retriever_id,
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExplainRetrieverRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | ExplainRetrieverResponse | HTTPValidationError]:
    r"""Explain Retriever Execution Plan

     Get a detailed execution plan for a retriever without actually executing it. Similar to MongoDB's
    explain plan or SQL's EXPLAIN command, this endpoint helps you understand performance
    characteristics, identify bottlenecks, estimate costs, and troubleshoot retrieval issues before
    running expensive queries.

    **What This Returns:**
    - Stage-by-stage execution plan (AFTER automatic optimizations)
    - Estimated costs (credits + time per stage)
    - Document flow projections (input/output counts per stage)
    - Efficiency metrics (selectivity ratios, cache likelihood)
    - Bottleneck identification (slowest/most expensive stages)
    - Optimization details (transformations applied by the optimizer)
    - Performance warnings and improvement suggestions


    **Key Features:**
    - **Cost Estimation**: See how many credits and milliseconds each stage will consume
    - **Bottleneck Detection**: Identify which stages dominate execution time
    - **Optimization Transparency**: Understand how your pipeline was optimized
    - **Cache Analysis**: See which stages are likely to hit cache
    - **Accuracy Troubleshooting**: Analyze stage efficiency and document flow
    - **Latency Analysis**: Break down estimated duration by stage


    **Important:** The execution_plan shows OPTIMIZED stages (after automatic transformations like
    filter push-down, stage fusion, and grouping optimization). Check optimization_details to understand
    what changed from your original configuration.


    **Use Cases:**
    - Debug slow retrievers by identifying bottleneck stages
    - Estimate costs before running expensive queries
    - Understand how the optimizer transformed your pipeline
    - Troubleshoot accuracy issues by analyzing stage selectivity
    - Compare different retriever configurations
    - Plan budget allocation for production workloads


    **Example Response:**
    ```json
    {
      \"retriever_id\": \"ret_abc123\",
      \"retriever_name\": \"product_search\",
      \"execution_plan\": [
        {
          \"stage_index\": 0,
          \"stage_name\": \"attribute_filter\",
          \"stage_type\": \"filter\",
          \"estimated_input\": 10000,
          \"estimated_output\": 5000,
          \"estimated_efficiency\": 0.5,
          \"estimated_cost_credits\": 0.01,
          \"estimated_duration_ms\": 20,
          \"cache_likely\": true,
          \"optimization_notes\": [\"Pushed down from stage 2\"],
          \"warnings\": []
        },
        {
          \"stage_index\": 1,
          \"stage_name\": \"semantic_search\",
          \"stage_type\": \"filter\",
          \"estimated_input\": 5000,
          \"estimated_output\": 100,
          \"estimated_efficiency\": 0.02,
          \"estimated_cost_credits\": 0.5,
          \"estimated_duration_ms\": 200,
          \"cache_likely\": false,
          \"optimization_notes\": [],
          \"warnings\": [\"High cost stage - consider reducing limit\"]
        }
      ],
      \"estimated_cost\": {
        \"total_credits\": 0.51,
        \"total_duration_ms\": 220
      },
      \"bottleneck_stages\": [\"semantic_search\"],
      \"optimization_applied\": true,
      \"optimization_details\": {
        \"original_stage_count\": 3,
        \"optimized_stage_count\": 2,
        \"optimization_time_ms\": 8.2,
        \"stage_reduction_pct\": 33.3,
        \"decisions\": [
          {
            \"rule_type\": \"push_down_filters\",
            \"applied\": true,
            \"reason\": \"Moved attribute_filter before semantic_search to reduce search scope\"
          }
        ]
      },
      \"optimization_suggestions\": [
        {
          \"type\": \"reduce_limit\",
          \"stage\": \"semantic_search\",
          \"message\": \"Consider reducing limit to improve latency\"
        }
      ]
    }
    ```

    Args:
        retriever_id (str): Retriever ID or name to explain. The execution plan will show the
            OPTIMIZED version after automatic transformations.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ExplainRetrieverRequest): Request to get execution plan for a retriever.

            Provides optional hypothetical inputs to tailor the execution plan estimation.
            The explain endpoint analyzes your retriever configuration and returns cost/latency
            estimates without actually executing the query.

            Use Cases:
                - See how plan changes with different input values
                - Estimate costs for different query patterns
                - Understand impact of parameter changes (e.g., top_k)
                - Test stage behavior with representative inputs

            Behavior:
                - If inputs are provided, they're used for tailored estimation
                - If inputs are not provided, default/representative values are used
                - Inputs do NOT need to match your input_schema exactly
                - No actual retrieval is performed (explain is analysis only)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ExplainRetrieverResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        retriever_id=retriever_id,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    retriever_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExplainRetrieverRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | ExplainRetrieverResponse | HTTPValidationError | None:
    r"""Explain Retriever Execution Plan

     Get a detailed execution plan for a retriever without actually executing it. Similar to MongoDB's
    explain plan or SQL's EXPLAIN command, this endpoint helps you understand performance
    characteristics, identify bottlenecks, estimate costs, and troubleshoot retrieval issues before
    running expensive queries.

    **What This Returns:**
    - Stage-by-stage execution plan (AFTER automatic optimizations)
    - Estimated costs (credits + time per stage)
    - Document flow projections (input/output counts per stage)
    - Efficiency metrics (selectivity ratios, cache likelihood)
    - Bottleneck identification (slowest/most expensive stages)
    - Optimization details (transformations applied by the optimizer)
    - Performance warnings and improvement suggestions


    **Key Features:**
    - **Cost Estimation**: See how many credits and milliseconds each stage will consume
    - **Bottleneck Detection**: Identify which stages dominate execution time
    - **Optimization Transparency**: Understand how your pipeline was optimized
    - **Cache Analysis**: See which stages are likely to hit cache
    - **Accuracy Troubleshooting**: Analyze stage efficiency and document flow
    - **Latency Analysis**: Break down estimated duration by stage


    **Important:** The execution_plan shows OPTIMIZED stages (after automatic transformations like
    filter push-down, stage fusion, and grouping optimization). Check optimization_details to understand
    what changed from your original configuration.


    **Use Cases:**
    - Debug slow retrievers by identifying bottleneck stages
    - Estimate costs before running expensive queries
    - Understand how the optimizer transformed your pipeline
    - Troubleshoot accuracy issues by analyzing stage selectivity
    - Compare different retriever configurations
    - Plan budget allocation for production workloads


    **Example Response:**
    ```json
    {
      \"retriever_id\": \"ret_abc123\",
      \"retriever_name\": \"product_search\",
      \"execution_plan\": [
        {
          \"stage_index\": 0,
          \"stage_name\": \"attribute_filter\",
          \"stage_type\": \"filter\",
          \"estimated_input\": 10000,
          \"estimated_output\": 5000,
          \"estimated_efficiency\": 0.5,
          \"estimated_cost_credits\": 0.01,
          \"estimated_duration_ms\": 20,
          \"cache_likely\": true,
          \"optimization_notes\": [\"Pushed down from stage 2\"],
          \"warnings\": []
        },
        {
          \"stage_index\": 1,
          \"stage_name\": \"semantic_search\",
          \"stage_type\": \"filter\",
          \"estimated_input\": 5000,
          \"estimated_output\": 100,
          \"estimated_efficiency\": 0.02,
          \"estimated_cost_credits\": 0.5,
          \"estimated_duration_ms\": 200,
          \"cache_likely\": false,
          \"optimization_notes\": [],
          \"warnings\": [\"High cost stage - consider reducing limit\"]
        }
      ],
      \"estimated_cost\": {
        \"total_credits\": 0.51,
        \"total_duration_ms\": 220
      },
      \"bottleneck_stages\": [\"semantic_search\"],
      \"optimization_applied\": true,
      \"optimization_details\": {
        \"original_stage_count\": 3,
        \"optimized_stage_count\": 2,
        \"optimization_time_ms\": 8.2,
        \"stage_reduction_pct\": 33.3,
        \"decisions\": [
          {
            \"rule_type\": \"push_down_filters\",
            \"applied\": true,
            \"reason\": \"Moved attribute_filter before semantic_search to reduce search scope\"
          }
        ]
      },
      \"optimization_suggestions\": [
        {
          \"type\": \"reduce_limit\",
          \"stage\": \"semantic_search\",
          \"message\": \"Consider reducing limit to improve latency\"
        }
      ]
    }
    ```

    Args:
        retriever_id (str): Retriever ID or name to explain. The execution plan will show the
            OPTIMIZED version after automatic transformations.
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (ExplainRetrieverRequest): Request to get execution plan for a retriever.

            Provides optional hypothetical inputs to tailor the execution plan estimation.
            The explain endpoint analyzes your retriever configuration and returns cost/latency
            estimates without actually executing the query.

            Use Cases:
                - See how plan changes with different input values
                - Estimate costs for different query patterns
                - Understand impact of parameter changes (e.g., top_k)
                - Test stage behavior with representative inputs

            Behavior:
                - If inputs are provided, they're used for tailored estimation
                - If inputs are not provided, default/representative values are used
                - Inputs do NOT need to match your input_schema exactly
                - No actual retrieval is performed (explain is analysis only)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ExplainRetrieverResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            retriever_id=retriever_id,
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
