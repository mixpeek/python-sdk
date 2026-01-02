from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_status import TriggerStatus
from ..models.trigger_type import TriggerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_trigger_request_schedule_config import CreateTriggerRequestScheduleConfig
    from ..models.trigger_execution_config import TriggerExecutionConfig


T = TypeVar("T", bound="CreateTriggerRequest")


@_attrs_define
class CreateTriggerRequest:
    """Request to create a new cluster trigger.

    Creates an automated trigger that executes clustering based on schedules, events, or conditions.

    Requirements:
        - trigger_type: REQUIRED - Determines which schedule_config fields are needed
        - schedule_config: REQUIRED - Configuration specific to trigger_type
        - execution_config OR cluster_id: REQUIRED - Either provide config directly or reference existing cluster

    Trigger Types and schedule_config:
        - **cron**: Requires {"cron_expression": str, "timezone": str}
        - **interval**: Requires {"interval_seconds": int, "start_immediately": bool}
        - **event**: Requires {"event_type": str, "event_threshold": int, "collection_id": str, "cooldown_seconds": int}
        - **conditional**: Requires {"condition_type": str, "threshold": float, "metric": str, "check_interval_seconds":
    int}

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

        Attributes:
            trigger_type (TriggerType): Type of trigger for automated cluster execution.

                Supported trigger types:
                - **cron**: Schedule-based execution using cron expressions (e.g., daily at 2am)
                - **interval**: Fixed-interval execution (e.g., every 6 hours)
                - **event**: Event-driven execution (e.g., after 100 documents added)
                - **conditional**: Condition-based execution (e.g., when drift exceeds threshold)
            schedule_config (CreateTriggerRequestScheduleConfig): REQUIRED. Type-specific schedule configuration. Contents
                depend on trigger_type. See trigger type examples above for required fields.
            cluster_id (None | str | Unset): OPTIONAL. Reference to existing cluster definition. If provided,
                execution_config is inherited from the cluster. Either cluster_id OR execution_config must be provided.
            execution_config (None | TriggerExecutionConfig | Unset): OPTIONAL. Clustering configuration for this trigger.
                Specifies collections and algorithm to use when trigger fires. Required if cluster_id is not provided.
            description (None | str | Unset): OPTIONAL. Human-readable description of what this trigger does. Helpful for
                identifying triggers in dashboards.
            status (TriggerStatus | Unset): Status of a cluster trigger.
    """

    trigger_type: TriggerType
    schedule_config: CreateTriggerRequestScheduleConfig
    cluster_id: None | str | Unset = UNSET
    execution_config: None | TriggerExecutionConfig | Unset = UNSET
    description: None | str | Unset = UNSET
    status: TriggerStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trigger_execution_config import TriggerExecutionConfig

        trigger_type = self.trigger_type.value

        schedule_config = self.schedule_config.to_dict()

        cluster_id: None | str | Unset
        if isinstance(self.cluster_id, Unset):
            cluster_id = UNSET
        else:
            cluster_id = self.cluster_id

        execution_config: dict[str, Any] | None | Unset
        if isinstance(self.execution_config, Unset):
            execution_config = UNSET
        elif isinstance(self.execution_config, TriggerExecutionConfig):
            execution_config = self.execution_config.to_dict()
        else:
            execution_config = self.execution_config

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trigger_type": trigger_type,
                "schedule_config": schedule_config,
            }
        )
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if execution_config is not UNSET:
            field_dict["execution_config"] = execution_config
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_trigger_request_schedule_config import CreateTriggerRequestScheduleConfig
        from ..models.trigger_execution_config import TriggerExecutionConfig

        d = dict(src_dict)
        trigger_type = TriggerType(d.pop("trigger_type"))

        schedule_config = CreateTriggerRequestScheduleConfig.from_dict(d.pop("schedule_config"))

        def _parse_cluster_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cluster_id = _parse_cluster_id(d.pop("cluster_id", UNSET))

        def _parse_execution_config(data: object) -> None | TriggerExecutionConfig | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                execution_config_type_0 = TriggerExecutionConfig.from_dict(data)

                return execution_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TriggerExecutionConfig | Unset, data)

        execution_config = _parse_execution_config(d.pop("execution_config", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _status = d.pop("status", UNSET)
        status: TriggerStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TriggerStatus(_status)

        create_trigger_request = cls(
            trigger_type=trigger_type,
            schedule_config=schedule_config,
            cluster_id=cluster_id,
            execution_config=execution_config,
            description=description,
            status=status,
        )

        create_trigger_request.additional_properties = d
        return create_trigger_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
