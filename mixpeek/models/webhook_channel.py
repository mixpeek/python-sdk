from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_channel import NotificationChannel

if TYPE_CHECKING:
    from ..models.email_config import EmailConfig
    from ..models.slack_config import SlackConfig
    from ..models.sms_config import SmsConfig
    from ..models.webhook_config import WebhookConfig


T = TypeVar("T", bound="WebhookChannel")


@_attrs_define
class WebhookChannel:
    """Notification channel configuration for webhook delivery.

    Defines how and where webhook event notifications should be delivered.
    Each webhook can have multiple channels configured for redundancy or
    different notification audiences.

    Supported Channels:
        - EMAIL: Send notifications via email to specified recipients
        - SLACK: Post messages to Slack channels or direct messages
        - WEBHOOK: HTTP POST to external endpoints (standard webhooks)
        - SMS: Send text message notifications to phone numbers

    Use Cases:
        - Route critical alerts to SMS and Slack simultaneously
        - Send audit trail events to external webhook endpoints
        - Notify team members via email for object lifecycle events
        - Post cluster completion status to Slack channels

    Requirements:
        - Channel type must match the config type (discriminated union)
        - Each config must have valid credentials/endpoints configured
        - Channel configs are validated at webhook creation time

        Attributes:
            channel (NotificationChannel): Enum for notification delivery channels.
            configs (EmailConfig | SlackConfig | SmsConfig | WebhookConfig): REQUIRED. Channel-specific configuration for
                notification delivery. Type depends on the channel field: - EmailConfig for EMAIL channel (recipients, subject
                template, etc.) - SlackConfig for SLACK channel (workspace, channel, bot token) - WebhookConfig for WEBHOOK
                channel (URL, headers, auth) - SmsConfig for SMS channel (phone numbers, provider credentials). See respective
                config models for detailed field requirements.
    """

    channel: NotificationChannel
    configs: EmailConfig | SlackConfig | SmsConfig | WebhookConfig
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.email_config import EmailConfig
        from ..models.slack_config import SlackConfig
        from ..models.webhook_config import WebhookConfig

        channel = self.channel.value

        configs: dict[str, Any]
        if isinstance(self.configs, EmailConfig):
            configs = self.configs.to_dict()
        elif isinstance(self.configs, SlackConfig):
            configs = self.configs.to_dict()
        elif isinstance(self.configs, WebhookConfig):
            configs = self.configs.to_dict()
        else:
            configs = self.configs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
                "configs": configs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_config import EmailConfig
        from ..models.slack_config import SlackConfig
        from ..models.sms_config import SmsConfig
        from ..models.webhook_config import WebhookConfig

        d = dict(src_dict)
        channel = NotificationChannel(d.pop("channel"))

        def _parse_configs(data: object) -> EmailConfig | SlackConfig | SmsConfig | WebhookConfig:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configs_type_0 = EmailConfig.from_dict(data)

                return configs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configs_type_1 = SlackConfig.from_dict(data)

                return configs_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configs_type_2 = WebhookConfig.from_dict(data)

                return configs_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            configs_type_3 = SmsConfig.from_dict(data)

            return configs_type_3

        configs = _parse_configs(d.pop("configs"))

        webhook_channel = cls(
            channel=channel,
            configs=configs,
        )

        webhook_channel.additional_properties = d
        return webhook_channel

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
