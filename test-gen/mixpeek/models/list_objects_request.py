from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logical_operator import LogicalOperator
    from ..models.sort_option import SortOption


T = TypeVar("T", bound="ListObjectsRequest")


@_attrs_define
class ListObjectsRequest:
    """Request model for listing objects in a bucket.

    Attributes:
        filters (LogicalOperator | None | Unset): Filters to apply to the object list
        sort (None | SortOption | Unset): Sort options for the object list
        search (None | str | Unset): Search term to filter objects by key or metadata
        select (list[str] | None | Unset): OPTIONAL. List of fields to include in the response. Supports dot notation
            for nested fields (e.g., 'metadata.title', 'status'). When specified, only the selected fields will be returned
            in the object results, reducing response size. System fields like 'object_id' and 'bucket_id' are always
            included. Use this to optimize response size when working with large objects.
    """

    filters: LogicalOperator | None | Unset = UNSET
    sort: None | SortOption | Unset = UNSET
    search: None | str | Unset = UNSET
    select: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_operator import LogicalOperator
        from ..models.sort_option import SortOption

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, LogicalOperator):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        sort: dict[str, Any] | None | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, SortOption):
            sort = self.sort.to_dict()
        else:
            sort = self.sort

        search: None | str | Unset
        if isinstance(self.search, Unset):
            search = UNSET
        else:
            search = self.search

        select: list[str] | None | Unset
        if isinstance(self.select, Unset):
            select = UNSET
        elif isinstance(self.select, list):
            select = self.select

        else:
            select = self.select

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters
        if sort is not UNSET:
            field_dict["sort"] = sort
        if search is not UNSET:
            field_dict["search"] = search
        if select is not UNSET:
            field_dict["select"] = select

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logical_operator import LogicalOperator
        from ..models.sort_option import SortOption

        d = dict(src_dict)

        def _parse_filters(data: object) -> LogicalOperator | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = LogicalOperator.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LogicalOperator | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_sort(data: object) -> None | SortOption | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sort_type_0 = SortOption.from_dict(data)

                return sort_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SortOption | Unset, data)

        sort = _parse_sort(d.pop("sort", UNSET))

        def _parse_search(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search = _parse_search(d.pop("search", UNSET))

        def _parse_select(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                select_type_0 = cast(list[str], data)

                return select_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        select = _parse_select(d.pop("select", UNSET))

        list_objects_request = cls(
            filters=filters,
            sort=sort,
            search=search,
            select=select,
        )

        list_objects_request.additional_properties = d
        return list_objects_request

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
