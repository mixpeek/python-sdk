from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_status_enum import TaskStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfirmUploadResponse")


@_attrs_define
class ConfirmUploadResponse:
    """Response from upload confirmation.

    Attributes:
        upload_id (str): Upload ID that was confirmed
        status (TaskStatusEnum): Enumeration of task statuses for tracking asynchronous operations.

            Task statuses indicate the current state of asynchronous operations like
            batch processing, object ingestion, clustering, and taxonomy execution.

            Status Categories:
                Operation Statuses: Track progress of async operations
                Lifecycle Statuses: Track entity state (buckets, collections, namespaces)

            Values:
                PENDING: Task is queued but has not started processing yet
                IN_PROGRESS: Task is currently being executed
                PROCESSING: Task is actively processing data (similar to IN_PROGRESS)
                COMPLETED: Task finished successfully with no errors
                COMPLETED_WITH_ERRORS: Task finished but some items failed (partial success)
                FAILED: Task encountered an error and could not complete
                CANCELED: Task was manually canceled by a user or system
                UNKNOWN: Task status could not be determined
                SKIPPED: Task was intentionally skipped
                DRAFT: Task is in draft state and not yet submitted

                ACTIVE: Entity is active and operational (for buckets, collections, etc.)
                ARCHIVED: Entity has been archived
                SUSPENDED: Entity has been temporarily suspended

            Terminal Statuses:
                COMPLETED, COMPLETED_WITH_ERRORS, FAILED, CANCELED are terminal statuses.
                Once a task reaches these states, it will not transition to another state.

            Partial Success Handling:
                COMPLETED_WITH_ERRORS indicates that the operation completed but some
                documents/items failed. The task result includes:
                - List of successful items
                - List of failed items with error details
                - Success rate percentage
                This allows clients to handle partial success scenarios appropriately.

            Polling Guidance:
                - Poll tasks in PENDING, IN_PROGRESS, or PROCESSING states
                - Stop polling when task reaches COMPLETED, COMPLETED_WITH_ERRORS, FAILED, or CANCELED
                - Use exponential backoff (1s → 30s) when polling
        etag (None | str | Unset): S3 ETag from uploaded object
        file_size_bytes (int | None | Unset): Actual file size from S3
        file_hash (None | str | Unset): File content hash (from ETag)
        verified_at (datetime.datetime | None | Unset): When verification completed
        completed_at (datetime.datetime | None | Unset): When upload completed
        object_id (None | str | Unset): Created bucket object ID (if create_object_on_confirm was true)
        task_id (None | str | Unset): Task ID for async processing (if async=true)
        message (None | str | Unset): Confirmation message
    """

    upload_id: str
    status: TaskStatusEnum
    etag: None | str | Unset = UNSET
    file_size_bytes: int | None | Unset = UNSET
    file_hash: None | str | Unset = UNSET
    verified_at: datetime.datetime | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    object_id: None | str | Unset = UNSET
    task_id: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_id = self.upload_id

        status = self.status.value

        etag: None | str | Unset
        if isinstance(self.etag, Unset):
            etag = UNSET
        else:
            etag = self.etag

        file_size_bytes: int | None | Unset
        if isinstance(self.file_size_bytes, Unset):
            file_size_bytes = UNSET
        else:
            file_size_bytes = self.file_size_bytes

        file_hash: None | str | Unset
        if isinstance(self.file_hash, Unset):
            file_hash = UNSET
        else:
            file_hash = self.file_hash

        verified_at: None | str | Unset
        if isinstance(self.verified_at, Unset):
            verified_at = UNSET
        elif isinstance(self.verified_at, datetime.datetime):
            verified_at = self.verified_at.isoformat()
        else:
            verified_at = self.verified_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        object_id: None | str | Unset
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        else:
            object_id = self.object_id

        task_id: None | str | Unset
        if isinstance(self.task_id, Unset):
            task_id = UNSET
        else:
            task_id = self.task_id

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upload_id": upload_id,
                "status": status,
            }
        )
        if etag is not UNSET:
            field_dict["etag"] = etag
        if file_size_bytes is not UNSET:
            field_dict["file_size_bytes"] = file_size_bytes
        if file_hash is not UNSET:
            field_dict["file_hash"] = file_hash
        if verified_at is not UNSET:
            field_dict["verified_at"] = verified_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upload_id = d.pop("upload_id")

        status = TaskStatusEnum(d.pop("status"))

        def _parse_etag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        etag = _parse_etag(d.pop("etag", UNSET))

        def _parse_file_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size_bytes = _parse_file_size_bytes(d.pop("file_size_bytes", UNSET))

        def _parse_file_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_hash = _parse_file_hash(d.pop("file_hash", UNSET))

        def _parse_verified_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verified_at_type_0 = isoparse(data)

                return verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        verified_at = _parse_verified_at(d.pop("verified_at", UNSET))

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_id = _parse_object_id(d.pop("object_id", UNSET))

        def _parse_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_id = _parse_task_id(d.pop("task_id", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        confirm_upload_response = cls(
            upload_id=upload_id,
            status=status,
            etag=etag,
            file_size_bytes=file_size_bytes,
            file_hash=file_hash,
            verified_at=verified_at,
            completed_at=completed_at,
            object_id=object_id,
            task_id=task_id,
            message=message,
        )

        confirm_upload_response.additional_properties = d
        return confirm_upload_response

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
