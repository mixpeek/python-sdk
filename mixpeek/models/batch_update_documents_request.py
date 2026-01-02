from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_document_update import BatchDocumentUpdate
    from ..models.batch_update_documents_request_update_data_type_0 import BatchUpdateDocumentsRequestUpdateDataType0
    from ..models.logical_operator import LogicalOperator


T = TypeVar("T", bound="BatchUpdateDocumentsRequest")


@_attrs_define
class BatchUpdateDocumentsRequest:
    """Request model for batch updating multiple documents by explicit IDs or filters.

    Supports TWO modes:
    1. Explicit IDs mode: Provide 'updates' array with document_id + update_data for each
    2. Filter mode: Provide 'filters' + 'update_data' to update all matching documents

    Key difference from BulkUpdateDocumentsRequest:
    - Batch (this): Can apply DIFFERENT updates to SPECIFIC documents by ID
    - Bulk: Applies SAME update to ALL documents matching filters

    Use Cases:
        - Update 5 specific documents with different metadata values
        - Update documents by IDs with per-document update control
        - Combine with filters for targeted batch updates

    Requirements:
        - EITHER 'updates' (explicit mode) OR 'filters' + 'update_data' (filter mode)
        - NOT BOTH modes simultaneously

        Attributes:
            updates (list[BatchDocumentUpdate] | None | Unset): OPTIONAL. List of document updates with explicit document
                IDs. Each entry specifies document_id and update_data. Use this mode when you know exact document IDs and want
                per-document control. Mutually exclusive with filters + update_data mode. Maximum 1000 documents per batch
                request.
            filters (LogicalOperator | None | Unset): OPTIONAL. Filter conditions to match documents for update. Must be
                used with 'update_data' field. Mutually exclusive with 'updates' array. If provided, applies same update_data to
                all matching documents.
            update_data (BatchUpdateDocumentsRequestUpdateDataType0 | None | Unset): OPTIONAL. Update data to apply when
                using filters mode. Must be used with 'filters' field. All matched documents receive the same updates. Can
                update any document field except vectors.
    """

    updates: list[BatchDocumentUpdate] | None | Unset = UNSET
    filters: LogicalOperator | None | Unset = UNSET
    update_data: BatchUpdateDocumentsRequestUpdateDataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_update_documents_request_update_data_type_0 import (
            BatchUpdateDocumentsRequestUpdateDataType0,
        )
        from ..models.logical_operator import LogicalOperator

        updates: list[dict[str, Any]] | None | Unset
        if isinstance(self.updates, Unset):
            updates = UNSET
        elif isinstance(self.updates, list):
            updates = []
            for updates_type_0_item_data in self.updates:
                updates_type_0_item = updates_type_0_item_data.to_dict()
                updates.append(updates_type_0_item)

        else:
            updates = self.updates

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, LogicalOperator):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        update_data: dict[str, Any] | None | Unset
        if isinstance(self.update_data, Unset):
            update_data = UNSET
        elif isinstance(self.update_data, BatchUpdateDocumentsRequestUpdateDataType0):
            update_data = self.update_data.to_dict()
        else:
            update_data = self.update_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if updates is not UNSET:
            field_dict["updates"] = updates
        if filters is not UNSET:
            field_dict["filters"] = filters
        if update_data is not UNSET:
            field_dict["update_data"] = update_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_document_update import BatchDocumentUpdate
        from ..models.batch_update_documents_request_update_data_type_0 import (
            BatchUpdateDocumentsRequestUpdateDataType0,
        )
        from ..models.logical_operator import LogicalOperator

        d = dict(src_dict)

        def _parse_updates(data: object) -> list[BatchDocumentUpdate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                updates_type_0 = []
                _updates_type_0 = data
                for updates_type_0_item_data in _updates_type_0:
                    updates_type_0_item = BatchDocumentUpdate.from_dict(updates_type_0_item_data)

                    updates_type_0.append(updates_type_0_item)

                return updates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BatchDocumentUpdate] | None | Unset, data)

        updates = _parse_updates(d.pop("updates", UNSET))

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

        def _parse_update_data(data: object) -> BatchUpdateDocumentsRequestUpdateDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                update_data_type_0 = BatchUpdateDocumentsRequestUpdateDataType0.from_dict(data)

                return update_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchUpdateDocumentsRequestUpdateDataType0 | None | Unset, data)

        update_data = _parse_update_data(d.pop("update_data", UNSET))

        batch_update_documents_request = cls(
            updates=updates,
            filters=filters,
            update_data=update_data,
        )

        batch_update_documents_request.additional_properties = d
        return batch_update_documents_request

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
