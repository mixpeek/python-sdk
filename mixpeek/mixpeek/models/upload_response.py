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
    from ..models.upload_response_metadata import UploadResponseMetadata
    from ..models.upload_response_object_metadata_type_0 import UploadResponseObjectMetadataType0


T = TypeVar("T", bound="UploadResponse")


@_attrs_define
class UploadResponse:
    """Response containing presigned URL and upload tracking information.

    This response includes everything needed to:
    1. Upload your file to S3 using the presigned_url
    2. Track the upload status using upload_id
    3. Confirm the upload using the confirmation endpoint

    The presigned_url is time-limited and specific to this upload.
    After uploading to S3, call POST /v1/buckets/{bucket_id}/uploads/{upload_id}/confirm.

        Attributes:
            upload_id (str): Unique identifier for this upload. Auto-generated.

                ⚠️  NEXT STEP: After uploading to S3, you MUST confirm:   POST /v1/uploads/{upload_id}/confirm

                Other operations:   - Check status: GET /v1/uploads/{upload_id}   - Cancel upload: DELETE
                /v1/uploads/{upload_id}

                Format: 'upl_' followed by 16 random characters.
            bucket_id (str): Target bucket ID where object will be created
            filename (str): Name of the file to upload
            content_type (str): MIME type enforced by the presigned URL
            presigned_url_expiration (int): How long the presigned URL is valid, in seconds
            s3_key (str): Full S3 object key where the file will be stored. Format:
                {internal_id}/{namespace_id}/api_buckets_uploads_create/{upload_id}/{filename}. Used internally for verification
                and object creation.
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
            create_object_on_confirm (bool): Whether bucket object will be auto-created on confirmation
            created_at (datetime.datetime): When this upload record was created (ISO 8601 format)
            expires_at (datetime.datetime): When the presigned URL expires (ISO 8601 format). After this time:   - The
                presigned URL cannot be used   - Upload status will be marked as FAILED if not completed   - The upload record
                will be auto-deleted 30 days later (MongoDB TTL)
            file_size_bytes (int | None | Unset): Expected file size in bytes if provided in request. Will be validated
                during confirmation.
            presigned_url (None | str | Unset): Time-limited HTTPS URL for uploading directly to S3.

                **Step 1 - Upload to S3:**   curl -X PUT '{presigned_url}' -H 'Content-Type: {content_type}' --upload-file
                {filename}

                **Step 2 - REQUIRED: Confirm the upload:**   POST /v1/uploads/{upload_id}/confirm   (S3 has no callback - you
                MUST call confirm to finalize)

                The URL includes authentication and expires after presigned_url_expiration seconds. S3 returns an ETag header on
                success - pass it to confirm for integrity validation. NOTE: This will be null if is_duplicate=true (duplicate
                found, no upload needed).
            metadata (UploadResponseMetadata | Unset): Custom metadata for tracking
            object_metadata (None | Unset | UploadResponseObjectMetadataType0): Metadata for the bucket object (if
                create_object_on_confirm=true)
            blob_property (None | str | Unset): Property name for the blob in bucket object
            blob_type (None | str | Unset): Type of blob (IMAGE, VIDEO, etc.)
            file_hash (None | str | Unset): SHA256 hash of the file content. Set during confirmation from S3 metadata or
                provided in request. Used for duplicate detection.
            skip_duplicates (bool | Unset): Whether duplicate detection was enabled for this upload Default: True.
            is_duplicate (bool | Unset): Whether this upload was identified as a duplicate of an existing file. If true:   -
                duplicate_of_upload_id contains the original upload   - presigned_url will be null (no upload needed)   - You
                can use the original upload's S3 object. This saves bandwidth and storage costs. Default: False.
            duplicate_of_upload_id (None | str | Unset): If skip_duplicates=true and duplicate found, this is the original
                upload_id. The response will reference the existing upload instead of creating a new one.
            skipped_unique_key (bool | Unset): Whether this upload was skipped because the unique key already exists in the
                bucket. If true:   - existing_object_id contains the ID of the existing object   - presigned_url will be null
                (no upload needed)   - No S3 upload is required This saves bandwidth and prevents duplicate objects. Default:
                False.
            existing_object_id (None | str | Unset): If skipped_unique_key=true, this is the object_id of the existing
                object that has the same unique key values. The upload was skipped to prevent duplicates.
            message (None | str | Unset): Human-readable message about the upload. Provided when is_duplicate=true or other
                special conditions. Example: 'File already exists with the same content hash. No upload needed - returning
                existing upload.'
            completed_at (datetime.datetime | None | Unset): When the upload was completed and verified (ISO 8601 format)
            verified_at (datetime.datetime | None | Unset): When S3 object existence was verified (ISO 8601 format)
            etag (None | str | Unset): S3 ETag from the uploaded object (set during confirmation)
            object_id (None | str | Unset): Created bucket object ID (if create_object_on_confirm was true)
            task_id (None | str | Unset): Celery task ID for async confirmation (if processed asynchronously)
    """

    upload_id: str
    bucket_id: str
    filename: str
    content_type: str
    presigned_url_expiration: int
    s3_key: str
    status: TaskStatusEnum
    create_object_on_confirm: bool
    created_at: datetime.datetime
    expires_at: datetime.datetime
    file_size_bytes: int | None | Unset = UNSET
    presigned_url: None | str | Unset = UNSET
    metadata: UploadResponseMetadata | Unset = UNSET
    object_metadata: None | Unset | UploadResponseObjectMetadataType0 = UNSET
    blob_property: None | str | Unset = UNSET
    blob_type: None | str | Unset = UNSET
    file_hash: None | str | Unset = UNSET
    skip_duplicates: bool | Unset = True
    is_duplicate: bool | Unset = False
    duplicate_of_upload_id: None | str | Unset = UNSET
    skipped_unique_key: bool | Unset = False
    existing_object_id: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    verified_at: datetime.datetime | None | Unset = UNSET
    etag: None | str | Unset = UNSET
    object_id: None | str | Unset = UNSET
    task_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.upload_response_object_metadata_type_0 import UploadResponseObjectMetadataType0

        upload_id = self.upload_id

        bucket_id = self.bucket_id

        filename = self.filename

        content_type = self.content_type

        presigned_url_expiration = self.presigned_url_expiration

        s3_key = self.s3_key

        status = self.status.value

        create_object_on_confirm = self.create_object_on_confirm

        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        file_size_bytes: int | None | Unset
        if isinstance(self.file_size_bytes, Unset):
            file_size_bytes = UNSET
        else:
            file_size_bytes = self.file_size_bytes

        presigned_url: None | str | Unset
        if isinstance(self.presigned_url, Unset):
            presigned_url = UNSET
        else:
            presigned_url = self.presigned_url

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        object_metadata: dict[str, Any] | None | Unset
        if isinstance(self.object_metadata, Unset):
            object_metadata = UNSET
        elif isinstance(self.object_metadata, UploadResponseObjectMetadataType0):
            object_metadata = self.object_metadata.to_dict()
        else:
            object_metadata = self.object_metadata

        blob_property: None | str | Unset
        if isinstance(self.blob_property, Unset):
            blob_property = UNSET
        else:
            blob_property = self.blob_property

        blob_type: None | str | Unset
        if isinstance(self.blob_type, Unset):
            blob_type = UNSET
        else:
            blob_type = self.blob_type

        file_hash: None | str | Unset
        if isinstance(self.file_hash, Unset):
            file_hash = UNSET
        else:
            file_hash = self.file_hash

        skip_duplicates = self.skip_duplicates

        is_duplicate = self.is_duplicate

        duplicate_of_upload_id: None | str | Unset
        if isinstance(self.duplicate_of_upload_id, Unset):
            duplicate_of_upload_id = UNSET
        else:
            duplicate_of_upload_id = self.duplicate_of_upload_id

        skipped_unique_key = self.skipped_unique_key

        existing_object_id: None | str | Unset
        if isinstance(self.existing_object_id, Unset):
            existing_object_id = UNSET
        else:
            existing_object_id = self.existing_object_id

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        verified_at: None | str | Unset
        if isinstance(self.verified_at, Unset):
            verified_at = UNSET
        elif isinstance(self.verified_at, datetime.datetime):
            verified_at = self.verified_at.isoformat()
        else:
            verified_at = self.verified_at

        etag: None | str | Unset
        if isinstance(self.etag, Unset):
            etag = UNSET
        else:
            etag = self.etag

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upload_id": upload_id,
                "bucket_id": bucket_id,
                "filename": filename,
                "content_type": content_type,
                "presigned_url_expiration": presigned_url_expiration,
                "s3_key": s3_key,
                "status": status,
                "create_object_on_confirm": create_object_on_confirm,
                "created_at": created_at,
                "expires_at": expires_at,
            }
        )
        if file_size_bytes is not UNSET:
            field_dict["file_size_bytes"] = file_size_bytes
        if presigned_url is not UNSET:
            field_dict["presigned_url"] = presigned_url
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if object_metadata is not UNSET:
            field_dict["object_metadata"] = object_metadata
        if blob_property is not UNSET:
            field_dict["blob_property"] = blob_property
        if blob_type is not UNSET:
            field_dict["blob_type"] = blob_type
        if file_hash is not UNSET:
            field_dict["file_hash"] = file_hash
        if skip_duplicates is not UNSET:
            field_dict["skip_duplicates"] = skip_duplicates
        if is_duplicate is not UNSET:
            field_dict["is_duplicate"] = is_duplicate
        if duplicate_of_upload_id is not UNSET:
            field_dict["duplicate_of_upload_id"] = duplicate_of_upload_id
        if skipped_unique_key is not UNSET:
            field_dict["skipped_unique_key"] = skipped_unique_key
        if existing_object_id is not UNSET:
            field_dict["existing_object_id"] = existing_object_id
        if message is not UNSET:
            field_dict["message"] = message
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if verified_at is not UNSET:
            field_dict["verified_at"] = verified_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if task_id is not UNSET:
            field_dict["task_id"] = task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_response_metadata import UploadResponseMetadata
        from ..models.upload_response_object_metadata_type_0 import UploadResponseObjectMetadataType0

        d = dict(src_dict)
        upload_id = d.pop("upload_id")

        bucket_id = d.pop("bucket_id")

        filename = d.pop("filename")

        content_type = d.pop("content_type")

        presigned_url_expiration = d.pop("presigned_url_expiration")

        s3_key = d.pop("s3_key")

        status = TaskStatusEnum(d.pop("status"))

        create_object_on_confirm = d.pop("create_object_on_confirm")

        created_at = isoparse(d.pop("created_at"))

        expires_at = isoparse(d.pop("expires_at"))

        def _parse_file_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size_bytes = _parse_file_size_bytes(d.pop("file_size_bytes", UNSET))

        def _parse_presigned_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        presigned_url = _parse_presigned_url(d.pop("presigned_url", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: UploadResponseMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = UploadResponseMetadata.from_dict(_metadata)

        def _parse_object_metadata(data: object) -> None | Unset | UploadResponseObjectMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                object_metadata_type_0 = UploadResponseObjectMetadataType0.from_dict(data)

                return object_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UploadResponseObjectMetadataType0, data)

        object_metadata = _parse_object_metadata(d.pop("object_metadata", UNSET))

        def _parse_blob_property(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        blob_property = _parse_blob_property(d.pop("blob_property", UNSET))

        def _parse_blob_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        blob_type = _parse_blob_type(d.pop("blob_type", UNSET))

        def _parse_file_hash(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_hash = _parse_file_hash(d.pop("file_hash", UNSET))

        skip_duplicates = d.pop("skip_duplicates", UNSET)

        is_duplicate = d.pop("is_duplicate", UNSET)

        def _parse_duplicate_of_upload_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        duplicate_of_upload_id = _parse_duplicate_of_upload_id(d.pop("duplicate_of_upload_id", UNSET))

        skipped_unique_key = d.pop("skipped_unique_key", UNSET)

        def _parse_existing_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        existing_object_id = _parse_existing_object_id(d.pop("existing_object_id", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

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

        def _parse_etag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        etag = _parse_etag(d.pop("etag", UNSET))

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

        upload_response = cls(
            upload_id=upload_id,
            bucket_id=bucket_id,
            filename=filename,
            content_type=content_type,
            presigned_url_expiration=presigned_url_expiration,
            s3_key=s3_key,
            status=status,
            create_object_on_confirm=create_object_on_confirm,
            created_at=created_at,
            expires_at=expires_at,
            file_size_bytes=file_size_bytes,
            presigned_url=presigned_url,
            metadata=metadata,
            object_metadata=object_metadata,
            blob_property=blob_property,
            blob_type=blob_type,
            file_hash=file_hash,
            skip_duplicates=skip_duplicates,
            is_duplicate=is_duplicate,
            duplicate_of_upload_id=duplicate_of_upload_id,
            skipped_unique_key=skipped_unique_key,
            existing_object_id=existing_object_id,
            message=message,
            completed_at=completed_at,
            verified_at=verified_at,
            etag=etag,
            object_id=object_id,
            task_id=task_id,
        )

        upload_response.additional_properties = d
        return upload_response

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
