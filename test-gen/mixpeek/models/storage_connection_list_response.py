from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination_response import PaginationResponse
    from ..models.storage_connection_model import StorageConnectionModel


T = TypeVar("T", bound="StorageConnectionListResponse")


@_attrs_define
class StorageConnectionListResponse:
    """Response envelope for listing storage connections.

    Contains paginated results and metadata about the listing operation.

        Attributes:
            results (list[StorageConnectionModel]): List of storage connections matching the request filters. Results are
                paginated according to the pagination parameters. SECURITY: Sensitive credential fields are automatically
                redacted.
            pagination (PaginationResponse): PaginationResponse.

                Cursor-based pagination response:
                - Use next_cursor for navigation
                - Total count fields only populated when include_total=true
            total (int): Total number of connections matching the filters (before pagination). Use this to calculate total
                pages and display pagination controls.
    """

    results: list[StorageConnectionModel]
    pagination: PaginationResponse
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        pagination = self.pagination.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "pagination": pagination,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination_response import PaginationResponse
        from ..models.storage_connection_model import StorageConnectionModel

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = StorageConnectionModel.from_dict(results_item_data)

            results.append(results_item)

        pagination = PaginationResponse.from_dict(d.pop("pagination"))

        total = d.pop("total")

        storage_connection_list_response = cls(
            results=results,
            pagination=pagination,
            total=total,
        )

        storage_connection_list_response.additional_properties = d
        return storage_connection_list_response

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
