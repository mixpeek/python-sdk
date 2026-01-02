from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination_response import PaginationResponse
    from ..models.upload_list_stats import UploadListStats
    from ..models.upload_response import UploadResponse


T = TypeVar("T", bound="ListUploadsResponse")


@_attrs_define
class ListUploadsResponse:
    """Response model for listing uploads.

    Attributes:
        results (list[UploadResponse]): List of upload records matching the query
        pagination (PaginationResponse): PaginationResponse.

            Cursor-based pagination response:
            - Use next_cursor for navigation
            - Total count fields only populated when include_total=true
        stats (UploadListStats): Aggregate statistics for a list of uploads.
    """

    results: list[UploadResponse]
    pagination: PaginationResponse
    stats: UploadListStats
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        pagination = self.pagination.to_dict()

        stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "pagination": pagination,
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination_response import PaginationResponse
        from ..models.upload_list_stats import UploadListStats
        from ..models.upload_response import UploadResponse

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = UploadResponse.from_dict(results_item_data)

            results.append(results_item)

        pagination = PaginationResponse.from_dict(d.pop("pagination"))

        stats = UploadListStats.from_dict(d.pop("stats"))

        list_uploads_response = cls(
            results=results,
            pagination=pagination,
            stats=stats,
        )

        list_uploads_response.additional_properties = d
        return list_uploads_response

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
