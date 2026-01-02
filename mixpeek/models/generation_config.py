from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generation_config_response_schema_type_0 import GenerationConfigResponseSchemaType0


T = TypeVar("T", bound="GenerationConfig")


@_attrs_define
class GenerationConfig:
    """Configuration for generative models.

    Attributes:
        candidate_count (int | Unset): Number of candidate responses to generate for video description. Default: 1.
        max_output_tokens (int | Unset): Maximum number of tokens for the generated video description. Default: 1024.
        temperature (float | Unset): Controls randomness for video description generation. Higher is more random.
            Default: 0.7.
        top_p (float | Unset): Nucleus sampling (top-p) for video description generation. Default: 0.8.
        response_mime_type (None | str | Unset): MIME type for response (e.g., 'application/json')
        response_schema (GenerationConfigResponseSchemaType0 | None | Unset): JSON schema for structured output
    """

    candidate_count: int | Unset = 1
    max_output_tokens: int | Unset = 1024
    temperature: float | Unset = 0.7
    top_p: float | Unset = 0.8
    response_mime_type: None | str | Unset = UNSET
    response_schema: GenerationConfigResponseSchemaType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.generation_config_response_schema_type_0 import GenerationConfigResponseSchemaType0

        candidate_count = self.candidate_count

        max_output_tokens = self.max_output_tokens

        temperature = self.temperature

        top_p = self.top_p

        response_mime_type: None | str | Unset
        if isinstance(self.response_mime_type, Unset):
            response_mime_type = UNSET
        else:
            response_mime_type = self.response_mime_type

        response_schema: dict[str, Any] | None | Unset
        if isinstance(self.response_schema, Unset):
            response_schema = UNSET
        elif isinstance(self.response_schema, GenerationConfigResponseSchemaType0):
            response_schema = self.response_schema.to_dict()
        else:
            response_schema = self.response_schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if candidate_count is not UNSET:
            field_dict["candidate_count"] = candidate_count
        if max_output_tokens is not UNSET:
            field_dict["max_output_tokens"] = max_output_tokens
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if top_p is not UNSET:
            field_dict["top_p"] = top_p
        if response_mime_type is not UNSET:
            field_dict["response_mime_type"] = response_mime_type
        if response_schema is not UNSET:
            field_dict["response_schema"] = response_schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generation_config_response_schema_type_0 import GenerationConfigResponseSchemaType0

        d = dict(src_dict)
        candidate_count = d.pop("candidate_count", UNSET)

        max_output_tokens = d.pop("max_output_tokens", UNSET)

        temperature = d.pop("temperature", UNSET)

        top_p = d.pop("top_p", UNSET)

        def _parse_response_mime_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response_mime_type = _parse_response_mime_type(d.pop("response_mime_type", UNSET))

        def _parse_response_schema(data: object) -> GenerationConfigResponseSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_schema_type_0 = GenerationConfigResponseSchemaType0.from_dict(data)

                return response_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GenerationConfigResponseSchemaType0 | None | Unset, data)

        response_schema = _parse_response_schema(d.pop("response_schema", UNSET))

        generation_config = cls(
            candidate_count=candidate_count,
            max_output_tokens=max_output_tokens,
            temperature=temperature,
            top_p=top_p,
            response_mime_type=response_mime_type,
            response_schema=response_schema,
        )

        generation_config.additional_properties = d
        return generation_config

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
