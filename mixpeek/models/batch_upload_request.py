from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_upload_request_shared_metadata_type_0 import BatchUploadRequestSharedMetadataType0
    from ..models.batch_upload_request_shared_object_metadata_type_0 import BatchUploadRequestSharedObjectMetadataType0
    from ..models.create_upload_request import CreateUploadRequest


T = TypeVar("T", bound="BatchUploadRequest")


@_attrs_define
class BatchUploadRequest:
    """Request to generate multiple presigned URLs in a single request.

    Attributes:
        uploads (list[CreateUploadRequest]): List of upload requests (max 100)
        shared_metadata (BatchUploadRequestSharedMetadataType0 | None | Unset): Metadata to apply to all uploads (merged
            with individual metadata)
        shared_object_metadata (BatchUploadRequestSharedObjectMetadataType0 | None | Unset): Object metadata to apply to
            all uploads (merged with individual)
    """

    uploads: list[CreateUploadRequest]
    shared_metadata: BatchUploadRequestSharedMetadataType0 | None | Unset = UNSET
    shared_object_metadata: BatchUploadRequestSharedObjectMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_upload_request_shared_metadata_type_0 import BatchUploadRequestSharedMetadataType0
        from ..models.batch_upload_request_shared_object_metadata_type_0 import (
            BatchUploadRequestSharedObjectMetadataType0,
        )

        uploads = []
        for uploads_item_data in self.uploads:
            uploads_item = uploads_item_data.to_dict()
            uploads.append(uploads_item)

        shared_metadata: dict[str, Any] | None | Unset
        if isinstance(self.shared_metadata, Unset):
            shared_metadata = UNSET
        elif isinstance(self.shared_metadata, BatchUploadRequestSharedMetadataType0):
            shared_metadata = self.shared_metadata.to_dict()
        else:
            shared_metadata = self.shared_metadata

        shared_object_metadata: dict[str, Any] | None | Unset
        if isinstance(self.shared_object_metadata, Unset):
            shared_object_metadata = UNSET
        elif isinstance(self.shared_object_metadata, BatchUploadRequestSharedObjectMetadataType0):
            shared_object_metadata = self.shared_object_metadata.to_dict()
        else:
            shared_object_metadata = self.shared_object_metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploads": uploads,
            }
        )
        if shared_metadata is not UNSET:
            field_dict["shared_metadata"] = shared_metadata
        if shared_object_metadata is not UNSET:
            field_dict["shared_object_metadata"] = shared_object_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_upload_request_shared_metadata_type_0 import BatchUploadRequestSharedMetadataType0
        from ..models.batch_upload_request_shared_object_metadata_type_0 import (
            BatchUploadRequestSharedObjectMetadataType0,
        )
        from ..models.create_upload_request import CreateUploadRequest

        d = dict(src_dict)
        uploads = []
        _uploads = d.pop("uploads")
        for uploads_item_data in _uploads:
            uploads_item = CreateUploadRequest.from_dict(uploads_item_data)

            uploads.append(uploads_item)

        def _parse_shared_metadata(data: object) -> BatchUploadRequestSharedMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shared_metadata_type_0 = BatchUploadRequestSharedMetadataType0.from_dict(data)

                return shared_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchUploadRequestSharedMetadataType0 | None | Unset, data)

        shared_metadata = _parse_shared_metadata(d.pop("shared_metadata", UNSET))

        def _parse_shared_object_metadata(data: object) -> BatchUploadRequestSharedObjectMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shared_object_metadata_type_0 = BatchUploadRequestSharedObjectMetadataType0.from_dict(data)

                return shared_object_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchUploadRequestSharedObjectMetadataType0 | None | Unset, data)

        shared_object_metadata = _parse_shared_object_metadata(d.pop("shared_object_metadata", UNSET))

        batch_upload_request = cls(
            uploads=uploads,
            shared_metadata=shared_metadata,
            shared_object_metadata=shared_object_metadata,
        )

        batch_upload_request.additional_properties = d
        return batch_upload_request

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
