from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UuidIndexParams")


@_attrs_define
class UuidIndexParams:
    """Configuration for UUID index.

    Attributes:
        type_ (str | Unset):  Default: 'uuid'.
        is_tenant (bool | Unset):  Default: False.
    """

    type_: str | Unset = "uuid"
    is_tenant: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        is_tenant = self.is_tenant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if is_tenant is not UNSET:
            field_dict["is_tenant"] = is_tenant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        is_tenant = d.pop("is_tenant", UNSET)

        uuid_index_params = cls(
            type_=type_,
            is_tenant=is_tenant,
        )

        uuid_index_params.additional_properties = d
        return uuid_index_params

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
