from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_update_documents_request_update_data import BulkUpdateDocumentsRequestUpdateData
    from ..models.logical_operator import LogicalOperator


T = TypeVar("T", bound="BulkUpdateDocumentsRequest")


@_attrs_define
class BulkUpdateDocumentsRequest:
    """Request model for bulk updating documents by filters.

    Updates ALL documents matching the provided filters with the SAME update_data.
    For updating specific documents by ID or different values per document, use BatchUpdateDocumentsRequest.

    Use Cases:
        - Update all pending documents to processed
        - Update all documents from a specific date range
        - Apply uniform changes across filtered document sets

    Requirements:
        - update_data: REQUIRED - fields to update on all matching documents
        - filters: OPTIONAL - if omitted, updates ALL documents in collection

        Attributes:
            update_data (BulkUpdateDocumentsRequestUpdateData): REQUIRED. Dictionary of field-value pairs to update on ALL
                matching documents. Can update any document field except vectors (metadata, source_blobs, etc.). All matched
                documents receive the SAME updates. Example: {'metadata.status': 'processed', 'metadata.reviewed': true}
            filters (LogicalOperator | None | Unset): OPTIONAL. Filter conditions to match documents for update. If not
                provided, updates ALL documents in the collection. Supports complex logical operators (AND, OR, NOT). Example:
                {'must': [{'key': 'metadata.status', 'value': 'pending'}]}
    """

    update_data: BulkUpdateDocumentsRequestUpdateData
    filters: LogicalOperator | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_operator import LogicalOperator

        update_data = self.update_data.to_dict()

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, LogicalOperator):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "update_data": update_data,
            }
        )
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_update_documents_request_update_data import BulkUpdateDocumentsRequestUpdateData
        from ..models.logical_operator import LogicalOperator

        d = dict(src_dict)
        update_data = BulkUpdateDocumentsRequestUpdateData.from_dict(d.pop("update_data"))

        def _parse_filters(data: object) -> LogicalOperator | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = LogicalOperator.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LogicalOperator | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        bulk_update_documents_request = cls(
            update_data=update_data,
            filters=filters,
        )

        bulk_update_documents_request.additional_properties = d
        return bulk_update_documents_request

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
