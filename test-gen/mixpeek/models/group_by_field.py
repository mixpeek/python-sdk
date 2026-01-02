from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.date_part_unit import DatePartUnit
from ..models.date_trunc_unit import DateTruncUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupByField")


@_attrs_define
class GroupByField:
    """Configuration for grouping by a field.

    Defines how to group data by a specific field, with optional transformations.

    Requirements:
        - field: REQUIRED, the field to group by
        - alias: OPTIONAL, name for the grouped field in results
        - date_trunc: OPTIONAL, truncate date fields to time periods
        - date_part: OPTIONAL, extract part of date field

    Examples:
        - Simple grouping: GroupByField(field="metadata.category")
        - Daily grouping: GroupByField(field="created_at", date_trunc=DateTruncUnit.DAY)
        - Hour of day: GroupByField(field="created_at", date_part=DatePartUnit.HOUR)

        Attributes:
            field (str): The field path to group by. Supports dot notation for nested fields (e.g., 'metadata.category').
                For date fields, can be combined with date_trunc or date_part.
            alias (None | str | Unset): Optional alias for the grouped field in results. If not provided, uses the field
                name. Useful for nested fields to create simpler result names.
            date_trunc (DateTruncUnit | None | Unset): Truncate date field to specified unit. REQUIRED when grouping by
                date/time periods. Only valid for date/datetime fields. Cannot be used with date_part.
            date_part (DatePartUnit | None | Unset): Extract specific part from date field. OPTIONAL for analyzing date
                patterns. Only valid for date/datetime fields. Cannot be used with date_trunc.
    """

    field: str
    alias: None | str | Unset = UNSET
    date_trunc: DateTruncUnit | None | Unset = UNSET
    date_part: DatePartUnit | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        date_trunc: None | str | Unset
        if isinstance(self.date_trunc, Unset):
            date_trunc = UNSET
        elif isinstance(self.date_trunc, DateTruncUnit):
            date_trunc = self.date_trunc.value
        else:
            date_trunc = self.date_trunc

        date_part: None | str | Unset
        if isinstance(self.date_part, Unset):
            date_part = UNSET
        elif isinstance(self.date_part, DatePartUnit):
            date_part = self.date_part.value
        else:
            date_part = self.date_part

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if date_trunc is not UNSET:
            field_dict["date_trunc"] = date_trunc
        if date_part is not UNSET:
            field_dict["date_part"] = date_part

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        def _parse_date_trunc(data: object) -> DateTruncUnit | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_trunc_type_0 = DateTruncUnit(data)

                return date_trunc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DateTruncUnit | None | Unset, data)

        date_trunc = _parse_date_trunc(d.pop("date_trunc", UNSET))

        def _parse_date_part(data: object) -> DatePartUnit | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_part_type_0 = DatePartUnit(data)

                return date_part_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatePartUnit | None | Unset, data)

        date_part = _parse_date_part(d.pop("date_part", UNSET))

        group_by_field = cls(
            field=field,
            alias=alias,
            date_trunc=date_trunc,
            date_part=date_part,
        )

        group_by_field.additional_properties = d
        return group_by_field

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
