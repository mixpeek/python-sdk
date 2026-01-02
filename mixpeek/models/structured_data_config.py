from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.structured_data_config_additional_properties import StructuredDataConfigAdditionalProperties


T = TypeVar("T", bound="StructuredDataConfig")


@_attrs_define
class StructuredDataConfig:
    """Schema.org structured data configuration for search engines.

    Enables rich search results and better understanding of the page content.

        Attributes:
            type_ (str | Unset): Schema.org type for structured data Default: 'WebApplication'.
            additional_properties (StructuredDataConfigAdditionalProperties | Unset): Additional Schema.org properties
    """

    type_: str | Unset = "WebApplication"
    additional_properties: StructuredDataConfigAdditionalProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        additional_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_properties, Unset):
            additional_properties = self.additional_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if additional_properties is not UNSET:
            field_dict["additional_properties"] = additional_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structured_data_config_additional_properties import StructuredDataConfigAdditionalProperties

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _additional_properties = d.pop("additional_properties", UNSET)
        additional_properties: StructuredDataConfigAdditionalProperties | Unset
        if isinstance(_additional_properties, Unset):
            additional_properties = UNSET
        else:
            additional_properties = StructuredDataConfigAdditionalProperties.from_dict(_additional_properties)

        structured_data_config = cls(
            type_=type_,
            additional_properties=additional_properties,
        )

        structured_data_config.additional_properties = d
        return structured_data_config

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
