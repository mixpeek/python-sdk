from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_document_update_result import BatchDocumentUpdateResult


T = TypeVar("T", bound="BatchUpdateDocumentsResponse")


@_attrs_define
class BatchUpdateDocumentsResponse:
    """Response model for batch document update operation.

    Provides detailed per-document results showing success/failure for each update.

        Attributes:
            updated_count (int): Total number of documents successfully updated
            failed_count (int | Unset): Total number of documents that failed to update Default: 0.
            results (list[BatchDocumentUpdateResult] | Unset): Detailed per-document results. Each entry shows document_id,
                success status, and error message (if failed). Empty list when using filter mode (only counts returned).
            message (str | Unset): Summary message of the operation Default: 'Batch update completed'.
    """

    updated_count: int
    failed_count: int | Unset = 0
    results: list[BatchDocumentUpdateResult] | Unset = UNSET
    message: str | Unset = "Batch update completed"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_count = self.updated_count

        failed_count = self.failed_count

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updated_count": updated_count,
            }
        )
        if failed_count is not UNSET:
            field_dict["failed_count"] = failed_count
        if results is not UNSET:
            field_dict["results"] = results
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_document_update_result import BatchDocumentUpdateResult

        d = dict(src_dict)
        updated_count = d.pop("updated_count")

        failed_count = d.pop("failed_count", UNSET)

        _results = d.pop("results", UNSET)
        results: list[BatchDocumentUpdateResult] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = BatchDocumentUpdateResult.from_dict(results_item_data)

                results.append(results_item)

        message = d.pop("message", UNSET)

        batch_update_documents_response = cls(
            updated_count=updated_count,
            failed_count=failed_count,
            results=results,
            message=message,
        )

        batch_update_documents_response.additional_properties = d
        return batch_update_documents_response

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
