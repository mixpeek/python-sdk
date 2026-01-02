from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_scope import TemplateScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTemplateFromResourceRequest")


@_attrs_define
class CreateTemplateFromResourceRequest:
    """Request to create a template from an existing resource.

    Attributes:
        template_name (str): Name for the new template
        description (None | str | Unset): Description of the template's purpose (OPTIONAL)
        scope (TemplateScope | Unset): Scope of template availability.

            system: Mixpeek-provided, available to all orgs
            organization: Private to org members
            user: Private to creator only
            public: User-created, discoverable by all orgs (marketplace)
        category (None | str | Unset): Optional category for organizing templates
        tags (list[str] | Unset): Optional tags for the template
        is_public (bool | Unset): Whether this template should be publicly discoverable Default: False.
    """

    template_name: str
    description: None | str | Unset = UNSET
    scope: TemplateScope | Unset = UNSET
    category: None | str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    is_public: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_name = self.template_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        is_public = self.is_public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template_name": template_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if scope is not UNSET:
            field_dict["scope"] = scope
        if category is not UNSET:
            field_dict["category"] = category
        if tags is not UNSET:
            field_dict["tags"] = tags
        if is_public is not UNSET:
            field_dict["is_public"] = is_public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_name = d.pop("template_name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _scope = d.pop("scope", UNSET)
        scope: TemplateScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = TemplateScope(_scope)

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        is_public = d.pop("is_public", UNSET)

        create_template_from_resource_request = cls(
            template_name=template_name,
            description=description,
            scope=scope,
            category=category,
            tags=tags,
            is_public=is_public,
        )

        create_template_from_resource_request.additional_properties = d
        return create_template_from_resource_request

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
