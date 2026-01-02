from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_namespaces_request_filters_type_0 import ListNamespacesRequestFiltersType0
    from ..models.list_namespaces_request_sort_type_0 import ListNamespacesRequestSortType0


T = TypeVar("T", bound="ListNamespacesRequest")


@_attrs_define
class ListNamespacesRequest:
    """Request schema for listing namespaces.

    Attributes:
        filters (ListNamespacesRequestFiltersType0 | None | Unset): Optional filters to apply to the namespace list.
            Supports filtering by namespace_id or namespace_name. Example: {'namespace_id': 'ns_abc123', 'namespace_name':
            {'$regex': '^my_namespace'}}.
        sort (ListNamespacesRequestSortType0 | None | Unset): Optional sort criteria for the namespace list. Example:
            {'direction': 'asc', 'field': 'namespace_name'}.
        search (None | str | Unset): Search term for wildcard search across namespace_id, namespace_name, description,
            and other text fields. Example: ns_abc123.
        case_sensitive (bool | Unset): If True, filters and search will be case-sensitive Default: False.
    """

    filters: ListNamespacesRequestFiltersType0 | None | Unset = UNSET
    sort: ListNamespacesRequestSortType0 | None | Unset = UNSET
    search: None | str | Unset = UNSET
    case_sensitive: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_namespaces_request_filters_type_0 import ListNamespacesRequestFiltersType0
        from ..models.list_namespaces_request_sort_type_0 import ListNamespacesRequestSortType0

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, ListNamespacesRequestFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        sort: dict[str, Any] | None | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, ListNamespacesRequestSortType0):
            sort = self.sort.to_dict()
        else:
            sort = self.sort

        search: None | str | Unset
        if isinstance(self.search, Unset):
            search = UNSET
        else:
            search = self.search

        case_sensitive = self.case_sensitive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters
        if sort is not UNSET:
            field_dict["sort"] = sort
        if search is not UNSET:
            field_dict["search"] = search
        if case_sensitive is not UNSET:
            field_dict["case_sensitive"] = case_sensitive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_namespaces_request_filters_type_0 import ListNamespacesRequestFiltersType0
        from ..models.list_namespaces_request_sort_type_0 import ListNamespacesRequestSortType0

        d = dict(src_dict)

        def _parse_filters(data: object) -> ListNamespacesRequestFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = ListNamespacesRequestFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListNamespacesRequestFiltersType0 | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_sort(data: object) -> ListNamespacesRequestSortType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sort_type_0 = ListNamespacesRequestSortType0.from_dict(data)

                return sort_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListNamespacesRequestSortType0 | None | Unset, data)

        sort = _parse_sort(d.pop("sort", UNSET))

        def _parse_search(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search = _parse_search(d.pop("search", UNSET))

        case_sensitive = d.pop("case_sensitive", UNSET)

        list_namespaces_request = cls(
            filters=filters,
            sort=sort,
            search=search,
            case_sensitive=case_sensitive,
        )

        list_namespaces_request.additional_properties = d
        return list_namespaces_request

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
