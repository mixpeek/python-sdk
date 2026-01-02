from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_filter_date_range_type_0 import ResourceFilterDateRangeType0


T = TypeVar("T", bound="ResourceFilter")


@_attrs_define
class ResourceFilter:
    """Filters for selective resource migration.

    Attributes:
        collection_ids (list[str] | None | Unset): Specific collection IDs to migrate
        taxonomy_ids (list[str] | None | Unset): Specific taxonomy IDs to migrate
        cluster_ids (list[str] | None | Unset): Specific cluster IDs to migrate
        retriever_ids (list[str] | None | Unset): Specific retriever IDs to migrate
        date_range (None | ResourceFilterDateRangeType0 | Unset): Date range filter (after, before)
        auto_include_dependencies (bool | Unset): Automatically include required dependencies Default: True.
    """

    collection_ids: list[str] | None | Unset = UNSET
    taxonomy_ids: list[str] | None | Unset = UNSET
    cluster_ids: list[str] | None | Unset = UNSET
    retriever_ids: list[str] | None | Unset = UNSET
    date_range: None | ResourceFilterDateRangeType0 | Unset = UNSET
    auto_include_dependencies: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resource_filter_date_range_type_0 import ResourceFilterDateRangeType0

        collection_ids: list[str] | None | Unset
        if isinstance(self.collection_ids, Unset):
            collection_ids = UNSET
        elif isinstance(self.collection_ids, list):
            collection_ids = self.collection_ids

        else:
            collection_ids = self.collection_ids

        taxonomy_ids: list[str] | None | Unset
        if isinstance(self.taxonomy_ids, Unset):
            taxonomy_ids = UNSET
        elif isinstance(self.taxonomy_ids, list):
            taxonomy_ids = self.taxonomy_ids

        else:
            taxonomy_ids = self.taxonomy_ids

        cluster_ids: list[str] | None | Unset
        if isinstance(self.cluster_ids, Unset):
            cluster_ids = UNSET
        elif isinstance(self.cluster_ids, list):
            cluster_ids = self.cluster_ids

        else:
            cluster_ids = self.cluster_ids

        retriever_ids: list[str] | None | Unset
        if isinstance(self.retriever_ids, Unset):
            retriever_ids = UNSET
        elif isinstance(self.retriever_ids, list):
            retriever_ids = self.retriever_ids

        else:
            retriever_ids = self.retriever_ids

        date_range: dict[str, Any] | None | Unset
        if isinstance(self.date_range, Unset):
            date_range = UNSET
        elif isinstance(self.date_range, ResourceFilterDateRangeType0):
            date_range = self.date_range.to_dict()
        else:
            date_range = self.date_range

        auto_include_dependencies = self.auto_include_dependencies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collection_ids is not UNSET:
            field_dict["collection_ids"] = collection_ids
        if taxonomy_ids is not UNSET:
            field_dict["taxonomy_ids"] = taxonomy_ids
        if cluster_ids is not UNSET:
            field_dict["cluster_ids"] = cluster_ids
        if retriever_ids is not UNSET:
            field_dict["retriever_ids"] = retriever_ids
        if date_range is not UNSET:
            field_dict["date_range"] = date_range
        if auto_include_dependencies is not UNSET:
            field_dict["auto_include_dependencies"] = auto_include_dependencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_filter_date_range_type_0 import ResourceFilterDateRangeType0

        d = dict(src_dict)

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

        def _parse_taxonomy_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                taxonomy_ids_type_0 = cast(list[str], data)

                return taxonomy_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        taxonomy_ids = _parse_taxonomy_ids(d.pop("taxonomy_ids", UNSET))

        def _parse_cluster_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cluster_ids_type_0 = cast(list[str], data)

                return cluster_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cluster_ids = _parse_cluster_ids(d.pop("cluster_ids", UNSET))

        def _parse_retriever_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                retriever_ids_type_0 = cast(list[str], data)

                return retriever_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        retriever_ids = _parse_retriever_ids(d.pop("retriever_ids", UNSET))

        def _parse_date_range(data: object) -> None | ResourceFilterDateRangeType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                date_range_type_0 = ResourceFilterDateRangeType0.from_dict(data)

                return date_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResourceFilterDateRangeType0 | Unset, data)

        date_range = _parse_date_range(d.pop("date_range", UNSET))

        auto_include_dependencies = d.pop("auto_include_dependencies", UNSET)

        resource_filter = cls(
            collection_ids=collection_ids,
            taxonomy_ids=taxonomy_ids,
            cluster_ids=cluster_ids,
            retriever_ids=retriever_ids,
            date_range=date_range,
            auto_include_dependencies=auto_include_dependencies,
        )

        resource_filter.additional_properties = d
        return resource_filter

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
