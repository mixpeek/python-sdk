from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.notification_priority import NotificationPriority
from ..models.notification_type import NotificationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_delivery_status import NotificationDeliveryStatus
    from ..models.notification_metadata import NotificationMetadata


T = TypeVar("T", bound="Notification")


@_attrs_define
class Notification:
    """Model for a notification instance.

    Attributes:
        type_ (NotificationType): Enum for notification types.
        priority (NotificationPriority): Enum for notification priority levels.
        title (str): Notification title
        content (str): Notification content
        organization_id (str): Organization ID
        id (str | Unset): Unique ID
        created_at (datetime.datetime | Unset): Creation timestamp
        user_id (None | str | Unset): User ID (if applicable)
        metadata (NotificationMetadata | Unset): Additional metadata
        delivery_status (NotificationDeliveryStatus | Unset): Delivery status by channel
        read (bool | Unset): Whether the notification has been read Default: False.
        read_at (datetime.datetime | None | Unset): When the notification was read
    """

    type_: NotificationType
    priority: NotificationPriority
    title: str
    content: str
    organization_id: str
    id: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    user_id: None | str | Unset = UNSET
    metadata: NotificationMetadata | Unset = UNSET
    delivery_status: NotificationDeliveryStatus | Unset = UNSET
    read: bool | Unset = False
    read_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        priority = self.priority.value

        title = self.title

        content = self.content

        organization_id = self.organization_id

        id = self.id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        delivery_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delivery_status, Unset):
            delivery_status = self.delivery_status.to_dict()

        read = self.read

        read_at: None | str | Unset
        if isinstance(self.read_at, Unset):
            read_at = UNSET
        elif isinstance(self.read_at, datetime.datetime):
            read_at = self.read_at.isoformat()
        else:
            read_at = self.read_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "priority": priority,
                "title": title,
                "content": content,
                "organization_id": organization_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if delivery_status is not UNSET:
            field_dict["delivery_status"] = delivery_status
        if read is not UNSET:
            field_dict["read"] = read
        if read_at is not UNSET:
            field_dict["read_at"] = read_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_delivery_status import NotificationDeliveryStatus
        from ..models.notification_metadata import NotificationMetadata

        d = dict(src_dict)
        type_ = NotificationType(d.pop("type"))

        priority = NotificationPriority(d.pop("priority"))

        title = d.pop("title")

        content = d.pop("content")

        organization_id = d.pop("organization_id")

        id = d.pop("id", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: NotificationMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = NotificationMetadata.from_dict(_metadata)

        _delivery_status = d.pop("delivery_status", UNSET)
        delivery_status: NotificationDeliveryStatus | Unset
        if isinstance(_delivery_status, Unset):
            delivery_status = UNSET
        else:
            delivery_status = NotificationDeliveryStatus.from_dict(_delivery_status)

        read = d.pop("read", UNSET)

        def _parse_read_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                read_at_type_0 = isoparse(data)

                return read_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        read_at = _parse_read_at(d.pop("read_at", UNSET))

        notification = cls(
            type_=type_,
            priority=priority,
            title=title,
            content=content,
            organization_id=organization_id,
            id=id,
            created_at=created_at,
            user_id=user_id,
            metadata=metadata,
            delivery_status=delivery_status,
            read=read,
            read_at=read_at,
        )

        notification.additional_properties = d
        return notification

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
