from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartEvaluationResponse")


@_attrs_define
class StartEvaluationResponse:
    """Response when starting an evaluation.

    Attributes:
        task_id (str): Task ID for tracking progress
        evaluation_id (str): Evaluation ID
        created_at (str): Creation timestamp
        task_type (str | Unset): Task type Default: 'retriever.evaluation'.
        status (str | Unset): Initial status Default: 'pending'.
    """

    task_id: str
    evaluation_id: str
    created_at: str
    task_type: str | Unset = "retriever.evaluation"
    status: str | Unset = "pending"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        evaluation_id = self.evaluation_id

        created_at = self.created_at

        task_type = self.task_type

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
                "evaluation_id": evaluation_id,
                "created_at": created_at,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = d.pop("task_id")

        evaluation_id = d.pop("evaluation_id")

        created_at = d.pop("created_at")

        task_type = d.pop("task_type", UNSET)

        status = d.pop("status", UNSET)

        start_evaluation_response = cls(
            task_id=task_id,
            evaluation_id=evaluation_id,
            created_at=created_at,
            task_type=task_type,
            status=status,
        )

        start_evaluation_response.additional_properties = d
        return start_evaluation_response

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
