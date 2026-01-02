from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldPassthrough")


@_attrs_define
class FieldPassthrough:
    """Configuration for passing fields from source to output documents.

    Simple field passthrough: specify which fields to copy from source (bucket object
    or upstream collection document) to the output documents alongside extractor outputs.

    Use Cases:
        - Preserve identifiers: campaign_id, product_sku, user_id
        - Keep metadata: category, tags, author, timestamp
        - Maintain business context: priority, status, region
        - Extract nested values: metadata.author, config.model_version
        - Rename fields for cleaner schemas: doc_title → title

    Field Selection:
        - WITHOUT field_passthrough: Only extractor outputs appear in documents
        - WITH field_passthrough: Specified fields + extractor outputs
        - WITH include_all_source_fields=True: All source fields + extractor outputs

    Field Naming:
        - WITHOUT target_path: Output uses source name (or last component for nested)
          - "title" → "title"
          - "metadata.author" → "author"
        - WITH target_path: Output uses specified name
          - source_path="doc_title", target_path="title" → "title"
          - source_path="metadata.author", target_path="contributor" → "contributor"

    Requirements:
        - source_path is REQUIRED - specifies which field to copy (supports dot notation)
        - target_path is OPTIONAL - rename field in output (default: auto-derived name)
        - default is OPTIONAL - provides fallback if field missing (default: omit field)
        - required is OPTIONAL - errors if field missing (default: false, omit field)

        Attributes:
            source_path (str): REQUIRED. Path to the source field to copy. Simple fields: Use field name directly (e.g.,
                'title', 'campaign_id'). Nested fields: Use dot notation (e.g., 'metadata.author', 'config.model.version'). The
                field must exist in the source bucket schema or upstream collection schema. Without target_path, nested fields
                are flattened: 'metadata.author' becomes 'author' in output.
            target_path (None | str | Unset): OPTIONAL. Target field name in output document. If NOT PROVIDED: Uses
                source_path name (or last component for nested paths).   - 'title' → 'title'   - 'metadata.author' → 'author' If
                PROVIDED: Uses this exact name in output.   - source_path='doc_title', target_path='title' → 'title'   -
                source_path='metadata.author', target_path='contributor' → 'contributor' Use cases:   - Rename fields for
                cleaner API schemas   - Avoid name conflicts with extractor outputs   - Standardize field names across different
                sources Constraints:   - Must not conflict with system fields (document_id, collection_id, etc.)   - Must not
                conflict with extractor output fields   - Must be a valid field name (alphanumeric, underscores, hyphens)
            default (Any | None | Unset): OPTIONAL. Default value if source field doesn't exist or is None. If NOT PROVIDED
                and field missing: Field is omitted from output document. If PROVIDED and field missing: Field is included with
                this default value. Type should match expected field type (string, int, list, dict, etc.).
            required (bool | Unset): OPTIONAL. Whether this field MUST exist in source. If True and field missing: Raises
                validation error, processing fails. If False and field missing: Field omitted (or default used if provided). Use
                True for: Critical identifiers, required business fields. Use False for: Optional metadata, nice-to-have fields.
                Default: False (field is optional). Default: False.
    """

    source_path: str
    target_path: None | str | Unset = UNSET
    default: Any | None | Unset = UNSET
    required: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_path = self.source_path

        target_path: None | str | Unset
        if isinstance(self.target_path, Unset):
            target_path = UNSET
        else:
            target_path = self.target_path

        default: Any | None | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_path": source_path,
            }
        )
        if target_path is not UNSET:
            field_dict["target_path"] = target_path
        if default is not UNSET:
            field_dict["default"] = default
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_path = d.pop("source_path")

        def _parse_target_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_path = _parse_target_path(d.pop("target_path", UNSET))

        def _parse_default(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        required = d.pop("required", UNSET)

        field_passthrough = cls(
            source_path=source_path,
            target_path=target_path,
            default=default,
            required=required,
        )

        field_passthrough.additional_properties = d
        return field_passthrough

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
