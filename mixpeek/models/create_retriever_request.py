from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_limits import BudgetLimits
    from ..models.create_retriever_request_input_schema import CreateRetrieverRequestInputSchema
    from ..models.display_config import DisplayConfig
    from ..models.stage_config import StageConfig


T = TypeVar("T", bound="CreateRetrieverRequest")


@_attrs_define
class CreateRetrieverRequest:
    """Payload for creating a new retriever.

    Attributes:
        retriever_name (str): Unique retriever name (REQUIRED).
        stages (list[StageConfig]): Ordered stage configurations (REQUIRED).
        description (None | str | Unset): Human readable retriever description (OPTIONAL).
        collection_identifiers (list[str] | Unset): Collection identifiers (names or IDs) queried by the retriever
            (OPTIONAL). Identifiers can be collection names (e.g., 'my_collection') or collection IDs (e.g., 'col_abc123').
            The system will resolve names to IDs automatically. Can be empty for inference-only pipelines (e.g., LLM query
            analysis without document retrieval).
        input_schema (CreateRetrieverRequestInputSchema | Unset): Input schema properties keyed by field name
            (OPTIONAL). Can be empty for static retrievers with hardcoded stage parameters. Each field can include: type,
            description, required, default, and examples. The 'examples' field (list) provides sample values that will be
            shown to users when the retriever is published with include_metadata=true.
        budget_limits (BudgetLimits | Unset): User-defined limits for time and credits during execution.
        tags (list[str] | Unset): Optional retriever tags for search/filters.
        display_config (DisplayConfig | None | Unset): Display configuration for public retriever UI rendering
            (OPTIONAL). Defines how the search interface should appear when the retriever is published, including input
            fields, theme, layout, exposed result fields, and field formatting. This configuration is used as the default
            when publishing the retriever.
    """

    retriever_name: str
    stages: list[StageConfig]
    description: None | str | Unset = UNSET
    collection_identifiers: list[str] | Unset = UNSET
    input_schema: CreateRetrieverRequestInputSchema | Unset = UNSET
    budget_limits: BudgetLimits | Unset = UNSET
    tags: list[str] | Unset = UNSET
    display_config: DisplayConfig | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.display_config import DisplayConfig

        retriever_name = self.retriever_name

        stages = []
        for stages_item_data in self.stages:
            stages_item = stages_item_data.to_dict()
            stages.append(stages_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        collection_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.collection_identifiers, Unset):
            collection_identifiers = self.collection_identifiers

        input_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_schema, Unset):
            input_schema = self.input_schema.to_dict()

        budget_limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.budget_limits, Unset):
            budget_limits = self.budget_limits.to_dict()

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
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
                "stages": stages,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if collection_identifiers is not UNSET:
            field_dict["collection_identifiers"] = collection_identifiers
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
        from ..models.create_retriever_request_input_schema import CreateRetrieverRequestInputSchema
        from ..models.display_config import DisplayConfig
        from ..models.stage_config import StageConfig

        d = dict(src_dict)
        retriever_name = d.pop("retriever_name")

        stages = []
        _stages = d.pop("stages")
        for stages_item_data in _stages:
            stages_item = StageConfig.from_dict(stages_item_data)

            stages.append(stages_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        collection_identifiers = cast(list[str], d.pop("collection_identifiers", UNSET))

        _input_schema = d.pop("input_schema", UNSET)
        input_schema: CreateRetrieverRequestInputSchema | Unset
        if isinstance(_input_schema, Unset):
            input_schema = UNSET
        else:
            input_schema = CreateRetrieverRequestInputSchema.from_dict(_input_schema)

        _budget_limits = d.pop("budget_limits", UNSET)
        budget_limits: BudgetLimits | Unset
        if isinstance(_budget_limits, Unset):
            budget_limits = UNSET
        else:
            budget_limits = BudgetLimits.from_dict(_budget_limits)

        tags = cast(list[str], d.pop("tags", UNSET))

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

        create_retriever_request = cls(
            retriever_name=retriever_name,
            stages=stages,
            description=description,
            collection_identifiers=collection_identifiers,
            input_schema=input_schema,
            budget_limits=budget_limits,
            tags=tags,
            display_config=display_config,
        )

        create_retriever_request.additional_properties = d
        return create_retriever_request

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
