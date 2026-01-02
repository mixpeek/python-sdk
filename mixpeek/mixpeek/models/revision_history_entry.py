from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RevisionHistoryEntry")


@_attrs_define
class RevisionHistoryEntry:
    """A single entry in the revision history.

    Attributes:
        version (int): Version number
        updated_at (datetime.datetime): When this version was created
        updated_by (None | str | Unset): User who made the change
        changes (None | str | Unset): Description of changes made
    """

    version: int
    updated_at: datetime.datetime
    updated_by: None | str | Unset = UNSET
    changes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        updated_at = self.updated_at.isoformat()

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        changes: None | str | Unset
        if isinstance(self.changes, Unset):
            changes = UNSET
        else:
            changes = self.changes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "updated_at": updated_at,
            }
        )
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version")

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        def _parse_changes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        changes = _parse_changes(d.pop("changes", UNSET))

        revision_history_entry = cls(
            version=version,
            updated_at=updated_at,
            updated_by=updated_by,
            changes=changes,
        )

        revision_history_entry.additional_properties = d
        return revision_history_entry

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
