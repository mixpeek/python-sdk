from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.batch_type import BatchType
from ..models.task_status_enum import TaskStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_model_error_summary_type_0 import BatchModelErrorSummaryType0
    from ..models.batch_model_internal_metadata_type_0 import BatchModelInternalMetadataType0
    from ..models.batch_model_metadata import BatchModelMetadata
    from ..models.tier_task_info import TierTaskInfo


T = TypeVar("T", bound="BatchModel")


@_attrs_define
class BatchModel:
    """Model representing a batch of objects for processing through collections.

    A batch groups bucket objects together for processing through one or more collections.
    Batches support multi-tier processing where collections are processed in dependency order
    (e.g., bucket → chunks → frames → scenes). Each tier has independent task tracking.

    Use Cases:
        - Process multiple objects through collections in a single batch
        - Track progress of multi-tier decomposition pipelines
        - Monitor and retry individual processing tiers
        - Query batch status and tier-specific task information

    Lifecycle:
        1. Created in DRAFT status with object_ids
        2. Submitted for processing → status changes to PENDING
        3. Each tier processes sequentially (tier 0 → tier 1 → ... → tier N)
        4. Batch completes when all tiers finish (status=COMPLETED) or any tier fails (status=FAILED)

    Multi-Tier Processing:
        - Tier 0: Bucket objects → Collections (bucket as source)
        - Tier N (N > 0): Collection documents → Collections (upstream collection as source)
        - Each tier gets independent task tracking via tier_tasks array
        - Processing proceeds tier-by-tier with automatic chaining

    Requirements:
        - batch_id: OPTIONAL (auto-generated if not provided)
        - bucket_id: REQUIRED
        - status: OPTIONAL (defaults to DRAFT)
        - object_ids: REQUIRED for processing (must have at least 1 object)
        - collection_ids: OPTIONAL (discovered via DAG resolution)
        - tier_tasks: OPTIONAL (populated during processing)
        - current_tier: OPTIONAL (set during processing)
        - total_tiers: OPTIONAL (defaults to 1, set during DAG resolution)
        - dag_tiers: OPTIONAL (populated during DAG resolution)

        Attributes:
            bucket_id (str): REQUIRED. Unique identifier of the bucket containing the objects to process. Must be a valid
                bucket ID that exists in the system. All object_ids must belong to this bucket. Format: Bucket ID as defined
                when bucket was created.
            batch_id (str | Unset): OPTIONAL (auto-generated if not provided). Unique identifier for this batch. Format:
                'btch_' prefix followed by 12-character secure token. Generated using generate_secure_token() from
                shared.utilities.helpers. Used to query batch status and track processing across tiers. Immutable after
                creation.
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
            object_ids (list[str] | Unset): REQUIRED for processing (must have at least 1). List of object IDs to include in
                this batch. All objects must exist in the specified bucket_id. These objects are the source data for tier 0
                processing. Minimum 1 object, no maximum limit. Objects are processed in parallel within each tier.
            collection_ids (list[str] | None | Unset): OPTIONAL. List of all collection IDs involved in this batch's
                processing. Automatically populated during DAG resolution from dag_tiers. Includes collections from all tiers
                (flattened view of dag_tiers). Used for quick lookups without traversing tier structure. Format: List of
                collection IDs across all tiers.
            error (None | str | Unset): OPTIONAL. Legacy error message field for backward compatibility. None if batch
                succeeded or is still processing. Contains human-readable error description from first failed tier. DEPRECATED:
                Use tier_tasks[].errors for detailed error information. For multi-tier batches, typically contains the error
                from the first failed tier. Check tier_tasks array for tier-specific error details and error_summary for
                aggregation.
            error_summary (BatchModelErrorSummaryType0 | None | Unset): OPTIONAL. Aggregated summary of errors across ALL
                tiers in the batch. None if batch succeeded or is still processing. Maps error_type (category) to total count of
                affected documents across all tiers. Provides quick batch-wide overview of error distribution. Example:
                {'dependency': 15, 'authentication': 25, 'validation': 5} means across all tiers, 15 documents failed with
                dependency errors, 25 with auth errors, 5 with validation errors. Automatically aggregated from
                tier_tasks[].error_summary. Used for batch health dashboard and error trend analysis.
            type_ (BatchType | Unset): The type of batch.
            manifest_key (None | str | Unset): OPTIONAL. S3 key where the batch manifest is stored. Contains metadata and
                row data (Parquet) for Engine processing. For tier 0, points to bucket object manifest. For tier N+, points to
                collection document manifest. Format: S3 path (e.g., 'namespace_id/internal_id/manifests/tier_0.parquet').
                Generated during batch submission.
            task_id (None | str | Unset): OPTIONAL. Primary task ID for the batch (typically tier 0 task). Used for backward
                compatibility with single-tier batch tracking. For multi-tier batches, prefer querying tier_tasks array for
                granular tracking. Format: Task ID as generated for tier 0.
            loaded_object_ids (list[str] | None | Unset): OPTIONAL. List of object IDs that were successfully validated and
                loaded into the batch. Subset of object_ids that passed validation. Used to track which objects are ready for
                processing. None if batch hasn't been validated yet.
            internal_metadata (BatchModelInternalMetadataType0 | None | Unset): OPTIONAL. Internal engine/job metadata for
                system use. May contain: job_id (provider-specific), engine_version, processing hints, last_health_check.
                last_health_check: Most recent health check results with health_status, enriched_documents,
                vector_populated_count, stall_duration_seconds, recommendations, missing_features. Populated asynchronously via
                Celery task (non-blocking, best-effort). Used for troubleshooting batch processing issues via API. NOTE: In
                MongoDB, this is stored under '_internal.processing' path.
            metadata (BatchModelMetadata | Unset): OPTIONAL. User-defined metadata for the batch. Arbitrary key-value pairs
                for user tracking and organization. Persisted with the batch and returned in API responses. Not used by the
                system for processing logic. Examples: campaign_id, user_email, processing_notes.
            tier_tasks (list[TierTaskInfo] | Unset): OPTIONAL. List of tier task tracking information for multi-tier
                processing. Each element represents one tier in the processing pipeline. Empty array for simple single-tier
                batches. Populated during batch submission with tier 0 info, then appended as tiers progress. Each TierTaskInfo
                contains: tier_num, task_id, status, collection_ids, timestamps. Used for granular monitoring: 'Show me status
                of tier 2' or 'Retry tier 1'. Array index typically matches tier_num (tier_tasks[0] = tier 0, tier_tasks[1] =
                tier 1, etc.).
            current_tier (int | None | Unset): OPTIONAL. Zero-based index of the currently processing tier. None if batch
                hasn't started processing (status=DRAFT or PENDING). Updated as batch progresses through tiers. Used to show
                processing progress: 'Processing tier 2 of 5'. Set to last tier number when batch completes. Example: If
                processing tier 1 (frames), current_tier=1.
            total_tiers (int | Unset): OPTIONAL (defaults to 1). Total number of tiers in the collection DAG. Minimum 1
                (tier 0 only = bucket → collection). Set during DAG resolution when batch is submitted. Equals len(dag_tiers) if
                dag_tiers is populated. Used to calculate progress: current_tier / total_tiers. Example: 5-tier pipeline (bucket
                → chunks → frames → scenes → summaries) has total_tiers=5. Default: 1.
            dag_tiers (list[list[str]] | None | Unset): OPTIONAL. Complete DAG tier structure for this batch. List of tiers,
                where each tier is a list of collection IDs to process at that stage. Tier 0 = bucket-sourced collections. Tier
                N (N > 0) = collection-sourced collections. Collections within same tier have no dependencies (can run in
                parallel). Collections in tier N+1 depend on collections in tier N. Populated during DAG resolution at batch
                submission. Used for tier-by-tier processing orchestration. Example: [['col_chunks'], ['col_frames',
                'col_objects'], ['col_scenes']] = 3 tiers where frames and objects run in parallel at tier 1.
            created_at (datetime.datetime | Unset): OPTIONAL (auto-set on creation). ISO 8601 timestamp when batch was
                created. Set using current_time() from shared.utilities.helpers. Immutable after creation. Used for batch age
                tracking and cleanup of old batches.
            updated_at (datetime.datetime | Unset): OPTIONAL (auto-updated). ISO 8601 timestamp when batch was last
                modified. Updated using current_time() whenever batch status or tier_tasks change. Used to track batch activity
                and identify stale batches.
    """

    bucket_id: str
    batch_id: str | Unset = UNSET
    status: TaskStatusEnum | Unset = UNSET
    object_ids: list[str] | Unset = UNSET
    collection_ids: list[str] | None | Unset = UNSET
    error: None | str | Unset = UNSET
    error_summary: BatchModelErrorSummaryType0 | None | Unset = UNSET
    type_: BatchType | Unset = UNSET
    manifest_key: None | str | Unset = UNSET
    task_id: None | str | Unset = UNSET
    loaded_object_ids: list[str] | None | Unset = UNSET
    internal_metadata: BatchModelInternalMetadataType0 | None | Unset = UNSET
    metadata: BatchModelMetadata | Unset = UNSET
    tier_tasks: list[TierTaskInfo] | Unset = UNSET
    current_tier: int | None | Unset = UNSET
    total_tiers: int | Unset = 1
    dag_tiers: list[list[str]] | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_model_error_summary_type_0 import BatchModelErrorSummaryType0
        from ..models.batch_model_internal_metadata_type_0 import BatchModelInternalMetadataType0

        bucket_id = self.bucket_id

        batch_id = self.batch_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        object_ids: list[str] | Unset = UNSET
        if not isinstance(self.object_ids, Unset):
            object_ids = self.object_ids

        collection_ids: list[str] | None | Unset
        if isinstance(self.collection_ids, Unset):
            collection_ids = UNSET
        elif isinstance(self.collection_ids, list):
            collection_ids = self.collection_ids

        else:
            collection_ids = self.collection_ids

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        error_summary: dict[str, Any] | None | Unset
        if isinstance(self.error_summary, Unset):
            error_summary = UNSET
        elif isinstance(self.error_summary, BatchModelErrorSummaryType0):
            error_summary = self.error_summary.to_dict()
        else:
            error_summary = self.error_summary

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        manifest_key: None | str | Unset
        if isinstance(self.manifest_key, Unset):
            manifest_key = UNSET
        else:
            manifest_key = self.manifest_key

        task_id: None | str | Unset
        if isinstance(self.task_id, Unset):
            task_id = UNSET
        else:
            task_id = self.task_id

        loaded_object_ids: list[str] | None | Unset
        if isinstance(self.loaded_object_ids, Unset):
            loaded_object_ids = UNSET
        elif isinstance(self.loaded_object_ids, list):
            loaded_object_ids = self.loaded_object_ids

        else:
            loaded_object_ids = self.loaded_object_ids

        internal_metadata: dict[str, Any] | None | Unset
        if isinstance(self.internal_metadata, Unset):
            internal_metadata = UNSET
        elif isinstance(self.internal_metadata, BatchModelInternalMetadataType0):
            internal_metadata = self.internal_metadata.to_dict()
        else:
            internal_metadata = self.internal_metadata

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        tier_tasks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tier_tasks, Unset):
            tier_tasks = []
            for tier_tasks_item_data in self.tier_tasks:
                tier_tasks_item = tier_tasks_item_data.to_dict()
                tier_tasks.append(tier_tasks_item)

        current_tier: int | None | Unset
        if isinstance(self.current_tier, Unset):
            current_tier = UNSET
        else:
            current_tier = self.current_tier

        total_tiers = self.total_tiers

        dag_tiers: list[list[str]] | None | Unset
        if isinstance(self.dag_tiers, Unset):
            dag_tiers = UNSET
        elif isinstance(self.dag_tiers, list):
            dag_tiers = []
            for dag_tiers_type_0_item_data in self.dag_tiers:
                dag_tiers_type_0_item = dag_tiers_type_0_item_data

                dag_tiers.append(dag_tiers_type_0_item)

        else:
            dag_tiers = self.dag_tiers

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket_id": bucket_id,
            }
        )
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if status is not UNSET:
            field_dict["status"] = status
        if object_ids is not UNSET:
            field_dict["object_ids"] = object_ids
        if collection_ids is not UNSET:
            field_dict["collection_ids"] = collection_ids
        if error is not UNSET:
            field_dict["error"] = error
        if error_summary is not UNSET:
            field_dict["error_summary"] = error_summary
        if type_ is not UNSET:
            field_dict["type"] = type_
        if manifest_key is not UNSET:
            field_dict["manifest_key"] = manifest_key
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if loaded_object_ids is not UNSET:
            field_dict["loaded_object_ids"] = loaded_object_ids
        if internal_metadata is not UNSET:
            field_dict["internal_metadata"] = internal_metadata
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tier_tasks is not UNSET:
            field_dict["tier_tasks"] = tier_tasks
        if current_tier is not UNSET:
            field_dict["current_tier"] = current_tier
        if total_tiers is not UNSET:
            field_dict["total_tiers"] = total_tiers
        if dag_tiers is not UNSET:
            field_dict["dag_tiers"] = dag_tiers
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_model_error_summary_type_0 import BatchModelErrorSummaryType0
        from ..models.batch_model_internal_metadata_type_0 import BatchModelInternalMetadataType0
        from ..models.batch_model_metadata import BatchModelMetadata
        from ..models.tier_task_info import TierTaskInfo

        d = dict(src_dict)
        bucket_id = d.pop("bucket_id")

        batch_id = d.pop("batch_id", UNSET)

        _status = d.pop("status", UNSET)
        status: TaskStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskStatusEnum(_status)

        object_ids = cast(list[str], d.pop("object_ids", UNSET))

        def _parse_collection_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collection_ids_type_0 = cast(list[str], data)

                return collection_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        collection_ids = _parse_collection_ids(d.pop("collection_ids", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_error_summary(data: object) -> BatchModelErrorSummaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_summary_type_0 = BatchModelErrorSummaryType0.from_dict(data)

                return error_summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchModelErrorSummaryType0 | None | Unset, data)

        error_summary = _parse_error_summary(d.pop("error_summary", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: BatchType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BatchType(_type_)

        def _parse_manifest_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        manifest_key = _parse_manifest_key(d.pop("manifest_key", UNSET))

        def _parse_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_id = _parse_task_id(d.pop("task_id", UNSET))

        def _parse_loaded_object_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                loaded_object_ids_type_0 = cast(list[str], data)

                return loaded_object_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        loaded_object_ids = _parse_loaded_object_ids(d.pop("loaded_object_ids", UNSET))

        def _parse_internal_metadata(data: object) -> BatchModelInternalMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                internal_metadata_type_0 = BatchModelInternalMetadataType0.from_dict(data)

                return internal_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchModelInternalMetadataType0 | None | Unset, data)

        internal_metadata = _parse_internal_metadata(d.pop("internal_metadata", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: BatchModelMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = BatchModelMetadata.from_dict(_metadata)

        _tier_tasks = d.pop("tier_tasks", UNSET)
        tier_tasks: list[TierTaskInfo] | Unset = UNSET
        if _tier_tasks is not UNSET:
            tier_tasks = []
            for tier_tasks_item_data in _tier_tasks:
                tier_tasks_item = TierTaskInfo.from_dict(tier_tasks_item_data)

                tier_tasks.append(tier_tasks_item)

        def _parse_current_tier(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        current_tier = _parse_current_tier(d.pop("current_tier", UNSET))

        total_tiers = d.pop("total_tiers", UNSET)

        def _parse_dag_tiers(data: object) -> list[list[str]] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dag_tiers_type_0 = []
                _dag_tiers_type_0 = data
                for dag_tiers_type_0_item_data in _dag_tiers_type_0:
                    dag_tiers_type_0_item = cast(list[str], dag_tiers_type_0_item_data)

                    dag_tiers_type_0.append(dag_tiers_type_0_item)

                return dag_tiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[list[str]] | None | Unset, data)

        dag_tiers = _parse_dag_tiers(d.pop("dag_tiers", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        batch_model = cls(
            bucket_id=bucket_id,
            batch_id=batch_id,
            status=status,
            object_ids=object_ids,
            collection_ids=collection_ids,
            error=error,
            error_summary=error_summary,
            type_=type_,
            manifest_key=manifest_key,
            task_id=task_id,
            loaded_object_ids=loaded_object_ids,
            internal_metadata=internal_metadata,
            metadata=metadata,
            tier_tasks=tier_tasks,
            current_tier=current_tier,
            total_tiers=total_tiers,
            dag_tiers=dag_tiers,
            created_at=created_at,
            updated_at=updated_at,
        )

        batch_model.additional_properties = d
        return batch_model

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
