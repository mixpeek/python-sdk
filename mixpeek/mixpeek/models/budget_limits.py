from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetLimits")


@_attrs_define
class BudgetLimits:
    """User-defined limits for time and credits during execution.

    Attributes:
        max_credits (float | None | Unset): Maximum credits allowed for a single execution (OPTIONAL).
        max_time_ms (int | None | Unset): Maximum wall-clock time in milliseconds before forcing halt (OPTIONAL).
    """

    max_credits: float | None | Unset = UNSET
    max_time_ms: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_credits: float | None | Unset
        if isinstance(self.max_credits, Unset):
            max_credits = UNSET
        else:
            max_credits = self.max_credits

        max_time_ms: int | None | Unset
        if isinstance(self.max_time_ms, Unset):
            max_time_ms = UNSET
        else:
            max_time_ms = self.max_time_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_credits is not UNSET:
            field_dict["max_credits"] = max_credits
        if max_time_ms is not UNSET:
            field_dict["max_time_ms"] = max_time_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_max_credits(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_credits = _parse_max_credits(d.pop("max_credits", UNSET))

        def _parse_max_time_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_time_ms = _parse_max_time_ms(d.pop("max_time_ms", UNSET))

        budget_limits = cls(
            max_credits=max_credits,
            max_time_ms=max_time_ms,
        )

        budget_limits.additional_properties = d
        return budget_limits

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
