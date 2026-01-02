from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicRetrieverListItem")


@_attrs_define
class PublicRetrieverListItem:
    """Simplified retriever information for public listing.

    Provides essential details for browsing public retrievers without
    exposing sensitive configuration or credentials.

        Attributes:
            public_name (str): Public URL-safe name used in the public URL
            public_url (str): Full public URL to the retriever page
            title (str): Display title from display_config
            password_protected (bool): Whether password authentication is required
            is_active (bool): Whether the retriever is active
            created_at (datetime.datetime): When the retriever was published
            updated_at (datetime.datetime): When the retriever was last updated
            description (None | str | Unset): Display description from display_config
            logo_url (None | str | Unset): Logo URL from display_config
            og_image_url (None | str | Unset): Social preview/OG image URL from display_config
    """

    public_name: str
    public_url: str
    title: str
    password_protected: bool
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    og_image_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_name = self.public_name

        public_url = self.public_url

        title = self.title

        password_protected = self.password_protected

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        og_image_url: None | str | Unset
        if isinstance(self.og_image_url, Unset):
            og_image_url = UNSET
        else:
            og_image_url = self.og_image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_name": public_name,
                "public_url": public_url,
                "title": title,
                "password_protected": password_protected,
                "is_active": is_active,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if og_image_url is not UNSET:
            field_dict["og_image_url"] = og_image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public_name = d.pop("public_name")

        public_url = d.pop("public_url")

        title = d.pop("title")

        password_protected = d.pop("password_protected")

        is_active = d.pop("is_active")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_og_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        og_image_url = _parse_og_image_url(d.pop("og_image_url", UNSET))

        public_retriever_list_item = cls(
            public_name=public_name,
            public_url=public_url,
            title=title,
            password_protected=password_protected,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            logo_url=logo_url,
            og_image_url=og_image_url,
        )

        public_retriever_list_item.additional_properties = d
        return public_retriever_list_item

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
