from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.key_status import KeyStatus
from ..models.permission import Permission
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_scope import ResourceScope


T = TypeVar("T", bound="APIKeyUpdateRequest")


@_attrs_define
class APIKeyUpdateRequest:
    """Partial update payload for an API key.

    Attributes:
        name (None | str | Unset): New key label.
        description (None | str | Unset): Updated description for the key.
        permissions (list[Permission] | None | Unset): Replace existing permissions with the provided list.
        scopes (list[ResourceScope] | None | Unset): Replace existing scopes. Use empty list for global access.
        rate_limit_override (int | None | Unset): Updated per-key rate limit override.
        expires_at (datetime.datetime | None | Unset): New expiration timestamp. Use null to remove expiration.
        status (KeyStatus | None | Unset): Manually set key status (e.g. revoke).
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    permissions: list[Permission] | None | Unset = UNSET
    scopes: list[ResourceScope] | None | Unset = UNSET
    rate_limit_override: int | None | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    status: KeyStatus | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        permissions: list[str] | None | Unset
        if isinstance(self.permissions, Unset):
            permissions = UNSET
        elif isinstance(self.permissions, list):
            permissions = []
            for permissions_type_0_item_data in self.permissions:
                permissions_type_0_item = permissions_type_0_item_data.value
                permissions.append(permissions_type_0_item)

        else:
            permissions = self.permissions

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

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, KeyStatus):
            status = self.status.value
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_scope import ResourceScope

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_permissions(data: object) -> list[Permission] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permissions_type_0 = []
                _permissions_type_0 = data
                for permissions_type_0_item_data in _permissions_type_0:
                    permissions_type_0_item = Permission(permissions_type_0_item_data)

                    permissions_type_0.append(permissions_type_0_item)

                return permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Permission] | None | Unset, data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))

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

        def _parse_status(data: object) -> KeyStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = KeyStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeyStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        api_key_update_request = cls(
            name=name,
            description=description,
            permissions=permissions,
            scopes=scopes,
            rate_limit_override=rate_limit_override,
            expires_at=expires_at,
            status=status,
        )

        api_key_update_request.additional_properties = d
        return api_key_update_request

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
