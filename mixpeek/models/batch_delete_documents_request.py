from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logical_operator import LogicalOperator


T = TypeVar("T", bound="BatchDeleteDocumentsRequest")


@_attrs_define
class BatchDeleteDocumentsRequest:
    """Request model for batch deleting multiple documents by explicit IDs or filters.

    Supports TWO modes:
    1. Explicit IDs mode: Provide 'document_ids' array
    2. Filter mode: Provide 'filters' to delete all matching documents

    Use Cases:
        - Delete 5 specific documents in one API call
        - Delete all documents matching criteria
        - Bulk cleanup operations

    Requirements:
        - EITHER 'document_ids' OR 'filters' must be provided
        - NOT BOTH modes simultaneously

        Attributes:
            document_ids (list[str] | None | Unset): OPTIONAL. List of document IDs to delete. Use this mode when you know
                exact document IDs to delete. Mutually exclusive with filters mode. Maximum 1000 documents per batch request.
            filters (LogicalOperator | None | Unset): OPTIONAL. Filter conditions to match documents for deletion. Mutually
                exclusive with 'document_ids' array. If provided, deletes ALL documents matching the filters. Use with caution -
                can delete many documents at once.
    """

    document_ids: list[str] | None | Unset = UNSET
    filters: LogicalOperator | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_operator import LogicalOperator

        document_ids: list[str] | None | Unset
        if isinstance(self.document_ids, Unset):
            document_ids = UNSET
        elif isinstance(self.document_ids, list):
            document_ids = self.document_ids

        else:
            document_ids = self.document_ids

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, LogicalOperator):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_ids is not UNSET:
            field_dict["document_ids"] = document_ids
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logical_operator import LogicalOperator

        d = dict(src_dict)

        def _parse_document_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                document_ids_type_0 = cast(list[str], data)

                return document_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        document_ids = _parse_document_ids(d.pop("document_ids", UNSET))

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

        batch_delete_documents_request = cls(
            document_ids=document_ids,
            filters=filters,
        )

        batch_delete_documents_request.additional_properties = d
        return batch_delete_documents_request

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
