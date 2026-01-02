from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.trigger_status import TriggerStatus
from ..models.trigger_type import TriggerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigger_execution_config import TriggerExecutionConfig
    from ..models.trigger_model_schedule_config import TriggerModelScheduleConfig


T = TypeVar("T", bound="TriggerModel")


@_attrs_define
class TriggerModel:
    """Model for cluster trigger.

    Attributes:
        namespace_id (str): Namespace ID
        internal_id (str): Organization internal ID
        execution_config (TriggerExecutionConfig): Configuration for cluster execution when trigger fires.

            Defines what clustering algorithm and parameters to use when the trigger executes.

            Examples:
                K-means clustering on 3 collections:
                    {
                        "collection_ids": ["col_abc123", "col_def456", "col_ghi789"],
                        "config": {
                            "algorithm": "kmeans",
                            "n_clusters": 5,
                            "min_cluster_size": 2
                        }
                    }

                HDBSCAN clustering on single collection:
                    {
                        "collection_ids": ["col_products"],
                        "config": {
                            "algorithm": "hdbscan",
                            "min_cluster_size": 10,
                            "min_samples": 5
                        }
                    }
        trigger_type (TriggerType): Type of trigger for automated cluster execution.

            Supported trigger types:
            - **cron**: Schedule-based execution using cron expressions (e.g., daily at 2am)
            - **interval**: Fixed-interval execution (e.g., every 6 hours)
            - **event**: Event-driven execution (e.g., after 100 documents added)
            - **conditional**: Condition-based execution (e.g., when drift exceeds threshold)
        schedule_config (TriggerModelScheduleConfig): Type-specific schedule configuration
        trigger_id (str | Unset): Unique trigger ID
        cluster_id (None | str | Unset): Optional link to cluster definition
        status (TriggerStatus | Unset): Status of a cluster trigger.
        last_triggered_at (datetime.datetime | None | Unset): Last time trigger fired
        last_execution_job_id (None | str | Unset): Job ID of last execution
        next_scheduled_at (datetime.datetime | None | Unset): Next scheduled execution time
        execution_count (int | Unset): Total executions Default: 0.
        consecutive_failures (int | Unset): Consecutive execution failures Default: 0.
        last_execution_status (None | str | Unset): Status of last execution
        last_execution_error (None | str | Unset): Error from last execution
        event_counter (int | Unset): Current event count since last trigger Default: 0.
        last_cooldown_at (datetime.datetime | None | Unset): Last time cooldown was applied
        created_at (datetime.datetime | Unset): Creation timestamp
        updated_at (datetime.datetime | Unset): Last update timestamp
        created_by (None | str | Unset): User who created trigger
        description (None | str | Unset): Trigger description
    """

    namespace_id: str
    internal_id: str
    execution_config: TriggerExecutionConfig
    trigger_type: TriggerType
    schedule_config: TriggerModelScheduleConfig
    trigger_id: str | Unset = UNSET
    cluster_id: None | str | Unset = UNSET
    status: TriggerStatus | Unset = UNSET
    last_triggered_at: datetime.datetime | None | Unset = UNSET
    last_execution_job_id: None | str | Unset = UNSET
    next_scheduled_at: datetime.datetime | None | Unset = UNSET
    execution_count: int | Unset = 0
    consecutive_failures: int | Unset = 0
    last_execution_status: None | str | Unset = UNSET
    last_execution_error: None | str | Unset = UNSET
    event_counter: int | Unset = 0
    last_cooldown_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    created_by: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace_id = self.namespace_id

        internal_id = self.internal_id

        execution_config = self.execution_config.to_dict()

        trigger_type = self.trigger_type.value

        schedule_config = self.schedule_config.to_dict()

        trigger_id = self.trigger_id

        cluster_id: None | str | Unset
        if isinstance(self.cluster_id, Unset):
            cluster_id = UNSET
        else:
            cluster_id = self.cluster_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        last_triggered_at: None | str | Unset
        if isinstance(self.last_triggered_at, Unset):
            last_triggered_at = UNSET
        elif isinstance(self.last_triggered_at, datetime.datetime):
            last_triggered_at = self.last_triggered_at.isoformat()
        else:
            last_triggered_at = self.last_triggered_at

        last_execution_job_id: None | str | Unset
        if isinstance(self.last_execution_job_id, Unset):
            last_execution_job_id = UNSET
        else:
            last_execution_job_id = self.last_execution_job_id

        next_scheduled_at: None | str | Unset
        if isinstance(self.next_scheduled_at, Unset):
            next_scheduled_at = UNSET
        elif isinstance(self.next_scheduled_at, datetime.datetime):
            next_scheduled_at = self.next_scheduled_at.isoformat()
        else:
            next_scheduled_at = self.next_scheduled_at

        execution_count = self.execution_count

        consecutive_failures = self.consecutive_failures

        last_execution_status: None | str | Unset
        if isinstance(self.last_execution_status, Unset):
            last_execution_status = UNSET
        else:
            last_execution_status = self.last_execution_status

        last_execution_error: None | str | Unset
        if isinstance(self.last_execution_error, Unset):
            last_execution_error = UNSET
        else:
            last_execution_error = self.last_execution_error

        event_counter = self.event_counter

        last_cooldown_at: None | str | Unset
        if isinstance(self.last_cooldown_at, Unset):
            last_cooldown_at = UNSET
        elif isinstance(self.last_cooldown_at, datetime.datetime):
            last_cooldown_at = self.last_cooldown_at.isoformat()
        else:
            last_cooldown_at = self.last_cooldown_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace_id": namespace_id,
                "internal_id": internal_id,
                "execution_config": execution_config,
                "trigger_type": trigger_type,
                "schedule_config": schedule_config,
            }
        )
        if trigger_id is not UNSET:
            field_dict["trigger_id"] = trigger_id
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if status is not UNSET:
            field_dict["status"] = status
        if last_triggered_at is not UNSET:
            field_dict["last_triggered_at"] = last_triggered_at
        if last_execution_job_id is not UNSET:
            field_dict["last_execution_job_id"] = last_execution_job_id
        if next_scheduled_at is not UNSET:
            field_dict["next_scheduled_at"] = next_scheduled_at
        if execution_count is not UNSET:
            field_dict["execution_count"] = execution_count
        if consecutive_failures is not UNSET:
            field_dict["consecutive_failures"] = consecutive_failures
        if last_execution_status is not UNSET:
            field_dict["last_execution_status"] = last_execution_status
        if last_execution_error is not UNSET:
            field_dict["last_execution_error"] = last_execution_error
        if event_counter is not UNSET:
            field_dict["event_counter"] = event_counter
        if last_cooldown_at is not UNSET:
            field_dict["last_cooldown_at"] = last_cooldown_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_execution_config import TriggerExecutionConfig
        from ..models.trigger_model_schedule_config import TriggerModelScheduleConfig

        d = dict(src_dict)
        namespace_id = d.pop("namespace_id")

        internal_id = d.pop("internal_id")

        execution_config = TriggerExecutionConfig.from_dict(d.pop("execution_config"))

        trigger_type = TriggerType(d.pop("trigger_type"))

        schedule_config = TriggerModelScheduleConfig.from_dict(d.pop("schedule_config"))

        trigger_id = d.pop("trigger_id", UNSET)

        def _parse_cluster_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cluster_id = _parse_cluster_id(d.pop("cluster_id", UNSET))

        _status = d.pop("status", UNSET)
        status: TriggerStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TriggerStatus(_status)

        def _parse_last_triggered_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_triggered_at_type_0 = isoparse(data)

                return last_triggered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_triggered_at = _parse_last_triggered_at(d.pop("last_triggered_at", UNSET))

        def _parse_last_execution_job_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_execution_job_id = _parse_last_execution_job_id(d.pop("last_execution_job_id", UNSET))

        def _parse_next_scheduled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_scheduled_at_type_0 = isoparse(data)

                return next_scheduled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_scheduled_at = _parse_next_scheduled_at(d.pop("next_scheduled_at", UNSET))

        execution_count = d.pop("execution_count", UNSET)

        consecutive_failures = d.pop("consecutive_failures", UNSET)

        def _parse_last_execution_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_execution_status = _parse_last_execution_status(d.pop("last_execution_status", UNSET))

        def _parse_last_execution_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_execution_error = _parse_last_execution_error(d.pop("last_execution_error", UNSET))

        event_counter = d.pop("event_counter", UNSET)

        def _parse_last_cooldown_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_cooldown_at_type_0 = isoparse(data)

                return last_cooldown_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_cooldown_at = _parse_last_cooldown_at(d.pop("last_cooldown_at", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        trigger_model = cls(
            namespace_id=namespace_id,
            internal_id=internal_id,
            execution_config=execution_config,
            trigger_type=trigger_type,
            schedule_config=schedule_config,
            trigger_id=trigger_id,
            cluster_id=cluster_id,
            status=status,
            last_triggered_at=last_triggered_at,
            last_execution_job_id=last_execution_job_id,
            next_scheduled_at=next_scheduled_at,
            execution_count=execution_count,
            consecutive_failures=consecutive_failures,
            last_execution_status=last_execution_status,
            last_execution_error=last_execution_error,
            event_counter=event_counter,
            last_cooldown_at=last_cooldown_at,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            description=description,
        )

        trigger_model.additional_properties = d
        return trigger_model

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
