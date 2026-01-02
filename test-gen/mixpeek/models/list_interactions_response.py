from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.interaction_response import InteractionResponse
    from ..models.pagination_response import PaginationResponse


T = TypeVar("T", bound="ListInteractionsResponse")


@_attrs_define
class ListInteractionsResponse:
    """Response for listing interactions with pagination.

    Returns a paginated list of interaction records matching the query filters.

        Attributes:
            results (list[InteractionResponse]): List of interactions matching the query filters
            pagination (PaginationResponse): PaginationResponse.

                Cursor-based pagination response:
                - Use next_cursor for navigation
                - Total count fields only populated when include_total=true
    """

    results: list[InteractionResponse]
    pagination: PaginationResponse
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interaction_response import InteractionResponse
        from ..models.pagination_response import PaginationResponse

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = InteractionResponse.from_dict(results_item_data)

            results.append(results_item)

        pagination = PaginationResponse.from_dict(d.pop("pagination"))

        list_interactions_response = cls(
            results=results,
            pagination=pagination,
        )

        list_interactions_response.additional_properties = d
        return list_interactions_response

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
