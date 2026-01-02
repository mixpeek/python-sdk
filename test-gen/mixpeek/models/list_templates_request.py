from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_scope import TemplateScope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_templates_request_filters_type_0 import ListTemplatesRequestFiltersType0
    from ..models.list_templates_request_sort_type_0 import ListTemplatesRequestSortType0


T = TypeVar("T", bound="ListTemplatesRequest")


@_attrs_define
class ListTemplatesRequest:
    """Request model for listing templates.

    Provides the same filtering, sorting, and search capabilities as other
    list operations (list collections, list buckets, etc.).

        Attributes:
            filters (ListTemplatesRequestFiltersType0 | None | Unset): Filters to apply when listing templates. Format:
                {"AND": [{"field": "field_name", "operator": "eq", "value": "value"}]}
            sort (ListTemplatesRequestSortType0 | None | Unset): Sort options for the results. Format: {'field': 'name',
                'direction': 'asc'}
            search (None | str | Unset): Search term for wildcard search across template_id, name, description, and tags
            scope (None | TemplateScope | Unset): Filter by scope (system, organization, or user)
            category (None | str | Unset): Filter by category
            is_active (bool | Unset): Show only active templates Default: True.
            tags (list[str] | None | Unset): Filter by tags (templates must have ALL specified tags)
    """

    filters: ListTemplatesRequestFiltersType0 | None | Unset = UNSET
    sort: ListTemplatesRequestSortType0 | None | Unset = UNSET
    search: None | str | Unset = UNSET
    scope: None | TemplateScope | Unset = UNSET
    category: None | str | Unset = UNSET
    is_active: bool | Unset = True
    tags: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_templates_request_filters_type_0 import ListTemplatesRequestFiltersType0
        from ..models.list_templates_request_sort_type_0 import ListTemplatesRequestSortType0

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, ListTemplatesRequestFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        sort: dict[str, Any] | None | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, ListTemplatesRequestSortType0):
            sort = self.sort.to_dict()
        else:
            sort = self.sort

        search: None | str | Unset
        if isinstance(self.search, Unset):
            search = UNSET
        else:
            search = self.search

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        elif isinstance(self.scope, TemplateScope):
            scope = self.scope.value
        else:
            scope = self.scope

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        is_active = self.is_active

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters
        if sort is not UNSET:
            field_dict["sort"] = sort
        if search is not UNSET:
            field_dict["search"] = search
        if scope is not UNSET:
            field_dict["scope"] = scope
        if category is not UNSET:
            field_dict["category"] = category
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_templates_request_filters_type_0 import ListTemplatesRequestFiltersType0
        from ..models.list_templates_request_sort_type_0 import ListTemplatesRequestSortType0

        d = dict(src_dict)

        def _parse_filters(data: object) -> ListTemplatesRequestFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = ListTemplatesRequestFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListTemplatesRequestFiltersType0 | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_sort(data: object) -> ListTemplatesRequestSortType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sort_type_0 = ListTemplatesRequestSortType0.from_dict(data)

                return sort_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListTemplatesRequestSortType0 | None | Unset, data)

        sort = _parse_sort(d.pop("sort", UNSET))

        def _parse_search(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search = _parse_search(d.pop("search", UNSET))

        def _parse_scope(data: object) -> None | TemplateScope | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scope_type_0 = TemplateScope(data)

                return scope_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TemplateScope | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        is_active = d.pop("is_active", UNSET)

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        list_templates_request = cls(
            filters=filters,
            sort=sort,
            search=search,
            scope=scope,
            category=category,
            is_active=is_active,
            tags=tags,
        )

        list_templates_request.additional_properties = d
        return list_templates_request

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
