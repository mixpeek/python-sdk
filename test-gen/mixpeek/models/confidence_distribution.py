from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConfidenceDistribution")


@_attrs_define
class ConfidenceDistribution:
    """Confidence score distribution bucket.

    Attributes:
        confidence_range (str): Confidence range (e.g., '0.8-0.9')
        count (int):
        percentage (float):
    """

    confidence_range: str
    count: int
    percentage: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confidence_range = self.confidence_range

        count = self.count

        percentage = self.percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confidence_range": confidence_range,
                "count": count,
                "percentage": percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confidence_range = d.pop("confidence_range")

        count = d.pop("count")

        percentage = d.pop("percentage")

        confidence_distribution = cls(
            confidence_range=confidence_range,
            count=count,
            percentage=percentage,
        )

        confidence_distribution.additional_properties = d
        return confidence_distribution

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
