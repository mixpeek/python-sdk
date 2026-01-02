from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AssignmentMetric")


@_attrs_define
class AssignmentMetric:
    """Taxonomy assignment metrics.

    Attributes:
        time_bucket (datetime.datetime):
        assignment_count (int):
        avg_confidence (float):
        unique_labels (int):
    """

    time_bucket: datetime.datetime
    assignment_count: int
    avg_confidence: float
    unique_labels: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_bucket = self.time_bucket.isoformat()

        assignment_count = self.assignment_count

        avg_confidence = self.avg_confidence

        unique_labels = self.unique_labels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time_bucket": time_bucket,
                "assignment_count": assignment_count,
                "avg_confidence": avg_confidence,
                "unique_labels": unique_labels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time_bucket = isoparse(d.pop("time_bucket"))

        assignment_count = d.pop("assignment_count")

        avg_confidence = d.pop("avg_confidence")

        unique_labels = d.pop("unique_labels")

        assignment_metric = cls(
            time_bucket=time_bucket,
            assignment_count=assignment_count,
            avg_confidence=avg_confidence,
            unique_labels=unique_labels,
        )

        assignment_metric.additional_properties = d
        return assignment_metric

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
