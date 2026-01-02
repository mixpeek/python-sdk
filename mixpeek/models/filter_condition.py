from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.filter_operator import FilterOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dynamic_value import DynamicValue


T = TypeVar("T", bound="FilterCondition")


@_attrs_define
class FilterCondition:
    """Represents a single filter condition.

    Attributes:
        field: The field to filter on
        operator: The comparison operator
        value: The value to compare against

        Attributes:
            field (str): Field name to filter on
            value (Any | DynamicValue): Value to compare against
            operator (FilterOperator | Unset): Supported filter operators across database implementations.
    """

    field: str
    value: Any | DynamicValue
    operator: FilterOperator | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dynamic_value import DynamicValue

        field = self.field

        value: Any | dict[str, Any]
        if isinstance(self.value, DynamicValue):
            value = self.value.to_dict()
        else:
            value = self.value

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "value": value,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dynamic_value import DynamicValue

        d = dict(src_dict)
        field = d.pop("field")

        def _parse_value(data: object) -> Any | DynamicValue:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = DynamicValue.from_dict(data)

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Any | DynamicValue, data)

        value = _parse_value(d.pop("value"))

        _operator = d.pop("operator", UNSET)
        operator: FilterOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = FilterOperator(_operator)

        filter_condition = cls(
            field=field,
            value=value,
            operator=operator,
        )

        filter_condition.additional_properties = d
        return filter_condition

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
