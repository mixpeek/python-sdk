from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.error_category import ErrorCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_error_detail_metadata import BatchErrorDetailMetadata


T = TypeVar("T", bound="BatchErrorDetail")


@_attrs_define
class BatchErrorDetail:
    """Detailed error information for batch processing failures.

    Provides structured error tracking at both object and batch levels.
    Enables better debugging, retry logic, and error analytics.

    Use Cases:
        - Track specific errors that occurred during processing
        - Identify error patterns across multiple documents
        - Provide actionable recovery suggestions
        - Enable intelligent retry logic based on error type

    Object-level tracking: Attached to individual document processing failures
    Batch-level tracking: Aggregated summaries in batch metadata

        Attributes:
            error_type (ErrorCategory): Categories for batch processing errors.

                Used to classify errors for better observability, retry logic, and debugging.
                Helps distinguish between transient errors (worth retrying) and permanent errors.
            message (str): REQUIRED. Human-readable error message. Concise description of what went wrong. Should be
                actionable and help users understand the issue.
            component (None | str | Unset): OPTIONAL. Component or service where the error occurred. Helps identify which
                part of the system failed. Examples: service class names, module names, or feature names.
            stage (None | str | Unset): OPTIONAL. Processing stage where the error occurred. Identifies which pipeline stage
                failed. Examples: pipeline stage names from collection configuration.
            traceback (None | str | Unset): OPTIONAL. Full Python traceback for debugging. Includes stack trace for code-
                level troubleshooting. Should be truncated if too long (e.g., max 2000 chars).
            timestamp (datetime.datetime | Unset): REQUIRED. ISO 8601 timestamp when the error occurred. Used for
                chronological error tracking and debugging.
            affected_document_ids (list[str] | Unset): OPTIONAL. List of document IDs affected by this error. For object-
                level errors: contains single document ID. For batch-level aggregation: contains all affected document IDs. Used
                to identify scope of impact.
            affected_count (int | Unset): REQUIRED. Number of documents affected by this error. For object-level: typically
                1. For batch-level aggregation: total count of affected documents. Used for error impact analysis. Default: 1.
            recovery_suggestion (None | str | Unset): OPTIONAL. Actionable suggestion for resolving the error. Helps users
                quickly fix common issues. Examples: install missing package, check credentials, update schema.
            metadata (BatchErrorDetailMetadata | Unset): OPTIONAL. Additional error context and metadata. Free-form
                dictionary for error-specific details. Examples: retry_count, last_retry_at, error_code, http_status.
    """

    error_type: ErrorCategory
    message: str
    component: None | str | Unset = UNSET
    stage: None | str | Unset = UNSET
    traceback: None | str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    affected_document_ids: list[str] | Unset = UNSET
    affected_count: int | Unset = 1
    recovery_suggestion: None | str | Unset = UNSET
    metadata: BatchErrorDetailMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_type = self.error_type.value

        message = self.message

        component: None | str | Unset
        if isinstance(self.component, Unset):
            component = UNSET
        else:
            component = self.component

        stage: None | str | Unset
        if isinstance(self.stage, Unset):
            stage = UNSET
        else:
            stage = self.stage

        traceback: None | str | Unset
        if isinstance(self.traceback, Unset):
            traceback = UNSET
        else:
            traceback = self.traceback

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        affected_document_ids: list[str] | Unset = UNSET
        if not isinstance(self.affected_document_ids, Unset):
            affected_document_ids = self.affected_document_ids

        affected_count = self.affected_count

        recovery_suggestion: None | str | Unset
        if isinstance(self.recovery_suggestion, Unset):
            recovery_suggestion = UNSET
        else:
            recovery_suggestion = self.recovery_suggestion

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error_type": error_type,
                "message": message,
            }
        )
        if component is not UNSET:
            field_dict["component"] = component
        if stage is not UNSET:
            field_dict["stage"] = stage
        if traceback is not UNSET:
            field_dict["traceback"] = traceback
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if affected_document_ids is not UNSET:
            field_dict["affected_document_ids"] = affected_document_ids
        if affected_count is not UNSET:
            field_dict["affected_count"] = affected_count
        if recovery_suggestion is not UNSET:
            field_dict["recovery_suggestion"] = recovery_suggestion
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_error_detail_metadata import BatchErrorDetailMetadata

        d = dict(src_dict)
        error_type = ErrorCategory(d.pop("error_type"))

        message = d.pop("message")

        def _parse_component(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        component = _parse_component(d.pop("component", UNSET))

        def _parse_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage = _parse_stage(d.pop("stage", UNSET))

        def _parse_traceback(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        traceback = _parse_traceback(d.pop("traceback", UNSET))

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        affected_document_ids = cast(list[str], d.pop("affected_document_ids", UNSET))

        affected_count = d.pop("affected_count", UNSET)

        def _parse_recovery_suggestion(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recovery_suggestion = _parse_recovery_suggestion(d.pop("recovery_suggestion", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: BatchErrorDetailMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = BatchErrorDetailMetadata.from_dict(_metadata)

        batch_error_detail = cls(
            error_type=error_type,
            message=message,
            component=component,
            stage=stage,
            traceback=traceback,
            timestamp=timestamp,
            affected_document_ids=affected_document_ids,
            affected_count=affected_count,
            recovery_suggestion=recovery_suggestion,
            metadata=metadata,
        )

        batch_error_detail.additional_properties = d
        return batch_error_detail

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
