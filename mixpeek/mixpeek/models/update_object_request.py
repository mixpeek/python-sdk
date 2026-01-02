from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_blob_request import CreateBlobRequest
    from ..models.update_object_request_metadata_type_0 import UpdateObjectRequestMetadataType0


T = TypeVar("T", bound="UpdateObjectRequest")


@_attrs_define
class UpdateObjectRequest:
    """Request model for updating an existing bucket object.

    Attributes:
        key_prefix (None | str | Unset): Updated storage key/path prefix of the object, this will be used to retrieve
            the object from the storage. It's at the root of the object.
        blobs (list[CreateBlobRequest] | None | Unset): List of new or updated blobs for this object
        metadata (None | Unset | UpdateObjectRequestMetadataType0): Updated metadata for the object, this will be merged
            with existing metadata.
        skip_duplicates (bool | None | Unset): Skip duplicate blobs, if a blob with the same hash already exists, it
            will be skipped.
    """

    key_prefix: None | str | Unset = UNSET
    blobs: list[CreateBlobRequest] | None | Unset = UNSET
    metadata: None | Unset | UpdateObjectRequestMetadataType0 = UNSET
    skip_duplicates: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_object_request_metadata_type_0 import UpdateObjectRequestMetadataType0

        key_prefix: None | str | Unset
        if isinstance(self.key_prefix, Unset):
            key_prefix = UNSET
        else:
            key_prefix = self.key_prefix

        blobs: list[dict[str, Any]] | None | Unset
        if isinstance(self.blobs, Unset):
            blobs = UNSET
        elif isinstance(self.blobs, list):
            blobs = []
            for blobs_type_0_item_data in self.blobs:
                blobs_type_0_item = blobs_type_0_item_data.to_dict()
                blobs.append(blobs_type_0_item)

        else:
            blobs = self.blobs

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, UpdateObjectRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        skip_duplicates: bool | None | Unset
        if isinstance(self.skip_duplicates, Unset):
            skip_duplicates = UNSET
        else:
            skip_duplicates = self.skip_duplicates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_prefix is not UNSET:
            field_dict["key_prefix"] = key_prefix
        if blobs is not UNSET:
            field_dict["blobs"] = blobs
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if skip_duplicates is not UNSET:
            field_dict["skip_duplicates"] = skip_duplicates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_blob_request import CreateBlobRequest
        from ..models.update_object_request_metadata_type_0 import UpdateObjectRequestMetadataType0

        d = dict(src_dict)

        def _parse_key_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_prefix = _parse_key_prefix(d.pop("key_prefix", UNSET))

        def _parse_blobs(data: object) -> list[CreateBlobRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blobs_type_0 = []
                _blobs_type_0 = data
                for blobs_type_0_item_data in _blobs_type_0:
                    blobs_type_0_item = CreateBlobRequest.from_dict(blobs_type_0_item_data)

                    blobs_type_0.append(blobs_type_0_item)

                return blobs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CreateBlobRequest] | None | Unset, data)

        blobs = _parse_blobs(d.pop("blobs", UNSET))

        def _parse_metadata(data: object) -> None | Unset | UpdateObjectRequestMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = UpdateObjectRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateObjectRequestMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_skip_duplicates(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_duplicates = _parse_skip_duplicates(d.pop("skip_duplicates", UNSET))

        update_object_request = cls(
            key_prefix=key_prefix,
            blobs=blobs,
            metadata=metadata,
            skip_duplicates=skip_duplicates,
        )

        update_object_request.additional_properties = d
        return update_object_request

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
