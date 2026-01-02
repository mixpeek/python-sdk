from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_status_enum import TaskStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.blob_model import BlobModel
    from ..models.source_details import SourceDetails


T = TypeVar("T", bound="ObjectResponse")


@_attrs_define
class ObjectResponse:
    """Response model for bucket objects.

    Attributes:
        bucket_id (str): ID of the bucket this object belongs to
        object_id (str | Unset): Unique identifier for the object
        key_prefix (None | str | Unset): Storage key/path of the object, this will be used to retrieve the object from
            the storage. It is similar to a file path. If not provided, it will be placed in the root of the bucket.
        blobs (list[BlobModel] | Unset): List of blobs contained in this object
        source_details (list[SourceDetails] | Unset): Lineage/source details for this object; used for downstream
            references.
        status (TaskStatusEnum | Unset): Enumeration of task statuses for tracking asynchronous operations.

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
        error (None | str | Unset): The error message if the object failed to process.
        created_at (datetime.datetime | None | Unset): Timestamp when the object was created. Automatically populated by
            the system.
        updated_at (datetime.datetime | None | Unset): Timestamp when the object was last updated. Automatically
            populated by the system.
    """

    bucket_id: str
    object_id: str | Unset = UNSET
    key_prefix: None | str | Unset = UNSET
    blobs: list[BlobModel] | Unset = UNSET
    source_details: list[SourceDetails] | Unset = UNSET
    status: TaskStatusEnum | Unset = UNSET
    error: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_id = self.bucket_id

        object_id = self.object_id

        key_prefix: None | str | Unset
        if isinstance(self.key_prefix, Unset):
            key_prefix = UNSET
        else:
            key_prefix = self.key_prefix

        blobs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.blobs, Unset):
            blobs = []
            for blobs_item_data in self.blobs:
                blobs_item = blobs_item_data.to_dict()
                blobs.append(blobs_item)

        source_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.source_details, Unset):
            source_details = []
            for source_details_item_data in self.source_details:
                source_details_item = source_details_item_data.to_dict()
                source_details.append(source_details_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket_id": bucket_id,
            }
        )
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if key_prefix is not UNSET:
            field_dict["key_prefix"] = key_prefix
        if blobs is not UNSET:
            field_dict["blobs"] = blobs
        if source_details is not UNSET:
            field_dict["source_details"] = source_details
        if status is not UNSET:
            field_dict["status"] = status
        if error is not UNSET:
            field_dict["error"] = error
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blob_model import BlobModel
        from ..models.source_details import SourceDetails

        d = dict(src_dict)
        bucket_id = d.pop("bucket_id")

        object_id = d.pop("object_id", UNSET)

        def _parse_key_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_prefix = _parse_key_prefix(d.pop("key_prefix", UNSET))

        _blobs = d.pop("blobs", UNSET)
        blobs: list[BlobModel] | Unset = UNSET
        if _blobs is not UNSET:
            blobs = []
            for blobs_item_data in _blobs:
                blobs_item = BlobModel.from_dict(blobs_item_data)

                blobs.append(blobs_item)

        _source_details = d.pop("source_details", UNSET)
        source_details: list[SourceDetails] | Unset = UNSET
        if _source_details is not UNSET:
            source_details = []
            for source_details_item_data in _source_details:
                source_details_item = SourceDetails.from_dict(source_details_item_data)

                source_details.append(source_details_item)

        _status = d.pop("status", UNSET)
        status: TaskStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskStatusEnum(_status)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        object_response = cls(
            bucket_id=bucket_id,
            object_id=object_id,
            key_prefix=key_prefix,
            blobs=blobs,
            source_details=source_details,
            status=status,
            error=error,
            created_at=created_at,
            updated_at=updated_at,
        )

        object_response.additional_properties = d
        return object_response

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
