from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.migration_status import MigrationStatus

T = TypeVar("T", bound="CancelMigrationResponse")


@_attrs_define
class CancelMigrationResponse:
    """Response after cancelling a migration.

    Attributes:
        migration_id (str): Migration ID
        status (MigrationStatus): Migration execution status.
        cancelled_at (datetime.datetime): Cancellation timestamp
        message (str): Human-readable message
    """

    migration_id: str
    status: MigrationStatus
    cancelled_at: datetime.datetime
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        migration_id = self.migration_id

        status = self.status.value

        cancelled_at = self.cancelled_at.isoformat()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "migration_id": migration_id,
                "status": status,
                "cancelled_at": cancelled_at,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        migration_id = d.pop("migration_id")

        status = MigrationStatus(d.pop("status"))

        cancelled_at = isoparse(d.pop("cancelled_at"))

        message = d.pop("message")

        cancel_migration_response = cls(
            migration_id=migration_id,
            status=status,
            cancelled_at=cancelled_at,
            message=message,
        )

        cancel_migration_response.additional_properties = d
        return cancel_migration_response

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
