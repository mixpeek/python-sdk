from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_retriever_list_item import PublicRetrieverListItem
    from ..models.public_retriever_list_stats import PublicRetrieverListStats


T = TypeVar("T", bound="ListPublicRetrieversResponse")


@_attrs_define
class ListPublicRetrieversResponse:
    """Response for listing public retrievers.

    Follows the same pattern as ListCollectionsResponse for consistent developer experience.

        Attributes:
            results (list[PublicRetrieverListItem]): List of public retrievers
            total_count (int): Total number of public retrievers matching the query
            page (int): Current page number
            page_size (int): Results per page
            total_pages (int): Total number of pages
            stats (None | PublicRetrieverListStats | Unset): Aggregate statistics across all public retrievers
    """

    results: list[PublicRetrieverListItem]
    total_count: int
    page: int
    page_size: int
    total_pages: int
    stats: None | PublicRetrieverListStats | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.public_retriever_list_stats import PublicRetrieverListStats

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        total_count = self.total_count

        page = self.page

        page_size = self.page_size

        total_pages = self.total_pages

        stats: dict[str, Any] | None | Unset
        if isinstance(self.stats, Unset):
            stats = UNSET
        elif isinstance(self.stats, PublicRetrieverListStats):
            stats = self.stats.to_dict()
        else:
            stats = self.stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "total_count": total_count,
                "page": page,
                "page_size": page_size,
                "total_pages": total_pages,
            }
        )
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_retriever_list_item import PublicRetrieverListItem
        from ..models.public_retriever_list_stats import PublicRetrieverListStats

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = PublicRetrieverListItem.from_dict(results_item_data)

            results.append(results_item)

        total_count = d.pop("total_count")

        page = d.pop("page")

        page_size = d.pop("page_size")

        total_pages = d.pop("total_pages")

        def _parse_stats(data: object) -> None | PublicRetrieverListStats | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stats_type_0 = PublicRetrieverListStats.from_dict(data)

                return stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublicRetrieverListStats | Unset, data)

        stats = _parse_stats(d.pop("stats", UNSET))

        list_public_retrievers_response = cls(
            results=results,
            total_count=total_count,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
            stats=stats,
        )

        list_public_retrievers_response.additional_properties = d
        return list_public_retrievers_response

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
