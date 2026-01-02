from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransitionPath")


@_attrs_define
class TransitionPath:
    """Represents a multi-step path between two steps.

    Tracks the intermediate steps documents take when transitioning from
    from_step to to_step.

    Attributes:
        path: Ordered sequence of steps (e.g., ["inquiry", "followup", "proposal", "closed_won"])
        count: Number of sequences that followed this exact path
        percentage: Percentage of all completing sequences that used this path
        avg_duration_sec: Average time to complete this path

    Example:
        ```python
        # 30% of successful conversions took this 4-step path
        TransitionPath(
            path=["inquiry", "followup", "proposal", "closed_won"],
            count=120,
            percentage=34.3,
            avg_duration_sec=604800.0  # 7 days average
        )
        ```

        Attributes:
            path (list[str]): Ordered sequence of steps
            count (int): Number of sequences following this path
            percentage (float): Percentage of total completing sequences
            avg_duration_sec (float | None | Unset): Average time to complete this path (seconds)
    """

    path: list[str]
    count: int
    percentage: float
    avg_duration_sec: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        count = self.count

        percentage = self.percentage

        avg_duration_sec: float | None | Unset
        if isinstance(self.avg_duration_sec, Unset):
            avg_duration_sec = UNSET
        else:
            avg_duration_sec = self.avg_duration_sec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "count": count,
                "percentage": percentage,
            }
        )
        if avg_duration_sec is not UNSET:
            field_dict["avg_duration_sec"] = avg_duration_sec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = cast(list[str], d.pop("path"))

        count = d.pop("count")

        percentage = d.pop("percentage")

        def _parse_avg_duration_sec(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_duration_sec = _parse_avg_duration_sec(d.pop("avg_duration_sec", UNSET))

        transition_path = cls(
            path=path,
            count=count,
            percentage=percentage,
            avg_duration_sec=avg_duration_sec,
        )

        transition_path.additional_properties = d
        return transition_path

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
