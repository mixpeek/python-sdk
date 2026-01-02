from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_trigger_request import CreateTriggerRequest
from ...models.error_response import ErrorResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.trigger_model import TriggerModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateTriggerRequest,
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
        "url": "/v1/clusters/triggers",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | TriggerModel | None:
    if response.status_code == 201:
        response_201 = TriggerModel.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | TriggerModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTriggerRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | TriggerModel]:
    """Create Cluster Trigger

     Create a new trigger for automated cluster execution.

        Supports multiple trigger types:
        - **cron**: Execute at specific times using cron expressions
        - **interval**: Execute at fixed intervals
        - **event**: Execute when specific events occur (e.g., documents added)
        - **conditional**: Execute when conditions are met (e.g., drift threshold)

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateTriggerRequest): Request to create a new cluster trigger.

            Creates an automated trigger that executes clustering based on schedules, events, or
            conditions.

            Requirements:
                - trigger_type: REQUIRED - Determines which schedule_config fields are needed
                - schedule_config: REQUIRED - Configuration specific to trigger_type
                - execution_config OR cluster_id: REQUIRED - Either provide config directly or
            reference existing cluster

            Trigger Types and schedule_config:
                - **cron**: Requires {"cron_expression": str, "timezone": str}
                - **interval**: Requires {"interval_seconds": int, "start_immediately": bool}
                - **event**: Requires {"event_type": str, "event_threshold": int, "collection_id":
            str, "cooldown_seconds": int}
                - **conditional**: Requires {"condition_type": str, "threshold": float, "metric": str,
            "check_interval_seconds": int}

            Use Cases:
                - Scheduled maintenance: Use cron or interval triggers
                - Reactive clustering: Use event triggers to cluster when data changes
                - Intelligent clustering: Use conditional triggers based on metrics

            Examples:
                Cron trigger (daily at 2am UTC):
                    {
                        "trigger_type": "cron",
                        "schedule_config": {
                            "cron_expression": "0 2 * * *",
                            "timezone": "UTC"
                        },
                        "execution_config": {
                            "collection_ids": ["col_abc123"],
                            "config": {
                                "algorithm": "kmeans",
                                "n_clusters": 5
                            }
                        },
                        "description": "Daily clustering at 2am"
                    }

                Interval trigger (every 6 hours):
                    {
                        "trigger_type": "interval",
                        "schedule_config": {
                            "interval_seconds": 21600,
                            "start_immediately": false
                        },
                        "execution_config": {
                            "collection_ids": ["col_products"],
                            "config": {
                                "algorithm": "hdbscan",
                                "min_cluster_size": 10
                            }
                        },
                        "description": "Cluster every 6 hours"
                    }

                Event trigger (after 100 documents added):
                    {
                        "trigger_type": "event",
                        "schedule_config": {
                            "event_type": "documents_added",
                            "event_threshold": 100,
                            "collection_id": "col_abc123",
                            "cooldown_seconds": 300
                        },
                        "execution_config": {
                            "collection_ids": ["col_abc123"],
                            "config": {
                                "algorithm": "kmeans",
                                "n_clusters": 3
                            }
                        },
                        "description": "Cluster after 100 new documents"
                    }

                Conditional trigger (when drift exceeds 30%):
                    {
                        "trigger_type": "conditional",
                        "schedule_config": {
                            "condition_type": "drift",
                            "threshold": 0.3,
                            "metric": "cosine_drift",
                            "check_interval_seconds": 3600
                        },
                        "execution_config": {
                            "collection_ids": ["col_abc123"],
                            "config": {
                                "algorithm": "hdbscan",
                                "min_cluster_size": 5
                            }
                        },
                        "description": "Re-cluster when drift > 30%"
                    }

                Using existing cluster definition:
                    {
                        "trigger_type": "interval",
                        "schedule_config": {
                            "interval_seconds": 3600,
                            "start_immediately": true
                        },
                        "cluster_id": "cluster_xyz789",
                        "description": "Hourly clustering using cluster_xyz789"
                    }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | TriggerModel]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTriggerRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | TriggerModel | None:
    """Create Cluster Trigger

     Create a new trigger for automated cluster execution.

        Supports multiple trigger types:
        - **cron**: Execute at specific times using cron expressions
        - **interval**: Execute at fixed intervals
        - **event**: Execute when specific events occur (e.g., documents added)
        - **conditional**: Execute when conditions are met (e.g., drift threshold)

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateTriggerRequest): Request to create a new cluster trigger.

            Creates an automated trigger that executes clustering based on schedules, events, or
            conditions.

            Requirements:
                - trigger_type: REQUIRED - Determines which schedule_config fields are needed
                - schedule_config: REQUIRED - Configuration specific to trigger_type
                - execution_config OR cluster_id: REQUIRED - Either provide config directly or
            reference existing cluster

            Trigger Types and schedule_config:
                - **cron**: Requires {"cron_expression": str, "timezone": str}
                - **interval**: Requires {"interval_seconds": int, "start_immediately": bool}
                - **event**: Requires {"event_type": str, "event_threshold": int, "collection_id":
            str, "cooldown_seconds": int}
                - **conditional**: Requires {"condition_type": str, "threshold": float, "metric": str,
            "check_interval_seconds": int}

            Use Cases:
                - Scheduled maintenance: Use cron or interval triggers
                - Reactive clustering: Use event triggers to cluster when data changes
                - Intelligent clustering: Use conditional triggers based on metrics

            Examples:
                Cron trigger (daily at 2am UTC):
                    {
                        "trigger_type": "cron",
                        "schedule_config": {
                            "cron_expression": "0 2 * * *",
                            "timezone": "UTC"
                        },
                        "execution_config": {
                            "collection_ids": ["col_abc123"],
                            "config": {
                                "algorithm": "kmeans",
                                "n_clusters": 5
                            }
                        },
                        "description": "Daily clustering at 2am"
                    }

                Interval trigger (every 6 hours):
                    {
                        "trigger_type": "interval",
                        "schedule_config": {
                            "interval_seconds": 21600,
                            "start_immediately": false
                        },
                        "execution_config": {
                            "collection_ids": ["col_products"],
                            "config": {
                                "algorithm": "hdbscan",
                                "min_cluster_size": 10
                            }
                        },
                        "description": "Cluster every 6 hours"
                    }

                Event trigger (after 100 documents added):
                    {
                        "trigger_type": "event",
                        "schedule_config": {
                            "event_type": "documents_added",
                            "event_threshold": 100,
                            "collection_id": "col_abc123",
                            "cooldown_seconds": 300
                        },
                        "execution_config": {
                            "collection_ids": ["col_abc123"],
                            "config": {
                                "algorithm": "kmeans",
                                "n_clusters": 3
                            }
                        },
                        "description": "Cluster after 100 new documents"
                    }

                Conditional trigger (when drift exceeds 30%):
                    {
                        "trigger_type": "conditional",
                        "schedule_config": {
                            "condition_type": "drift",
                            "threshold": 0.3,
                            "metric": "cosine_drift",
                            "check_interval_seconds": 3600
                        },
                        "execution_config": {
                            "collection_ids": ["col_abc123"],
                            "config": {
                                "algorithm": "hdbscan",
                                "min_cluster_size": 5
                            }
                        },
                        "description": "Re-cluster when drift > 30%"
                    }

                Using existing cluster definition:
                    {
                        "trigger_type": "interval",
                        "schedule_config": {
                            "interval_seconds": 3600,
                            "start_immediately": true
                        },
                        "cluster_id": "cluster_xyz789",
                        "description": "Hourly clustering using cluster_xyz789"
                    }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | TriggerModel
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTriggerRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> Response[ErrorResponse | HTTPValidationError | TriggerModel]:
    """Create Cluster Trigger

     Create a new trigger for automated cluster execution.

        Supports multiple trigger types:
        - **cron**: Execute at specific times using cron expressions
        - **interval**: Execute at fixed intervals
        - **event**: Execute when specific events occur (e.g., documents added)
        - **conditional**: Execute when conditions are met (e.g., drift threshold)

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateTriggerRequest): Request to create a new cluster trigger.

            Creates an automated trigger that executes clustering based on schedules, events, or
            conditions.

            Requirements:
                - trigger_type: REQUIRED - Determines which schedule_config fields are needed
                - schedule_config: REQUIRED - Configuration specific to trigger_type
                - execution_config OR cluster_id: REQUIRED - Either provide config directly or
            reference existing cluster

            Trigger Types and schedule_config:
                - **cron**: Requires {"cron_expression": str, "timezone": str}
                - **interval**: Requires {"interval_seconds": int, "start_immediately": bool}
                - **event**: Requires {"event_type": str, "event_threshold": int, "collection_id":
            str, "cooldown_seconds": int}
                - **conditional**: Requires {"condition_type": str, "threshold": float, "metric": str,
            "check_interval_seconds": int}

            Use Cases:
                - Scheduled maintenance: Use cron or interval triggers
                - Reactive clustering: Use event triggers to cluster when data changes
                - Intelligent clustering: Use conditional triggers based on metrics

            Examples:
                Cron trigger (daily at 2am UTC):
                    {
                        "trigger_type": "cron",
                        "schedule_config": {
                            "cron_expression": "0 2 * * *",
                            "timezone": "UTC"
                        },
                        "execution_config": {
                            "collection_ids": ["col_abc123"],
                            "config": {
                                "algorithm": "kmeans",
                                "n_clusters": 5
                            }
                        },
                        "description": "Daily clustering at 2am"
                    }

                Interval trigger (every 6 hours):
                    {
                        "trigger_type": "interval",
                        "schedule_config": {
                            "interval_seconds": 21600,
                            "start_immediately": false
                        },
                        "execution_config": {
                            "collection_ids": ["col_products"],
                            "config": {
                                "algorithm": "hdbscan",
                                "min_cluster_size": 10
                            }
                        },
                        "description": "Cluster every 6 hours"
                    }

                Event trigger (after 100 documents added):
                    {
                        "trigger_type": "event",
                        "schedule_config": {
                            "event_type": "documents_added",
                            "event_threshold": 100,
                            "collection_id": "col_abc123",
                            "cooldown_seconds": 300
                        },
                        "execution_config": {
                            "collection_ids": ["col_abc123"],
                            "config": {
                                "algorithm": "kmeans",
                                "n_clusters": 3
                            }
                        },
                        "description": "Cluster after 100 new documents"
                    }

                Conditional trigger (when drift exceeds 30%):
                    {
                        "trigger_type": "conditional",
                        "schedule_config": {
                            "condition_type": "drift",
                            "threshold": 0.3,
                            "metric": "cosine_drift",
                            "check_interval_seconds": 3600
                        },
                        "execution_config": {
                            "collection_ids": ["col_abc123"],
                            "config": {
                                "algorithm": "hdbscan",
                                "min_cluster_size": 5
                            }
                        },
                        "description": "Re-cluster when drift > 30%"
                    }

                Using existing cluster definition:
                    {
                        "trigger_type": "interval",
                        "schedule_config": {
                            "interval_seconds": 3600,
                            "start_immediately": true
                        },
                        "cluster_id": "cluster_xyz789",
                        "description": "Hourly clustering using cluster_xyz789"
                    }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | TriggerModel]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_namespace=x_namespace,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateTriggerRequest,
    authorization: str | Unset = UNSET,
    x_namespace: str | Unset = UNSET,
) -> ErrorResponse | HTTPValidationError | TriggerModel | None:
    """Create Cluster Trigger

     Create a new trigger for automated cluster execution.

        Supports multiple trigger types:
        - **cron**: Execute at specific times using cron expressions
        - **interval**: Execute at fixed intervals
        - **event**: Execute when specific events occur (e.g., documents added)
        - **conditional**: Execute when conditions are met (e.g., drift threshold)

    Args:
        authorization (str | Unset): REQUIRED: Bearer token authentication using your API key.
            Format: 'Bearer sk_xxxxxxxxxxxxx'. You can create API keys in the Mixpeek dashboard under
            Organization Settings.
        x_namespace (str | Unset): REQUIRED: Namespace identifier for scoping this request. All
            resources (collections, buckets, taxonomies, etc.) are scoped to a namespace. You can
            provide either the namespace name or namespace ID. Format: ns_xxxxxxxxxxxxx (ID) or a
            custom name like 'my-namespace'
        body (CreateTriggerRequest): Request to create a new cluster trigger.

            Creates an automated trigger that executes clustering based on schedules, events, or
            conditions.

            Requirements:
                - trigger_type: REQUIRED - Determines which schedule_config fields are needed
                - schedule_config: REQUIRED - Configuration specific to trigger_type
                - execution_config OR cluster_id: REQUIRED - Either provide config directly or
            reference existing cluster

            Trigger Types and schedule_config:
                - **cron**: Requires {"cron_expression": str, "timezone": str}
                - **interval**: Requires {"interval_seconds": int, "start_immediately": bool}
                - **event**: Requires {"event_type": str, "event_threshold": int, "collection_id":
            str, "cooldown_seconds": int}
                - **conditional**: Requires {"condition_type": str, "threshold": float, "metric": str,
            "check_interval_seconds": int}

            Use Cases:
                - Scheduled maintenance: Use cron or interval triggers
                - Reactive clustering: Use event triggers to cluster when data changes
                - Intelligent clustering: Use conditional triggers based on metrics

            Examples:
                Cron trigger (daily at 2am UTC):
                    {
                        "trigger_type": "cron",
                        "schedule_config": {
                            "cron_expression": "0 2 * * *",
                            "timezone": "UTC"
                        },
                        "execution_config": {
                            "collection_ids": ["col_abc123"],
                            "config": {
                                "algorithm": "kmeans",
                                "n_clusters": 5
                            }
                        },
                        "description": "Daily clustering at 2am"
                    }

                Interval trigger (every 6 hours):
                    {
                        "trigger_type": "interval",
                        "schedule_config": {
                            "interval_seconds": 21600,
                            "start_immediately": false
                        },
                        "execution_config": {
                            "collection_ids": ["col_products"],
                            "config": {
                                "algorithm": "hdbscan",
                                "min_cluster_size": 10
                            }
                        },
                        "description": "Cluster every 6 hours"
                    }

                Event trigger (after 100 documents added):
                    {
                        "trigger_type": "event",
                        "schedule_config": {
                            "event_type": "documents_added",
                            "event_threshold": 100,
                            "collection_id": "col_abc123",
                            "cooldown_seconds": 300
                        },
                        "execution_config": {
                            "collection_ids": ["col_abc123"],
                            "config": {
                                "algorithm": "kmeans",
                                "n_clusters": 3
                            }
                        },
                        "description": "Cluster after 100 new documents"
                    }

                Conditional trigger (when drift exceeds 30%):
                    {
                        "trigger_type": "conditional",
                        "schedule_config": {
                            "condition_type": "drift",
                            "threshold": 0.3,
                            "metric": "cosine_drift",
                            "check_interval_seconds": 3600
                        },
                        "execution_config": {
                            "collection_ids": ["col_abc123"],
                            "config": {
                                "algorithm": "hdbscan",
                                "min_cluster_size": 5
                            }
                        },
                        "description": "Re-cluster when drift > 30%"
                    }

                Using existing cluster definition:
                    {
                        "trigger_type": "interval",
                        "schedule_config": {
                            "interval_seconds": 3600,
                            "start_immediately": true
                        },
                        "cluster_id": "cluster_xyz789",
                        "description": "Hourly clustering using cluster_xyz789"
                    }

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | TriggerModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
            x_namespace=x_namespace,
        )
    ).parsed
