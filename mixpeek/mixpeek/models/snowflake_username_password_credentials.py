from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnowflakeUsernamePasswordCredentials")


@_attrs_define
class SnowflakeUsernamePasswordCredentials:
    """Snowflake username/password authentication (FALLBACK option).

    Traditional username/password authentication for Snowflake.
    Less secure than key pair authentication but simpler to set up.

    Security:
        - Password encrypted at rest via CSFLE
        - Consider using key pair auth for production
        - Enable MFA on Snowflake user account

        Attributes:
            username (str): REQUIRED. Snowflake username (case-insensitive).
            password (str): REQUIRED. Snowflake password for authentication. SECURITY: This field is encrypted at rest via
                CSFLE. Never log or expose.
            type_ (Literal['username_password'] | Unset):  Default: 'username_password'.
    """

    username: str
    password: str
    type_: Literal["username_password"] | Unset = "username_password"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password")

        type_ = cast(Literal["username_password"] | Unset, d.pop("type", UNSET))
        if type_ != "username_password" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'username_password', got '{type_}'")

        snowflake_username_password_credentials = cls(
            username=username,
            password=password,
            type_=type_,
        )

        snowflake_username_password_credentials.additional_properties = d
        return snowflake_username_password_credentials

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
