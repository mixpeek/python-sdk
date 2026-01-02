from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.blob_mapping_entry import BlobMappingEntry
    from ..models.field_mapping_entry import FieldMappingEntry


T = TypeVar("T", bound="SchemaMappingMappings")


@_attrs_define
class SchemaMappingMappings:
    """Dictionary mapping target field names to their source extractors. Keys are bucket schema field names (e.g.,
    'content', 'category'). Values are mapping entries defining how to extract and store the data. At least one blob
    mapping (target_type='blob') is recommended for file syncs.

    """

    additional_properties: dict[str, BlobMappingEntry | FieldMappingEntry] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.field_mapping_entry import FieldMappingEntry

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, FieldMappingEntry):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blob_mapping_entry import BlobMappingEntry
        from ..models.field_mapping_entry import FieldMappingEntry

        d = dict(src_dict)
        schema_mapping_mappings = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> BlobMappingEntry | FieldMappingEntry:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = FieldMappingEntry.from_dict(data)

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_1 = BlobMappingEntry.from_dict(data)

                return additional_property_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        schema_mapping_mappings.additional_properties = additional_properties
        return schema_mapping_mappings

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> BlobMappingEntry | FieldMappingEntry:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: BlobMappingEntry | FieldMappingEntry) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
