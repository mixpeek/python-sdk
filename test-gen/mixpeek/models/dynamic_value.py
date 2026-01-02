from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DynamicValue")


@_attrs_define
class DynamicValue:
    """A value that should be dynamically resolved from the query request.

    Attributes:
        field (str): The dot-notation path to the value in the runtime query request, e.g., 'inputs.user_id'
        type_ (Literal['dynamic'] | Unset):  Default: 'dynamic'.
    """

    field: str
    type_: Literal["dynamic"] | Unset = "dynamic"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        type_ = cast(Literal["dynamic"] | Unset, d.pop("type", UNSET))
        if type_ != "dynamic" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'dynamic', got '{type_}'")

        dynamic_value = cls(
            field=field,
            type_=type_,
        )

        dynamic_value.additional_properties = d
        return dynamic_value

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
