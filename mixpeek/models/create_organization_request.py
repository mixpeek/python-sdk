from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_organization_request_metadata_type_0 import CreateOrganizationRequestMetadataType0
    from ..models.user_create_request import UserCreateRequest


T = TypeVar("T", bound="CreateOrganizationRequest")


@_attrs_define
class CreateOrganizationRequest:
    """Payload for creating a new organization (private/admin endpoint).

    Attributes:
        organization_name (str): Display name for the organization.
        logo_url (None | str | Unset): Organization logo URL (e.g., from Google Favicon service). If not provided, will
            be auto-generated from first user's email domain.
        users (list[UserCreateRequest] | None | Unset): Initial users to create with the organization.
        metadata (CreateOrganizationRequestMetadataType0 | None | Unset): Custom metadata for the organization.
        credit_count (int | None | Unset): Initial credit count for the organization. Defaults to 1000 if not provided.
        account_type (None | str | Unset): Account type for the organization (free, pro, team, enterprise). Defaults to
            'free'.
    """

    organization_name: str
    logo_url: None | str | Unset = UNSET
    users: list[UserCreateRequest] | None | Unset = UNSET
    metadata: CreateOrganizationRequestMetadataType0 | None | Unset = UNSET
    credit_count: int | None | Unset = UNSET
    account_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_organization_request_metadata_type_0 import CreateOrganizationRequestMetadataType0

        organization_name = self.organization_name

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        users: list[dict[str, Any]] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = users_type_0_item_data.to_dict()
                users.append(users_type_0_item)

        else:
            users = self.users

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CreateOrganizationRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        credit_count: int | None | Unset
        if isinstance(self.credit_count, Unset):
            credit_count = UNSET
        else:
            credit_count = self.credit_count

        account_type: None | str | Unset
        if isinstance(self.account_type, Unset):
            account_type = UNSET
        else:
            account_type = self.account_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization_name": organization_name,
            }
        )
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if users is not UNSET:
            field_dict["users"] = users
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if credit_count is not UNSET:
            field_dict["credit_count"] = credit_count
        if account_type is not UNSET:
            field_dict["account_type"] = account_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_organization_request_metadata_type_0 import CreateOrganizationRequestMetadataType0
        from ..models.user_create_request import UserCreateRequest

        d = dict(src_dict)
        organization_name = d.pop("organization_name")

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_users(data: object) -> list[UserCreateRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in _users_type_0:
                    users_type_0_item = UserCreateRequest.from_dict(users_type_0_item_data)

                    users_type_0.append(users_type_0_item)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UserCreateRequest] | None | Unset, data)

        users = _parse_users(d.pop("users", UNSET))

        def _parse_metadata(data: object) -> CreateOrganizationRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CreateOrganizationRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateOrganizationRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_credit_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        credit_count = _parse_credit_count(d.pop("credit_count", UNSET))

        def _parse_account_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_type = _parse_account_type(d.pop("account_type", UNSET))

        create_organization_request = cls(
            organization_name=organization_name,
            logo_url=logo_url,
            users=users,
            metadata=metadata,
            credit_count=credit_count,
            account_type=account_type,
        )

        create_organization_request.additional_properties = d
        return create_organization_request

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
