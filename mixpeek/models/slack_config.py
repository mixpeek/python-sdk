from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SlackConfig")


@_attrs_define
class SlackConfig:
    """Configuration for Slack notifications.

    Attributes:
        webhook_url (str): Slack webhook URL
        channel (None | str | Unset): Slack channel to send to
        username (None | str | Unset): Username to use for the message
        icon_emoji (None | str | Unset): Emoji to use as the icon
        icon_url (None | str | Unset): URL to an image to use as the icon
        blocks_template (None | str | Unset): Template for Slack blocks
    """

    webhook_url: str
    channel: None | str | Unset = UNSET
    username: None | str | Unset = UNSET
    icon_emoji: None | str | Unset = UNSET
    icon_url: None | str | Unset = UNSET
    blocks_template: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_url = self.webhook_url

        channel: None | str | Unset
        if isinstance(self.channel, Unset):
            channel = UNSET
        else:
            channel = self.channel

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        icon_emoji: None | str | Unset
        if isinstance(self.icon_emoji, Unset):
            icon_emoji = UNSET
        else:
            icon_emoji = self.icon_emoji

        icon_url: None | str | Unset
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        blocks_template: None | str | Unset
        if isinstance(self.blocks_template, Unset):
            blocks_template = UNSET
        else:
            blocks_template = self.blocks_template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "webhook_url": webhook_url,
            }
        )
        if channel is not UNSET:
            field_dict["channel"] = channel
        if username is not UNSET:
            field_dict["username"] = username
        if icon_emoji is not UNSET:
            field_dict["icon_emoji"] = icon_emoji
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url
        if blocks_template is not UNSET:
            field_dict["blocks_template"] = blocks_template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_url = d.pop("webhook_url")

        def _parse_channel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel = _parse_channel(d.pop("channel", UNSET))

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_icon_emoji(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_emoji = _parse_icon_emoji(d.pop("icon_emoji", UNSET))

        def _parse_icon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url = _parse_icon_url(d.pop("icon_url", UNSET))

        def _parse_blocks_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        blocks_template = _parse_blocks_template(d.pop("blocks_template", UNSET))

        slack_config = cls(
            webhook_url=webhook_url,
            channel=channel,
            username=username,
            icon_emoji=icon_emoji,
            icon_url=icon_url,
            blocks_template=blocks_template,
        )

        slack_config.additional_properties = d
        return slack_config

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
