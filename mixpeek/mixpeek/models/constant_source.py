from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConstantSource")


@_attrs_define
class ConstantSource:
    """Use a constant/static value for all synced objects.

    Useful for adding fixed metadata to all objects from a sync, such as:
    - Source system identifier
    - Environment tags
    - Default categories
    - Static labels

    Provider Compatibility: All providers

    Example mappings:
        {"type": "constant", "value": "tigris-cdn"} -> All objects get "tigris-cdn"
        {"type": "constant", "value": ["tag1", "tag2"]} -> All objects get this array
        {"type": "constant", "value": {"env": "prod"}} -> All objects get this object

    Attributes:
        type: Must be "constant" to identify this source type
        value: The constant value (any JSON-serializable type)

        Attributes:
            value (Any): The constant value to use for all objects. Can be any JSON-serializable value: string, number,
                boolean, array, object. Arrays are useful for tags, objects for structured metadata.
            type_ (Literal['constant'] | Unset): Source type identifier. Must be 'constant' for static values. Default:
                'constant'.
    """

    value: Any
    type_: Literal["constant"] | Unset = "constant"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        type_ = cast(Literal["constant"] | Unset, d.pop("type", UNSET))
        if type_ != "constant" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'constant', got '{type_}'")

        constant_source = cls(
            value=value,
            type_=type_,
        )

        constant_source.additional_properties = d
        return constant_source

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
