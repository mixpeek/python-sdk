from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="S3TagSource")


@_attrs_define
class S3TagSource:
    r""" Extract value from an S3/Tigris object tag.

    S3 object tags are key-value pairs attached to objects, commonly used for
    categorization, cost allocation, and metadata. Tags are limited to 10 per object
    with keys up to 128 chars and values up to 256 chars.

    Provider Compatibility: S3, Tigris, MinIO, DigitalOcean Spaces, Wasabi

    Example S3 CLI to set tag:
        aws s3api put-object-tagging --bucket my-bucket --key video.mp4 \
            --tagging 'TagSet=[{Key=category,Value=marketing}]'

    Example mapping:
        {"type": "tag", "key": "category"} -> extracts "marketing" from the tag

    Attributes:
        type: Must be "tag" to identify this source type
        key: The tag key to extract (case-sensitive, max 128 chars)

        Attributes:
            key (str): The tag key to extract. Case-sensitive. Must match the exact tag key on the S3/Tigris object. Common
                examples: 'category', 'project', 'owner', 'environment'. Maximum length: 128 characters.
            type_ (Literal['tag'] | Unset): Source type identifier. Must be 'tag' for S3/Tigris object tags. Default: 'tag'.
     """

    key: str
    type_: Literal["tag"] | Unset = "tag"
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

        type_ = cast(Literal["tag"] | Unset, d.pop("type", UNSET))
        if type_ != "tag" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'tag', got '{type_}'")

        s3_tag_source = cls(
            key=key,
            type_=type_,
        )

        s3_tag_source.additional_properties = d
        return s3_tag_source

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
