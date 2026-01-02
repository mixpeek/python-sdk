from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bucket_schema_field_type import BucketSchemaFieldType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_blob_request_data_type_5 import CreateBlobRequestDataType5
    from ..models.create_blob_request_metadata_type_0 import CreateBlobRequestMetadataType0


T = TypeVar("T", bound="CreateBlobRequest")


@_attrs_define
class CreateBlobRequest:
    """Request model for creating a new blob.

    ⚠️  IMPORTANT: For presigned URL uploads, use the existing /buckets/{id}/uploads system!
        DO NOT create a new presigned upload endpoint - one already exists.

    Supports two modes:

    Mode 1: Direct Data Upload
        - Provide 'data' field with URL or base64 content
        - File is processed immediately during object creation
        - Use for: Small files, public URLs, inline data

    Mode 2: Upload Reference (Recommended for large files)
        - First: POST /buckets/{id}/uploads → Returns presigned_url + upload_id
        - User uploads file directly to S3 via presigned_url
        - Then: POST /uploads/{upload_id}/confirm → Validates upload
        - Finally: Reference upload_id in this blob request
        - Use for: Large files, client-side uploads, multi-blob objects

    Why upload_id?
        - Combine multiple uploads into one object
        - Upload files in parallel, create object later
        - Reuse uploads across multiple objects
        - Better UX: upload progress, retry logic, validation

    Related Endpoints:
        - POST /buckets/{id}/uploads - Generate presigned URLs (EXISTING SYSTEM)
        - POST /uploads/{id}/confirm - Confirm upload completed
        - See: api/buckets/uploads/services.py for full upload workflow

    Examples:
        # Direct data (simple)
        {
          "property": "thumbnail",
          "type": "IMAGE",
          "data": "https://example.com/image.jpg"
        }

        # Upload reference (recommended)
        {
          "property": "video",
          "type": "VIDEO",
          "upload_id": "upl_abc123"  # From /uploads endpoint
        }

        # Multiple uploads → one object
        {
          "blobs": [
            {"property": "video", "upload_id": "upl_video123"},
            {"property": "thumbnail", "upload_id": "upl_thumb456"},
            {"property": "transcript", "upload_id": "upl_trans789"}
          ]
        }

        Attributes:
            property_ (str): REQUIRED. Property name from the bucket schema that this blob belongs to. Must match a field
                defined in the bucket's schema. Used to validate blob type compatibility and determine storage path. Common
                values: 'video', 'thumbnail', 'transcript', 'document', 'image'
            type_ (BucketSchemaFieldType): Supported data types for bucket schema fields.

                Types fall into two categories:

                1. **Metadata Types** (JSON types):
                   - Stored as object metadata
                   - Standard JSON-compatible types
                   - Not processed by extractors (unless explicitly mapped)
                   - Examples: string, number, boolean, date

                2. **File Types** (blobs):
                   - Stored as files/blobs
                   - Processed by extractors
                   - Require file content (URL or base64)
                   - Examples: text, image, video, pdf

                **GIF Special Handling**:
                    GIF files can be declared as either IMAGE or VIDEO type:

                    - As IMAGE: GIF is embedded as a single static image (first frame)
                    - As VIDEO: GIF is decomposed frame-by-frame with embeddings per frame

                    The multimodal extractor detects GIFs via MIME type (image/gif) and routes
                    them based on your schema declaration. Use VIDEO for animated GIFs where
                    frame-level search is needed, IMAGE for static/thumbnail use cases.

                NOTE: For retriever input schemas that need to accept document references
                (e.g., "find similar documents"), use RetrieverInputSchemaFieldType instead,
                which includes all bucket types plus document_reference.
            key_prefix (None | str | Unset): OPTIONAL. Storage path prefix for organizing blobs within the bucket. If not
                provided, uses default bucket organization. Use for: grouping blobs by campaign, date, category, etc. Example:
                'campaigns/summer_2025' or 'products/electronics'
            data (bool | CreateBlobRequestDataType5 | float | int | list[Any] | None | str | Unset): EITHER data OR
                upload_id must be provided (mutually exclusive).

                File data in one of several INTERCHANGEABLE formats:

                **Format 1: URL String (HTTP/HTTPS/S3)** - Direct URL to file on the web or in S3 - Examples:
                'https://example.com/video.mp4', 's3://bucket/key' - Use for: Public files, existing S3 objects, pre-signed URLs
                - File is downloaded and uploaded to internal S3 (if canonicalize_source=True)

                **Format 2: Data URI String (base64)** - Self-contained base64 data with MIME type - Format:
                'data:<mime_type>;base64,<encoded_data>' - Example: 'data:image/jpeg;base64,/9j/4AAQSkZJRg...' - Use for: Small
                files (<5MB), mobile uploads, inline test data - MIME type automatically extracted from URI - Data is decoded,
                validated, and uploaded to S3 automatically

                **Format 3: Base64 Dictionary** - Structured format with explicit metadata - Required keys: 'base64' (encoded
                data) - Optional keys: 'mime_type', 'filename' - Example: {'base64': '/9j/4AAQ...', 'mime_type': 'image/jpeg',
                'filename': 'photo.jpg'} - Use for: When you need explicit MIME type control - Data is decoded, validated, and
                uploaded to S3 automatically

                **Format 4: URL Dictionary** - Structured format for URL references - Required keys: 'url' - Example: {'url':
                'https://example.com/file.jpg'} - Use for: Consistency with other dict formats

                **Processing:** All formats are converted to internal S3 URLs before storage. The engine always receives S3 URLs
                regardless of input format.

                **Size Limits (Base64 only):** Base64 data: 5MB (free), 10MB (pro), 50MB (enterprise). URLs: No limit
                (downloaded on-demand). For files exceeding limits, use presigned upload workflow: POST /buckets/{id}/uploads

                **Validation:** - Base64: Encoding validated, MIME type detected, size checked - URLs: Accessibility verified,
                content-type validated - All: Schema type compatibility enforced
            upload_id (None | str | Unset): EITHER upload_id OR data must be provided. Reference to an existing upload from
                the presigned URL workflow.

                ⚠️  PRESIGNED URLS: Use existing POST /buckets/{id}/uploads endpoint! It already handles presigned URL
                generation, upload tracking, and validation. DO NOT create a new /presigned-upload endpoint - it's redundant.

                Workflow: 1. POST /buckets/{id}/uploads → {upload_id, presigned_url} 2. User uploads file to presigned_url 3.
                POST /uploads/{upload_id}/confirm → Validates upload 4. Use upload_id here to reference the uploaded file

                The upload must be in CONFIRMED or ACTIVE status. Format: 'upl_' prefix followed by alphanumeric characters.

                Use Cases: - Combine multiple uploads into one object - Upload files in parallel, create object later - Reuse
                same upload across multiple objects

                See: api/buckets/uploads/ for the complete upload system
            metadata (CreateBlobRequestMetadataType0 | None | Unset): Metadata for the blob, this will only be applied to
                the documents that use this blob
            canonicalize_source (bool | None | Unset): If set, override object-level default to control source
                canonicalization for this blob.
            force_remirror (bool | None | Unset): If set, override object-level default to force re-upload even if an
                identical blob exists.
    """

    property_: str
    type_: BucketSchemaFieldType
    key_prefix: None | str | Unset = UNSET
    data: bool | CreateBlobRequestDataType5 | float | int | list[Any] | None | str | Unset = UNSET
    upload_id: None | str | Unset = UNSET
    metadata: CreateBlobRequestMetadataType0 | None | Unset = UNSET
    canonicalize_source: bool | None | Unset = UNSET
    force_remirror: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_blob_request_data_type_5 import CreateBlobRequestDataType5
        from ..models.create_blob_request_metadata_type_0 import CreateBlobRequestMetadataType0

        property_ = self.property_

        type_ = self.type_.value

        key_prefix: None | str | Unset
        if isinstance(self.key_prefix, Unset):
            key_prefix = UNSET
        else:
            key_prefix = self.key_prefix

        data: bool | dict[str, Any] | float | int | list[Any] | None | str | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, CreateBlobRequestDataType5):
            data = self.data.to_dict()
        elif isinstance(self.data, list):
            data = self.data

        else:
            data = self.data

        upload_id: None | str | Unset
        if isinstance(self.upload_id, Unset):
            upload_id = UNSET
        else:
            upload_id = self.upload_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CreateBlobRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        canonicalize_source: bool | None | Unset
        if isinstance(self.canonicalize_source, Unset):
            canonicalize_source = UNSET
        else:
            canonicalize_source = self.canonicalize_source

        force_remirror: bool | None | Unset
        if isinstance(self.force_remirror, Unset):
            force_remirror = UNSET
        else:
            force_remirror = self.force_remirror

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "property": property_,
                "type": type_,
            }
        )
        if key_prefix is not UNSET:
            field_dict["key_prefix"] = key_prefix
        if data is not UNSET:
            field_dict["data"] = data
        if upload_id is not UNSET:
            field_dict["upload_id"] = upload_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if canonicalize_source is not UNSET:
            field_dict["canonicalize_source"] = canonicalize_source
        if force_remirror is not UNSET:
            field_dict["force_remirror"] = force_remirror

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_blob_request_data_type_5 import CreateBlobRequestDataType5
        from ..models.create_blob_request_metadata_type_0 import CreateBlobRequestMetadataType0

        d = dict(src_dict)
        property_ = d.pop("property")

        type_ = BucketSchemaFieldType(d.pop("type"))

        def _parse_key_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_prefix = _parse_key_prefix(d.pop("key_prefix", UNSET))

        def _parse_data(
            data: object,
        ) -> bool | CreateBlobRequestDataType5 | float | int | list[Any] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_5 = CreateBlobRequestDataType5.from_dict(data)

                return data_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_6 = cast(list[Any], data)

                return data_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | CreateBlobRequestDataType5 | float | int | list[Any] | None | str | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_upload_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_id = _parse_upload_id(d.pop("upload_id", UNSET))

        def _parse_metadata(data: object) -> CreateBlobRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CreateBlobRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateBlobRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_canonicalize_source(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        canonicalize_source = _parse_canonicalize_source(d.pop("canonicalize_source", UNSET))

        def _parse_force_remirror(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force_remirror = _parse_force_remirror(d.pop("force_remirror", UNSET))

        create_blob_request = cls(
            property_=property_,
            type_=type_,
            key_prefix=key_prefix,
            data=data,
            upload_id=upload_id,
            metadata=metadata,
            canonicalize_source=canonicalize_source,
            force_remirror=force_remirror,
        )

        create_blob_request.additional_properties = d
        return create_blob_request

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
