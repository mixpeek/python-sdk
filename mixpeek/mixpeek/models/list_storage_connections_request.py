from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.storage_provider import StorageProvider
from ..models.task_status_enum import TaskStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListStorageConnectionsRequest")


@_attrs_define
class ListStorageConnectionsRequest:
    """Request payload for listing storage connections with filters.

    Use this to filter connections by provider type, status, or active flag.
    Results are paginated automatically.

    **Use Cases:**
    - List all active Google Drive connections
    - Find failed connections that need attention
    - Filter by provider type for sync configuration

    **Examples:**
    ```python
    # List all active Google Drive connections
    {
        "provider_type": "google_drive",
        "is_active": True
    }

    # Find failed connections
    {
        "status": "failed"
    }
    ```

        Attributes:
            provider_type (None | StorageProvider | Unset): OPTIONAL. Filter connections by provider type. Supported:
                google_drive, s3, snowflake, sharepoint, tigris. If not provided, returns connections of all types.
            status (None | TaskStatusEnum | Unset): OPTIONAL. Filter connections by operational status. ACTIVE: Healthy and
                ready for use. SUSPENDED: Temporarily disabled. FAILED: Health checks failing. ARCHIVED: Permanently retired.
            is_active (bool | None | Unset): OPTIONAL. Filter by active flag. True: Returns only active connections
                (status=ACTIVE). False: Returns only inactive connections (SUSPENDED/FAILED/ARCHIVED). If not provided, returns
                connections of all active states.
    """

    provider_type: None | StorageProvider | Unset = UNSET
    status: None | TaskStatusEnum | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_type: None | str | Unset
        if isinstance(self.provider_type, Unset):
            provider_type = UNSET
        elif isinstance(self.provider_type, StorageProvider):
            provider_type = self.provider_type.value
        else:
            provider_type = self.provider_type

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider_type is not UNSET:
            field_dict["provider_type"] = provider_type
        if status is not UNSET:
            field_dict["status"] = status
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_provider_type(data: object) -> None | StorageProvider | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provider_type_type_0 = StorageProvider(data)

                return provider_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StorageProvider | Unset, data)

        provider_type = _parse_provider_type(d.pop("provider_type", UNSET))

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

        list_storage_connections_request = cls(
            provider_type=provider_type,
            status=status,
            is_active=is_active,
        )

        list_storage_connections_request.additional_properties = d
        return list_storage_connections_request

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
