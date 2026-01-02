from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_content_type import NotificationContentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailConfig")


@_attrs_define
class EmailConfig:
    """Configuration for email notifications.

    Attributes:
        to_addresses (list[str]): Email addresses to send to
        subject_template (None | str | Unset): Template for email subject
        body_template (None | str | Unset): Template for email body
        content_type (NotificationContentType | Unset): Enum for content formats.
        cc_addresses (list[str] | Unset): CC addresses
        bcc_addresses (list[str] | Unset): BCC addresses
    """

    to_addresses: list[str]
    subject_template: None | str | Unset = UNSET
    body_template: None | str | Unset = UNSET
    content_type: NotificationContentType | Unset = UNSET
    cc_addresses: list[str] | Unset = UNSET
    bcc_addresses: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        to_addresses = self.to_addresses

        subject_template: None | str | Unset
        if isinstance(self.subject_template, Unset):
            subject_template = UNSET
        else:
            subject_template = self.subject_template

        body_template: None | str | Unset
        if isinstance(self.body_template, Unset):
            body_template = UNSET
        else:
            body_template = self.body_template

        content_type: str | Unset = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value

        cc_addresses: list[str] | Unset = UNSET
        if not isinstance(self.cc_addresses, Unset):
            cc_addresses = self.cc_addresses

        bcc_addresses: list[str] | Unset = UNSET
        if not isinstance(self.bcc_addresses, Unset):
            bcc_addresses = self.bcc_addresses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "to_addresses": to_addresses,
            }
        )
        if subject_template is not UNSET:
            field_dict["subject_template"] = subject_template
        if body_template is not UNSET:
            field_dict["body_template"] = body_template
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if cc_addresses is not UNSET:
            field_dict["cc_addresses"] = cc_addresses
        if bcc_addresses is not UNSET:
            field_dict["bcc_addresses"] = bcc_addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        to_addresses = cast(list[str], d.pop("to_addresses"))

        def _parse_subject_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject_template = _parse_subject_template(d.pop("subject_template", UNSET))

        def _parse_body_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body_template = _parse_body_template(d.pop("body_template", UNSET))

        _content_type = d.pop("content_type", UNSET)
        content_type: NotificationContentType | Unset
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = NotificationContentType(_content_type)

        cc_addresses = cast(list[str], d.pop("cc_addresses", UNSET))

        bcc_addresses = cast(list[str], d.pop("bcc_addresses", UNSET))

        email_config = cls(
            to_addresses=to_addresses,
            subject_template=subject_template,
            body_template=body_template,
            content_type=content_type,
            cc_addresses=cc_addresses,
            bcc_addresses=bcc_addresses,
        )

        email_config.additional_properties = d
        return email_config

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
