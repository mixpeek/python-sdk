from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaSyncRequest")


@_attrs_define
class SchemaSyncRequest:
    """Request to sync a collection's schema by sampling documents.

    Used by:
    - Manual API calls from users
    - Automatic triggers from BatchJobPoller

        Attributes:
            sample_size (int | Unset): Number of documents to sample for schema discovery Default: 1000.
            force (bool | Unset): Force schema sync even if within debounce window. Default: false (respects 5-minute
                debounce) Default: False.
            cascade_to_downstream (bool | Unset): Automatically update downstream collections that use this collection as
                source. Default: true Default: True.
    """

    sample_size: int | Unset = 1000
    force: bool | Unset = False
    cascade_to_downstream: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sample_size = self.sample_size

        force = self.force

        cascade_to_downstream = self.cascade_to_downstream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sample_size is not UNSET:
            field_dict["sample_size"] = sample_size
        if force is not UNSET:
            field_dict["force"] = force
        if cascade_to_downstream is not UNSET:
            field_dict["cascade_to_downstream"] = cascade_to_downstream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sample_size = d.pop("sample_size", UNSET)

        force = d.pop("force", UNSET)

        cascade_to_downstream = d.pop("cascade_to_downstream", UNSET)

        schema_sync_request = cls(
            sample_size=sample_size,
            force=force,
            cascade_to_downstream=cascade_to_downstream,
        )

        schema_sync_request.additional_properties = d
        return schema_sync_request

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
