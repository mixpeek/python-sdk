from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.compound_index_pattern import CompoundIndexPattern


T = TypeVar("T", bound="CompoundIndexResponse")


@_attrs_define
class CompoundIndexResponse:
    """Response for compound index patterns endpoint.

    Attributes:
        namespace_id (str): Namespace ID analyzed
        time_range_days (int): Number of days analyzed
        patterns (list[CompoundIndexPattern]): Compound field patterns
        total_patterns (int): Total patterns found
    """

    namespace_id: str
    time_range_days: int
    patterns: list[CompoundIndexPattern]
    total_patterns: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace_id = self.namespace_id

        time_range_days = self.time_range_days

        patterns = []
        for patterns_item_data in self.patterns:
            patterns_item = patterns_item_data.to_dict()
            patterns.append(patterns_item)

        total_patterns = self.total_patterns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace_id": namespace_id,
                "time_range_days": time_range_days,
                "patterns": patterns,
                "total_patterns": total_patterns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compound_index_pattern import CompoundIndexPattern

        d = dict(src_dict)
        namespace_id = d.pop("namespace_id")

        time_range_days = d.pop("time_range_days")

        patterns = []
        _patterns = d.pop("patterns")
        for patterns_item_data in _patterns:
            patterns_item = CompoundIndexPattern.from_dict(patterns_item_data)

            patterns.append(patterns_item)

        total_patterns = d.pop("total_patterns")

        compound_index_response = cls(
            namespace_id=namespace_id,
            time_range_days=time_range_days,
            patterns=patterns,
            total_patterns=total_patterns,
        )

        compound_index_response.additional_properties = d
        return compound_index_response

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
