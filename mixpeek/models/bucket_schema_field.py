from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bucket_schema_field_type import BucketSchemaFieldType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bucket_schema_field_properties_type_0 import BucketSchemaFieldPropertiesType0


T = TypeVar("T", bound="BucketSchemaField")


@_attrs_define
class BucketSchemaField:
    """Schema field definition for bucket objects.

    Attributes:
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
        default (Any | None | Unset):
        items (BucketSchemaField | None | Unset):
        properties (BucketSchemaFieldPropertiesType0 | None | Unset):
        examples (list[Any] | None | Unset): OPTIONAL. List of example values for this field. Used by Apps to show
            example inputs in the UI. Provide multiple diverse examples when possible.
        description (None | str | Unset):
        enum (list[Any] | None | Unset):
        required (bool | None | Unset):  Default: False.
    """

    type_: BucketSchemaFieldType
    default: Any | None | Unset = UNSET
    items: BucketSchemaField | None | Unset = UNSET
    properties: BucketSchemaFieldPropertiesType0 | None | Unset = UNSET
    examples: list[Any] | None | Unset = UNSET
    description: None | str | Unset = UNSET
    enum: list[Any] | None | Unset = UNSET
    required: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bucket_schema_field_properties_type_0 import BucketSchemaFieldPropertiesType0

        type_ = self.type_.value

        default: Any | None | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        items: dict[str, Any] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, BucketSchemaField):
            items = self.items.to_dict()
        else:
            items = self.items

        properties: dict[str, Any] | None | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif isinstance(self.properties, BucketSchemaFieldPropertiesType0):
            properties = self.properties.to_dict()
        else:
            properties = self.properties

        examples: list[Any] | None | Unset
        if isinstance(self.examples, Unset):
            examples = UNSET
        elif isinstance(self.examples, list):
            examples = self.examples

        else:
            examples = self.examples

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enum: list[Any] | None | Unset
        if isinstance(self.enum, Unset):
            enum = UNSET
        elif isinstance(self.enum, list):
            enum = self.enum

        else:
            enum = self.enum

        required: bool | None | Unset
        if isinstance(self.required, Unset):
            required = UNSET
        else:
            required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if items is not UNSET:
            field_dict["items"] = items
        if properties is not UNSET:
            field_dict["properties"] = properties
        if examples is not UNSET:
            field_dict["examples"] = examples
        if description is not UNSET:
            field_dict["description"] = description
        if enum is not UNSET:
            field_dict["enum"] = enum
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bucket_schema_field_properties_type_0 import BucketSchemaFieldPropertiesType0

        d = dict(src_dict)
        type_ = BucketSchemaFieldType(d.pop("type"))

        def _parse_default(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        def _parse_items(data: object) -> BucketSchemaField | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                items_type_0 = BucketSchemaField.from_dict(data)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BucketSchemaField | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))

        def _parse_properties(data: object) -> BucketSchemaFieldPropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = BucketSchemaFieldPropertiesType0.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BucketSchemaFieldPropertiesType0 | None | Unset, data)

        properties = _parse_properties(d.pop("properties", UNSET))

        def _parse_examples(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                examples_type_0 = cast(list[Any], data)

                return examples_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        examples = _parse_examples(d.pop("examples", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_enum(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                enum_type_0 = cast(list[Any], data)

                return enum_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        enum = _parse_enum(d.pop("enum", UNSET))

        def _parse_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        required = _parse_required(d.pop("required", UNSET))

        bucket_schema_field = cls(
            type_=type_,
            default=default,
            items=items,
            properties=properties,
            examples=examples,
            description=description,
            enum=enum,
            required=required,
        )

        bucket_schema_field.additional_properties = d
        return bucket_schema_field

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
