from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bucket_storage_response_summary import BucketStorageResponseSummary
    from ..models.storage_metric import StorageMetric
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="BucketStorageResponse")


@_attrs_define
class BucketStorageResponse:
    """Storage growth trends response.

    Attributes:
        bucket_id (str): Bucket identifier
        time_range (TimeRange): Time range for analytics queries.
        metrics (list[StorageMetric]): Time-series storage metrics
        summary (BucketStorageResponseSummary | Unset): Summary statistics
    """

    bucket_id: str
    time_range: TimeRange
    metrics: list[StorageMetric]
    summary: BucketStorageResponseSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_id = self.bucket_id

        time_range = self.time_range.to_dict()

        metrics = []
        for metrics_item_data in self.metrics:
            metrics_item = metrics_item_data.to_dict()
            metrics.append(metrics_item)

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket_id": bucket_id,
                "time_range": time_range,
                "metrics": metrics,
            }
        )
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bucket_storage_response_summary import BucketStorageResponseSummary
        from ..models.storage_metric import StorageMetric
        from ..models.time_range import TimeRange

        d = dict(src_dict)
        bucket_id = d.pop("bucket_id")

        time_range = TimeRange.from_dict(d.pop("time_range"))

        metrics = []
        _metrics = d.pop("metrics")
        for metrics_item_data in _metrics:
            metrics_item = StorageMetric.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        _summary = d.pop("summary", UNSET)
        summary: BucketStorageResponseSummary | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = BucketStorageResponseSummary.from_dict(_summary)

        bucket_storage_response = cls(
            bucket_id=bucket_id,
            time_range=time_range,
            metrics=metrics,
            summary=summary,
        )

        bucket_storage_response.additional_properties = d
        return bucket_storage_response

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
