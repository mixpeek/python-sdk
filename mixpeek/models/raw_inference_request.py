from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.raw_inference_request_inputs import RawInferenceRequestInputs
    from ..models.raw_inference_request_parameters_type_0 import RawInferenceRequestParametersType0


T = TypeVar("T", bound="RawInferenceRequest")


@_attrs_define
class RawInferenceRequest:
    """Request for raw inference without retriever framework.

    This endpoint provides direct access to inference services with minimal configuration.
    Ideal for simple LLM calls, embeddings, transcription, or vision tasks without
    requiring collection setup or retriever configuration.

    Examples:
        # Chat completion
        {
            "provider": "openai",
            "model": "gpt-4o-mini",
            "inputs": {"prompts": ["What is AI?"]},
            "parameters": {"temperature": 0.7, "max_tokens": 500}
        }

        # Text embedding
        {
            "provider": "openai",
            "model": "text-embedding-3-large",
            "inputs": {"text": "machine learning"},
            "parameters": {}
        }

        # Audio transcription
        {
            "provider": "openai",
            "model": "whisper-1",
            "inputs": {"audio_url": "https://example.com/audio.mp3"},
            "parameters": {}
        }

        # Vision (multimodal)
        {
            "provider": "openai",
            "model": "gpt-4o",
            "inputs": {
                "prompts": ["Describe this image"],
                "image_url": "https://example.com/image.jpg"
            },
            "parameters": {"temperature": 0.5}
        }

        Attributes:
            provider (str): Provider name: openai, google, anthropic
            model (str): Model identifier specific to the provider
            inputs (RawInferenceRequestInputs): Model-specific inputs. Chat: {prompts: [str]}, Embeddings: {text: str} or
                {texts: [str]}, Transcription: {audio_url: str}, Vision: {prompts: [str], image_url: str}
            parameters (None | RawInferenceRequestParametersType0 | Unset): Optional parameters for inference. Common:
                temperature (float), max_tokens (int), schema (dict for structured output)
    """

    provider: str
    model: str
    inputs: RawInferenceRequestInputs
    parameters: None | RawInferenceRequestParametersType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.raw_inference_request_parameters_type_0 import RawInferenceRequestParametersType0

        provider = self.provider

        model = self.model

        inputs = self.inputs.to_dict()

        parameters: dict[str, Any] | None | Unset
        if isinstance(self.parameters, Unset):
            parameters = UNSET
        elif isinstance(self.parameters, RawInferenceRequestParametersType0):
            parameters = self.parameters.to_dict()
        else:
            parameters = self.parameters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "model": model,
                "inputs": inputs,
            }
        )
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_inference_request_inputs import RawInferenceRequestInputs
        from ..models.raw_inference_request_parameters_type_0 import RawInferenceRequestParametersType0

        d = dict(src_dict)
        provider = d.pop("provider")

        model = d.pop("model")

        inputs = RawInferenceRequestInputs.from_dict(d.pop("inputs"))

        def _parse_parameters(data: object) -> None | RawInferenceRequestParametersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parameters_type_0 = RawInferenceRequestParametersType0.from_dict(data)

                return parameters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RawInferenceRequestParametersType0 | Unset, data)

        parameters = _parse_parameters(d.pop("parameters", UNSET))

        raw_inference_request = cls(
            provider=provider,
            model=model,
            inputs=inputs,
            parameters=parameters,
        )

        raw_inference_request.additional_properties = d
        return raw_inference_request

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
