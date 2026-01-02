from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxonomyOptions")


@_attrs_define
class TaxonomyOptions:
    """Options for taxonomy migration.

    Attributes:
        preserve_taxonomy_ids (bool | Unset): Keep same taxonomy IDs in target Default: True.
        preserve_enrichment_fields (bool | Unset): Keep _taxonomy_* fields in documents Default: True.
        re_run_enrichment (bool | Unset): Re-run taxonomy enrichment after migration Default: False.
        migrate_reference_collections (bool | Unset): Automatically migrate reference collections Default: True.
    """

    preserve_taxonomy_ids: bool | Unset = True
    preserve_enrichment_fields: bool | Unset = True
    re_run_enrichment: bool | Unset = False
    migrate_reference_collections: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preserve_taxonomy_ids = self.preserve_taxonomy_ids

        preserve_enrichment_fields = self.preserve_enrichment_fields

        re_run_enrichment = self.re_run_enrichment

        migrate_reference_collections = self.migrate_reference_collections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preserve_taxonomy_ids is not UNSET:
            field_dict["preserve_taxonomy_ids"] = preserve_taxonomy_ids
        if preserve_enrichment_fields is not UNSET:
            field_dict["preserve_enrichment_fields"] = preserve_enrichment_fields
        if re_run_enrichment is not UNSET:
            field_dict["re_run_enrichment"] = re_run_enrichment
        if migrate_reference_collections is not UNSET:
            field_dict["migrate_reference_collections"] = migrate_reference_collections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        preserve_taxonomy_ids = d.pop("preserve_taxonomy_ids", UNSET)

        preserve_enrichment_fields = d.pop("preserve_enrichment_fields", UNSET)

        re_run_enrichment = d.pop("re_run_enrichment", UNSET)

        migrate_reference_collections = d.pop("migrate_reference_collections", UNSET)

        taxonomy_options = cls(
            preserve_taxonomy_ids=preserve_taxonomy_ids,
            preserve_enrichment_fields=preserve_enrichment_fields,
            re_run_enrichment=re_run_enrichment,
            migrate_reference_collections=migrate_reference_collections,
        )

        taxonomy_options.additional_properties = d
        return taxonomy_options

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
