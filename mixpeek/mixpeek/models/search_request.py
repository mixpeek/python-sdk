from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_request_resource_types_type_0_item import SearchRequestResourceTypesType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchRequest")


@_attrs_define
class SearchRequest:
    """Request model for searching across resource names and IDs.

    Search is performed across all resource types within the authenticated namespace.
    The search is case-insensitive and supports partial matching on both names and IDs.

    Use Cases:
        - Find resources by partial name match
        - Locate resources by ID prefix
        - Filter search to specific resource types
        - Paginate through large result sets

    Requirements:
        - query: REQUIRED - Search term (minimum 1 character)
        - resource_types: OPTIONAL - Filter by specific types
        - limit: OPTIONAL - Results per page (1-100, default 20)
        - offset: OPTIONAL - Pagination offset (default 0)

        Attributes:
            query (str): Search term to match against resource names and IDs. REQUIRED. Minimum 1 character. Case-
                insensitive partial matching is performed. Matches against: bucket_name, bucket_id, collection_name,
                collection_id, retriever_name, retriever_id, taxonomy_name, taxonomy_id, cluster_name, cluster_id,
                namespace_name, namespace_id. Example: 'prod' matches 'production-videos', 'bkt_prod123', 'Products Collection'.
            resource_types (list[SearchRequestResourceTypesType0Item] | None | Unset): Filter search to specific resource
                types. OPTIONAL - If not provided, searches all resource types. Valid values: 'bucket', 'collection',
                'retriever', 'taxonomy', 'cluster', 'published_retriever', 'namespace'. Example: ['bucket', 'collection']
                searches only buckets and collections.
            limit (int | Unset): Maximum number of results to return. OPTIONAL - Defaults to 20. Minimum: 1, Maximum: 100.
                Use with offset for pagination. Default: 20.
            offset (int | Unset): Number of results to skip for pagination. OPTIONAL - Defaults to 0. Minimum: 0. Use with
                limit for pagination. Example: offset=20 with limit=20 returns results 21-40. Default: 0.
    """

    query: str
    resource_types: list[SearchRequestResourceTypesType0Item] | None | Unset = UNSET
    limit: int | Unset = 20
    offset: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        resource_types: list[str] | None | Unset
        if isinstance(self.resource_types, Unset):
            resource_types = UNSET
        elif isinstance(self.resource_types, list):
            resource_types = []
            for resource_types_type_0_item_data in self.resource_types:
                resource_types_type_0_item = resource_types_type_0_item_data.value
                resource_types.append(resource_types_type_0_item)

        else:
            resource_types = self.resource_types

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if resource_types is not UNSET:
            field_dict["resource_types"] = resource_types
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        def _parse_resource_types(data: object) -> list[SearchRequestResourceTypesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resource_types_type_0 = []
                _resource_types_type_0 = data
                for resource_types_type_0_item_data in _resource_types_type_0:
                    resource_types_type_0_item = SearchRequestResourceTypesType0Item(resource_types_type_0_item_data)

                    resource_types_type_0.append(resource_types_type_0_item)

                return resource_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SearchRequestResourceTypesType0Item] | None | Unset, data)

        resource_types = _parse_resource_types(d.pop("resource_types", UNSET))

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        search_request = cls(
            query=query,
            resource_types=resource_types,
            limit=limit,
            offset=offset,
        )

        search_request.additional_properties = d
        return search_request

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
