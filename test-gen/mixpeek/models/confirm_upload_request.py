from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfirmUploadRequest")


@_attrs_define
class ConfirmUploadRequest:
    """Request to confirm S3 upload completion and create bucket object.

    ⚠️  THIS ENDPOINT IS REQUIRED AFTER UPLOADING TO S3!

    S3 presigned URLs have no callback mechanism - the API cannot detect when
    your upload completes. You MUST call this endpoint to finalize the upload.

    Why confirmation is required:
        - S3 doesn't notify us when uploads complete
        - We need to verify the file actually exists in S3
        - We need to create the bucket object
        - We need to update quotas and tracking

    The system will:
    1. Verify the S3 object exists (HeadObject call)
    2. Validate ETag matches (if provided) - RECOMMENDED for integrity
    3. Validate file size matches (if provided)
    4. Create bucket object (default, unless create_object_on_confirm=false)
    5. Update upload status to COMPLETED

    If you don't call confirm:
        - Upload stays in PENDING status
        - No bucket object is created
        - File is orphaned in S3

        Attributes:
            etag (None | str | Unset): S3 ETag returned from the upload. OPTIONAL but RECOMMENDED. After uploading to S3,
                the response includes an ETag header. Providing this ensures the file wasn't corrupted during upload. If
                provided and doesn't match S3's ETag, confirmation will fail with error. Format: Usually an MD5 hash, may be
                enclosed in quotes.
            file_size_bytes (int | None | Unset): Actual file size uploaded, in bytes. OPTIONAL but RECOMMENDED. If
                provided, will be validated against the actual S3 object size. Mismatch indicates upload corruption or network
                issues. If not provided, size validation is skipped.
    """

    etag: None | str | Unset = UNSET
    file_size_bytes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        etag: None | str | Unset
        if isinstance(self.etag, Unset):
            etag = UNSET
        else:
            etag = self.etag

        file_size_bytes: int | None | Unset
        if isinstance(self.file_size_bytes, Unset):
            file_size_bytes = UNSET
        else:
            file_size_bytes = self.file_size_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if etag is not UNSET:
            field_dict["etag"] = etag
        if file_size_bytes is not UNSET:
            field_dict["file_size_bytes"] = file_size_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_etag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        etag = _parse_etag(d.pop("etag", UNSET))

        def _parse_file_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size_bytes = _parse_file_size_bytes(d.pop("file_size_bytes", UNSET))

        confirm_upload_request = cls(
            etag=etag,
            file_size_bytes=file_size_bytes,
        )

        confirm_upload_request.additional_properties = d
        return confirm_upload_request

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
