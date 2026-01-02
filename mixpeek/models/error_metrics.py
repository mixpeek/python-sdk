from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ErrorMetrics")


@_attrs_define
class ErrorMetrics:
    """Error analysis metrics.

    Attributes:
        error_type (str):
        count (int):
        percentage (float):
        recent_message (str):
    """

    error_type: str
    count: int
    percentage: float
    recent_message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_type = self.error_type

        count = self.count

        percentage = self.percentage

        recent_message = self.recent_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error_type": error_type,
                "count": count,
                "percentage": percentage,
                "recent_message": recent_message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_type = d.pop("error_type")

        count = d.pop("count")

        percentage = d.pop("percentage")

        recent_message = d.pop("recent_message")

        error_metrics = cls(
            error_type=error_type,
            count=count,
            percentage=percentage,
            recent_message=recent_message,
        )

        error_metrics.additional_properties = d
        return error_metrics

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
