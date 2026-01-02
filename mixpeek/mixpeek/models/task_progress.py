from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskProgress")


@_attrs_define
class TaskProgress:
    """Progress information for a task.

    Attributes:
        processed_documents (int | Unset): Number of documents processed Default: 0.
        total_documents (int | Unset): Total documents to process Default: 0.
        percentage (float | Unset): Progress percentage (0-100) Default: 0.0.
    """

    processed_documents: int | Unset = 0
    total_documents: int | Unset = 0
    percentage: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        processed_documents = self.processed_documents

        total_documents = self.total_documents

        percentage = self.percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if processed_documents is not UNSET:
            field_dict["processed_documents"] = processed_documents
        if total_documents is not UNSET:
            field_dict["total_documents"] = total_documents
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        processed_documents = d.pop("processed_documents", UNSET)

        total_documents = d.pop("total_documents", UNSET)

        percentage = d.pop("percentage", UNSET)

        task_progress = cls(
            processed_documents=processed_documents,
            total_documents=total_documents,
            percentage=percentage,
        )

        task_progress.additional_properties = d
        return task_progress

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
