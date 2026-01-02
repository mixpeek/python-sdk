from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enrichment_merge_mode import EnrichmentMergeMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnrichmentField")


@_attrs_define
class EnrichmentField:
    """Field-level enrichment behaviour specification.

    Defines how to copy fields from taxonomy source nodes to enriched documents.
    Supports field renaming via target_field parameter.

    Examples:
        - Copy field as-is: {"field_path": "category", "merge_mode": "replace"}
        - Rename field: {"field_path": "label", "target_field": "visual_style", "merge_mode": "replace"}
        - Append to array: {"field_path": "tags", "merge_mode": "append"}

        Attributes:
            field_path (str): Dot-notation path of the field to copy from the taxonomy node.
            target_field (None | str | Unset): Optional target field name in the enriched document. If specified, the source
                field will be renamed to this name. If not specified, the field_path is used as the target name. Use this to
                rename fields during enrichment (e.g., label → visual_style).
            merge_mode (EnrichmentMergeMode | Unset): How a field from the taxonomy node should be merged into the target
                doc.
    """

    field_path: str
    target_field: None | str | Unset = UNSET
    merge_mode: EnrichmentMergeMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_path = self.field_path

        target_field: None | str | Unset
        if isinstance(self.target_field, Unset):
            target_field = UNSET
        else:
            target_field = self.target_field

        merge_mode: str | Unset = UNSET
        if not isinstance(self.merge_mode, Unset):
            merge_mode = self.merge_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_path": field_path,
            }
        )
        if target_field is not UNSET:
            field_dict["target_field"] = target_field
        if merge_mode is not UNSET:
            field_dict["merge_mode"] = merge_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_path = d.pop("field_path")

        def _parse_target_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_field = _parse_target_field(d.pop("target_field", UNSET))

        _merge_mode = d.pop("merge_mode", UNSET)
        merge_mode: EnrichmentMergeMode | Unset
        if isinstance(_merge_mode, Unset):
            merge_mode = UNSET
        else:
            merge_mode = EnrichmentMergeMode(_merge_mode)

        enrichment_field = cls(
            field_path=field_path,
            target_field=target_field,
            merge_mode=merge_mode,
        )

        enrichment_field.additional_properties = d
        return enrichment_field

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
