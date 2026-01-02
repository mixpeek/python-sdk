from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_buckets_request_filters_type_0 import ListBucketsRequestFiltersType0
    from ..models.list_buckets_request_sort_type_0 import ListBucketsRequestSortType0


T = TypeVar("T", bound="ListBucketsRequest")


@_attrs_define
class ListBucketsRequest:
    """Request model for listing buckets.

    Attributes:
        search (None | str | Unset): Search term for wildcard search across bucket_id, bucket_name, description, and
            other text fields
        filters (ListBucketsRequestFiltersType0 | None | Unset): Filters to apply to the bucket list. Supports filtering
            by bucket_id or bucket_name.
        sort (ListBucketsRequestSortType0 | None | Unset): Sort options for the bucket list
        case_sensitive (bool | Unset): If True, filters and search will be case-sensitive Default: False.
        limit (int | Unset): Number of results to return Default: 10.
        offset (int | Unset): Number of results to skip Default: 0.
    """

    search: None | str | Unset = UNSET
    filters: ListBucketsRequestFiltersType0 | None | Unset = UNSET
    sort: ListBucketsRequestSortType0 | None | Unset = UNSET
    case_sensitive: bool | Unset = False
    limit: int | Unset = 10
    offset: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_buckets_request_filters_type_0 import ListBucketsRequestFiltersType0
        from ..models.list_buckets_request_sort_type_0 import ListBucketsRequestSortType0

        search: None | str | Unset
        if isinstance(self.search, Unset):
            search = UNSET
        else:
            search = self.search

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, ListBucketsRequestFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        sort: dict[str, Any] | None | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, ListBucketsRequestSortType0):
            sort = self.sort.to_dict()
        else:
            sort = self.sort

        case_sensitive = self.case_sensitive

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search is not UNSET:
            field_dict["search"] = search
        if filters is not UNSET:
            field_dict["filters"] = filters
        if sort is not UNSET:
            field_dict["sort"] = sort
        if case_sensitive is not UNSET:
            field_dict["case_sensitive"] = case_sensitive
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_buckets_request_filters_type_0 import ListBucketsRequestFiltersType0
        from ..models.list_buckets_request_sort_type_0 import ListBucketsRequestSortType0

        d = dict(src_dict)

        def _parse_search(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search = _parse_search(d.pop("search", UNSET))

        def _parse_filters(data: object) -> ListBucketsRequestFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = ListBucketsRequestFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListBucketsRequestFiltersType0 | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_sort(data: object) -> ListBucketsRequestSortType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sort_type_0 = ListBucketsRequestSortType0.from_dict(data)

                return sort_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListBucketsRequestSortType0 | None | Unset, data)

        sort = _parse_sort(d.pop("sort", UNSET))

        case_sensitive = d.pop("case_sensitive", UNSET)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        list_buckets_request = cls(
            search=search,
            filters=filters,
            sort=sort,
            case_sensitive=case_sensitive,
            limit=limit,
            offset=offset,
        )

        list_buckets_request.additional_properties = d
        return list_buckets_request

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
