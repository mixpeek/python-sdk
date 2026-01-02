from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HavingCondition")


@_attrs_define
class HavingCondition:
    """Filtering condition for aggregated results.

    Filters groups after aggregation (like SQL HAVING clause).

    Requirements:
        - field: REQUIRED, the aggregation alias to filter on
        - operator: REQUIRED, comparison operator
        - value: REQUIRED, value to compare against

    Examples:
        - Keep high-count groups: HavingCondition(field="total_count", operator="gt", value=100)
        - Filter by average: HavingCondition(field="avg_duration", operator="gte", value=60)

        Attributes:
            field (str): The aggregated field to filter on. REQUIRED, must match an aggregation operation alias. Used after
                aggregation to filter groups. Not a source field, but a computed field.
            operator (str): Comparison operator. REQUIRED, valid operators: gt (greater than), gte (greater than or equal),
                lt (less than), lte (less than or equal), eq (equal), ne (not equal).
            value (float | int | str): Value to compare against. REQUIRED, type should match aggregation result type.
                Numeric for COUNT/SUM/AVG, string for grouped values.
    """

    field: str
    operator: str
    value: float | int | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        operator = self.operator

        value: float | int | str
        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "operator": operator,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        operator = d.pop("operator")

        def _parse_value(data: object) -> float | int | str:
            return cast(float | int | str, data)

        value = _parse_value(d.pop("value"))

        having_condition = cls(
            field=field,
            operator=operator,
            value=value,
        )

        having_condition.additional_properties = d
        return having_condition

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
