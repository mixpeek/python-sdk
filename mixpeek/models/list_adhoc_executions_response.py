from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adhoc_execution_summary import AdhocExecutionSummary


T = TypeVar("T", bound="ListAdhocExecutionsResponse")


@_attrs_define
class ListAdhocExecutionsResponse:
    """Response from listing ad-hoc retriever executions.

    Attributes:
        pagination (Any): Pagination metadata.
        results (list[AdhocExecutionSummary] | Unset): List of ad-hoc execution summaries.
        total (int | Unset): Total number of ad-hoc executions matching filters. Default: 0.
    """

    pagination: Any
    results: list[AdhocExecutionSummary] | Unset = UNSET
    total: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
            }
        )
        if results is not UNSET:
            field_dict["results"] = results
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.adhoc_execution_summary import AdhocExecutionSummary

        d = dict(src_dict)
        pagination = d.pop("pagination")

        _results = d.pop("results", UNSET)
        results: list[AdhocExecutionSummary] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = AdhocExecutionSummary.from_dict(results_item_data)

                results.append(results_item)

        total = d.pop("total", UNSET)

        list_adhoc_executions_response = cls(
            pagination=pagination,
            results=results,
            total=total,
        )

        list_adhoc_executions_response.additional_properties = d
        return list_adhoc_executions_response

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
