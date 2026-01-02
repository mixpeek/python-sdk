from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeatureAddress")


@_attrs_define
class FeatureAddress:
    """Canonical feature address: mixpeek://{extractor}@{version}/{output}.

    The output segment is the inference_name (embedding model identifier), which enables
    cross-extractor compatibility checking. Two feature URIs with the same inference_name
    in the output segment produce compatible embeddings that can be compared/fused.

    Format examples:
        - mixpeek://text_extractor@v1/multilingual_e5_large_instruct_v1
        - mixpeek://multimodal_extractor@v1/multilingual_e5_large_instruct_v1  (compatible with above!)
        - mixpeek://image_extractor@v1/google_siglip_base_v1  (different model = incompatible)

    Short form without the output segment is allowed only if the extractor has
    a single vector output.

        Attributes:
            extractor (str):
            version (str):
            scheme (str | Unset):  Default: 'mixpeek'.
            output (None | str | Unset):
    """

    extractor: str
    version: str
    scheme: str | Unset = "mixpeek"
    output: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extractor = self.extractor

        version = self.version

        scheme = self.scheme

        output: None | str | Unset
        if isinstance(self.output, Unset):
            output = UNSET
        else:
            output = self.output

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extractor": extractor,
                "version": version,
            }
        )
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        extractor = d.pop("extractor")

        version = d.pop("version")

        scheme = d.pop("scheme", UNSET)

        def _parse_output(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output = _parse_output(d.pop("output", UNSET))

        feature_address = cls(
            extractor=extractor,
            version=version,
            scheme=scheme,
            output=output,
        )

        feature_address.additional_properties = d
        return feature_address

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
