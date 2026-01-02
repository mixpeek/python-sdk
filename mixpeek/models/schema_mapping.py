from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.schema_mapping_mappings import SchemaMappingMappings


T = TypeVar("T", bound="SchemaMapping")


@_attrs_define
class SchemaMapping:
    """Complete schema mapping configuration for a sync.

    Defines how source data (files, tags, metadata, columns) maps to the
    target bucket schema. Each key is a target field/blob name in the bucket.

    **Key Concepts:**
    - Keys are target bucket schema field names
    - Values define the source and extraction method
    - At least one blob mapping is typically required for file syncs
    - Field mappings extract metadata alongside the file content

    **Provider Examples:**

    **S3/Tigris Video Sync:**
    ```json
    {
        "content": {
            "target_type": "blob",
            "source": {"type": "file"},
            "blob_type": "video"
        },
        "category": {
            "target_type": "field",
            "source": {"type": "tag", "key": "category"}
        },
        "source_bucket": {
            "target_type": "field",
            "source": {"type": "constant", "value": "production-videos"}
        }
    }
    ```

    **Snowflake Customer Table Sync:**
    ```json
    {
        "customer_name": {
            "target_type": "field",
            "source": {"type": "column", "name": "NAME"}
        },
        "profile_image": {
            "target_type": "blob",
            "source": {"type": "column", "name": "AVATAR_URL"},
            "blob_type": "image"
        },
        "segment": {
            "target_type": "field",
            "source": {"type": "column", "name": "CUSTOMER_SEGMENT"},
            "transform": "lowercase"
        }
    }
    ```

    **Google Drive with Folder Categories:**
    ```json
    {
        "content": {
            "target_type": "blob",
            "source": {"type": "file"},
            "blob_type": "auto"
        },
        "department": {
            "target_type": "field",
            "source": {"type": "folder_path", "segment": 0},
            "transform": "lowercase"
        },
        "description": {
            "target_type": "field",
            "source": {"type": "drive_property", "key": "description"}
        }
    }
    ```

    Attributes:
        mappings: Dictionary mapping target field names to their source extractors

        Attributes:
            mappings (SchemaMappingMappings): Dictionary mapping target field names to their source extractors. Keys are
                bucket schema field names (e.g., 'content', 'category'). Values are mapping entries defining how to extract and
                store the data. At least one blob mapping (target_type='blob') is recommended for file syncs.
    """

    mappings: SchemaMappingMappings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mappings = self.mappings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mappings": mappings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_mapping_mappings import SchemaMappingMappings

        d = dict(src_dict)
        mappings = SchemaMappingMappings.from_dict(d.pop("mappings"))

        schema_mapping = cls(
            mappings=mappings,
        )

        schema_mapping.additional_properties = d
        return schema_mapping

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
