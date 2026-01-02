from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditSettings")


@_attrs_define
class AuditSettings:
    """Organization audit configuration.

    Controls audit logging behavior for the organization. Allows enabling
    read access auditing for compliance requirements.

        Attributes:
            read_auditing_enabled (bool | Unset): When enabled, read operations (GET requests) are logged to the audit
                trail. This includes resource access like NAMESPACE_ACCESSED, BUCKET_ACCESSED, etc. Disabled by default to
                reduce audit log volume. Enable for compliance requirements that mandate tracking all resource access. Default:
                False.
    """

    read_auditing_enabled: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        read_auditing_enabled = self.read_auditing_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if read_auditing_enabled is not UNSET:
            field_dict["read_auditing_enabled"] = read_auditing_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        read_auditing_enabled = d.pop("read_auditing_enabled", UNSET)

        audit_settings = cls(
            read_auditing_enabled=read_auditing_enabled,
        )

        audit_settings.additional_properties = d
        return audit_settings

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
