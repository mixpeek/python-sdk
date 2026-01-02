from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.migration_status import MigrationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_result import ValidationResult


T = TypeVar("T", bound="CreateMigrationResponse")


@_attrs_define
class CreateMigrationResponse:
    """Response after creating a migration.

    Example:
        {'created_at': '2025-12-03T10:00:00Z', 'message': 'Migration created successfully. Use POST
            /migrations/{id}/start to begin execution.', 'migration_id': 'mig_abc123xyz789', 'status': 'draft',
            'validation_result': {'errors': [], 'estimated_duration_seconds': 1800, 'estimated_resources': {'cluster': 1,
            'collection': 5, 'taxonomy': 2}, 'valid': True, 'warnings': []}}

    Attributes:
        migration_id (str): Created migration ID
        status (MigrationStatus): Migration execution status.
        created_at (datetime.datetime): Creation timestamp
        message (str): Human-readable message
        validation_result (None | Unset | ValidationResult): Validation result if available
    """

    migration_id: str
    status: MigrationStatus
    created_at: datetime.datetime
    message: str
    validation_result: None | Unset | ValidationResult = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.validation_result import ValidationResult

        migration_id = self.migration_id

        status = self.status.value

        created_at = self.created_at.isoformat()

        message = self.message

        validation_result: dict[str, Any] | None | Unset
        if isinstance(self.validation_result, Unset):
            validation_result = UNSET
        elif isinstance(self.validation_result, ValidationResult):
            validation_result = self.validation_result.to_dict()
        else:
            validation_result = self.validation_result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "migration_id": migration_id,
                "status": status,
                "created_at": created_at,
                "message": message,
            }
        )
        if validation_result is not UNSET:
            field_dict["validation_result"] = validation_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validation_result import ValidationResult

        d = dict(src_dict)
        migration_id = d.pop("migration_id")

        status = MigrationStatus(d.pop("status"))

        created_at = isoparse(d.pop("created_at"))

        message = d.pop("message")

        def _parse_validation_result(data: object) -> None | Unset | ValidationResult:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                validation_result_type_0 = ValidationResult.from_dict(data)

                return validation_result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ValidationResult, data)

        validation_result = _parse_validation_result(d.pop("validation_result", UNSET))

        create_migration_response = cls(
            migration_id=migration_id,
            status=status,
            created_at=created_at,
            message=message,
            validation_result=validation_result,
        )

        create_migration_response.additional_properties = d
        return create_migration_response

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
