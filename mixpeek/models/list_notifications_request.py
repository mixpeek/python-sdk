from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_priority import NotificationPriority
from ..models.notification_type import NotificationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListNotificationsRequest")


@_attrs_define
class ListNotificationsRequest:
    """Request model for listing notifications.

    Attributes:
        notification_type (None | NotificationType | Unset): Filter by notification type
        priority (None | NotificationPriority | Unset): Filter by priority
        read (bool | None | Unset): Filter by read status
        user_id (None | str | Unset): Filter by user ID
    """

    notification_type: None | NotificationType | Unset = UNSET
    priority: None | NotificationPriority | Unset = UNSET
    read: bool | None | Unset = UNSET
    user_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notification_type: None | str | Unset
        if isinstance(self.notification_type, Unset):
            notification_type = UNSET
        elif isinstance(self.notification_type, NotificationType):
            notification_type = self.notification_type.value
        else:
            notification_type = self.notification_type

        priority: None | str | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, NotificationPriority):
            priority = self.priority.value
        else:
            priority = self.priority

        read: bool | None | Unset
        if isinstance(self.read, Unset):
            read = UNSET
        else:
            read = self.read

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notification_type is not UNSET:
            field_dict["notification_type"] = notification_type
        if priority is not UNSET:
            field_dict["priority"] = priority
        if read is not UNSET:
            field_dict["read"] = read
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_notification_type(data: object) -> None | NotificationType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                notification_type_type_0 = NotificationType(data)

                return notification_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NotificationType | Unset, data)

        notification_type = _parse_notification_type(d.pop("notification_type", UNSET))

        def _parse_priority(data: object) -> None | NotificationPriority | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_0 = NotificationPriority(data)

                return priority_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NotificationPriority | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_read(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        read = _parse_read(d.pop("read", UNSET))

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        list_notifications_request = cls(
            notification_type=notification_type,
            priority=priority,
            read=read,
            user_id=user_id,
        )

        list_notifications_request.additional_properties = d
        return list_notifications_request

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
