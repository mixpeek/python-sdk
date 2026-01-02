from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logical_operator import LogicalOperator
    from ..models.sort_option import SortOption


T = TypeVar("T", bound="ListDocumentsRequest")


@_attrs_define
class ListDocumentsRequest:
    """Request model for listing documents.

    Supports two pagination strategies:

    **Offset-based (default)**: Use query params `?page=2&page_size=10`
    - Simple and familiar
    - Works well for shallow pagination (first ~100 pages)
    - Less efficient for deep pagination with sorting

    **Cursor-based (optional)**: Pass `cursor` from previous response's `next_cursor`
    - More efficient for deep pagination (page 100+)
    - Required for consistent results when sorting large datasets
    - When cursor is provided, offset is ignored

        Attributes:
            filters (LogicalOperator | None | Unset): Filters to apply.
            sort (None | SortOption | Unset): Sort options.
            search (None | str | Unset): Search term.
            cursor (None | str | Unset): OPTIONAL cursor for efficient deep pagination. Pass the 'pagination.next_cursor'
                value from a previous response to fetch the next page. When cursor is provided, the page/offset query params are
                ignored. Use cursor-based pagination when: (1) paginating beyond page ~100, (2) sorting large datasets, or (3)
                you need consistent iteration. Use offset-based pagination (default) for: simple use cases, random page access,
                or when page numbers are needed in the UI.
            return_url (bool | None | Unset): Whether to return presigned URLs for object keys. Default: False.
            return_vectors (bool | None | Unset): Whether to return vector embeddings in the document results. Default:
                False.
            group_by (None | str | Unset): OPTIONAL. Field to group documents by. Supports dot notation for nested fields
                (e.g., 'metadata.category', 'source_type'). When specified, documents are grouped by the field value and
                returned as grouped results. Requires a payload index on the field in Qdrant for optimal performance. If no
                index exists, the operation will fail with a validation error. Common groupable fields: 'source_object_id',
                'root_object_id', 'collection_id', 'metadata.category'.
            select (list[str] | None | Unset): OPTIONAL. List of fields to include in the response. Supports dot notation
                for nested fields (e.g., 'metadata.title', 'content'). When specified, only the selected fields will be returned
                in the document results, reducing response size. System fields like '_id' and 'document_id' are always included.
                Use this to optimize response size when working with large documents.
    """

    filters: LogicalOperator | None | Unset = UNSET
    sort: None | SortOption | Unset = UNSET
    search: None | str | Unset = UNSET
    cursor: None | str | Unset = UNSET
    return_url: bool | None | Unset = False
    return_vectors: bool | None | Unset = False
    group_by: None | str | Unset = UNSET
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

        cursor: None | str | Unset
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        return_url: bool | None | Unset
        if isinstance(self.return_url, Unset):
            return_url = UNSET
        else:
            return_url = self.return_url

        return_vectors: bool | None | Unset
        if isinstance(self.return_vectors, Unset):
            return_vectors = UNSET
        else:
            return_vectors = self.return_vectors

        group_by: None | str | Unset
        if isinstance(self.group_by, Unset):
            group_by = UNSET
        else:
            group_by = self.group_by

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
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if return_url is not UNSET:
            field_dict["return_url"] = return_url
        if return_vectors is not UNSET:
            field_dict["return_vectors"] = return_vectors
        if group_by is not UNSET:
            field_dict["group_by"] = group_by
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

        def _parse_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        def _parse_return_url(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        return_url = _parse_return_url(d.pop("return_url", UNSET))

        def _parse_return_vectors(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        return_vectors = _parse_return_vectors(d.pop("return_vectors", UNSET))

        def _parse_group_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_by = _parse_group_by(d.pop("group_by", UNSET))

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

        list_documents_request = cls(
            filters=filters,
            sort=sort,
            search=search,
            cursor=cursor,
            return_url=return_url,
            return_vectors=return_vectors,
            group_by=group_by,
            select=select,
        )

        list_documents_request.additional_properties = d
        return list_documents_request

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
