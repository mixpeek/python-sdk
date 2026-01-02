from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.migration_status import MigrationStatus
from ..models.migration_type import MigrationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListMigrationsRequest")


@_attrs_define
class ListMigrationsRequest:
    """Request to list migrations with filters.

    Attributes:
        status (MigrationStatus | None | Unset): Filter by status
        migration_type (MigrationType | None | Unset): Filter by type
        source_namespace_id (None | str | Unset): Filter by source namespace
        limit (int | Unset): Maximum results Default: 20.
        offset (int | Unset): Result offset for pagination Default: 0.
    """

    status: MigrationStatus | None | Unset = UNSET
    migration_type: MigrationType | None | Unset = UNSET
    source_namespace_id: None | str | Unset = UNSET
    limit: int | Unset = 20
    offset: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, MigrationStatus):
            status = self.status.value
        else:
            status = self.status

        migration_type: None | str | Unset
        if isinstance(self.migration_type, Unset):
            migration_type = UNSET
        elif isinstance(self.migration_type, MigrationType):
            migration_type = self.migration_type.value
        else:
            migration_type = self.migration_type

        source_namespace_id: None | str | Unset
        if isinstance(self.source_namespace_id, Unset):
            source_namespace_id = UNSET
        else:
            source_namespace_id = self.source_namespace_id

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if migration_type is not UNSET:
            field_dict["migration_type"] = migration_type
        if source_namespace_id is not UNSET:
            field_dict["source_namespace_id"] = source_namespace_id
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_status(data: object) -> MigrationStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = MigrationStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MigrationStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_migration_type(data: object) -> MigrationType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                migration_type_type_0 = MigrationType(data)

                return migration_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MigrationType | None | Unset, data)

        migration_type = _parse_migration_type(d.pop("migration_type", UNSET))

        def _parse_source_namespace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_namespace_id = _parse_source_namespace_id(d.pop("source_namespace_id", UNSET))

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        list_migrations_request = cls(
            status=status,
            migration_type=migration_type,
            source_namespace_id=source_namespace_id,
            limit=limit,
            offset=offset,
        )

        list_migrations_request.additional_properties = d
        return list_migrations_request

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
