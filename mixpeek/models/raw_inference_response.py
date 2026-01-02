from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.raw_inference_response_tokens_used_type_0 import RawInferenceResponseTokensUsedType0


T = TypeVar("T", bound="RawInferenceResponse")


@_attrs_define
class RawInferenceResponse:
    """Response from raw inference.

    Returns the inference results along with metadata about the request.

        Attributes:
            data (Any): Inference results (structure varies by modality)
            provider (str): Provider that was used
            model (str): Model that was used
            latency_ms (float): Total inference latency in milliseconds
            tokens_used (None | RawInferenceResponseTokensUsedType0 | Unset): Token usage statistics (if available)
    """

    data: Any
    provider: str
    model: str
    latency_ms: float
    tokens_used: None | RawInferenceResponseTokensUsedType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.raw_inference_response_tokens_used_type_0 import RawInferenceResponseTokensUsedType0

        data = self.data

        provider = self.provider

        model = self.model

        latency_ms = self.latency_ms

        tokens_used: dict[str, Any] | None | Unset
        if isinstance(self.tokens_used, Unset):
            tokens_used = UNSET
        elif isinstance(self.tokens_used, RawInferenceResponseTokensUsedType0):
            tokens_used = self.tokens_used.to_dict()
        else:
            tokens_used = self.tokens_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "provider": provider,
                "model": model,
                "latency_ms": latency_ms,
            }
        )
        if tokens_used is not UNSET:
            field_dict["tokens_used"] = tokens_used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_inference_response_tokens_used_type_0 import RawInferenceResponseTokensUsedType0

        d = dict(src_dict)
        data = d.pop("data")

        provider = d.pop("provider")

        model = d.pop("model")

        latency_ms = d.pop("latency_ms")

        def _parse_tokens_used(data: object) -> None | RawInferenceResponseTokensUsedType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tokens_used_type_0 = RawInferenceResponseTokensUsedType0.from_dict(data)

                return tokens_used_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RawInferenceResponseTokensUsedType0 | Unset, data)

        tokens_used = _parse_tokens_used(d.pop("tokens_used", UNSET))

        raw_inference_response = cls(
            data=data,
            provider=provider,
            model=model,
            latency_ms=latency_ms,
            tokens_used=tokens_used,
        )

        raw_inference_response.additional_properties = d
        return raw_inference_response

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
