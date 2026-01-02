from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmitBatchRequest")


@_attrs_define
class SubmitBatchRequest:
    """Request model for submitting a batch for processing.

    This model allows configuration of processing behavior for the batch,
    such as whether to track processing history in document metadata.

    Use Cases:
        - Submit batch with full audit trail (include_processing_history=True)
        - Submit batch without processing history for cleaner metadata (include_processing_history=False)
        - Default behavior includes processing history for debugging and lineage tracking

    Requirements:
        - include_processing_history: OPTIONAL, defaults to True

        Attributes:
            include_processing_history (bool | Unset): OPTIONAL (defaults to True). Controls whether processing operations
                are tracked in document internal_metadata.processing_history. When True: Each enrichment operation (taxonomy
                application, clustering, etc.) adds an audit trail entry. When False: Documents are enriched without processing
                history tracking, resulting in cleaner metadata. Use True for: Debugging, audit requirements, lineage tracking,
                understanding document transformations. Use False for: Production workloads where metadata size matters,
                simplified document structure. Processing history entries include: operation type, timestamp, and IDs of applied
                resources (taxonomies, clusters, etc.). Default: True.
    """

    include_processing_history: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_processing_history = self.include_processing_history

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_processing_history is not UNSET:
            field_dict["include_processing_history"] = include_processing_history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_processing_history = d.pop("include_processing_history", UNSET)

        submit_batch_request = cls(
            include_processing_history=include_processing_history,
        )

        submit_batch_request.additional_properties = d
        return submit_batch_request

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
