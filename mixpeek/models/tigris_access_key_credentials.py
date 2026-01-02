from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TigrisAccessKeyCredentials")


@_attrs_define
class TigrisAccessKeyCredentials:
    """Tigris Data access key credentials.

    Tigris uses S3-compatible authentication with access keys.
    Credentials can be obtained from the Tigris dashboard at https://console.tigris.dev.

    Prerequisites:
        - Create a Tigris account at https://www.tigrisdata.com
        - Create a bucket in the Tigris console
        - Generate access keys from the dashboard

    Security:
        - secret_access_key is encrypted at rest using MongoDB CSFLE
        - Rotate keys regularly via the Tigris dashboard
        - Use bucket-scoped keys when possible for least privilege

    Use Cases:
        - Globally distributed object storage
        - Low-latency content delivery
        - S3-compatible workflows with zero egress fees

        Attributes:
            access_key_id (str): REQUIRED. Tigris access key ID for authentication. Obtain from: Tigris Console > Access
                Keys
            secret_access_key (str): REQUIRED. Tigris secret access key for authentication. SECURITY: This field is
                encrypted at rest. Never log or expose this value. Obtain from: Tigris Console when creating access key (shown
                only once)
            type_ (Literal['access_key'] | Unset):  Default: 'access_key'.
    """

    access_key_id: str
    secret_access_key: str
    type_: Literal["access_key"] | Unset = "access_key"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_key_id = self.access_key_id

        secret_access_key = self.secret_access_key

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_key_id": access_key_id,
                "secret_access_key": secret_access_key,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_key_id = d.pop("access_key_id")

        secret_access_key = d.pop("secret_access_key")

        type_ = cast(Literal["access_key"] | Unset, d.pop("type", UNSET))
        if type_ != "access_key" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'access_key', got '{type_}'")

        tigris_access_key_credentials = cls(
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            type_=type_,
        )

        tigris_access_key_credentials.additional_properties = d
        return tigris_access_key_credentials

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
