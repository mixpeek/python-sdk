from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bucket_patch_request_metadata_type_0 import BucketPatchRequestMetadataType0


T = TypeVar("T", bound="BucketPatchRequest")


@_attrs_define
class BucketPatchRequest:
    """Request model for partial update of an existing bucket (PATCH operation).

    Attributes:
        bucket_name (None | str | Unset): Human-readable name for the bucket
        description (None | str | Unset): Description of the bucket
        metadata (BucketPatchRequestMetadataType0 | None | Unset): Additional metadata for the bucket
    """

    bucket_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    metadata: BucketPatchRequestMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bucket_patch_request_metadata_type_0 import BucketPatchRequestMetadataType0

        bucket_name: None | str | Unset
        if isinstance(self.bucket_name, Unset):
            bucket_name = UNSET
        else:
            bucket_name = self.bucket_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, BucketPatchRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_name is not UNSET:
            field_dict["bucket_name"] = bucket_name
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bucket_patch_request_metadata_type_0 import BucketPatchRequestMetadataType0

        d = dict(src_dict)

        def _parse_bucket_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bucket_name = _parse_bucket_name(d.pop("bucket_name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_metadata(data: object) -> BucketPatchRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = BucketPatchRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BucketPatchRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        bucket_patch_request = cls(
            bucket_name=bucket_name,
            description=description,
            metadata=metadata,
        )

        bucket_patch_request.additional_properties = d
        return bucket_patch_request

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
