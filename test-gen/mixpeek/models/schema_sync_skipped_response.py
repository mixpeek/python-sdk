from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaSyncSkippedResponse")


@_attrs_define
class SchemaSyncSkippedResponse:
    """Response when schema sync was skipped (debounce or disabled).

    Attributes:
        reason (str): Why sync was skipped
        collection_id (str): Collection ID
        schema_version (int): Current schema version
        success (bool | Unset): Request succeeded Default: True.
        skipped (bool | Unset): Schema sync was skipped Default: True.
        last_sync (None | str | Unset): Last sync timestamp
    """

    reason: str
    collection_id: str
    schema_version: int
    success: bool | Unset = True
    skipped: bool | Unset = True
    last_sync: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        collection_id = self.collection_id

        schema_version = self.schema_version

        success = self.success

        skipped = self.skipped

        last_sync: None | str | Unset
        if isinstance(self.last_sync, Unset):
            last_sync = UNSET
        else:
            last_sync = self.last_sync

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
                "collection_id": collection_id,
                "schema_version": schema_version,
            }
        )
        if success is not UNSET:
            field_dict["success"] = success
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if last_sync is not UNSET:
            field_dict["last_sync"] = last_sync

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason")

        collection_id = d.pop("collection_id")

        schema_version = d.pop("schema_version")

        success = d.pop("success", UNSET)

        skipped = d.pop("skipped", UNSET)

        def _parse_last_sync(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_sync = _parse_last_sync(d.pop("last_sync", UNSET))

        schema_sync_skipped_response = cls(
            reason=reason,
            collection_id=collection_id,
            schema_version=schema_version,
            success=success,
            skipped=skipped,
            last_sync=last_sync,
        )

        schema_sync_skipped_response.additional_properties = d
        return schema_sync_skipped_response

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
