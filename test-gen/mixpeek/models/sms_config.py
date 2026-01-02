from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmsConfig")


@_attrs_define
class SmsConfig:
    """Configuration for SMS notifications.

    Attributes:
        phone_numbers (list[str]): Phone numbers to send to
        message_template (None | str | Unset): Template for SMS message
    """

    phone_numbers: list[str]
    message_template: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone_numbers = self.phone_numbers

        message_template: None | str | Unset
        if isinstance(self.message_template, Unset):
            message_template = UNSET
        else:
            message_template = self.message_template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phone_numbers": phone_numbers,
            }
        )
        if message_template is not UNSET:
            field_dict["message_template"] = message_template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phone_numbers = cast(list[str], d.pop("phone_numbers"))

        def _parse_message_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message_template = _parse_message_template(d.pop("message_template", UNSET))

        sms_config = cls(
            phone_numbers=phone_numbers,
            message_template=message_template,
        )

        sms_config.additional_properties = d
        return sms_config

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
