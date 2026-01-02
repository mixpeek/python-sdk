from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.template_mode import TemplateMode
from ..models.template_scope import TemplateScope
from ..models.template_type import TemplateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_template_model_configuration import BaseTemplateModelConfiguration


T = TypeVar("T", bound="BaseTemplateModel")


@_attrs_define
class BaseTemplateModel:
    """Base template model with common fields for all template types.

    This model is stored in MongoDB and supports three template scopes:
    - System: Mixpeek defaults (all orgs)
    - Organization: All users in the org
    - User: Only the creator

        Attributes:
            template_id (str): Unique template identifier (e.g., 'tmpl_semantic_search')
            template_type (TemplateType): Types of resources that can be templated.
            scope (TemplateScope): Scope of template availability.

                system: Mixpeek-provided, available to all orgs
                organization: Private to org members
                user: Private to creator only
                public: User-created, discoverable by all orgs (marketplace)
            internal_id (str): Organization internal ID. For system templates, use 'system'. For org templates, use the
                actual internal_id.
            name (str): Human-readable template name
            description (str): Detailed description of the template's purpose
            configuration (BaseTemplateModelConfiguration): Template-specific configuration (varies by template_type)
            mode (TemplateMode | Unset): Mode of template instantiation.

                scaffold: Create from pre-built preset
                    - Creates: namespace + bucket + collection + retriever
                    - Endpoint: POST /templates/scaffolds/{id}/instantiate
                    - All resources empty, ready for data

                config: Copy resource configuration only
                    - Creates: empty resource with same settings
                    - Endpoint: POST /templates/{resource}/{id}/instantiate
                    - No data copied

                clone: Copy resource with all data
                    - Creates: full copy including vectors/embeddings
                    - Endpoint: POST /namespaces/{id}/clone
                    - For config-only, use templates instead
            category (None | str | Unset): Optional category for organizing templates
            tags (list[str] | Unset): Tags for categorizing and filtering templates
            is_active (bool | Unset): Whether this template is available for use Default: True.
            is_public (bool | Unset): Whether this template is publicly discoverable without authentication Default: False.
            use_cases (list[str] | Unset): List of common use cases for this template
            requirements (list[str] | Unset): List of requirements (e.g., 'Requires text embeddings')
            created_by (None | str | Unset): User ID who created this template (for org templates)
            source_resource_id (None | str | Unset): ID of the resource this template was created from (for org templates)
            created_at (datetime.datetime | Unset): Timestamp when template was created
            updated_at (datetime.datetime | Unset): Timestamp when template was last updated
    """

    template_id: str
    template_type: TemplateType
    scope: TemplateScope
    internal_id: str
    name: str
    description: str
    configuration: BaseTemplateModelConfiguration
    mode: TemplateMode | Unset = UNSET
    category: None | str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    is_active: bool | Unset = True
    is_public: bool | Unset = False
    use_cases: list[str] | Unset = UNSET
    requirements: list[str] | Unset = UNSET
    created_by: None | str | Unset = UNSET
    source_resource_id: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        template_type = self.template_type.value

        scope = self.scope.value

        internal_id = self.internal_id

        name = self.name

        description = self.description

        configuration = self.configuration.to_dict()

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        is_active = self.is_active

        is_public = self.is_public

        use_cases: list[str] | Unset = UNSET
        if not isinstance(self.use_cases, Unset):
            use_cases = self.use_cases

        requirements: list[str] | Unset = UNSET
        if not isinstance(self.requirements, Unset):
            requirements = self.requirements

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        source_resource_id: None | str | Unset
        if isinstance(self.source_resource_id, Unset):
            source_resource_id = UNSET
        else:
            source_resource_id = self.source_resource_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template_id": template_id,
                "template_type": template_type,
                "scope": scope,
                "internal_id": internal_id,
                "name": name,
                "description": description,
                "configuration": configuration,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode
        if category is not UNSET:
            field_dict["category"] = category
        if tags is not UNSET:
            field_dict["tags"] = tags
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if use_cases is not UNSET:
            field_dict["use_cases"] = use_cases
        if requirements is not UNSET:
            field_dict["requirements"] = requirements
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if source_resource_id is not UNSET:
            field_dict["source_resource_id"] = source_resource_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_template_model_configuration import BaseTemplateModelConfiguration

        d = dict(src_dict)
        template_id = d.pop("template_id")

        template_type = TemplateType(d.pop("template_type"))

        scope = TemplateScope(d.pop("scope"))

        internal_id = d.pop("internal_id")

        name = d.pop("name")

        description = d.pop("description")

        configuration = BaseTemplateModelConfiguration.from_dict(d.pop("configuration"))

        _mode = d.pop("mode", UNSET)
        mode: TemplateMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = TemplateMode(_mode)

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        is_active = d.pop("is_active", UNSET)

        is_public = d.pop("is_public", UNSET)

        use_cases = cast(list[str], d.pop("use_cases", UNSET))

        requirements = cast(list[str], d.pop("requirements", UNSET))

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_source_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_resource_id = _parse_source_resource_id(d.pop("source_resource_id", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        base_template_model = cls(
            template_id=template_id,
            template_type=template_type,
            scope=scope,
            internal_id=internal_id,
            name=name,
            description=description,
            configuration=configuration,
            mode=mode,
            category=category,
            tags=tags,
            is_active=is_active,
            is_public=is_public,
            use_cases=use_cases,
            requirements=requirements,
            created_by=created_by,
            source_resource_id=source_resource_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        base_template_model.additional_properties = d
        return base_template_model

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
