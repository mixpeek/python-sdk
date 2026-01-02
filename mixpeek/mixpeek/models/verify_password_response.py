from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifyPasswordResponse")


@_attrs_define
class VerifyPasswordResponse:
    """Response from password verification.

    Attributes:
        valid (bool): Whether the provided password is valid
        public_api_key (None | str | Unset): Public API key for this retriever (only included if password is valid)
    """

    valid: bool
    public_api_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valid = self.valid

        public_api_key: None | str | Unset
        if isinstance(self.public_api_key, Unset):
            public_api_key = UNSET
        else:
            public_api_key = self.public_api_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valid": valid,
            }
        )
        if public_api_key is not UNSET:
            field_dict["public_api_key"] = public_api_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        valid = d.pop("valid")

        def _parse_public_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_api_key = _parse_public_api_key(d.pop("public_api_key", UNSET))

        verify_password_response = cls(
            valid=valid,
            public_api_key=public_api_key,
        )

        verify_password_response.additional_properties = d
        return verify_password_response

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
