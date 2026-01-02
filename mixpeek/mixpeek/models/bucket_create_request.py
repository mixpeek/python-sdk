from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bucket_create_request_metadata import BucketCreateRequestMetadata
    from ..models.bucket_schema import BucketSchema
    from ..models.unique_key_config import UniqueKeyConfig


T = TypeVar("T", bound="BucketCreateRequest")


@_attrs_define
class BucketCreateRequest:
    """Request model for creating a new bucket.

    REQUIRED: A bucket_schema must be defined to enable data processing and validation.

    The bucket_schema tells the system what fields your objects will have, enabling:
    - Collections to map your data fields to feature extractors via input_mappings
    - Validation of object structure at upload time
    - Type-safe data pipelines from bucket → collection → retrieval

    Every bucket must have a schema that defines the structure of objects it will contain.

        Attributes:
            bucket_name (str): Human-readable name for the bucket
            bucket_schema (BucketSchema): Schema definition for bucket objects.

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
            description (None | str | Unset): Description of the bucket
            unique_key (None | UniqueKeyConfig | Unset): Unique key configuration for this bucket (OPTIONAL). Enables
                uniqueness enforcement and upsert operations on specified field(s) from the schema. Cannot be changed after
                bucket creation.
            metadata (BucketCreateRequestMetadata | Unset): Additional metadata for the bucket
    """

    bucket_name: str
    bucket_schema: BucketSchema
    description: None | str | Unset = UNSET
    unique_key: None | UniqueKeyConfig | Unset = UNSET
    metadata: BucketCreateRequestMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.unique_key_config import UniqueKeyConfig

        bucket_name = self.bucket_name

        bucket_schema = self.bucket_schema.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        unique_key: dict[str, Any] | None | Unset
        if isinstance(self.unique_key, Unset):
            unique_key = UNSET
        elif isinstance(self.unique_key, UniqueKeyConfig):
            unique_key = self.unique_key.to_dict()
        else:
            unique_key = self.unique_key

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket_name": bucket_name,
                "bucket_schema": bucket_schema,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if unique_key is not UNSET:
            field_dict["unique_key"] = unique_key
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bucket_create_request_metadata import BucketCreateRequestMetadata
        from ..models.bucket_schema import BucketSchema
        from ..models.unique_key_config import UniqueKeyConfig

        d = dict(src_dict)
        bucket_name = d.pop("bucket_name")

        bucket_schema = BucketSchema.from_dict(d.pop("bucket_schema"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_unique_key(data: object) -> None | UniqueKeyConfig | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                unique_key_type_0 = UniqueKeyConfig.from_dict(data)

                return unique_key_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UniqueKeyConfig | Unset, data)

        unique_key = _parse_unique_key(d.pop("unique_key", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: BucketCreateRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = BucketCreateRequestMetadata.from_dict(_metadata)

        bucket_create_request = cls(
            bucket_name=bucket_name,
            bucket_schema=bucket_schema,
            description=description,
            unique_key=unique_key,
            metadata=metadata,
        )

        bucket_create_request.additional_properties = d
        return bucket_create_request

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
