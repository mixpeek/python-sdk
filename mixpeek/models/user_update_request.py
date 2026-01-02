from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_role import UserRole
from ..models.user_status import UserStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_update_request_metadata_type_0 import UserUpdateRequestMetadataType0


T = TypeVar("T", bound="UserUpdateRequest")


@_attrs_define
class UserUpdateRequest:
    """Partial update payload for a user.

    Attributes:
        user_name (None | str | Unset): Updated display name.
        avatar_url (None | str | Unset): Updated profile image URL (e.g., custom avatar to override Gravatar).
        role (None | Unset | UserRole): Updated organization role.
        status (None | Unset | UserStatus): Lifecycle status update (active, suspended, pending).
        metadata (None | Unset | UserUpdateRequestMetadataType0): Replaces metadata with the provided dictionary when
            set.
    """

    user_name: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    role: None | Unset | UserRole = UNSET
    status: None | Unset | UserStatus = UNSET
    metadata: None | Unset | UserUpdateRequestMetadataType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_update_request_metadata_type_0 import UserUpdateRequestMetadataType0

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, UserRole):
            role = self.role.value
        else:
            role = self.role

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, UserStatus):
            status = self.status.value
        else:
            status = self.status

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, UserUpdateRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if role is not UNSET:
            field_dict["role"] = role
        if status is not UNSET:
            field_dict["status"] = status
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_update_request_metadata_type_0 import UserUpdateRequestMetadataType0

        d = dict(src_dict)

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("user_name", UNSET))

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        def _parse_role(data: object) -> None | Unset | UserRole:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_0 = UserRole(data)

                return role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserRole, data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_status(data: object) -> None | Unset | UserStatus:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = UserStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserStatus, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_metadata(data: object) -> None | Unset | UserUpdateRequestMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = UserUpdateRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserUpdateRequestMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        user_update_request = cls(
            user_name=user_name,
            avatar_url=avatar_url,
            role=role,
            status=status,
            metadata=metadata,
        )

        user_update_request.additional_properties = d
        return user_update_request

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
