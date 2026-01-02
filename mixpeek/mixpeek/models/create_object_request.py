from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_blob_request import CreateBlobRequest


T = TypeVar("T", bound="CreateObjectRequest")


@_attrs_define
class CreateObjectRequest:
    """Request model for creating a bucket object.

    Objects can be created with blobs from two sources:
    1. Direct data (URLs, base64) - Use CreateBlobRequest.data field
    2. Upload references - Use CreateBlobRequest.upload_id field (from POST /buckets/{id}/uploads)

    Upload Reference Workflow:
        For large files or client-side uploads, use the presigned URL workflow:
        1. POST /buckets/{id}/uploads → Returns {upload_id, presigned_url}
        2. User uploads file to presigned_url (client-side)
        3. POST /uploads/{upload_id}/confirm → Validates upload
        4. POST /buckets/{id}/objects with upload_id in blobs (this endpoint)

    Use Cases:
        - Single blob with direct data (simple)
        - Multiple blobs from presigned uploads (recommended for large files)
        - Mix of direct data and upload references
        - Combine multiple uploads into one object

    See Also:
        - CreateBlobRequest for blob field documentation
        - POST /buckets/{id}/uploads for presigned URL generation

        Example:
            {'blobs': [{'data': {'num_pages': 5, 'title': 'Service Agreement 2024'}, 'key_prefix':
                '/contract-2024/content.pdf', 'metadata': {'author': 'John Doe', 'department': 'Legal'}, 'property': 'content',
                'type': 'json'}, {'data': {'filename': 'https://example.com/images/smartphone-x1.jpg', 'mime_type':
                'image/jpeg'}, 'key_prefix': '/contract-2024/thumbnail.jpg', 'metadata': {'height': 300, 'width': 200},
                'property': 'thumbnail', 'type': 'image'}], 'key_prefix': '/documents', 'metadata': {'category': 'contracts',
                'status': 'draft', 'year': 2024}}

        Attributes:
            key_prefix (None | str | Unset): Storage key/path prefix of the object, this will be used to retrieve the object
                from the storage. It's at the root of the object. Example: /contract-2024.
            blobs (list[CreateBlobRequest] | Unset): List of blobs to be created in this object Example: [{'data':
                {'num_pages': 5, 'title': 'Service Agreement 2024'}, 'key_prefix': '/content.pdf', 'metadata': {'author': 'John
                Doe', 'department': 'Legal'}, 'property': 'content', 'type': 'PDF'}].
            skip_duplicates (bool | Unset): Skip duplicate blobs, if a blob with the same hash already exists, it will be
                skipped. Default: False.
            canonicalize_source (bool | Unset): Mirror non-S3 sources into internal S3 and reference canonically. Default:
                True.
            force_remirror (bool | Unset): Force re-upload to S3 even if a blob with identical content already exists.
                Default: False.
    """

    key_prefix: None | str | Unset = UNSET
    blobs: list[CreateBlobRequest] | Unset = UNSET
    skip_duplicates: bool | Unset = False
    canonicalize_source: bool | Unset = True
    force_remirror: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_prefix: None | str | Unset
        if isinstance(self.key_prefix, Unset):
            key_prefix = UNSET
        else:
            key_prefix = self.key_prefix

        blobs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.blobs, Unset):
            blobs = []
            for blobs_item_data in self.blobs:
                blobs_item = blobs_item_data.to_dict()
                blobs.append(blobs_item)

        skip_duplicates = self.skip_duplicates

        canonicalize_source = self.canonicalize_source

        force_remirror = self.force_remirror

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_prefix is not UNSET:
            field_dict["key_prefix"] = key_prefix
        if blobs is not UNSET:
            field_dict["blobs"] = blobs
        if skip_duplicates is not UNSET:
            field_dict["skip_duplicates"] = skip_duplicates
        if canonicalize_source is not UNSET:
            field_dict["canonicalize_source"] = canonicalize_source
        if force_remirror is not UNSET:
            field_dict["force_remirror"] = force_remirror

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_blob_request import CreateBlobRequest

        d = dict(src_dict)

        def _parse_key_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_prefix = _parse_key_prefix(d.pop("key_prefix", UNSET))

        _blobs = d.pop("blobs", UNSET)
        blobs: list[CreateBlobRequest] | Unset = UNSET
        if _blobs is not UNSET:
            blobs = []
            for blobs_item_data in _blobs:
                blobs_item = CreateBlobRequest.from_dict(blobs_item_data)

                blobs.append(blobs_item)

        skip_duplicates = d.pop("skip_duplicates", UNSET)

        canonicalize_source = d.pop("canonicalize_source", UNSET)

        force_remirror = d.pop("force_remirror", UNSET)

        create_object_request = cls(
            key_prefix=key_prefix,
            blobs=blobs,
            skip_duplicates=skip_duplicates,
            canonicalize_source=canonicalize_source,
            force_remirror=force_remirror,
        )

        create_object_request.additional_properties = d
        return create_object_request

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
