from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_feature_extractor_model_params_type_0 import BaseFeatureExtractorModelParamsType0


T = TypeVar("T", bound="BaseFeatureExtractorModel")


@_attrs_define
class BaseFeatureExtractorModel:
    """Minimum feature extractor definition.

    Attributes:
        feature_extractor_name (str): Name of the feature extractor
        version (str): Version of the feature extractor
        params (BaseFeatureExtractorModelParamsType0 | None | Unset): Optional extractor parameters that affect vector
            index configuration. Parameters set here are locked at namespace creation and determine vector dimensions in
            Qdrant. Collections using this extractor must use compatible params. Example: {'model': 'siglip_base'}
    """

    feature_extractor_name: str
    version: str
    params: BaseFeatureExtractorModelParamsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.base_feature_extractor_model_params_type_0 import BaseFeatureExtractorModelParamsType0

        feature_extractor_name = self.feature_extractor_name

        version = self.version

        params: dict[str, Any] | None | Unset
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, BaseFeatureExtractorModelParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feature_extractor_name": feature_extractor_name,
                "version": version,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_feature_extractor_model_params_type_0 import BaseFeatureExtractorModelParamsType0

        d = dict(src_dict)
        feature_extractor_name = d.pop("feature_extractor_name")

        version = d.pop("version")

        def _parse_params(data: object) -> BaseFeatureExtractorModelParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = BaseFeatureExtractorModelParamsType0.from_dict(data)

                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BaseFeatureExtractorModelParamsType0 | None | Unset, data)

        params = _parse_params(d.pop("params", UNSET))

        base_feature_extractor_model = cls(
            feature_extractor_name=feature_extractor_name,
            version=version,
            params=params,
        )

        base_feature_extractor_model.additional_properties = d
        return base_feature_extractor_model

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
