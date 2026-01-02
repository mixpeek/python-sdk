from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JoinStats")


@_attrs_define
class JoinStats:
    """
    Attributes:
        processed_docs (int | Unset):  Default: 0.
        batches (int | Unset):  Default: 0.
        errors (int | Unset):  Default: 0.
    """

    processed_docs: int | Unset = 0
    batches: int | Unset = 0
    errors: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        processed_docs = self.processed_docs

        batches = self.batches

        errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if processed_docs is not UNSET:
            field_dict["processed_docs"] = processed_docs
        if batches is not UNSET:
            field_dict["batches"] = batches
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        processed_docs = d.pop("processed_docs", UNSET)

        batches = d.pop("batches", UNSET)

        errors = d.pop("errors", UNSET)

        join_stats = cls(
            processed_docs=processed_docs,
            batches=batches,
            errors=errors,
        )

        join_stats.additional_properties = d
        return join_stats

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
