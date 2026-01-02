from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.error_breakdown import ErrorBreakdown
    from ..models.sync_health_metric import SyncHealthMetric
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="BucketHealthResponse")


@_attrs_define
class BucketHealthResponse:
    """Bucket health monitoring response.

    Attributes:
        bucket_id (str): Bucket identifier
        time_range (TimeRange): Time range for analytics queries.
        overall_health (str): Overall health status
        total_errors (int): Total error count
        error_breakdown (list[ErrorBreakdown]): Errors by type
        sync_health (list[SyncHealthMetric]): Sync health per config
        stuck_syncs (list[str]): Sync configs with no recent activity
    """

    bucket_id: str
    time_range: TimeRange
    overall_health: str
    total_errors: int
    error_breakdown: list[ErrorBreakdown]
    sync_health: list[SyncHealthMetric]
    stuck_syncs: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_id = self.bucket_id

        time_range = self.time_range.to_dict()

        overall_health = self.overall_health

        total_errors = self.total_errors

        error_breakdown = []
        for error_breakdown_item_data in self.error_breakdown:
            error_breakdown_item = error_breakdown_item_data.to_dict()
            error_breakdown.append(error_breakdown_item)

        sync_health = []
        for sync_health_item_data in self.sync_health:
            sync_health_item = sync_health_item_data.to_dict()
            sync_health.append(sync_health_item)

        stuck_syncs = self.stuck_syncs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket_id": bucket_id,
                "time_range": time_range,
                "overall_health": overall_health,
                "total_errors": total_errors,
                "error_breakdown": error_breakdown,
                "sync_health": sync_health,
                "stuck_syncs": stuck_syncs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_breakdown import ErrorBreakdown
        from ..models.sync_health_metric import SyncHealthMetric
        from ..models.time_range import TimeRange

        d = dict(src_dict)
        bucket_id = d.pop("bucket_id")

        time_range = TimeRange.from_dict(d.pop("time_range"))

        overall_health = d.pop("overall_health")

        total_errors = d.pop("total_errors")

        error_breakdown = []
        _error_breakdown = d.pop("error_breakdown")
        for error_breakdown_item_data in _error_breakdown:
            error_breakdown_item = ErrorBreakdown.from_dict(error_breakdown_item_data)

            error_breakdown.append(error_breakdown_item)

        sync_health = []
        _sync_health = d.pop("sync_health")
        for sync_health_item_data in _sync_health:
            sync_health_item = SyncHealthMetric.from_dict(sync_health_item_data)

            sync_health.append(sync_health_item)

        stuck_syncs = cast(list[str], d.pop("stuck_syncs"))

        bucket_health_response = cls(
            bucket_id=bucket_id,
            time_range=time_range,
            overall_health=overall_health,
            total_errors=total_errors,
            error_breakdown=error_breakdown,
            sync_health=sync_health,
            stuck_syncs=stuck_syncs,
        )

        bucket_health_response.additional_properties = d
        return bucket_health_response

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
