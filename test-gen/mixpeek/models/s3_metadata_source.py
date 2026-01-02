from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="S3MetadataSource")


@_attrs_define
class S3MetadataSource:
    """Extract value from S3/Tigris object user metadata.

    S3 user metadata (x-amz-meta-*) provides custom key-value pairs stored
    with the object. Unlike tags, metadata is set at upload time and is
    immutable without re-uploading the object.

    Provider Compatibility: S3, Tigris, MinIO, DigitalOcean Spaces, Wasabi

    Example S3 CLI to set metadata:
        aws s3 cp video.mp4 s3://bucket/ --metadata '{"author":"john","version":"1.0"}'

    Example boto3 upload with metadata:
        s3.put_object(Bucket='b', Key='k', Body=data, Metadata={'author': 'john'})

    Example mapping:
        {"type": "metadata", "key": "author"} -> extracts "john" from x-amz-meta-author

    Attributes:
        type: Must be "metadata" to identify this source type
        key: The metadata key without 'x-amz-meta-' prefix (case-insensitive)

        Attributes:
            key (str): The metadata key to extract (without 'x-amz-meta-' prefix). Case-insensitive (S3 lowercases all
                metadata keys). Common examples: 'author', 'version', 'source-system', 'original-filename'. Note: S3
                automatically lowercases keys, so 'Author' becomes 'author'.
            type_ (Literal['metadata'] | Unset): Source type identifier. Must be 'metadata' for S3/Tigris user metadata.
                Default: 'metadata'.
    """

    key: str
    type_: Literal["metadata"] | Unset = "metadata"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        type_ = cast(Literal["metadata"] | Unset, d.pop("type", UNSET))
        if type_ != "metadata" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'metadata', got '{type_}'")

        s3_metadata_source = cls(
            key=key,
            type_=type_,
        )

        s3_metadata_source.additional_properties = d
        return s3_metadata_source

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
