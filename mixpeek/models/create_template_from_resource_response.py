from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.template_scope import TemplateScope
from ..models.template_type import TemplateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTemplateFromResourceResponse")


@_attrs_define
class CreateTemplateFromResourceResponse:
    """Response after creating a template from a resource.

    Attributes:
        template_id (str): ID of the created template
        template_name (str): Name of the created template
        template_type (TemplateType): Types of resources that can be templated.
        scope (TemplateScope): Scope of template availability.

            system: Mixpeek-provided, available to all orgs
            organization: Private to org members
            user: Private to creator only
            public: User-created, discoverable by all orgs (marketplace)
        source_resource_id (str): ID of the resource used to create this template
        created_at (datetime.datetime | Unset): Timestamp when template was created
    """

    template_id: str
    template_name: str
    template_type: TemplateType
    scope: TemplateScope
    source_resource_id: str
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        template_name = self.template_name

        template_type = self.template_type.value

        scope = self.scope.value

        source_resource_id = self.source_resource_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template_id": template_id,
                "template_name": template_name,
                "template_type": template_type,
                "scope": scope,
                "source_resource_id": source_resource_id,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_id = d.pop("template_id")

        template_name = d.pop("template_name")

        template_type = TemplateType(d.pop("template_type"))

        scope = TemplateScope(d.pop("scope"))

        source_resource_id = d.pop("source_resource_id")

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        create_template_from_resource_response = cls(
            template_id=template_id,
            template_name=template_name,
            template_type=template_type,
            scope=scope,
            source_resource_id=source_resource_id,
            created_at=created_at,
        )

        create_template_from_resource_response.additional_properties = d
        return create_template_from_resource_response

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
