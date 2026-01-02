from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logical_operator import LogicalOperator
    from ..models.sort_option import SortOption


T = TypeVar("T", bound="ListUploadsRequest")


@_attrs_define
class ListUploadsRequest:
    """Request model for listing uploads with filtering, sorting, and search.

    Provides flexible querying capabilities using the same filter/sort framework
    as documents, objects, and other list endpoints.

    Supports:
        - Complex filters using LogicalOperator (AND, OR, NOT)
        - Shorthand filter syntax: {"metadata.campaign": "summer_2024"}
        - Full-text search across filename and metadata
        - Multi-field sorting
        - Pagination with limit/offset

    Examples:
        - List all pending uploads in a bucket
        - Find uploads by metadata campaign
        - Search for uploads by filename pattern
        - Sort by file size or creation date

        Attributes:
            filters (LogicalOperator | None | Unset): Complex filters using logical operators (AND, OR, NOT). Supports
                shorthand syntax: pass field-value pairs for equality matching. Examples:   - Filter by status: {'status':
                'PENDING'}   - Filter by metadata: {'metadata.campaign': 'summer_2024'}   - Complex: {'AND': [{'field':
                'status', 'operator': 'eq', 'value': 'PENDING'},                       {'field': 'file_size_bytes', 'operator':
                'gte', 'value': 1000000}]} See LogicalOperator documentation for full syntax.
            sort (None | SortOption | Unset): Sort options for ordering results. Can sort by any field including metadata
                fields using dot notation. Default: created_at descending (newest first). Examples:   - Sort by creation date:
                {'field': 'created_at', 'direction': 'desc'}   - Sort by file size: {'field': 'file_size_bytes', 'direction':
                'asc'}   - Sort by metadata: {'field': 'metadata.priority', 'direction': 'desc'}
            search (None | str | Unset): Full-text search across filename and metadata fields. Case-insensitive partial
                matching. Searches in: filename, metadata values (converted to strings). Examples:   - 'video' - finds
                'product_video.mp4', 'tutorial_video.mov'   - 'summer' - finds uploads with metadata.campaign='summer_2024'
            return_presigned_urls (bool | Unset): Whether to regenerate presigned URLs for S3 access in the response.
                OPTIONAL, defaults to false. If true:   - Generates new GET presigned URLs for completed uploads   - Useful for
                downloading files from S3   - Adds ~50ms per upload to response time. If false:   - No presigned URLs in
                response   - Faster response time. Note: Original PUT presigned URLs are never returned (security). Default:
                False.
            limit (int | Unset): Maximum number of uploads to return. OPTIONAL, defaults to 20. Default: 20.
            offset (int | Unset): Number of uploads to skip for pagination. OPTIONAL, defaults to 0. Default: 0.
    """

    filters: LogicalOperator | None | Unset = UNSET
    sort: None | SortOption | Unset = UNSET
    search: None | str | Unset = UNSET
    return_presigned_urls: bool | Unset = False
    limit: int | Unset = 20
    offset: int | Unset = 0
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

        return_presigned_urls = self.return_presigned_urls

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters
        if sort is not UNSET:
            field_dict["sort"] = sort
        if search is not UNSET:
            field_dict["search"] = search
        if return_presigned_urls is not UNSET:
            field_dict["return_presigned_urls"] = return_presigned_urls
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

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

        return_presigned_urls = d.pop("return_presigned_urls", UNSET)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        list_uploads_request = cls(
            filters=filters,
            sort=sort,
            search=search,
            return_presigned_urls=return_presigned_urls,
            limit=limit,
            offset=offset,
        )

        list_uploads_request.additional_properties = d
        return list_uploads_request

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
