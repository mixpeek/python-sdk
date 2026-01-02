from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_performance_response_summary import SyncPerformanceResponseSummary
    from ..models.sync_run_metric import SyncRunMetric
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="SyncPerformanceResponse")


@_attrs_define
class SyncPerformanceResponse:
    """Sync performance analytics response.

    Attributes:
        bucket_id (str): Bucket identifier
        time_range (TimeRange): Time range for analytics queries.
        runs (list[SyncRunMetric]): Sync run metrics
        sync_config_id (None | str | Unset): Optional sync config filter
        summary (SyncPerformanceResponseSummary | Unset): Summary statistics
    """

    bucket_id: str
    time_range: TimeRange
    runs: list[SyncRunMetric]
    sync_config_id: None | str | Unset = UNSET
    summary: SyncPerformanceResponseSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_id = self.bucket_id

        time_range = self.time_range.to_dict()

        runs = []
        for runs_item_data in self.runs:
            runs_item = runs_item_data.to_dict()
            runs.append(runs_item)

        sync_config_id: None | str | Unset
        if isinstance(self.sync_config_id, Unset):
            sync_config_id = UNSET
        else:
            sync_config_id = self.sync_config_id

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket_id": bucket_id,
                "time_range": time_range,
                "runs": runs,
            }
        )
        if sync_config_id is not UNSET:
            field_dict["sync_config_id"] = sync_config_id
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_performance_response_summary import SyncPerformanceResponseSummary
        from ..models.sync_run_metric import SyncRunMetric
        from ..models.time_range import TimeRange

        d = dict(src_dict)
        bucket_id = d.pop("bucket_id")

        time_range = TimeRange.from_dict(d.pop("time_range"))

        runs = []
        _runs = d.pop("runs")
        for runs_item_data in _runs:
            runs_item = SyncRunMetric.from_dict(runs_item_data)

            runs.append(runs_item)

        def _parse_sync_config_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sync_config_id = _parse_sync_config_id(d.pop("sync_config_id", UNSET))

        _summary = d.pop("summary", UNSET)
        summary: SyncPerformanceResponseSummary | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = SyncPerformanceResponseSummary.from_dict(_summary)

        sync_performance_response = cls(
            bucket_id=bucket_id,
            time_range=time_range,
            runs=runs,
            sync_config_id=sync_config_id,
            summary=summary,
        )

        sync_performance_response.additional_properties = d
        return sync_performance_response

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
