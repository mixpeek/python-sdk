from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_group import DocumentGroup
    from ..models.document_list_stats import DocumentListStats
    from ..models.document_response import DocumentResponse
    from ..models.pagination_response import PaginationResponse


T = TypeVar("T", bound="ListDocumentsResponse")


@_attrs_define
class ListDocumentsResponse:
    """Response model for listing documents.

    Supports both regular document lists and grouped results based on the group_by parameter.
    When group_by is specified, results are returned as groups instead of a flat list.

    Pagination strategies:
    - **Offset-based (default)**: Use `pagination.page` and `pagination.page_size`
    - **Cursor-based (optional)**: Use `pagination.next_cursor` for efficient deep pagination

        Attributes:
            pagination (PaginationResponse): PaginationResponse.

                Cursor-based pagination response:
                - Use next_cursor for navigation
                - Total count fields only populated when include_total=true
            results (list[DocumentResponse] | None | Unset): List of documents when group_by is NOT specified. Contains flat
                list of documents with pagination applied. Mutually exclusive with 'groups' field.
            groups (list[DocumentGroup] | None | Unset): List of document groups when group_by IS specified. Each group
                contains documents sharing the same field value. Pagination applies to groups, not individual documents.
                Mutually exclusive with 'results' field.
            stats (DocumentListStats | None | Unset): Aggregate statistics across all documents in the result
            group_by_field (None | str | Unset): The field that was used for grouping when group_by was specified. None for
                non-grouped results. Useful for clients to understand the grouping structure.
    """

    pagination: PaginationResponse
    results: list[DocumentResponse] | None | Unset = UNSET
    groups: list[DocumentGroup] | None | Unset = UNSET
    stats: DocumentListStats | None | Unset = UNSET
    group_by_field: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.document_list_stats import DocumentListStats

        pagination = self.pagination.to_dict()

        results: list[dict[str, Any]] | None | Unset
        if isinstance(self.results, Unset):
            results = UNSET
        elif isinstance(self.results, list):
            results = []
            for results_type_0_item_data in self.results:
                results_type_0_item = results_type_0_item_data.to_dict()
                results.append(results_type_0_item)

        else:
            results = self.results

        groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = groups_type_0_item_data.to_dict()
                groups.append(groups_type_0_item)

        else:
            groups = self.groups

        stats: dict[str, Any] | None | Unset
        if isinstance(self.stats, Unset):
            stats = UNSET
        elif isinstance(self.stats, DocumentListStats):
            stats = self.stats.to_dict()
        else:
            stats = self.stats

        group_by_field: None | str | Unset
        if isinstance(self.group_by_field, Unset):
            group_by_field = UNSET
        else:
            group_by_field = self.group_by_field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
            }
        )
        if results is not UNSET:
            field_dict["results"] = results
        if groups is not UNSET:
            field_dict["groups"] = groups
        if stats is not UNSET:
            field_dict["stats"] = stats
        if group_by_field is not UNSET:
            field_dict["group_by_field"] = group_by_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_group import DocumentGroup
        from ..models.document_list_stats import DocumentListStats
        from ..models.document_response import DocumentResponse
        from ..models.pagination_response import PaginationResponse

        d = dict(src_dict)
        pagination = PaginationResponse.from_dict(d.pop("pagination"))

        def _parse_results(data: object) -> list[DocumentResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                results_type_0 = []
                _results_type_0 = data
                for results_type_0_item_data in _results_type_0:
                    results_type_0_item = DocumentResponse.from_dict(results_type_0_item_data)

                    results_type_0.append(results_type_0_item)

                return results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DocumentResponse] | None | Unset, data)

        results = _parse_results(d.pop("results", UNSET))

        def _parse_groups(data: object) -> list[DocumentGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in _groups_type_0:
                    groups_type_0_item = DocumentGroup.from_dict(groups_type_0_item_data)

                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DocumentGroup] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))

        def _parse_stats(data: object) -> DocumentListStats | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stats_type_0 = DocumentListStats.from_dict(data)

                return stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DocumentListStats | None | Unset, data)

        stats = _parse_stats(d.pop("stats", UNSET))

        def _parse_group_by_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_by_field = _parse_group_by_field(d.pop("group_by_field", UNSET))

        list_documents_response = cls(
            pagination=pagination,
            results=results,
            groups=groups,
            stats=stats,
            group_by_field=group_by_field,
        )

        list_documents_response.additional_properties = d
        return list_documents_response

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
