from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_upload_request_metadata import CreateUploadRequestMetadata
    from ..models.create_upload_request_object_metadata_type_0 import CreateUploadRequestObjectMetadataType0


T = TypeVar("T", bound="CreateUploadRequest")


@_attrs_define
class CreateUploadRequest:
    r"""Request to generate a presigned URL for direct S3 upload.

    ⚠️  ⚠️  ⚠️  THIS IS THE PRESIGNED URL SYSTEM ⚠️  ⚠️  ⚠️

    This endpoint (POST /buckets/{id}/uploads) is the COMPLETE presigned URL system.
    It handles:
    - ✅ Presigned URL generation (S3 PUT URLs)
    - ✅ Upload tracking and status management
    - ✅ Validation (quotas, file size, content type, schema)
    - ✅ Duplicate detection
    - ✅ Auto object creation on confirmation
    - ✅ Returns upload_id for later reference

    DO NOT CREATE A NEW PRESIGNED UPLOAD ENDPOINT!
    If you need presigned URLs, use this existing system.

    If you think you need a new endpoint:
    1. Check if this system already does it (it probably does)
    2. Extend this system instead of creating redundancy
    3. See api/buckets/uploads/services.py for implementation

    Integration Points:
    - Object creation: Use upload_id in CreateBlobRequest.upload_id field
    - See: shared/buckets/objects/blobs/models.py::CreateBlobRequest
    - See: api/buckets/objects/canonicalization.py::resolve_upload_reference()

    Workflow:
    1. POST /buckets/{id}/uploads → Returns presigned_url + upload_id
    2. PUT presigned_url with file content (client uploads directly to S3)
    3. POST /uploads/{upload_id}/confirm → REQUIRED to finalize upload
    4. Object is created automatically (default behavior)

    ⚠️  IMPORTANT: Step 3 (confirm) is REQUIRED!
    S3 presigned URLs have no callback mechanism - the API cannot detect when
    your upload to S3 completes. You MUST call the confirm endpoint to:
    - Verify the file exists in S3
    - Validate integrity (ETag/size)
    - Create the bucket object
    - Mark upload as COMPLETED

    If you don't confirm:
    - Upload stays in PENDING status forever
    - No object is created
    - File exists in S3 but is orphaned
    - Presigned URL expires (default: 1 hour)

    Use Cases:
        - Simple: Upload → confirm → object created automatically (default)
        - Advanced: Upload multiple files with create_object_on_confirm=false,
          then POST /buckets/{id}/objects with all upload_ids to create one object

    Requirements:
        - filename: REQUIRED, will be validated (no path traversal)
        - content_type: REQUIRED, must be valid MIME type
        - bucket_id: Comes from URL path parameter, not request body
        - All other fields: OPTIONAL with sensible defaults

    Note:
        The bucket_id comes from the URL path (/v1/buckets/{bucket_id}/uploads),
        not from the request body. The bucket is validated before generating presigned URL.

        Attributes:
            filename (str): Name of the file to upload. REQUIRED. Must be a valid filename without path traversal characters
                (../, \). The filename is used to derive the blob_property if not explicitly provided. Examples:
                'product_video.mp4', 'thumbnail.jpg', 'transcript.txt'
            content_type (str): MIME type of the file. REQUIRED. Must be a valid MIME type (e.g., 'video/mp4', 'image/jpeg',
                'application/pdf'). The presigned URL will enforce this content type during upload. Used to validate
                compatibility with bucket schema if create_object_on_confirm=true.
            file_size_bytes (int | None | Unset): Expected file size in bytes. OPTIONAL but RECOMMENDED. If provided, will
                be validated against: 1. Tier-based file size limits (100MB free, 5GB pro, 50GB enterprise) 2. Storage quota
                availability 3. Actual uploaded file size during confirmation. If not provided, quota checking is skipped until
                confirmation.
            presigned_url_expiration (int | Unset): How long the presigned URL is valid, in seconds. OPTIONAL, defaults to
                3600 (1 hour). Valid range: 60 seconds (1 minute) to 86400 seconds (24 hours). After expiration, the URL cannot
                be used and you must request a new one. Recommendation: Use shorter expiration (300-900 seconds) for security-
                sensitive files, longer expiration (3600-7200 seconds) for large files that take time to upload. Default: 3600.
            metadata (CreateUploadRequestMetadata | Unset): Custom metadata for tracking purposes. OPTIONAL. Stored with the
                upload record for filtering and analytics. Does NOT affect the created bucket object (use object_metadata for
                that). Common uses: campaign tracking, user identification, upload source.
            create_object_on_confirm (bool | Unset): Whether to automatically create a bucket object when upload is
                confirmed. OPTIONAL, defaults to TRUE (object is created automatically). If true (default):   - Bucket MUST have
                a schema defined   - blob_property must exist in bucket schema   - content_type must match schema field type   -
                Validation happens BEFORE generating presigned URL   - Object is created automatically on confirmation. If
                false:   - Upload is confirmed but no object is created   - Use this when combining multiple uploads into one
                object   - Reference the upload_id later in POST /buckets/{id}/objects. Default: True.
            object_metadata (CreateUploadRequestObjectMetadataType0 | None | Unset): Metadata to attach to the created
                bucket object. OPTIONAL. Only used if create_object_on_confirm=true. This metadata will be:   1. Validated
                against bucket schema (if keys match schema fields)   2. Attached to the bucket object   3. Passed to downstream
                documents in connected collections. Example: {'priority': 'high', 'category': 'products', 'tags': ['featured']}
            blob_property (None | str | Unset): Property name for the blob in the bucket object. OPTIONAL. Defaults to
                filename without extension (e.g., 'product_video.mp4' → 'product_video'). If create_object_on_confirm=true:   -
                Must exist in bucket schema   - Must be alphanumeric with underscores only   - Will be validated BEFORE
                generating presigned URL. Common values: 'video', 'image', 'thumbnail', 'transcript', 'content'.
            blob_type (None | str | Unset): Type of blob. OPTIONAL. Defaults to type derived from content_type (e.g.,
                'video/mp4' → 'VIDEO'). Must be a valid BucketSchemaFieldType if provided. Valid values: IMAGE, VIDEO, AUDIO,
                TEXT, PDF, DOCUMENT, etc. If create_object_on_confirm=true, will be validated against bucket schema field type.
            file_hash (None | str | Unset): SHA256 hash of the file content for duplicate detection. OPTIONAL. If provided:
                - System checks for existing confirmed uploads with same hash   - If duplicate found and skip_duplicates=true,
                returns existing upload   - Hash will be validated against actual S3 ETag during confirmation. If not provided:
                - Hash is calculated from S3 ETag after upload   - Duplicate detection only happens during confirmation. Use
                case: Pre-calculate hash client-side to avoid uploading duplicates. Format: 64-character hexadecimal string
                (SHA256).
            skip_duplicates (bool | Unset): Skip upload if a file with the same hash already exists. OPTIONAL, defaults to
                TRUE. If true (default):   - If file_hash provided: System checks MongoDB for existing completed upload with
                same hash   - If duplicate found: Returns existing upload details WITHOUT generating new presigned URL   - If
                file_hash NOT provided: Duplicate check happens during confirmation using S3 ETag   - Saves bandwidth, storage,
                and upload time by reusing existing files. If false:   - Always generates new presigned URL even if file already
                uploaded   - Creates separate upload record for same file content   - Useful when you need distinct upload
                tracking for identical files. Recommendation: Keep default (true) unless you specifically need multiple upload
                records for same file. Default: True.
    """

    filename: str
    content_type: str
    file_size_bytes: int | None | Unset = UNSET
    presigned_url_expiration: int | Unset = 3600
    metadata: CreateUploadRequestMetadata | Unset = UNSET
    create_object_on_confirm: bool | Unset = True
    object_metadata: CreateUploadRequestObjectMetadataType0 | None | Unset = UNSET
    blob_property: None | str | Unset = UNSET
    blob_type: None | str | Unset = UNSET
    file_hash: None | str | Unset = UNSET
    skip_duplicates: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_upload_request_object_metadata_type_0 import CreateUploadRequestObjectMetadataType0

        filename = self.filename

        content_type = self.content_type

        file_size_bytes: int | None | Unset
        if isinstance(self.file_size_bytes, Unset):
            file_size_bytes = UNSET
        else:
            file_size_bytes = self.file_size_bytes

        presigned_url_expiration = self.presigned_url_expiration

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        create_object_on_confirm = self.create_object_on_confirm

        object_metadata: dict[str, Any] | None | Unset
        if isinstance(self.object_metadata, Unset):
            object_metadata = UNSET
        elif isinstance(self.object_metadata, CreateUploadRequestObjectMetadataType0):
            object_metadata = self.object_metadata.to_dict()
        else:
            object_metadata = self.object_metadata

        blob_property: None | str | Unset
        if isinstance(self.blob_property, Unset):
            blob_property = UNSET
        else:
            blob_property = self.blob_property

        blob_type: None | str | Unset
        if isinstance(self.blob_type, Unset):
            blob_type = UNSET
        else:
            blob_type = self.blob_type

        file_hash: None | str | Unset
        if isinstance(self.file_hash, Unset):
            file_hash = UNSET
        else:
            file_hash = self.file_hash

        skip_duplicates = self.skip_duplicates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filename": filename,
                "content_type": content_type,
            }
        )
        if file_size_bytes is not UNSET:
            field_dict["file_size_bytes"] = file_size_bytes
        if presigned_url_expiration is not UNSET:
            field_dict["presigned_url_expiration"] = presigned_url_expiration
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if create_object_on_confirm is not UNSET:
            field_dict["create_object_on_confirm"] = create_object_on_confirm
        if object_metadata is not UNSET:
            field_dict["object_metadata"] = object_metadata
        if blob_property is not UNSET:
            field_dict["blob_property"] = blob_property
        if blob_type is not UNSET:
            field_dict["blob_type"] = blob_type
        if file_hash is not UNSET:
            field_dict["file_hash"] = file_hash
        if skip_duplicates is not UNSET:
            field_dict["skip_duplicates"] = skip_duplicates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_upload_request_metadata import CreateUploadRequestMetadata
        from ..models.create_upload_request_object_metadata_type_0 import CreateUploadRequestObjectMetadataType0

        d = dict(src_dict)
        filename = d.pop("filename")

        content_type = d.pop("content_type")

        def _parse_file_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size_bytes = _parse_file_size_bytes(d.pop("file_size_bytes", UNSET))

        presigned_url_expiration = d.pop("presigned_url_expiration", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateUploadRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateUploadRequestMetadata.from_dict(_metadata)

        create_object_on_confirm = d.pop("create_object_on_confirm", UNSET)

        def _parse_object_metadata(data: object) -> CreateUploadRequestObjectMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                object_metadata_type_0 = CreateUploadRequestObjectMetadataType0.from_dict(data)

                return object_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateUploadRequestObjectMetadataType0 | None | Unset, data)

        object_metadata = _parse_object_metadata(d.pop("object_metadata", UNSET))

        def _parse_blob_property(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        blob_property = _parse_blob_property(d.pop("blob_property", UNSET))

        def _parse_blob_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        blob_type = _parse_blob_type(d.pop("blob_type", UNSET))

        def _parse_file_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_hash = _parse_file_hash(d.pop("file_hash", UNSET))

        skip_duplicates = d.pop("skip_duplicates", UNSET)

        create_upload_request = cls(
            filename=filename,
            content_type=content_type,
            file_size_bytes=file_size_bytes,
            presigned_url_expiration=presigned_url_expiration,
            metadata=metadata,
            create_object_on_confirm=create_object_on_confirm,
            object_metadata=object_metadata,
            blob_property=blob_property,
            blob_type=blob_type,
            file_hash=file_hash,
            skip_duplicates=skip_duplicates,
        )

        create_upload_request.additional_properties = d
        return create_upload_request

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
