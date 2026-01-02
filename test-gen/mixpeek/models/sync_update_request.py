from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_status_enum import TaskStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_mapping import SchemaMapping
    from ..models.sync_update_request_metadata_type_0 import SyncUpdateRequestMetadataType0


T = TypeVar("T", bound="SyncUpdateRequest")


@_attrs_define
class SyncUpdateRequest:
    """Request to update an existing sync configuration.

    Allows partial updates to sync settings without recreating the configuration.
    All fields are optional - only provided fields will be updated.

    Use Cases:
        - Pause/resume syncs by toggling is_active
        - Adjust polling intervals based on activity patterns
        - Update batch sizes for performance tuning
        - Add metadata tags for organization

    Requirements:
        - All fields are OPTIONAL
        - At least one field should be provided for the update
        - Changes take effect on the next sync cycle

        Attributes:
            description (None | str | Unset): Optional human-readable description of the sync configuration. NOT REQUIRED.
                Used for documentation and UI display. Maximum 500 characters.
            metadata (None | SyncUpdateRequestMetadataType0 | Unset): Optional custom metadata to replace existing metadata.
                NOT REQUIRED. Completely replaces existing metadata (not merged). Use for tagging, categorization, or custom
                attributes. Maximum 50 keys, values must be JSON-serializable.
            status (None | TaskStatusEnum | Unset): Optional status to set for the sync configuration. NOT REQUIRED. Valid
                values: 'pending', 'processing', 'completed', 'failed', 'paused'. Typically managed automatically but can be
                manually overridden. Use pause/resume endpoints instead for active control.
            is_active (bool | None | Unset): Optional flag to enable or disable the sync configuration. NOT REQUIRED. When
                False, sync will not process new files. Prefer using the /pause and /resume endpoints for clarity. Changes take
                effect immediately.
            polling_interval_seconds (int | None | Unset): Optional new polling interval in seconds. NOT REQUIRED. Must be
                between 30 and 900 seconds if provided. Only applies to 'continuous' and 'scheduled' sync modes. Lower values
                increase responsiveness but API usage.
            batch_size (int | None | Unset): Optional new batch size for file processing. NOT REQUIRED. Must be between 1
                and 100 if provided. Larger batches improve throughput but use more memory. Changes apply to subsequent batches
                only.
            schema_mapping (None | SchemaMapping | Unset): Optional schema mapping to replace existing mapping. NOT
                REQUIRED. Completely replaces existing schema_mapping (not merged). Defines how source data maps to bucket
                schema fields and blobs. See SyncCreateRequest.schema_mapping for detailed documentation.
            skip_batch_submission (bool | None | Unset): If True, sync objects to the bucket without creating or submitting
                batches for collection processing. Objects are created in the bucket but no tier processing is triggered. NOT
                REQUIRED. When omitted, existing value is preserved.
    """

    description: None | str | Unset = UNSET
    metadata: None | SyncUpdateRequestMetadataType0 | Unset = UNSET
    status: None | TaskStatusEnum | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    polling_interval_seconds: int | None | Unset = UNSET
    batch_size: int | None | Unset = UNSET
    schema_mapping: None | SchemaMapping | Unset = UNSET
    skip_batch_submission: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.schema_mapping import SchemaMapping
        from ..models.sync_update_request_metadata_type_0 import SyncUpdateRequestMetadataType0

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, SyncUpdateRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, TaskStatusEnum):
            status = self.status.value
        else:
            status = self.status

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        polling_interval_seconds: int | None | Unset
        if isinstance(self.polling_interval_seconds, Unset):
            polling_interval_seconds = UNSET
        else:
            polling_interval_seconds = self.polling_interval_seconds

        batch_size: int | None | Unset
        if isinstance(self.batch_size, Unset):
            batch_size = UNSET
        else:
            batch_size = self.batch_size

        schema_mapping: dict[str, Any] | None | Unset
        if isinstance(self.schema_mapping, Unset):
            schema_mapping = UNSET
        elif isinstance(self.schema_mapping, SchemaMapping):
            schema_mapping = self.schema_mapping.to_dict()
        else:
            schema_mapping = self.schema_mapping

        skip_batch_submission: bool | None | Unset
        if isinstance(self.skip_batch_submission, Unset):
            skip_batch_submission = UNSET
        else:
            skip_batch_submission = self.skip_batch_submission

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if status is not UNSET:
            field_dict["status"] = status
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if polling_interval_seconds is not UNSET:
            field_dict["polling_interval_seconds"] = polling_interval_seconds
        if batch_size is not UNSET:
            field_dict["batch_size"] = batch_size
        if schema_mapping is not UNSET:
            field_dict["schema_mapping"] = schema_mapping
        if skip_batch_submission is not UNSET:
            field_dict["skip_batch_submission"] = skip_batch_submission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_mapping import SchemaMapping
        from ..models.sync_update_request_metadata_type_0 import SyncUpdateRequestMetadataType0

        d = dict(src_dict)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_metadata(data: object) -> None | SyncUpdateRequestMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SyncUpdateRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SyncUpdateRequestMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_status(data: object) -> None | TaskStatusEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = TaskStatusEnum(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskStatusEnum | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_polling_interval_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        polling_interval_seconds = _parse_polling_interval_seconds(d.pop("polling_interval_seconds", UNSET))

        def _parse_batch_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        batch_size = _parse_batch_size(d.pop("batch_size", UNSET))

        def _parse_schema_mapping(data: object) -> None | SchemaMapping | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schema_mapping_type_0 = SchemaMapping.from_dict(data)

                return schema_mapping_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SchemaMapping | Unset, data)

        schema_mapping = _parse_schema_mapping(d.pop("schema_mapping", UNSET))

        def _parse_skip_batch_submission(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_batch_submission = _parse_skip_batch_submission(d.pop("skip_batch_submission", UNSET))

        sync_update_request = cls(
            description=description,
            metadata=metadata,
            status=status,
            is_active=is_active,
            polling_interval_seconds=polling_interval_seconds,
            batch_size=batch_size,
            schema_mapping=schema_mapping,
            skip_batch_submission=skip_batch_submission,
        )

        sync_update_request.additional_properties = d
        return sync_update_request

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
