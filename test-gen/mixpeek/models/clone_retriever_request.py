from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_limits import BudgetLimits
    from ..models.clone_retriever_request_input_schema_type_0 import CloneRetrieverRequestInputSchemaType0
    from ..models.display_config import DisplayConfig
    from ..models.stage_config import StageConfig


T = TypeVar("T", bound="CloneRetrieverRequest")


@_attrs_define
class CloneRetrieverRequest:
    """Request to clone a retriever with optional modifications.

    **Purpose:**
    Cloning creates a NEW retriever (with new ID) based on an existing one,
    allowing you to make changes that aren't allowed via PATCH (stages,
    input_schema, collections). This is the recommended way to iterate on
    retriever designs.

    **Clone vs Template vs Version:**
    - **Clone**: Copy THIS retriever and modify it (for iteration/fixes)
    - **Template**: Create retriever from a reusable pattern (for new projects)
    - **Version**: (Not implemented) - Use clone instead

    **Use Cases:**
    - Fix a typo in a stage name without losing execution history
    - Add/remove stages while keeping the original intact
    - Change collections while preserving the original retriever
    - Test modifications before replacing production retriever
    - Create variants (e.g., "strict" vs "relaxed" versions)

    **All fields are OPTIONAL:**
    - Omit a field to keep the original value
    - Provide a field to override the original value
    - retriever_name is REQUIRED (clones must have unique names)

        Attributes:
            retriever_name (str): REQUIRED. Name for the cloned retriever. Must be unique and different from the source
                retriever.
            description (None | str | Unset): OPTIONAL. Description override. If omitted, copies from source retriever.
            collection_identifiers (list[str] | None | Unset): OPTIONAL. Override target collections. If omitted, copies
                from source retriever. This allows you to apply the same retriever logic to different collections.
            stages (list[StageConfig] | None | Unset): OPTIONAL. Override stage configurations. If omitted, copies from
                source retriever. This is where you'd fix typos, add stages, or tweak parameters.
            input_schema (CloneRetrieverRequestInputSchemaType0 | None | Unset): OPTIONAL. Override input schema. If
                omitted, copies from source retriever.
            budget_limits (BudgetLimits | None | Unset): OPTIONAL. Override budget limits. If omitted, copies from source
                retriever.
            tags (list[str] | None | Unset): OPTIONAL. Override tags. If omitted, copies from source retriever.
            display_config (DisplayConfig | None | Unset): OPTIONAL. Override display configuration. If omitted, copies from
                source retriever.
    """

    retriever_name: str
    description: None | str | Unset = UNSET
    collection_identifiers: list[str] | None | Unset = UNSET
    stages: list[StageConfig] | None | Unset = UNSET
    input_schema: CloneRetrieverRequestInputSchemaType0 | None | Unset = UNSET
    budget_limits: BudgetLimits | None | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    display_config: DisplayConfig | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.budget_limits import BudgetLimits
        from ..models.clone_retriever_request_input_schema_type_0 import CloneRetrieverRequestInputSchemaType0
        from ..models.display_config import DisplayConfig

        retriever_name = self.retriever_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        collection_identifiers: list[str] | None | Unset
        if isinstance(self.collection_identifiers, Unset):
            collection_identifiers = UNSET
        elif isinstance(self.collection_identifiers, list):
            collection_identifiers = self.collection_identifiers

        else:
            collection_identifiers = self.collection_identifiers

        stages: list[dict[str, Any]] | None | Unset
        if isinstance(self.stages, Unset):
            stages = UNSET
        elif isinstance(self.stages, list):
            stages = []
            for stages_type_0_item_data in self.stages:
                stages_type_0_item = stages_type_0_item_data.to_dict()
                stages.append(stages_type_0_item)

        else:
            stages = self.stages

        input_schema: dict[str, Any] | None | Unset
        if isinstance(self.input_schema, Unset):
            input_schema = UNSET
        elif isinstance(self.input_schema, CloneRetrieverRequestInputSchemaType0):
            input_schema = self.input_schema.to_dict()
        else:
            input_schema = self.input_schema

        budget_limits: dict[str, Any] | None | Unset
        if isinstance(self.budget_limits, Unset):
            budget_limits = UNSET
        elif isinstance(self.budget_limits, BudgetLimits):
            budget_limits = self.budget_limits.to_dict()
        else:
            budget_limits = self.budget_limits

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        display_config: dict[str, Any] | None | Unset
        if isinstance(self.display_config, Unset):
            display_config = UNSET
        elif isinstance(self.display_config, DisplayConfig):
            display_config = self.display_config.to_dict()
        else:
            display_config = self.display_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retriever_name": retriever_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if collection_identifiers is not UNSET:
            field_dict["collection_identifiers"] = collection_identifiers
        if stages is not UNSET:
            field_dict["stages"] = stages
        if input_schema is not UNSET:
            field_dict["input_schema"] = input_schema
        if budget_limits is not UNSET:
            field_dict["budget_limits"] = budget_limits
        if tags is not UNSET:
            field_dict["tags"] = tags
        if display_config is not UNSET:
            field_dict["display_config"] = display_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_limits import BudgetLimits
        from ..models.clone_retriever_request_input_schema_type_0 import CloneRetrieverRequestInputSchemaType0
        from ..models.display_config import DisplayConfig
        from ..models.stage_config import StageConfig

        d = dict(src_dict)
        retriever_name = d.pop("retriever_name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_collection_identifiers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collection_identifiers_type_0 = cast(list[str], data)

                return collection_identifiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        collection_identifiers = _parse_collection_identifiers(d.pop("collection_identifiers", UNSET))

        def _parse_stages(data: object) -> list[StageConfig] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stages_type_0 = []
                _stages_type_0 = data
                for stages_type_0_item_data in _stages_type_0:
                    stages_type_0_item = StageConfig.from_dict(stages_type_0_item_data)

                    stages_type_0.append(stages_type_0_item)

                return stages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StageConfig] | None | Unset, data)

        stages = _parse_stages(d.pop("stages", UNSET))

        def _parse_input_schema(data: object) -> CloneRetrieverRequestInputSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_schema_type_0 = CloneRetrieverRequestInputSchemaType0.from_dict(data)

                return input_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CloneRetrieverRequestInputSchemaType0 | None | Unset, data)

        input_schema = _parse_input_schema(d.pop("input_schema", UNSET))

        def _parse_budget_limits(data: object) -> BudgetLimits | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                budget_limits_type_0 = BudgetLimits.from_dict(data)

                return budget_limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BudgetLimits | None | Unset, data)

        budget_limits = _parse_budget_limits(d.pop("budget_limits", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_display_config(data: object) -> DisplayConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                display_config_type_0 = DisplayConfig.from_dict(data)

                return display_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DisplayConfig | None | Unset, data)

        display_config = _parse_display_config(d.pop("display_config", UNSET))

        clone_retriever_request = cls(
            retriever_name=retriever_name,
            description=description,
            collection_identifiers=collection_identifiers,
            stages=stages,
            input_schema=input_schema,
            budget_limits=budget_limits,
            tags=tags,
            display_config=display_config,
        )

        clone_retriever_request.additional_properties = d
        return clone_retriever_request

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
