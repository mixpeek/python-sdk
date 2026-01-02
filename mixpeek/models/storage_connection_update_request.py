from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_status_enum import TaskStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_connection_update_request_metadata_type_0 import StorageConnectionUpdateRequestMetadataType0
    from ..models.storage_connection_update_request_provider_config_type_0 import (
        StorageConnectionUpdateRequestProviderConfigType0,
    )


T = TypeVar("T", bound="StorageConnectionUpdateRequest")


@_attrs_define
class StorageConnectionUpdateRequest:
    """Request payload for updating storage connection metadata.

    Allows partial updates to connection metadata without changing credentials.
    Credentials can be updated via provider_config.

    **What You Can Update:**
    - Connection name and description
    - Metadata tags
    - Status (active/suspended)
    - Provider credentials (via provider_config)

    **Examples:**
    ```python
    # Update name and description
    {
        "name": "Updated Drive Name",
        "description": "New description"
    }

    # Suspend connection
    {
        "status": "suspended",
        "is_active": False
    }

    # Refresh credentials
    {
        "provider_config": {
            "credentials": {...}
        }
    }
    ```

        Attributes:
            name (None | str | Unset): OPTIONAL. New name for the connection. Must be unique within the organization if
                provided. Format: 1-100 characters.
            description (None | str | Unset): OPTIONAL. New description for the connection. Set to empty string to clear
                existing description. Format: Up to 500 characters.
            metadata (None | StorageConnectionUpdateRequestMetadataType0 | Unset): OPTIONAL. New metadata dictionary.
                Replaces existing metadata entirely (partial updates not supported). Set to empty dict {} to clear all metadata.
            status (None | TaskStatusEnum | Unset): OPTIONAL. New operational status. ACTIVE: Connection is healthy and
                ready for use. SUSPENDED: Temporarily disabled, credentials preserved. FAILED: Health checks failing. ARCHIVED:
                Permanently retired (cannot be reactivated).
            is_active (bool | None | Unset): OPTIONAL. Quick boolean flag for filtering. True when status is ACTIVE, False
                otherwise. Automatically maintained when status changes.
            provider_config (None | StorageConnectionUpdateRequestProviderConfigType0 | Unset): OPTIONAL. Updated provider
                configuration including credentials. Replaces entire provider_config (partial updates not supported). SECURITY:
                Sensitive fields are encrypted at rest.
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    metadata: None | StorageConnectionUpdateRequestMetadataType0 | Unset = UNSET
    status: None | TaskStatusEnum | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    provider_config: None | StorageConnectionUpdateRequestProviderConfigType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.storage_connection_update_request_metadata_type_0 import (
            StorageConnectionUpdateRequestMetadataType0,
        )
        from ..models.storage_connection_update_request_provider_config_type_0 import (
            StorageConnectionUpdateRequestProviderConfigType0,
        )

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, StorageConnectionUpdateRequestMetadataType0):
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

        provider_config: dict[str, Any] | None | Unset
        if isinstance(self.provider_config, Unset):
            provider_config = UNSET
        elif isinstance(self.provider_config, StorageConnectionUpdateRequestProviderConfigType0):
            provider_config = self.provider_config.to_dict()
        else:
            provider_config = self.provider_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if status is not UNSET:
            field_dict["status"] = status
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if provider_config is not UNSET:
            field_dict["provider_config"] = provider_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_connection_update_request_metadata_type_0 import (
            StorageConnectionUpdateRequestMetadataType0,
        )
        from ..models.storage_connection_update_request_provider_config_type_0 import (
            StorageConnectionUpdateRequestProviderConfigType0,
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_metadata(data: object) -> None | StorageConnectionUpdateRequestMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = StorageConnectionUpdateRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StorageConnectionUpdateRequestMetadataType0 | Unset, data)

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

        def _parse_provider_config(data: object) -> None | StorageConnectionUpdateRequestProviderConfigType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_config_type_0 = StorageConnectionUpdateRequestProviderConfigType0.from_dict(data)

                return provider_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StorageConnectionUpdateRequestProviderConfigType0 | Unset, data)

        provider_config = _parse_provider_config(d.pop("provider_config", UNSET))

        storage_connection_update_request = cls(
            name=name,
            description=description,
            metadata=metadata,
            status=status,
            is_active=is_active,
            provider_config=provider_config,
        )

        storage_connection_update_request.additional_properties = d
        return storage_connection_update_request

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
