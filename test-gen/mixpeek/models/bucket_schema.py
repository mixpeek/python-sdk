from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bucket_schema_properties import BucketSchemaProperties


T = TypeVar("T", bound="BucketSchema")


@_attrs_define
class BucketSchema:
    """Schema definition for bucket objects.

    IMPORTANT: The bucket schema defines what fields your bucket objects will have.
    This schema is REQUIRED if you want to:
    1. Create collections that use input_mappings to process your bucket data
    2. Validate object structure before ingestion
    3. Enable type-safe data pipelines

    The schema defines the custom fields that will be used in:
    - Blob properties (e.g., "content", "thumbnail", "transcript")
    - Object metadata structure
    - Blob data structures

    Example workflow:
    1. Create bucket WITH schema defining your data structure
    2. Upload objects that conform to that schema
    3. Create collections that map schema fields to feature extractors

    Without a bucket_schema, collections cannot use input_mappings.

        Attributes:
            properties (BucketSchemaProperties):
    """

    properties: BucketSchemaProperties
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "properties": properties,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bucket_schema_properties import BucketSchemaProperties

        d = dict(src_dict)
        properties = BucketSchemaProperties.from_dict(d.pop("properties"))

        bucket_schema = cls(
            properties=properties,
        )

        bucket_schema.additional_properties = d
        return bucket_schema

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
