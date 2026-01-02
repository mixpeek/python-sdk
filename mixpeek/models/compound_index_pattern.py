from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompoundIndexPattern")


@_attrs_define
class CompoundIndexPattern:
    """Pattern of fields commonly queried together.

    Attributes:
        field_combination (list[str]): Fields used together
        combination_count (int): Number of times this combination was used
        avg_latency_ms (float): Average latency for this combination
        p95_latency_ms (float): 95th percentile latency
    """

    field_combination: list[str]
    combination_count: int
    avg_latency_ms: float
    p95_latency_ms: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_combination = self.field_combination

        combination_count = self.combination_count

        avg_latency_ms = self.avg_latency_ms

        p95_latency_ms = self.p95_latency_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_combination": field_combination,
                "combination_count": combination_count,
                "avg_latency_ms": avg_latency_ms,
                "p95_latency_ms": p95_latency_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_combination = cast(list[str], d.pop("field_combination"))

        combination_count = d.pop("combination_count")

        avg_latency_ms = d.pop("avg_latency_ms")

        p95_latency_ms = d.pop("p95_latency_ms")

        compound_index_pattern = cls(
            field_combination=field_combination,
            combination_count=combination_count,
            avg_latency_ms=avg_latency_ms,
            p95_latency_ms=p95_latency_ms,
        )

        compound_index_pattern.additional_properties = d
        return compound_index_pattern

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
