from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentListStats")


@_attrs_define
class DocumentListStats:
    """Aggregate statistics for a list of documents.

    Attributes:
        total_documents (int | Unset): Total number of documents in the result Default: 0.
        avg_blobs_per_document (float | Unset): Average number of source blobs per document Default: 0.0.
        total_groups (int | None | Unset): Total number of groups when group_by is used. None for non-grouped results.
        avg_documents_per_group (float | None | Unset): Average number of documents per group when group_by is used.
            None for non-grouped results.
    """

    total_documents: int | Unset = 0
    avg_blobs_per_document: float | Unset = 0.0
    total_groups: int | None | Unset = UNSET
    avg_documents_per_group: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_documents = self.total_documents

        avg_blobs_per_document = self.avg_blobs_per_document

        total_groups: int | None | Unset
        if isinstance(self.total_groups, Unset):
            total_groups = UNSET
        else:
            total_groups = self.total_groups

        avg_documents_per_group: float | None | Unset
        if isinstance(self.avg_documents_per_group, Unset):
            avg_documents_per_group = UNSET
        else:
            avg_documents_per_group = self.avg_documents_per_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_documents is not UNSET:
            field_dict["total_documents"] = total_documents
        if avg_blobs_per_document is not UNSET:
            field_dict["avg_blobs_per_document"] = avg_blobs_per_document
        if total_groups is not UNSET:
            field_dict["total_groups"] = total_groups
        if avg_documents_per_group is not UNSET:
            field_dict["avg_documents_per_group"] = avg_documents_per_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_documents = d.pop("total_documents", UNSET)

        avg_blobs_per_document = d.pop("avg_blobs_per_document", UNSET)

        def _parse_total_groups(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_groups = _parse_total_groups(d.pop("total_groups", UNSET))

        def _parse_avg_documents_per_group(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_documents_per_group = _parse_avg_documents_per_group(d.pop("avg_documents_per_group", UNSET))

        document_list_stats = cls(
            total_documents=total_documents,
            avg_blobs_per_document=avg_blobs_per_document,
            total_groups=total_groups,
            avg_documents_per_group=avg_documents_per_group,
        )

        document_list_stats.additional_properties = d
        return document_list_stats

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
