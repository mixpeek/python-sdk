from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.webhook_event_type import WebhookEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_channel import WebhookChannel


T = TypeVar("T", bound="Webhook")


@_attrs_define
class Webhook:
    """Configured webhook subscription for organization event notifications.

    Webhooks enable real-time notifications when events occur in the system.
    Each webhook subscribes to specific event types and delivers notifications
    via one or more configured channels (Slack, email, HTTP, SMS).

    Webhook Lifecycle:
        1. Created with event_types and channels configured
        2. is_active=True enables notification delivery
        3. Events matching event_types trigger notifications to all channels
        4. is_active=False temporarily pauses notifications without deletion
        5. Webhook can be updated to add/remove event types or channels
        6. Permanent deletion removes the webhook configuration

    Use Cases:
        - Integrate Mixpeek events with external systems via HTTP webhooks
        - Notify teams in Slack when ingestion jobs complete
        - Send email alerts when critical failures occur
        - Trigger automated workflows based on state changes
        - Maintain audit trails by forwarding events to SIEM systems

    Best Practices:
        - Subscribe only to events you need (reduces noise)
        - Use descriptive webhook_name for identification
        - Configure multiple channels for critical events (redundancy)
        - Set is_active=False to temporarily disable without losing config
        - Monitor webhook delivery failures via last_error tracking

        Attributes:
            webhook_name (str): REQUIRED. Human-readable name for the webhook. Displayed in dashboards, logs, and
                notification metadata. Should describe the webhook's purpose or destination. Format: 1-200 characters.
            event_types (list[WebhookEventType]): REQUIRED. List of event types that trigger this webhook. When any of these
                events occur, notifications are sent to all channels. Must contain at least one event type. Common patterns: -
                ['object.created', 'object.updated'] for object lifecycle tracking - ['cluster.execution.completed',
                'cluster.execution.failed'] for job monitoring - ['*'] for all events (use cautiously, high volume)
            channels (list[WebhookChannel]): REQUIRED. List of notification channels for event delivery. When an event
                occurs, notifications are sent to ALL configured channels. Must contain at least one channel. Multiple channels
                provide redundancy and multi-audience delivery. Example: Send to both Slack (team) and email (manager) for
                critical events.
            webhook_id (str | Unset): Unique identifier for the webhook. Auto-generated with 'wh_' prefix followed by secure
                random token. Format: wh_{10-character alphanumeric}. Used for API operations and event tracking.
            internal_id (None | str | Unset): Organization internal identifier for multi-tenancy scoping. All webhook
                operations are scoped to this organization. Excluded from API responses for security. Format: int_{24-character
                secure token}.
            is_active (bool | Unset): Whether the webhook is currently active and should send notifications. True: Events
                trigger notifications to channels. False: Webhook is paused, no notifications sent but config preserved. Use to
                temporarily disable webhooks without losing configuration. Default: True Default: True.
            created_at (datetime.datetime | Unset): UTC timestamp when the webhook was created. Auto-generated at creation
                time. Immutable after creation. Format: ISO 8601 datetime.
            updated_at (datetime.datetime | Unset): UTC timestamp of the most recent webhook update. Updated automatically
                when event_types, channels, or is_active changes. Tracks configuration modifications. Format: ISO 8601 datetime.
    """

    webhook_name: str
    event_types: list[WebhookEventType]
    channels: list[WebhookChannel]
    webhook_id: str | Unset = UNSET
    internal_id: None | str | Unset = UNSET
    is_active: bool | Unset = True
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_name = self.webhook_name

        event_types = []
        for event_types_item_data in self.event_types:
            event_types_item = event_types_item_data.value
            event_types.append(event_types_item)

        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()
            channels.append(channels_item)

        webhook_id = self.webhook_id

        internal_id: None | str | Unset
        if isinstance(self.internal_id, Unset):
            internal_id = UNSET
        else:
            internal_id = self.internal_id

        is_active = self.is_active

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "webhook_name": webhook_name,
                "event_types": event_types,
                "channels": channels,
            }
        )
        if webhook_id is not UNSET:
            field_dict["webhook_id"] = webhook_id
        if internal_id is not UNSET:
            field_dict["internal_id"] = internal_id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_channel import WebhookChannel

        d = dict(src_dict)
        webhook_name = d.pop("webhook_name")

        event_types = []
        _event_types = d.pop("event_types")
        for event_types_item_data in _event_types:
            event_types_item = WebhookEventType(event_types_item_data)

            event_types.append(event_types_item)

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = WebhookChannel.from_dict(channels_item_data)

            channels.append(channels_item)

        webhook_id = d.pop("webhook_id", UNSET)

        def _parse_internal_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_id = _parse_internal_id(d.pop("internal_id", UNSET))

        is_active = d.pop("is_active", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        webhook = cls(
            webhook_name=webhook_name,
            event_types=event_types,
            channels=channels,
            webhook_id=webhook_id,
            internal_id=internal_id,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
        )

        webhook.additional_properties = d
        return webhook

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
