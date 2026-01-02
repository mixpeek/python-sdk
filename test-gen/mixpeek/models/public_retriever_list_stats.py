from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicRetrieverListStats")


@_attrs_define
class PublicRetrieverListStats:
    """Aggregate statistics for public retrievers list.

    Attributes:
        total_active (int | Unset): Number of active public retrievers Default: 0.
        total_password_protected (int | Unset): Number of password-protected retrievers Default: 0.
        total_open (int | Unset): Number of fully open (no password) retrievers Default: 0.
    """

    total_active: int | Unset = 0
    total_password_protected: int | Unset = 0
    total_open: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_active = self.total_active

        total_password_protected = self.total_password_protected

        total_open = self.total_open

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_active is not UNSET:
            field_dict["total_active"] = total_active
        if total_password_protected is not UNSET:
            field_dict["total_password_protected"] = total_password_protected
        if total_open is not UNSET:
            field_dict["total_open"] = total_open

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_active = d.pop("total_active", UNSET)

        total_password_protected = d.pop("total_password_protected", UNSET)

        total_open = d.pop("total_open", UNSET)

        public_retriever_list_stats = cls(
            total_active=total_active,
            total_password_protected=total_password_protected,
            total_open=total_open,
        )

        public_retriever_list_stats.additional_properties = d
        return public_retriever_list_stats

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
