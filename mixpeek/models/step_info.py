from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StepInfo")


@_attrs_define
class StepInfo:
    """Information about a single step in the taxonomy analytics data.

    Attributes:
        step_key: The step identifier (e.g., "inquiry", "closed_won")
        event_count: Number of events with this step
        sequence_count: Number of unique sequences with this step
        first_seen: ISO timestamp of earliest event with this step
        last_seen: ISO timestamp of most recent event with this step

        Attributes:
            step_key (str): Step identifier
            event_count (int): Total events for this step
            sequence_count (int): Unique sequences with this step
            first_seen (str): Earliest event timestamp (ISO format)
            last_seen (str): Most recent event timestamp (ISO format)
    """

    step_key: str
    event_count: int
    sequence_count: int
    first_seen: str
    last_seen: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step_key = self.step_key

        event_count = self.event_count

        sequence_count = self.sequence_count

        first_seen = self.first_seen

        last_seen = self.last_seen

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "step_key": step_key,
                "event_count": event_count,
                "sequence_count": sequence_count,
                "first_seen": first_seen,
                "last_seen": last_seen,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        step_key = d.pop("step_key")

        event_count = d.pop("event_count")

        sequence_count = d.pop("sequence_count")

        first_seen = d.pop("first_seen")

        last_seen = d.pop("last_seen")

        step_info = cls(
            step_key=step_key,
            event_count=event_count,
            sequence_count=sequence_count,
            first_seen=first_seen,
            last_seen=last_seen,
        )

        step_info.additional_properties = d
        return step_info

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
