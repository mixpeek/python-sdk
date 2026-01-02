from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_role import UserRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_create_request_metadata_type_0 import UserCreateRequestMetadataType0


T = TypeVar("T", bound="UserCreateRequest")


@_attrs_define
class UserCreateRequest:
    """Payload for creating an organization user.

    Attributes:
        email (str): Unique email address within the organization.
        user_name (str): Display name shown in dashboards and audit trails.
        avatar_url (None | str | Unset): Profile picture URL (e.g., from PropelAuth picture_url property).
        role (UserRole | Unset): High-level organization role applied to users.

            Roles define the baseline permissions a user has within an organization:

            - ADMIN: Full administrative access including user management, billing,
              and organization settings. Can create/modify/delete all resources.
            - MEMBER: Standard user access. Can create and manage their own resources
              (namespaces, collections, clusters) but cannot manage other users or
              organization-level settings.
            - VIEWER: Read-only access. Can view resources and execute retrievers but
              cannot create, modify, or delete any resources.
        metadata (None | Unset | UserCreateRequestMetadataType0): Custom key/value metadata stored with the user record.
    """

    email: str
    user_name: str
    avatar_url: None | str | Unset = UNSET
    role: UserRole | Unset = UNSET
    metadata: None | Unset | UserCreateRequestMetadataType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_create_request_metadata_type_0 import UserCreateRequestMetadataType0

        email = self.email

        user_name = self.user_name

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, UserCreateRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "user_name": user_name,
            }
        )
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if role is not UNSET:
            field_dict["role"] = role
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_create_request_metadata_type_0 import UserCreateRequestMetadataType0

        d = dict(src_dict)
        email = d.pop("email")

        user_name = d.pop("user_name")

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        _role = d.pop("role", UNSET)
        role: UserRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = UserRole(_role)

        def _parse_metadata(data: object) -> None | Unset | UserCreateRequestMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = UserCreateRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserCreateRequestMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        user_create_request = cls(
            email=email,
            user_name=user_name,
            avatar_url=avatar_url,
            role=role,
            metadata=metadata,
        )

        user_create_request.additional_properties = d
        return user_create_request

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
