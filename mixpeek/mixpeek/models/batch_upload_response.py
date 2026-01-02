from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.upload_response import UploadResponse


T = TypeVar("T", bound="BatchUploadResponse")


@_attrs_define
class BatchUploadResponse:
    """Response from batch upload request.

    Attributes:
        uploads (list[UploadResponse]): Generated uploads with presigned URLs
        total (int): Total number of uploads created
    """

    uploads: list[UploadResponse]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uploads = []
        for uploads_item_data in self.uploads:
            uploads_item = uploads_item_data.to_dict()
            uploads.append(uploads_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploads": uploads,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_response import UploadResponse

        d = dict(src_dict)
        uploads = []
        _uploads = d.pop("uploads")
        for uploads_item_data in _uploads:
            uploads_item = UploadResponse.from_dict(uploads_item_data)

            uploads.append(uploads_item)

        total = d.pop("total")

        batch_upload_response = cls(
            uploads=uploads,
            total=total,
        )

        batch_upload_response.additional_properties = d
        return batch_upload_response

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
