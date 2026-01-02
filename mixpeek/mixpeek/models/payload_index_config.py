from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.payload_schema_type import PayloadSchemaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bool_index_params import BoolIndexParams
    from ..models.datetime_index_params import DatetimeIndexParams
    from ..models.float_index_params import FloatIndexParams
    from ..models.geo_index_params import GeoIndexParams
    from ..models.integer_index_params import IntegerIndexParams
    from ..models.keyword_index_params import KeywordIndexParams
    from ..models.text_index_params import TextIndexParams
    from ..models.uuid_index_params import UuidIndexParams


T = TypeVar("T", bound="PayloadIndexConfig")


@_attrs_define
class PayloadIndexConfig:
    """Configuration for a payload index.

    Defines the structure and behavior of a payload field index in Qdrant collections.
    Payload indexes enable efficient filtering and searching on document metadata.

    Protected Indexes:
        System-managed indexes (is_protected=True) cannot be modified or deleted by users.
        These are essential for Mixpeek's internal operations:
        - internal_id: Tenant isolation
        - namespace_id: Namespace scoping
        - collection_id, document_id: Document lineage
        - bucket_id, object_id, root_object_id, root_bucket_id, source_object_id: Object lineage
        - created_at, updated_at: Timestamps

    Use Cases:
        - Create custom metadata indexes for efficient filtering
        - Configure full-text search on text fields
        - Set up geospatial queries on location data
        - Enable range queries on numeric fields

    Requirements:
        - field_name: REQUIRED - Must be unique within the namespace
        - type: REQUIRED - Must match PayloadSchemaType enum
        - field_schema: OPTIONAL - Auto-generated from type if not provided
        - is_protected: OPTIONAL - Defaults to False (user-managed index)

        Attributes:
            field_name (str): Name of the payload field to index. Must be unique within the namespace. Use dot notation for
                nested fields (e.g., 'metadata.title'). Cannot use protected system field names when is_protected=False.
            type_ (PayloadSchemaType): Payload schema type.
            field_schema (BoolIndexParams | DatetimeIndexParams | FloatIndexParams | GeoIndexParams | IntegerIndexParams |
                KeywordIndexParams | None | TextIndexParams | Unset | UuidIndexParams): Optional schema configuration for the
                index. If not provided, uses default parameters for the specified type. Different types support different
                parameters (e.g., KeywordIndexParams.is_tenant).
            is_protected (bool | Unset): Whether this index is system-managed and cannot be modified by users. Protected
                indexes (is_protected=True) are created automatically by Mixpeek and are essential for internal operations like
                tenant isolation, lineage tracking, and document management. Users cannot create, modify, or delete protected
                indexes. User-created indexes always have is_protected=False. Default: False.
    """

    field_name: str
    type_: PayloadSchemaType
    field_schema: (
        BoolIndexParams
        | DatetimeIndexParams
        | FloatIndexParams
        | GeoIndexParams
        | IntegerIndexParams
        | KeywordIndexParams
        | None
        | TextIndexParams
        | Unset
        | UuidIndexParams
    ) = UNSET
    is_protected: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bool_index_params import BoolIndexParams
        from ..models.datetime_index_params import DatetimeIndexParams
        from ..models.float_index_params import FloatIndexParams
        from ..models.geo_index_params import GeoIndexParams
        from ..models.integer_index_params import IntegerIndexParams
        from ..models.keyword_index_params import KeywordIndexParams
        from ..models.text_index_params import TextIndexParams
        from ..models.uuid_index_params import UuidIndexParams

        field_name = self.field_name

        type_ = self.type_.value

        field_schema: dict[str, Any] | None | Unset
        if isinstance(self.field_schema, Unset):
            field_schema = UNSET
        elif isinstance(self.field_schema, TextIndexParams):
            field_schema = self.field_schema.to_dict()
        elif isinstance(self.field_schema, IntegerIndexParams):
            field_schema = self.field_schema.to_dict()
        elif isinstance(self.field_schema, KeywordIndexParams):
            field_schema = self.field_schema.to_dict()
        elif isinstance(self.field_schema, FloatIndexParams):
            field_schema = self.field_schema.to_dict()
        elif isinstance(self.field_schema, GeoIndexParams):
            field_schema = self.field_schema.to_dict()
        elif isinstance(self.field_schema, DatetimeIndexParams):
            field_schema = self.field_schema.to_dict()
        elif isinstance(self.field_schema, UuidIndexParams):
            field_schema = self.field_schema.to_dict()
        elif isinstance(self.field_schema, BoolIndexParams):
            field_schema = self.field_schema.to_dict()
        else:
            field_schema = self.field_schema

        is_protected = self.is_protected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_name": field_name,
                "type": type_,
            }
        )
        if field_schema is not UNSET:
            field_dict["field_schema"] = field_schema
        if is_protected is not UNSET:
            field_dict["is_protected"] = is_protected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bool_index_params import BoolIndexParams
        from ..models.datetime_index_params import DatetimeIndexParams
        from ..models.float_index_params import FloatIndexParams
        from ..models.geo_index_params import GeoIndexParams
        from ..models.integer_index_params import IntegerIndexParams
        from ..models.keyword_index_params import KeywordIndexParams
        from ..models.text_index_params import TextIndexParams
        from ..models.uuid_index_params import UuidIndexParams

        d = dict(src_dict)
        field_name = d.pop("field_name")

        type_ = PayloadSchemaType(d.pop("type"))

        def _parse_field_schema(
            data: object,
        ) -> (
            BoolIndexParams
            | DatetimeIndexParams
            | FloatIndexParams
            | GeoIndexParams
            | IntegerIndexParams
            | KeywordIndexParams
            | None
            | TextIndexParams
            | Unset
            | UuidIndexParams
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_schema_type_0 = TextIndexParams.from_dict(data)

                return field_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_schema_type_1 = IntegerIndexParams.from_dict(data)

                return field_schema_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_schema_type_2 = KeywordIndexParams.from_dict(data)

                return field_schema_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_schema_type_3 = FloatIndexParams.from_dict(data)

                return field_schema_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_schema_type_4 = GeoIndexParams.from_dict(data)

                return field_schema_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_schema_type_5 = DatetimeIndexParams.from_dict(data)

                return field_schema_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_schema_type_6 = UuidIndexParams.from_dict(data)

                return field_schema_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_schema_type_7 = BoolIndexParams.from_dict(data)

                return field_schema_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                BoolIndexParams
                | DatetimeIndexParams
                | FloatIndexParams
                | GeoIndexParams
                | IntegerIndexParams
                | KeywordIndexParams
                | None
                | TextIndexParams
                | Unset
                | UuidIndexParams,
                data,
            )

        field_schema = _parse_field_schema(d.pop("field_schema", UNSET))

        is_protected = d.pop("is_protected", UNSET)

        payload_index_config = cls(
            field_name=field_name,
            type_=type_,
            field_schema=field_schema,
            is_protected=is_protected,
        )

        payload_index_config.additional_properties = d
        return payload_index_config

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
