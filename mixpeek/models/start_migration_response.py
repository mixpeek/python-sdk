from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.migration_status import MigrationStatus

T = TypeVar("T", bound="StartMigrationResponse")


@_attrs_define
class StartMigrationResponse:
    """Response after starting a migration.

    Example:
        {'message': 'Migration started successfully. Track progress at GET /migrations/{id}', 'migration_id':
            'mig_abc123xyz789', 'started_at': '2025-12-03T10:05:00Z', 'status': 'pending', 'task_id': 'task_xyz789'}

    Attributes:
        migration_id (str): Migration ID
        status (MigrationStatus): Migration execution status.
        task_id (str): Celery task ID
        started_at (datetime.datetime): Start timestamp
        message (str): Human-readable message
    """

    migration_id: str
    status: MigrationStatus
    task_id: str
    started_at: datetime.datetime
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        migration_id = self.migration_id

        status = self.status.value

        task_id = self.task_id

        started_at = self.started_at.isoformat()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "migration_id": migration_id,
                "status": status,
                "task_id": task_id,
                "started_at": started_at,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        migration_id = d.pop("migration_id")

        status = MigrationStatus(d.pop("status"))

        task_id = d.pop("task_id")

        started_at = isoparse(d.pop("started_at"))

        message = d.pop("message")

        start_migration_response = cls(
            migration_id=migration_id,
            status=status,
            task_id=task_id,
            started_at=started_at,
            message=message,
        )

        start_migration_response.additional_properties = d
        return start_migration_response

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
