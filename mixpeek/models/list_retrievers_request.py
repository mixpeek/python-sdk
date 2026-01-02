from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_retrievers_request_filters_type_0 import ListRetrieversRequestFiltersType0
    from ..models.list_retrievers_request_sorts_type_0_item import ListRetrieversRequestSortsType0Item


T = TypeVar("T", bound="ListRetrieversRequest")


@_attrs_define
class ListRetrieversRequest:
    """Request to list retrievers.

    Attributes:
        search (None | str | Unset): Search term for wildcard search across retriever_id, retriever_name, description,
            and other text fields
        filters (ListRetrieversRequestFiltersType0 | None | Unset): Filters to apply to the retriever list. Supports
            filtering by retriever_id or retriever_name.
        sorts (list[ListRetrieversRequestSortsType0Item] | None | Unset): Sort options for the retriever list
        case_sensitive (bool | Unset): If True, filters and search will be case-sensitive Default: False.
    """

    search: None | str | Unset = UNSET
    filters: ListRetrieversRequestFiltersType0 | None | Unset = UNSET
    sorts: list[ListRetrieversRequestSortsType0Item] | None | Unset = UNSET
    case_sensitive: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_retrievers_request_filters_type_0 import ListRetrieversRequestFiltersType0

        search: None | str | Unset
        if isinstance(self.search, Unset):
            search = UNSET
        else:
            search = self.search

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, ListRetrieversRequestFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        sorts: list[dict[str, Any]] | None | Unset
        if isinstance(self.sorts, Unset):
            sorts = UNSET
        elif isinstance(self.sorts, list):
            sorts = []
            for sorts_type_0_item_data in self.sorts:
                sorts_type_0_item = sorts_type_0_item_data.to_dict()
                sorts.append(sorts_type_0_item)

        else:
            sorts = self.sorts

        case_sensitive = self.case_sensitive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search is not UNSET:
            field_dict["search"] = search
        if filters is not UNSET:
            field_dict["filters"] = filters
        if sorts is not UNSET:
            field_dict["sorts"] = sorts
        if case_sensitive is not UNSET:
            field_dict["case_sensitive"] = case_sensitive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_retrievers_request_filters_type_0 import ListRetrieversRequestFiltersType0
        from ..models.list_retrievers_request_sorts_type_0_item import ListRetrieversRequestSortsType0Item

        d = dict(src_dict)

        def _parse_search(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search = _parse_search(d.pop("search", UNSET))

        def _parse_filters(data: object) -> ListRetrieversRequestFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = ListRetrieversRequestFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListRetrieversRequestFiltersType0 | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_sorts(data: object) -> list[ListRetrieversRequestSortsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sorts_type_0 = []
                _sorts_type_0 = data
                for sorts_type_0_item_data in _sorts_type_0:
                    sorts_type_0_item = ListRetrieversRequestSortsType0Item.from_dict(sorts_type_0_item_data)

                    sorts_type_0.append(sorts_type_0_item)

                return sorts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ListRetrieversRequestSortsType0Item] | None | Unset, data)

        sorts = _parse_sorts(d.pop("sorts", UNSET))

        case_sensitive = d.pop("case_sensitive", UNSET)

        list_retrievers_request = cls(
            search=search,
            filters=filters,
            sorts=sorts,
            case_sensitive=case_sensitive,
        )

        list_retrievers_request.additional_properties = d
        return list_retrievers_request

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
