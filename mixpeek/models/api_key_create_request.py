from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.permission import Permission
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_scope import ResourceScope


T = TypeVar("T", bound="APIKeyCreateRequest")


@_attrs_define
class APIKeyCreateRequest:
    """Payload for creating a new API key.

    Attributes:
        name (str): Human-friendly key label shown in dashboards.
        description (None | str | Unset): Optional description explaining the key's purpose.
        permissions (list[Permission] | Unset): Set of permissions granted to the API key (least privilege).
        scopes (list[ResourceScope] | None | Unset): Optional resource scope restrictions applied to the key.
        rate_limit_override (int | None | Unset): Per-key requests-per-minute override (defaults to plan limit when
            absent).
        expires_at (datetime.datetime | None | Unset): Optional UTC timestamp when the key automatically expires.
    """

    name: str
    description: None | str | Unset = UNSET
    permissions: list[Permission] | Unset = UNSET
    scopes: list[ResourceScope] | None | Unset = UNSET
    rate_limit_override: int | None | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.value
                permissions.append(permissions_item)

        scopes: list[dict[str, Any]] | None | Unset
        if isinstance(self.scopes, Unset):
            scopes = UNSET
        elif isinstance(self.scopes, list):
            scopes = []
            for scopes_type_0_item_data in self.scopes:
                scopes_type_0_item = scopes_type_0_item_data.to_dict()
                scopes.append(scopes_type_0_item)

        else:
            scopes = self.scopes

        rate_limit_override: int | None | Unset
        if isinstance(self.rate_limit_override, Unset):
            rate_limit_override = UNSET
        else:
            rate_limit_override = self.rate_limit_override

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if rate_limit_override is not UNSET:
            field_dict["rate_limit_override"] = rate_limit_override
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_scope import ResourceScope

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _permissions = d.pop("permissions", UNSET)
        permissions: list[Permission] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = Permission(permissions_item_data)

                permissions.append(permissions_item)

        def _parse_scopes(data: object) -> list[ResourceScope] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scopes_type_0 = []
                _scopes_type_0 = data
                for scopes_type_0_item_data in _scopes_type_0:
                    scopes_type_0_item = ResourceScope.from_dict(scopes_type_0_item_data)

                    scopes_type_0.append(scopes_type_0_item)

                return scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ResourceScope] | None | Unset, data)

        scopes = _parse_scopes(d.pop("scopes", UNSET))

        def _parse_rate_limit_override(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rate_limit_override = _parse_rate_limit_override(d.pop("rate_limit_override", UNSET))

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        api_key_create_request = cls(
            name=name,
            description=description,
            permissions=permissions,
            scopes=scopes,
            rate_limit_override=rate_limit_override,
            expires_at=expires_at,
        )

        api_key_create_request.additional_properties = d
        return api_key_create_request

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
