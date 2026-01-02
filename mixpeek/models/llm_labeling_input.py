from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.input_mapping import InputMapping


T = TypeVar("T", bound="LLMLabelingInput")


@_attrs_define
class LLMLabelingInput:
    """Input configuration for LLM-based cluster labeling.

    Supports flexible input mappings similar to retrievers and buckets,
    allowing multimodal inputs (text, images, videos, audio) for providers
    like Gemini that support native multimodal understanding.

    Examples:
        # Text-only labeling:
        LLMLabelingInput(input_mappings=[
            InputMapping(input_key="headline", source_type="payload", path="headline"),
            InputMapping(input_key="description", source_type="payload", path="description")
        ])

        # Multimodal labeling with images:
        LLMLabelingInput(input_mappings=[
            InputMapping(input_key="text", source_type="payload", path="headline"),
            InputMapping(input_key="image_url", source_type="payload", path="thumbnail_url")
        ])

        # Multimodal with video (for Gemini):
        LLMLabelingInput(input_mappings=[
            InputMapping(input_key="text", source_type="payload", path="description"),
            InputMapping(input_key="video_url", source_type="payload", path="video_url")
        ])

        Attributes:
            input_mappings (list[InputMapping]): Flexible input mappings for constructing LLM context. Supports multimodal
                inputs (text, image_url, video_url, audio_url). Each mapping specifies how to extract data from document
                payloads. At least one input mapping is required.
    """

    input_mappings: list[InputMapping]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_mappings = []
        for input_mappings_item_data in self.input_mappings:
            input_mappings_item = input_mappings_item_data.to_dict()
            input_mappings.append(input_mappings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input_mappings": input_mappings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_mapping import InputMapping

        d = dict(src_dict)
        input_mappings = []
        _input_mappings = d.pop("input_mappings")
        for input_mappings_item_data in _input_mappings:
            input_mappings_item = InputMapping.from_dict(input_mappings_item_data)

            input_mappings.append(input_mappings_item)

        llm_labeling_input = cls(
            input_mappings=input_mappings,
        )

        llm_labeling_input.additional_properties = d
        return llm_labeling_input

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
