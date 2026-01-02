from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigger_collection_request_source_filters_type_0 import TriggerCollectionRequestSourceFiltersType0


T = TypeVar("T", bound="TriggerCollectionRequest")


@_attrs_define
class TriggerCollectionRequest:
    """Request to trigger (re)processing through a collection.

    **For bucket-sourced collections (tier 0):**
    Discovers objects from source bucket(s) and creates a batch for processing.
    Use `include_buckets` to limit which source buckets to process from.

    **For collection-sourced collections (tier N):**
    Processes existing documents from upstream collection(s).
    Use `include_collections` to limit which source collections to process from.

    Use `source_filters` for field-level filtering on objects or documents.

    **Document Overwrite Behavior:**
    - If source bucket has `unique_key` configured: Documents are UPSERTED (overwrites existing)
    - If source bucket has NO `unique_key`: New documents are CREATED (may cause duplicates)

    To enable idempotent re-processing, configure `unique_key` on the source bucket.

        Attributes:
            include_buckets (list[str] | None | Unset): Limit processing to objects from these specific buckets (IDs or
                names). Only applies to bucket-sourced collections. If not provided, all configured source buckets are used.
            include_collections (list[str] | None | Unset): Limit processing to documents from these specific collections
                (IDs or names). Only applies to collection-sourced collections. If not provided, all configured source
                collections are used.
            source_filters (None | TriggerCollectionRequestSourceFiltersType0 | Unset): Field-level filters for objects
                (bucket-sourced) or documents (collection-sourced). Uses LogicalOperator format (AND/OR/NOT). Use this to filter
                by metadata fields, status, or any other object/document properties.
    """

    include_buckets: list[str] | None | Unset = UNSET
    include_collections: list[str] | None | Unset = UNSET
    source_filters: None | TriggerCollectionRequestSourceFiltersType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trigger_collection_request_source_filters_type_0 import TriggerCollectionRequestSourceFiltersType0

        include_buckets: list[str] | None | Unset
        if isinstance(self.include_buckets, Unset):
            include_buckets = UNSET
        elif isinstance(self.include_buckets, list):
            include_buckets = self.include_buckets

        else:
            include_buckets = self.include_buckets

        include_collections: list[str] | None | Unset
        if isinstance(self.include_collections, Unset):
            include_collections = UNSET
        elif isinstance(self.include_collections, list):
            include_collections = self.include_collections

        else:
            include_collections = self.include_collections

        source_filters: dict[str, Any] | None | Unset
        if isinstance(self.source_filters, Unset):
            source_filters = UNSET
        elif isinstance(self.source_filters, TriggerCollectionRequestSourceFiltersType0):
            source_filters = self.source_filters.to_dict()
        else:
            source_filters = self.source_filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_buckets is not UNSET:
            field_dict["include_buckets"] = include_buckets
        if include_collections is not UNSET:
            field_dict["include_collections"] = include_collections
        if source_filters is not UNSET:
            field_dict["source_filters"] = source_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_collection_request_source_filters_type_0 import TriggerCollectionRequestSourceFiltersType0

        d = dict(src_dict)

        def _parse_include_buckets(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                include_buckets_type_0 = cast(list[str], data)

                return include_buckets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        include_buckets = _parse_include_buckets(d.pop("include_buckets", UNSET))

        def _parse_include_collections(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                include_collections_type_0 = cast(list[str], data)

                return include_collections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        include_collections = _parse_include_collections(d.pop("include_collections", UNSET))

        def _parse_source_filters(data: object) -> None | TriggerCollectionRequestSourceFiltersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_filters_type_0 = TriggerCollectionRequestSourceFiltersType0.from_dict(data)

                return source_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TriggerCollectionRequestSourceFiltersType0 | Unset, data)

        source_filters = _parse_source_filters(d.pop("source_filters", UNSET))

        trigger_collection_request = cls(
            include_buckets=include_buckets,
            include_collections=include_collections,
            source_filters=source_filters,
        )

        trigger_collection_request.additional_properties = d
        return trigger_collection_request

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
