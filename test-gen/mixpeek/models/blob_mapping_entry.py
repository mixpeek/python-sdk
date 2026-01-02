from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blob_type import BlobType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_source import ColumnSource
    from ..models.constant_source import ConstantSource
    from ..models.drive_property_source import DrivePropertySource
    from ..models.file_source import FileSource
    from ..models.filename_regex_source import FilenameRegexSource
    from ..models.folder_path_source import FolderPathSource
    from ..models.s3_metadata_source import S3MetadataSource
    from ..models.s3_tag_source import S3TagSource


T = TypeVar("T", bound="BlobMappingEntry")


@_attrs_define
class BlobMappingEntry:
    """Maps a source to a blob in the bucket object.

    Used for mapping files or URL references to blob fields. The blob_type
    determines how the content is processed by extractors. This is the
    primary way to map synced files into the Mixpeek extraction pipeline.

    Example: Map the synced file to the primary "content" blob
        {
            "target_type": "blob",
            "source": {"type": "file"},
            "blob_type": "auto",
            "blob_property": "content"
        }

    Example: Map a database column URL to an image blob
        {
            "target_type": "blob",
            "source": {"type": "column", "name": "AVATAR_URL"},
            "blob_type": "image",
            "blob_property": "profile_image"
        }

    Example: Map with explicit mime_type override
        {
            "target_type": "blob",
            "source": {"type": "file"},
            "blob_type": "video",
            "blob_property": "content",
            "mime_type_override": "video/mp4"
        }

    Attributes:
        target_type: Must be "blob" for blob mappings
        source: The source extractor (usually "file" for synced content)
        blob_type: Content type hint for extractors (auto, image, video, etc.)
        blob_property: Name of the blob property in the bucket schema
        mime_type_override: Optional explicit mime_type to use

        Attributes:
            source (ColumnSource | ConstantSource | DrivePropertySource | FilenameRegexSource | FileSource |
                FolderPathSource | S3MetadataSource | S3TagSource): Source extractor defining where to get the blob content or
                URL. Use 'file' for the synced file itself (most common). Use 'column' for database URL columns pointing to
                external content. Use 'metadata' for S3 metadata containing URLs.
            target_type (Literal['blob'] | Unset): Target type. Must be 'blob' for blob mappings. Default: 'blob'.
            blob_type (BlobType | Unset): Type of blob content for schema mapping.

                Determines how the blob content is processed and what extractors can operate on it.
                This is critical for the extraction pipeline to route content correctly.

                Values:
                    auto: Automatically infer blob type from mime_type (recommended for files)
                    image: Image files (JPEG, PNG, WebP, BMP, TIFF, or GIF as static)
                    video: Video files (MP4, MOV, WebM, AVI, MKV, or GIF as animated frames)
                    audio: Audio files (MP3, WAV, FLAC, AAC, OGG)
                    text: Text files (TXT, MD, HTML, XML)
                    pdf: PDF documents
                    excel: Spreadsheet files (XLSX, XLS, CSV)

                **GIF Special Handling**:
                    GIF files are unique - they can be processed as either IMAGE or VIDEO:

                    - As IMAGE: Single static embedding (first frame), no decomposition
                    - As VIDEO: Frame-by-frame decomposition with per-frame embeddings

                    When using "auto", GIFs default to IMAGE. To get frame-level processing
                    for animated GIFs, explicitly set blob_type to VIDEO.

                Usage Guidelines:
                    - Use "auto" when syncing files with accurate mime_type headers
                    - Use explicit types when mime_type is missing or unreliable
                    - Use "video" for animated GIFs requiring frame-level search
            blob_property (str | Unset): The blob property name in the bucket schema. This identifies which blob in the
                object's blobs array. Default: 'content' (the primary blob). Must match a blob property defined in the bucket
                schema. Default: 'content'.
            mime_type_override (None | str | Unset): Optional mime_type to use instead of auto-detection. Useful when the
                source doesn't provide accurate mime_type. Format: 'type/subtype' (e.g., 'image/jpeg', 'video/mp4'). When set,
                this value is used for blob.details.mime_type.
    """

    source: (
        ColumnSource
        | ConstantSource
        | DrivePropertySource
        | FilenameRegexSource
        | FileSource
        | FolderPathSource
        | S3MetadataSource
        | S3TagSource
    )
    target_type: Literal["blob"] | Unset = "blob"
    blob_type: BlobType | Unset = UNSET
    blob_property: str | Unset = "content"
    mime_type_override: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.column_source import ColumnSource
        from ..models.drive_property_source import DrivePropertySource
        from ..models.file_source import FileSource
        from ..models.filename_regex_source import FilenameRegexSource
        from ..models.folder_path_source import FolderPathSource
        from ..models.s3_metadata_source import S3MetadataSource
        from ..models.s3_tag_source import S3TagSource

        source: dict[str, Any]
        if isinstance(self.source, S3TagSource):
            source = self.source.to_dict()
        elif isinstance(self.source, S3MetadataSource):
            source = self.source.to_dict()
        elif isinstance(self.source, FilenameRegexSource):
            source = self.source.to_dict()
        elif isinstance(self.source, ColumnSource):
            source = self.source.to_dict()
        elif isinstance(self.source, DrivePropertySource):
            source = self.source.to_dict()
        elif isinstance(self.source, FolderPathSource):
            source = self.source.to_dict()
        elif isinstance(self.source, FileSource):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()

        target_type = self.target_type

        blob_type: str | Unset = UNSET
        if not isinstance(self.blob_type, Unset):
            blob_type = self.blob_type.value

        blob_property = self.blob_property

        mime_type_override: None | str | Unset
        if isinstance(self.mime_type_override, Unset):
            mime_type_override = UNSET
        else:
            mime_type_override = self.mime_type_override

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
            }
        )
        if target_type is not UNSET:
            field_dict["target_type"] = target_type
        if blob_type is not UNSET:
            field_dict["blob_type"] = blob_type
        if blob_property is not UNSET:
            field_dict["blob_property"] = blob_property
        if mime_type_override is not UNSET:
            field_dict["mime_type_override"] = mime_type_override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.column_source import ColumnSource
        from ..models.constant_source import ConstantSource
        from ..models.drive_property_source import DrivePropertySource
        from ..models.file_source import FileSource
        from ..models.filename_regex_source import FilenameRegexSource
        from ..models.folder_path_source import FolderPathSource
        from ..models.s3_metadata_source import S3MetadataSource
        from ..models.s3_tag_source import S3TagSource

        d = dict(src_dict)

        def _parse_source(
            data: object,
        ) -> (
            ColumnSource
            | ConstantSource
            | DrivePropertySource
            | FilenameRegexSource
            | FileSource
            | FolderPathSource
            | S3MetadataSource
            | S3TagSource
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_0 = S3TagSource.from_dict(data)

                return source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_1 = S3MetadataSource.from_dict(data)

                return source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_2 = FilenameRegexSource.from_dict(data)

                return source_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_3 = ColumnSource.from_dict(data)

                return source_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_4 = DrivePropertySource.from_dict(data)

                return source_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_5 = FolderPathSource.from_dict(data)

                return source_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_6 = FileSource.from_dict(data)

                return source_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            source_type_7 = ConstantSource.from_dict(data)

            return source_type_7

        source = _parse_source(d.pop("source"))

        target_type = cast(Literal["blob"] | Unset, d.pop("target_type", UNSET))
        if target_type != "blob" and not isinstance(target_type, Unset):
            raise ValueError(f"target_type must match const 'blob', got '{target_type}'")

        _blob_type = d.pop("blob_type", UNSET)
        blob_type: BlobType | Unset
        if isinstance(_blob_type, Unset):
            blob_type = UNSET
        else:
            blob_type = BlobType(_blob_type)

        blob_property = d.pop("blob_property", UNSET)

        def _parse_mime_type_override(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mime_type_override = _parse_mime_type_override(d.pop("mime_type_override", UNSET))

        blob_mapping_entry = cls(
            source=source,
            target_type=target_type,
            blob_type=blob_type,
            blob_property=blob_property,
            mime_type_override=mime_type_override,
        )

        blob_mapping_entry.additional_properties = d
        return blob_mapping_entry

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
