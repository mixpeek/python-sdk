from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.evaluation_record import EvaluationRecord


T = TypeVar("T", bound="EvaluationListResponse")


@_attrs_define
class EvaluationListResponse:
    """Response for listing evaluations.

    Attributes:
        evaluations (list[EvaluationRecord]): List of evaluations
        total (int): Total count
        page (int): Current page
        page_size (int): Page size
    """

    evaluations: list[EvaluationRecord]
    total: int
    page: int
    page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        evaluations = []
        for evaluations_item_data in self.evaluations:
            evaluations_item = evaluations_item_data.to_dict()
            evaluations.append(evaluations_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "evaluations": evaluations,
                "total": total,
                "page": page,
                "page_size": page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evaluation_record import EvaluationRecord

        d = dict(src_dict)
        evaluations = []
        _evaluations = d.pop("evaluations")
        for evaluations_item_data in _evaluations:
            evaluations_item = EvaluationRecord.from_dict(evaluations_item_data)

            evaluations.append(evaluations_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        evaluation_list_response = cls(
            evaluations=evaluations,
            total=total,
            page=page,
            page_size=page_size,
        )

        evaluation_list_response.additional_properties = d
        return evaluation_list_response

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
