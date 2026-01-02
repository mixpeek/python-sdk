from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cors_configuration_info_cors_rules_type_0_item import CORSConfigurationInfoCorsRulesType0Item


T = TypeVar("T", bound="CORSConfigurationInfo")


@_attrs_define
class CORSConfigurationInfo:
    """Current CORS configuration information.

    Attributes:
        bucket (str): The object storage bucket name
        has_cors (bool): Whether CORS is currently configured on the bucket
        cors_rules (list[CORSConfigurationInfoCorsRulesType0Item] | None | Unset): The current CORS rules (if
            configured)
    """

    bucket: str
    has_cors: bool
    cors_rules: list[CORSConfigurationInfoCorsRulesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        has_cors = self.has_cors

        cors_rules: list[dict[str, Any]] | None | Unset
        if isinstance(self.cors_rules, Unset):
            cors_rules = UNSET
        elif isinstance(self.cors_rules, list):
            cors_rules = []
            for cors_rules_type_0_item_data in self.cors_rules:
                cors_rules_type_0_item = cors_rules_type_0_item_data.to_dict()
                cors_rules.append(cors_rules_type_0_item)

        else:
            cors_rules = self.cors_rules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket": bucket,
                "has_cors": has_cors,
            }
        )
        if cors_rules is not UNSET:
            field_dict["cors_rules"] = cors_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cors_configuration_info_cors_rules_type_0_item import CORSConfigurationInfoCorsRulesType0Item

        d = dict(src_dict)
        bucket = d.pop("bucket")

        has_cors = d.pop("has_cors")

        def _parse_cors_rules(data: object) -> list[CORSConfigurationInfoCorsRulesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cors_rules_type_0 = []
                _cors_rules_type_0 = data
                for cors_rules_type_0_item_data in _cors_rules_type_0:
                    cors_rules_type_0_item = CORSConfigurationInfoCorsRulesType0Item.from_dict(
                        cors_rules_type_0_item_data
                    )

                    cors_rules_type_0.append(cors_rules_type_0_item)

                return cors_rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CORSConfigurationInfoCorsRulesType0Item] | None | Unset, data)

        cors_rules = _parse_cors_rules(d.pop("cors_rules", UNSET))

        cors_configuration_info = cls(
            bucket=bucket,
            has_cors=has_cors,
            cors_rules=cors_rules,
        )

        cors_configuration_info.additional_properties = d
        return cors_configuration_info

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
