from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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


T = TypeVar("T", bound="FieldMappingEntry")


@_attrs_define
class FieldMappingEntry:
    r"""Maps a source value to a bucket schema field.

    Used for mapping metadata, tags, columns, or extracted values to
    regular fields in the bucket schema (strings, numbers, arrays, etc.).
    Does NOT handle file content - use BlobMappingEntry for that.

    Example: Map S3 tag "category" to bucket field "content_category"
        {
            "target_type": "field",
            "source": {"type": "tag", "key": "category"}
        }

    Example: Map folder name to "department" with lowercase transform
        {
            "target_type": "field",
            "source": {"type": "folder_path", "segment": 0},
            "transform": "lowercase"
        }

    Example: Map filename regex capture to "date" field
        {
            "target_type": "field",
            "source": {"type": "filename_regex", "pattern": "^(\d{4}-\d{2}-\d{2})"},
            "required": true
        }

    Attributes:
        target_type: Must be "field" for schema field mappings
        source: The source extractor defining where to get the value
        transform: Optional transformation to apply (lowercase, uppercase, trim)
        required: Whether missing values should fail the sync

        Attributes:
            source (ColumnSource | ConstantSource | DrivePropertySource | FilenameRegexSource | FileSource |
                FolderPathSource | S3MetadataSource | S3TagSource): Source extractor defining where to get the value. Options:
                tag, metadata, filename_regex, column, drive_property, folder_path, constant. The 'file' source is not valid for
                field mappings (use blob instead).
            target_type (Literal['field'] | Unset): Target type. Must be 'field' for regular schema fields. Default:
                'field'.
            transform (None | str | Unset): Optional transformation to apply to the extracted value. Supported transforms:
                'lowercase' - convert to lowercase, 'uppercase' - convert to uppercase, 'trim' - remove leading/trailing
                whitespace, 'json_parse' - parse JSON string to object/array. Transforms are applied after extraction, before
                storage.
            required (bool | Unset): If True, the sync will fail if this field cannot be extracted. If False (default),
                missing values result in the field being omitted. Use required=True for critical fields that must be present.
                Default: False.
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
    target_type: Literal["field"] | Unset = "field"
    transform: None | str | Unset = UNSET
    required: bool | Unset = False
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

        transform: None | str | Unset
        if isinstance(self.transform, Unset):
            transform = UNSET
        else:
            transform = self.transform

        required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
            }
        )
        if target_type is not UNSET:
            field_dict["target_type"] = target_type
        if transform is not UNSET:
            field_dict["transform"] = transform
        if required is not UNSET:
            field_dict["required"] = required

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

        target_type = cast(Literal["field"] | Unset, d.pop("target_type", UNSET))
        if target_type != "field" and not isinstance(target_type, Unset):
            raise ValueError(f"target_type must match const 'field', got '{target_type}'")

        def _parse_transform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transform = _parse_transform(d.pop("transform", UNSET))

        required = d.pop("required", UNSET)

        field_mapping_entry = cls(
            source=source,
            target_type=target_type,
            transform=transform,
            required=required,
        )

        field_mapping_entry.additional_properties = d
        return field_mapping_entry

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
