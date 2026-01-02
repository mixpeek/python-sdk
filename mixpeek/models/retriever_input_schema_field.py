from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.retriever_input_schema_field_type import RetrieverInputSchemaFieldType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retriever_input_schema_field_properties_type_0 import RetrieverInputSchemaFieldPropertiesType0


T = TypeVar("T", bound="RetrieverInputSchemaField")


@_attrs_define
class RetrieverInputSchemaField:
    """Schema field definition for retriever input parameters.

    Identical structure to BucketSchemaField but uses RetrieverInputSchemaFieldType
    which includes additional reference types like document_reference.

    This allows retrievers to accept:
    1. Metadata inputs (strings, numbers, dates, etc.)
    2. File inputs (images, videos, documents for search)
    3. Reference inputs (document_reference for "find similar" queries)

        Attributes:
            type_ (RetrieverInputSchemaFieldType): Supported data types for retriever input schema fields.

                Retriever input schemas define what parameters users can provide when executing
                a retriever. This includes all bucket schema types plus additional reference types.

                Types fall into three categories:

                1. **Metadata Types** (JSON types):
                   - Standard JSON-compatible types
                   - Examples: string, number, boolean, date
                   - Inherited from BucketSchemaFieldType

                2. **File Types** (blobs):
                   - Users can upload files/content as search inputs
                   - Examples: text, image, video, pdf
                   - Inherited from BucketSchemaFieldType

                3. **Reference Types** (structured metadata):
                   - Special types for referencing existing documents
                   - Examples: document_reference
                   - Only available in retriever input schemas (NOT in bucket schemas)

                **DOCUMENT_REFERENCE Usage**:
                    Accept document reference for "find similar" queries.

                    Example - Find similar products retriever:
                    {
                        "reference_product": {
                            "type": "document_reference",
                            "description": "Find products similar to this one",
                            "required": true
                        }
                    }

                    Execution input:
                    {
                        "inputs": {
                            "reference_product": {
                                "collection_id": "col_products",
                                "document_id": "doc_item_123"
                            }
                        }
                    }

                    The system will use the pre-computed features from doc_item_123
                    to find similar documents without re-processing.
            default (Any | None | Unset):
            items (None | RetrieverInputSchemaField | Unset):
            properties (None | RetrieverInputSchemaFieldPropertiesType0 | Unset):
            examples (list[Any] | None | Unset): OPTIONAL. List of example values for this field. Used by Apps to show
                example inputs in the UI. Provide multiple diverse examples when possible.
            description (None | str | Unset):
            enum (list[Any] | None | Unset):
            required (bool | None | Unset):  Default: False.
    """

    type_: RetrieverInputSchemaFieldType
    default: Any | None | Unset = UNSET
    items: None | RetrieverInputSchemaField | Unset = UNSET
    properties: None | RetrieverInputSchemaFieldPropertiesType0 | Unset = UNSET
    examples: list[Any] | None | Unset = UNSET
    description: None | str | Unset = UNSET
    enum: list[Any] | None | Unset = UNSET
    required: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.retriever_input_schema_field_properties_type_0 import RetrieverInputSchemaFieldPropertiesType0

        type_ = self.type_.value

        default: Any | None | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        items: dict[str, Any] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, RetrieverInputSchemaField):
            items = self.items.to_dict()
        else:
            items = self.items

        properties: dict[str, Any] | None | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif isinstance(self.properties, RetrieverInputSchemaFieldPropertiesType0):
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
        from ..models.retriever_input_schema_field_properties_type_0 import RetrieverInputSchemaFieldPropertiesType0

        d = dict(src_dict)
        type_ = RetrieverInputSchemaFieldType(d.pop("type"))

        def _parse_default(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        def _parse_items(data: object) -> None | RetrieverInputSchemaField | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                items_type_0 = RetrieverInputSchemaField.from_dict(data)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RetrieverInputSchemaField | Unset, data)

        items = _parse_items(d.pop("items", UNSET))

        def _parse_properties(data: object) -> None | RetrieverInputSchemaFieldPropertiesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = RetrieverInputSchemaFieldPropertiesType0.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RetrieverInputSchemaFieldPropertiesType0 | Unset, data)

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

        retriever_input_schema_field = cls(
            type_=type_,
            default=default,
            items=items,
            properties=properties,
            examples=examples,
            description=description,
            enum=enum,
            required=required,
        )

        retriever_input_schema_field.additional_properties = d
        return retriever_input_schema_field

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
