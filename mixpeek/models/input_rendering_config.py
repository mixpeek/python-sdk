from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retriever_input_schema_field import RetrieverInputSchemaField


T = TypeVar("T", bound="InputRenderingConfig")


@_attrs_define
class InputRenderingConfig:
    """Configuration for how to render an input field in the public UI.

    Maps to BucketSchemaField structure for consistency with how we define
    input types across the system.

        Attributes:
            field_name (str): Name of the input field (matches retriever input_schema key)
            field_schema (RetrieverInputSchemaField): Schema field definition for retriever input parameters.

                Identical structure to BucketSchemaField but uses RetrieverInputSchemaFieldType
                which includes additional reference types like document_reference.

                This allows retrievers to accept:
                1. Metadata inputs (strings, numbers, dates, etc.)
                2. File inputs (images, videos, documents for search)
                3. Reference inputs (document_reference for "find similar" queries)
            label (str): Human-readable label for the input
            input_type (str | Unset): UI input component type. Determines how the input is rendered: text (single line),
                select (dropdown), file (upload), multiselect (multiple choice) Default: 'text'.
            placeholder (None | str | Unset): Placeholder text for the input
            helper_text (None | str | Unset): Helper text displayed below the input to guide users
            suggestions (list[str] | None | Unset): Pre-filled suggestion chips that users can click to populate the input
            required (bool | Unset): Whether this input is required Default: True.
            order (int | Unset): Display order (lower numbers appear first) Default: 0.
    """

    field_name: str
    field_schema: RetrieverInputSchemaField
    label: str
    input_type: str | Unset = "text"
    placeholder: None | str | Unset = UNSET
    helper_text: None | str | Unset = UNSET
    suggestions: list[str] | None | Unset = UNSET
    required: bool | Unset = True
    order: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        field_schema = self.field_schema.to_dict()

        label = self.label

        input_type = self.input_type

        placeholder: None | str | Unset
        if isinstance(self.placeholder, Unset):
            placeholder = UNSET
        else:
            placeholder = self.placeholder

        helper_text: None | str | Unset
        if isinstance(self.helper_text, Unset):
            helper_text = UNSET
        else:
            helper_text = self.helper_text

        suggestions: list[str] | None | Unset
        if isinstance(self.suggestions, Unset):
            suggestions = UNSET
        elif isinstance(self.suggestions, list):
            suggestions = self.suggestions

        else:
            suggestions = self.suggestions

        required = self.required

        order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_name": field_name,
                "field_schema": field_schema,
                "label": label,
            }
        )
        if input_type is not UNSET:
            field_dict["input_type"] = input_type
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if helper_text is not UNSET:
            field_dict["helper_text"] = helper_text
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions
        if required is not UNSET:
            field_dict["required"] = required
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retriever_input_schema_field import RetrieverInputSchemaField

        d = dict(src_dict)
        field_name = d.pop("field_name")

        field_schema = RetrieverInputSchemaField.from_dict(d.pop("field_schema"))

        label = d.pop("label")

        input_type = d.pop("input_type", UNSET)

        def _parse_placeholder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        placeholder = _parse_placeholder(d.pop("placeholder", UNSET))

        def _parse_helper_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        helper_text = _parse_helper_text(d.pop("helper_text", UNSET))

        def _parse_suggestions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                suggestions_type_0 = cast(list[str], data)

                return suggestions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        suggestions = _parse_suggestions(d.pop("suggestions", UNSET))

        required = d.pop("required", UNSET)

        order = d.pop("order", UNSET)

        input_rendering_config = cls(
            field_name=field_name,
            field_schema=field_schema,
            label=label,
            input_type=input_type,
            placeholder=placeholder,
            helper_text=helper_text,
            suggestions=suggestions,
            required=required,
            order=order,
        )

        input_rendering_config.additional_properties = d
        return input_rendering_config

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
