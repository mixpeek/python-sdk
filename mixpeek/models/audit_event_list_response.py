from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_event_response import AuditEventResponse


T = TypeVar("T", bound="AuditEventListResponse")


@_attrs_define
class AuditEventListResponse:
    """Response for listing audit events.

    Attributes:
        results (list[AuditEventResponse]): Audit events
        total (int): Total count matching filters
        skip (int): Number of results skipped
        limit (int): Number of results returned
    """

    results: list[AuditEventResponse]
    total: int
    skip: int
    limit: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        total = self.total

        skip = self.skip

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "total": total,
                "skip": skip,
                "limit": limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_event_response import AuditEventResponse

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = AuditEventResponse.from_dict(results_item_data)

            results.append(results_item)

        total = d.pop("total")

        skip = d.pop("skip")

        limit = d.pop("limit")

        audit_event_list_response = cls(
            results=results,
            total=total,
            skip=skip,
            limit=limit,
        )

        audit_event_list_response.additional_properties = d
        return audit_event_list_response

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
