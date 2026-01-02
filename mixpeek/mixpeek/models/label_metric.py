from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LabelMetric")


@_attrs_define
class LabelMetric:
    """Label distribution metrics.

    Attributes:
        label (str):
        count (int):
        percentage (float):
        avg_confidence (float):
    """

    label: str
    count: int
    percentage: float
    avg_confidence: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        count = self.count

        percentage = self.percentage

        avg_confidence = self.avg_confidence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "count": count,
                "percentage": percentage,
                "avg_confidence": avg_confidence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        count = d.pop("count")

        percentage = d.pop("percentage")

        avg_confidence = d.pop("avg_confidence")

        label_metric = cls(
            label=label,
            count=count,
            percentage=percentage,
            avg_confidence=avg_confidence,
        )

        label_metric.additional_properties = d
        return label_metric

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
