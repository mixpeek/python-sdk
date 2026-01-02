from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stage_type import StageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stage_config_config import StageConfigConfig


T = TypeVar("T", bound="StageConfig")


@_attrs_define
class StageConfig:
    """Configuration for a single stage within a retriever.

    Stages support dynamic configuration through template expressions using Jinja2 syntax.

    IMPORTANT - Template Syntax:
        - Use DOUBLE curly braces: {{INPUT.query}} (correct)
        - Single curly braces will NOT work: {INPUT.query} (wrong - not substituted)
        - Namespace names are CASE-INSENSITIVE: {{INPUT.query}}, {{inputs.query}}, {{input.query}}
          all work identically

    Template Namespaces (case-insensitive):
        - INPUT / inputs / input: User-provided query parameters and inputs
        - DOC / doc: Current document fields (for per-document logic)
        - CONTEXT / context: Execution state (budget, timing, retriever metadata)
        - STAGE / stage: Previous stage outputs (for cascading logic)

    Examples:
        Correct: {{INPUT.query_text}}, {{inputs.query}}, {{DOC.content_type}}
        Correct: {{CONTEXT.budget_remaining}}, {{context.budget_remaining}}
        Wrong:   {INPUT.query} - single braces won't be substituted

        Attributes:
            stage_name (str): Human-readable stage instance name (REQUIRED).
            config (StageConfigConfig): Stage implementation parameters (REQUIRED). Must include `stage_id` key referencing
                a registered retriever stage. Supports template expressions using Jinja2 syntax resolved at execution time.
                Template namespaces support both uppercase and lowercase formats: {{INPUT.field}} or {{inputs.field}},
                {{DOC.field}} or {{doc.field}}, {{CONTEXT.field}} or {{context.field}}, {{STAGE.field}} or {{stage.field}}. All
                formats work identically. Provide stage-specific configuration under `parameters`.
            stage_type (None | StageType | Unset): Functional category of the stage. Optional for creation requests; auto-
                inferred from `stage_id` when omitted.
            batch_size (None | str | Unset): Optional templated batch size expression evaluated per execution. Supports
                template variables: {{INPUT.page_size}}, {{inputs.page_size}}, {{CONTEXT.budget_remaining}}, etc. Both uppercase
                and lowercase namespace names are supported (e.g., INPUT/inputs, DOC/doc, CONTEXT/context, STAGE/stage).
                Defaults to stage-specific value when omitted.
            description (None | str | Unset): User-facing description of the stage (OPTIONAL).
    """

    stage_name: str
    config: StageConfigConfig
    stage_type: None | StageType | Unset = UNSET
    batch_size: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_name = self.stage_name

        config = self.config.to_dict()

        stage_type: None | str | Unset
        if isinstance(self.stage_type, Unset):
            stage_type = UNSET
        elif isinstance(self.stage_type, StageType):
            stage_type = self.stage_type.value
        else:
            stage_type = self.stage_type

        batch_size: None | str | Unset
        if isinstance(self.batch_size, Unset):
            batch_size = UNSET
        else:
            batch_size = self.batch_size

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage_name": stage_name,
                "config": config,
            }
        )
        if stage_type is not UNSET:
            field_dict["stage_type"] = stage_type
        if batch_size is not UNSET:
            field_dict["batch_size"] = batch_size
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stage_config_config import StageConfigConfig

        d = dict(src_dict)
        stage_name = d.pop("stage_name")

        config = StageConfigConfig.from_dict(d.pop("config"))

        def _parse_stage_type(data: object) -> None | StageType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stage_type_type_0 = StageType(data)

                return stage_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StageType | Unset, data)

        stage_type = _parse_stage_type(d.pop("stage_type", UNSET))

        def _parse_batch_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_size = _parse_batch_size(d.pop("batch_size", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        stage_config = cls(
            stage_name=stage_name,
            config=config,
            stage_type=stage_type,
            batch_size=batch_size,
            description=description,
        )

        stage_config.additional_properties = d
        return stage_config

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
