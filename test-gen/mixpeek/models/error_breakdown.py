from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ErrorBreakdown")


@_attrs_define
class ErrorBreakdown:
    """Error breakdown by type.

    Attributes:
        error_type (str): Error type
        count (int): Error count
        percentage (float): Percentage of total errors
        first_seen (datetime.datetime): First occurrence
        last_seen (datetime.datetime): Last occurrence
    """

    error_type: str
    count: int
    percentage: float
    first_seen: datetime.datetime
    last_seen: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_type = self.error_type

        count = self.count

        percentage = self.percentage

        first_seen = self.first_seen.isoformat()

        last_seen = self.last_seen.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error_type": error_type,
                "count": count,
                "percentage": percentage,
                "first_seen": first_seen,
                "last_seen": last_seen,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_type = d.pop("error_type")

        count = d.pop("count")

        percentage = d.pop("percentage")

        first_seen = isoparse(d.pop("first_seen"))

        last_seen = isoparse(d.pop("last_seen"))

        error_breakdown = cls(
            error_type=error_type,
            count=count,
            percentage=percentage,
            first_seen=first_seen,
            last_seen=last_seen,
        )

        error_breakdown.additional_properties = d
        return error_breakdown

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
