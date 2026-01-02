from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_create_request import UserCreateRequest


T = TypeVar("T", bound="AddUserToOrganizationRequest")


@_attrs_define
class AddUserToOrganizationRequest:
    """Payload for adding users to an organization (private/admin endpoint).

    Attributes:
        organization_identifier (str): Organization ID or name to add users to.
        users (list[UserCreateRequest]): List of users to add to the organization.
        logo_url (None | str | Unset): Organization logo URL (e.g., from Google Favicon service). If provided and
            organization doesn't have a logo, this will be set.
    """

    organization_identifier: str
    users: list[UserCreateRequest]
    logo_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_identifier = self.organization_identifier

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization_identifier": organization_identifier,
                "users": users,
            }
        )
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_create_request import UserCreateRequest

        d = dict(src_dict)
        organization_identifier = d.pop("organization_identifier")

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = UserCreateRequest.from_dict(users_item_data)

            users.append(users_item)

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        add_user_to_organization_request = cls(
            organization_identifier=organization_identifier,
            users=users,
            logo_url=logo_url,
        )

        add_user_to_organization_request.additional_properties = d
        return add_user_to_organization_request

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
