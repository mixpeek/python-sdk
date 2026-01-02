from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_type import SourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_filters import SourceFilters


T = TypeVar("T", bound="SourceConfig")


@_attrs_define
class SourceConfig:
    """Configuration for collection source (bucket(s) or collection).

    Collections can process data from two types of sources:

    1. **Bucket Source**: Process raw objects from one or more buckets (first-stage processing)
       - Use this to create your initial collections from uploaded data
       - Can specify multiple buckets to consolidate data from different sources
       - All buckets must have compatible schemas (validated at creation)
       - Example: Videos from multiple regions → Frame extraction collection

    2. **Collection Source**: Process documents from another collection (decomposition trees)
       - Use this to create multi-stage processing pipelines
       - Example: Frames collection → Scene detection collection

    Multi-Bucket Requirements:
    - All buckets must have compatible schemas (same fields, types, and required status)
    - Schema compatibility is validated when the collection is created
    - Documents track which specific bucket they came from via root_bucket_id
    - Useful for consolidating data from multiple regions, teams, or environments

    The source determines:
    - What data the feature extractor receives as input
    - The input_schema available for input_mappings and field_passthrough
    - The lineage tracking in output documents

    Examples:
        Single bucket: {"type": "bucket", "bucket_ids": ["bkt_products"]}
        Multi-bucket: {"type": "bucket", "bucket_ids": ["bkt_us", "bkt_eu", "bkt_asia"]}
        Collection: {"type": "collection", "collection_id": "col_frames"}

        Attributes:
            type_ (SourceType): Generic source types for any Qdrant point/document.
            bucket_ids (list[str] | None | Unset): List of bucket IDs when type='bucket'. REQUIRED when type='bucket'. NOT
                ALLOWED when type='collection'. Can specify one or more buckets to process. Single bucket: Use array with one
                element ['bkt_id']. Multiple buckets: All buckets MUST have compatible schemas. Schema compatibility validated
                at collection creation. Compatible schemas have: 1) Same field names, 2) Same field types, 3) Same required
                status. Documents will include root_bucket_id to track which bucket they came from. Use cases: multi-region
                data, multi-team consolidation, environment aggregation.
            collection_id (None | str | Unset): Collection ID when type='collection' (single collection). Use this OR
                collection_ids (not both). REQUIRED when type='collection' and processing single collection. NOT ALLOWED when
                type='bucket'. The collection will process documents from this upstream collection. The upstream collection's
                output_schema becomes this collection's input_schema. This enables decomposition trees (multi-stage pipelines).
                Example: Process frames collection → create scenes collection.
            collection_ids (list[str] | None | Unset): List of collection IDs when type='collection' (multiple collections).
                Use this OR collection_id (not both). REQUIRED when type='collection' and processing multiple collections. NOT
                ALLOWED when type='bucket'. Used for operations that consolidate multiple upstream collections. Example:
                Clustering across multiple collections → cluster output collection. All collections must have compatible schemas
                for consolidation operations.
            inherited_bucket_ids (list[str] | None | Unset): List of original bucket IDs that source collections originated
                from. OPTIONAL. Only used when type='collection'. Tracks the complete lineage chain: buckets → collections →
                derived collections. Extracted from upstream collection metadata at collection creation time. Enables tracing
                derived collections (like cluster outputs) back to original data sources. Example: Cluster output collection
                inherits bucket IDs from its source collections. Format: List of bucket IDs with 'bkt_' prefix.
            source_filters (None | SourceFilters | Unset): Optional filters to apply to source data. When specified, only
                objects/documents matching these filters will be processed by this collection. Filters are evaluated at batch
                creation time. Uses same LogicalOperator model as list APIs for consistency.
    """

    type_: SourceType
    bucket_ids: list[str] | None | Unset = UNSET
    collection_id: None | str | Unset = UNSET
    collection_ids: list[str] | None | Unset = UNSET
    inherited_bucket_ids: list[str] | None | Unset = UNSET
    source_filters: None | SourceFilters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.source_filters import SourceFilters

        type_ = self.type_.value

        bucket_ids: list[str] | None | Unset
        if isinstance(self.bucket_ids, Unset):
            bucket_ids = UNSET
        elif isinstance(self.bucket_ids, list):
            bucket_ids = self.bucket_ids

        else:
            bucket_ids = self.bucket_ids

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        collection_ids: list[str] | None | Unset
        if isinstance(self.collection_ids, Unset):
            collection_ids = UNSET
        elif isinstance(self.collection_ids, list):
            collection_ids = self.collection_ids

        else:
            collection_ids = self.collection_ids

        inherited_bucket_ids: list[str] | None | Unset
        if isinstance(self.inherited_bucket_ids, Unset):
            inherited_bucket_ids = UNSET
        elif isinstance(self.inherited_bucket_ids, list):
            inherited_bucket_ids = self.inherited_bucket_ids

        else:
            inherited_bucket_ids = self.inherited_bucket_ids

        source_filters: dict[str, Any] | None | Unset
        if isinstance(self.source_filters, Unset):
            source_filters = UNSET
        elif isinstance(self.source_filters, SourceFilters):
            source_filters = self.source_filters.to_dict()
        else:
            source_filters = self.source_filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if bucket_ids is not UNSET:
            field_dict["bucket_ids"] = bucket_ids
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if collection_ids is not UNSET:
            field_dict["collection_ids"] = collection_ids
        if inherited_bucket_ids is not UNSET:
            field_dict["inherited_bucket_ids"] = inherited_bucket_ids
        if source_filters is not UNSET:
            field_dict["source_filters"] = source_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_filters import SourceFilters

        d = dict(src_dict)
        type_ = SourceType(d.pop("type"))

        def _parse_bucket_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bucket_ids_type_0 = cast(list[str], data)

                return bucket_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        bucket_ids = _parse_bucket_ids(d.pop("bucket_ids", UNSET))

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

        def _parse_collection_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collection_ids_type_0 = cast(list[str], data)

                return collection_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        collection_ids = _parse_collection_ids(d.pop("collection_ids", UNSET))

        def _parse_inherited_bucket_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inherited_bucket_ids_type_0 = cast(list[str], data)

                return inherited_bucket_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        inherited_bucket_ids = _parse_inherited_bucket_ids(d.pop("inherited_bucket_ids", UNSET))

        def _parse_source_filters(data: object) -> None | SourceFilters | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_filters_type_0 = SourceFilters.from_dict(data)

                return source_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SourceFilters | Unset, data)

        source_filters = _parse_source_filters(d.pop("source_filters", UNSET))

        source_config = cls(
            type_=type_,
            bucket_ids=bucket_ids,
            collection_id=collection_id,
            collection_ids=collection_ids,
            inherited_bucket_ids=inherited_bucket_ids,
            source_filters=source_filters,
        )

        source_config.additional_properties = d
        return source_config

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
