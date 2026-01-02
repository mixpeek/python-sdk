from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_status_enum import TaskStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListSyncConfigurationsRequest")


@_attrs_define
class ListSyncConfigurationsRequest:
    """Request to filter sync configurations for listing.

    All filters are optional - when omitted, returns all sync configurations
    for the bucket. Multiple filters can be combined for precise queries.

    Use Cases:
        - Find all syncs for a specific connection
        - List only active or paused syncs
        - Filter by status to find failed syncs

    Requirements:
        - All fields are OPTIONAL
        - Multiple filters are combined with AND logic
        - Empty request returns all configurations

        Attributes:
            connection_id (None | str | Unset): Filter sync configurations by connection ID. NOT REQUIRED. When provided,
                only returns syncs using this connection. Useful for managing syncs across multiple storage providers. Example:
                'conn_abc123'
            status (None | TaskStatusEnum | Unset): Filter sync configurations by status. NOT REQUIRED. Valid values:
                'pending', 'processing', 'completed', 'failed', 'paused'. Useful for finding syncs that need attention or
                monitoring. Example: 'failed' to find syncs with errors.
            is_active (bool | None | Unset): Filter sync configurations by active status. NOT REQUIRED. True: Only active
                syncs that are currently monitoring/processing. False: Only paused/disabled syncs. Omit to include both active
                and inactive.
    """

    connection_id: None | str | Unset = UNSET
    status: None | TaskStatusEnum | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_id: None | str | Unset
        if isinstance(self.connection_id, Unset):
            connection_id = UNSET
        else:
            connection_id = self.connection_id

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
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if status is not UNSET:
            field_dict["status"] = status
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_id = _parse_connection_id(d.pop("connection_id", UNSET))

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

        list_sync_configurations_request = cls(
            connection_id=connection_id,
            status=status,
            is_active=is_active,
        )

        list_sync_configurations_request.additional_properties = d
        return list_sync_configurations_request

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
