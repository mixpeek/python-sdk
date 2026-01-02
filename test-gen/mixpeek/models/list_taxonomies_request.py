from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logical_operator import LogicalOperator
    from ..models.sort_option import SortOption


T = TypeVar("T", bound="ListTaxonomiesRequest")


@_attrs_define
class ListTaxonomiesRequest:
    """Request model to list taxonomies.

    Attributes:
        search (None | str | Unset): Search term for wildcard search across taxonomy_id, taxonomy_name, description, and
            other text fields
        filters (LogicalOperator | None | Unset): Filters to apply to the taxonomy list. Supports filtering by
            taxonomy_id or taxonomy_name.
        sort (None | SortOption | Unset): Sort configuration for the taxonomy list
        case_sensitive (bool | Unset): If True, filters and search will be case-sensitive Default: False.
    """

    search: None | str | Unset = UNSET
    filters: LogicalOperator | None | Unset = UNSET
    sort: None | SortOption | Unset = UNSET
    case_sensitive: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_operator import LogicalOperator
        from ..models.sort_option import SortOption

        search: None | str | Unset
        if isinstance(self.search, Unset):
            search = UNSET
        else:
            search = self.search

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

        case_sensitive = self.case_sensitive

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logical_operator import LogicalOperator
        from ..models.sort_option import SortOption

        d = dict(src_dict)

        def _parse_search(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search = _parse_search(d.pop("search", UNSET))

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

        case_sensitive = d.pop("case_sensitive", UNSET)

        list_taxonomies_request = cls(
            search=search,
            filters=filters,
            sort=sort,
            case_sensitive=case_sensitive,
        )

        list_taxonomies_request.additional_properties = d
        return list_taxonomies_request

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
