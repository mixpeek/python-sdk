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
    from ..models.batch_error_detail import BatchErrorDetail
    from ..models.tier_task_info_error_summary_type_0 import TierTaskInfoErrorSummaryType0
    from ..models.tier_task_info_performance_type_0 import TierTaskInfoPerformanceType0


T = TypeVar("T", bound="TierTaskInfo")


@_attrs_define
class TierTaskInfo:
    """Tracking information for a single collection processing tier's task.

    In multi-tier collection processing, each tier represents a processing stage in the
    decomposition pipeline (e.g., bucket → chunks → frames → scenes). Each tier gets its
    own independent task for granular monitoring, status tracking, and retry capabilities.

    Use Cases:
        - Monitor progress of individual tiers in a multi-tier batch
        - Retry failed tiers without reprocessing successful ones
        - Track lineage of processing through parent_task_id linkage
        - Query task status for specific processing stages

    Tier Definitions:
        - Tier 0: Bucket → Collection (bucket objects as source)
        - Tier N (N > 0): Collection → Collection (upstream collection documents as source)

    Lifecycle:
        1. Created with status=PENDING when tier is scheduled
        2. Updated to status=IN_PROGRESS when processing starts (task_id assigned)
        3. Finalized to status=COMPLETED or status=FAILED when tier completes

    Requirements:
        - tier_num: REQUIRED. Zero-based tier number indicating processing stage
        - task_id: OPTIONAL. None until tier processing starts
        - status: REQUIRED. Defaults to PENDING
        - collection_ids: REQUIRED. Collections being processed in this tier
        - source_type: REQUIRED. "bucket" for tier 0, "collection" for tier N+
        - source_collection_ids: OPTIONAL. Required for tier N+ (collection sources)
        - parent_task_id: OPTIONAL. Links to previous tier for audit trail
        - started_at: OPTIONAL. Set when tier processing begins
        - completed_at: OPTIONAL. Set when tier processing finishes
        - error: OPTIONAL. Set if tier fails with error details

        Attributes:
            tier_num (int): REQUIRED. Zero-based tier number indicating the processing stage. Tier 0 = initial bucket-to-
                collection processing (bucket objects as source). Tier N (N > 0) = collection-to-collection processing (upstream
                documents as source). Used to determine processing order and identify which stage a task represents. Example: In
                a 5-tier pipeline (bucket → chunks → frames → scenes → summaries), chunks=tier 0, frames=tier 1, scenes=tier 2,
                summaries=tier 3.
            source_type (str): REQUIRED. Type of data source for this tier's processing. 'bucket': Tier 0 processing where
                source is bucket objects from the objects table. 'collection': Tier N+ processing where source is documents from
                upstream collection(s). Determines how the API prepares the input dataset manifest for the Engine. Bucket
                sources query the objects table and include file blobs. Collection sources query the documents table and include
                processed features.
            task_id (None | str | Unset): OPTIONAL. Unique task identifier for this tier's processing task. None if tier has
                not yet started (status=PENDING). Assigned when tier processing begins (status=IN_PROGRESS). Used to query task
                status via GET /v1/tasks/{task_id}. Format: 'task_' prefix followed by secure token. Generated using
                generate_secure_token() from shared.utilities.helpers.
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
            collection_ids (list[str] | Unset): REQUIRED. List of collection IDs being processed in this tier. Each tier can
                process one or more collections in parallel. Collections in the same tier have no dependencies on each other.
                Format: Collection IDs as defined when collections were created. Minimum 1 collection per tier. Example: Tier 1
                might process ['col_frames_30fps', 'col_frames_60fps'] in parallel.
            source_collection_ids (list[str] | None | Unset): OPTIONAL for tier 0 (must be None). REQUIRED for tier N+ (N >
                0). List of upstream collection IDs that provide documents as input to this tier. Typically contains collection
                IDs from the previous tier (tier_num - 1). Used by the API to query documents from these collections for
                processing. These upstream documents are converted to a Parquet manifest for the Engine. Example: If tier 1
                processes 'col_frames' and sources from tier 0's 'col_chunks', then source_collection_ids=['col_chunks'].
            parent_task_id (None | str | Unset): OPTIONAL. Task ID of the previous tier (tier_num - 1) that processed before
                this tier. Used to link tiers together for audit trail and lineage tracking. None for tier 0 (no parent).
                Enables queries like 'show all tiers that processed after tier 0' or 'trace back through all parent tiers to
                find the original batch'. Format: Same as task_id (e.g., 'task_tier0_abc123').
            started_at (datetime.datetime | None | Unset): OPTIONAL. ISO 8601 timestamp when this tier began processing.
                None if tier has not yet started (status=PENDING). Set using current_time() from shared.utilities.helpers when
                tier starts. Used to calculate tier processing duration and identify long-running tiers. Example:
                '2025-11-03T10:00:00Z'.
            completed_at (datetime.datetime | None | Unset): OPTIONAL. ISO 8601 timestamp when this tier finished processing
                (success or failure). None if tier has not yet completed (status=PENDING or IN_PROGRESS). Set using
                current_time() from shared.utilities.helpers when tier completes. Used to calculate tier processing duration
                (completed_at - started_at). Set for both COMPLETED and FAILED statuses. Example: '2025-11-03T10:05:00Z'.
            duration_ms (float | None | Unset): OPTIONAL. Processing duration in milliseconds for this tier. Calculated as
                (completed_at - started_at) when tier completes. None if tier has not yet completed or if started_at was not
                set. Provides a pre-computed duration for easy querying without timestamp math. Set for both COMPLETED and
                FAILED statuses.
            errors (list[BatchErrorDetail] | Unset): OPTIONAL. List of detailed errors that occurred during tier processing.
                Empty list if tier succeeded or has not yet completed. Each error includes: error_type, message, component,
                stage, traceback, timestamp. Multiple errors may occur if different documents fail with different issues. Used
                for detailed error analysis, debugging, and intelligent retry logic. Example: Multiple documents failing with
                different errors (dependency vs auth). For backward compatibility, check if list is empty for success/in-
                progress status.
            error_summary (None | TierTaskInfoErrorSummaryType0 | Unset): OPTIONAL. Aggregated summary of errors by error
                type. None if tier succeeded or has not yet completed. Maps error_type (category) to count of affected
                documents. Provides quick overview of error distribution without parsing full error list. Example:
                {'dependency': 5, 'authentication': 10, 'validation': 3} means 5 documents failed with dependency errors, 10
                with auth errors, 3 with validation. Automatically generated from errors list for convenience. Used for batch
                health monitoring and error trend analysis.
            performance (None | TierTaskInfoPerformanceType0 | Unset): OPTIONAL. Performance metrics summary for this tier's
                execution. Automatically populated after tier completion by collecting data from ClickHouse analytics. Contains:
                total_time_ms (total execution time), avg_latency_ms (average operation latency), bottlenecks (list of slowest
                operations), stage_count (number of profiled stages). Used for troubleshooting performance issues and
                identifying bottlenecks. None if tier has not completed or performance data collection failed. Populated
                asynchronously via Celery task (non-blocking, best-effort).
            ray_job_id (None | str | Unset): OPTIONAL. Ray/Anyscale job ID for tracking the infrastructure-level processing
                job. None if tier has not yet started or if the job ID was not returned by the engine. Set when tier processing
                is submitted to Ray/Anyscale via the Engine. Used for cancelling running jobs and monitoring infrastructure-
                level status. Format: 'raysubmit_' prefix followed by job identifier (e.g., 'raysubmit_9pDAyZbd5MN281TB'). This
                is the job ID that appears in the Ray/Anyscale dashboard.
            celery_task_id (None | str | Unset): OPTIONAL. Celery task ID for tracking the Celery worker processing this
                tier. None if tier has not yet started or is not processed via Celery. Set when process_tier Celery task is
                triggered. Used for revoking pending/running Celery tasks during batch cancellation or deletion. Format: UUID
                string (e.g., 'a1b2c3d4-e5f6-7890-abcd-ef1234567890').
            source_documents_fetched (int | None | Unset): OPTIONAL. Number of documents fetched from source collection(s)
                for Tier N processing. For Tier 0 (bucket source), this is the number of objects from the bucket. For Tier N+
                (collection source), this is the count of documents from upstream collection(s). Set at the start of tier
                artifact building in build_tier_n_artifacts(). If 0, the source collection is empty - check upstream tier
                completion.
            documents_after_source_filter (int | None | Unset): OPTIONAL. Number of documents remaining after applying
                source_filters. source_filters are optional conditions that exclude documents from processing. If this is 0 but
                source_documents_fetched > 0, your source_filters are too restrictive. Check that filter fields exist in source
                documents and conditions match expected values.
            documents_missing_input_fields (int | None | Unset): OPTIONAL. Number of documents missing required
                input_mapping fields. input_mappings define which fields from source documents map to extractor inputs. If this
                equals documents_after_source_filter, ALL documents are missing required fields. Common cause: upstream
                extractor didn't produce expected output (e.g., video_segment_url). Check upstream extractor configuration and
                verify output field names.
            documents_submitted_to_engine (int | None | Unset): OPTIONAL. Number of documents actually submitted to the
                Ray/Engine for processing. This is documents_after_source_filter minus documents_missing_input_fields. If 0, no
                documents were sent to the engine - check source_filters and input_mappings. If > 0 but documents_written = 0,
                the engine failed to process documents.
            documents_written (int | None | Unset): OPTIONAL. Final count of documents written to the target collection(s).
                Set after tier completion by querying the collection document count. If 0 but documents_submitted_to_engine > 0,
                check tier errors for processing failures. If less than documents_submitted_to_engine, some documents failed
                during processing.
    """

    tier_num: int
    source_type: str
    task_id: None | str | Unset = UNSET
    status: TaskStatusEnum | Unset = UNSET
    collection_ids: list[str] | Unset = UNSET
    source_collection_ids: list[str] | None | Unset = UNSET
    parent_task_id: None | str | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    duration_ms: float | None | Unset = UNSET
    errors: list[BatchErrorDetail] | Unset = UNSET
    error_summary: None | TierTaskInfoErrorSummaryType0 | Unset = UNSET
    performance: None | TierTaskInfoPerformanceType0 | Unset = UNSET
    ray_job_id: None | str | Unset = UNSET
    celery_task_id: None | str | Unset = UNSET
    source_documents_fetched: int | None | Unset = UNSET
    documents_after_source_filter: int | None | Unset = UNSET
    documents_missing_input_fields: int | None | Unset = UNSET
    documents_submitted_to_engine: int | None | Unset = UNSET
    documents_written: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tier_task_info_error_summary_type_0 import TierTaskInfoErrorSummaryType0
        from ..models.tier_task_info_performance_type_0 import TierTaskInfoPerformanceType0

        tier_num = self.tier_num

        source_type = self.source_type

        task_id: None | str | Unset
        if isinstance(self.task_id, Unset):
            task_id = UNSET
        else:
            task_id = self.task_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        collection_ids: list[str] | Unset = UNSET
        if not isinstance(self.collection_ids, Unset):
            collection_ids = self.collection_ids

        source_collection_ids: list[str] | None | Unset
        if isinstance(self.source_collection_ids, Unset):
            source_collection_ids = UNSET
        elif isinstance(self.source_collection_ids, list):
            source_collection_ids = self.source_collection_ids

        else:
            source_collection_ids = self.source_collection_ids

        parent_task_id: None | str | Unset
        if isinstance(self.parent_task_id, Unset):
            parent_task_id = UNSET
        else:
            parent_task_id = self.parent_task_id

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        duration_ms: float | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        error_summary: dict[str, Any] | None | Unset
        if isinstance(self.error_summary, Unset):
            error_summary = UNSET
        elif isinstance(self.error_summary, TierTaskInfoErrorSummaryType0):
            error_summary = self.error_summary.to_dict()
        else:
            error_summary = self.error_summary

        performance: dict[str, Any] | None | Unset
        if isinstance(self.performance, Unset):
            performance = UNSET
        elif isinstance(self.performance, TierTaskInfoPerformanceType0):
            performance = self.performance.to_dict()
        else:
            performance = self.performance

        ray_job_id: None | str | Unset
        if isinstance(self.ray_job_id, Unset):
            ray_job_id = UNSET
        else:
            ray_job_id = self.ray_job_id

        celery_task_id: None | str | Unset
        if isinstance(self.celery_task_id, Unset):
            celery_task_id = UNSET
        else:
            celery_task_id = self.celery_task_id

        source_documents_fetched: int | None | Unset
        if isinstance(self.source_documents_fetched, Unset):
            source_documents_fetched = UNSET
        else:
            source_documents_fetched = self.source_documents_fetched

        documents_after_source_filter: int | None | Unset
        if isinstance(self.documents_after_source_filter, Unset):
            documents_after_source_filter = UNSET
        else:
            documents_after_source_filter = self.documents_after_source_filter

        documents_missing_input_fields: int | None | Unset
        if isinstance(self.documents_missing_input_fields, Unset):
            documents_missing_input_fields = UNSET
        else:
            documents_missing_input_fields = self.documents_missing_input_fields

        documents_submitted_to_engine: int | None | Unset
        if isinstance(self.documents_submitted_to_engine, Unset):
            documents_submitted_to_engine = UNSET
        else:
            documents_submitted_to_engine = self.documents_submitted_to_engine

        documents_written: int | None | Unset
        if isinstance(self.documents_written, Unset):
            documents_written = UNSET
        else:
            documents_written = self.documents_written

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tier_num": tier_num,
                "source_type": source_type,
            }
        )
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if status is not UNSET:
            field_dict["status"] = status
        if collection_ids is not UNSET:
            field_dict["collection_ids"] = collection_ids
        if source_collection_ids is not UNSET:
            field_dict["source_collection_ids"] = source_collection_ids
        if parent_task_id is not UNSET:
            field_dict["parent_task_id"] = parent_task_id
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if errors is not UNSET:
            field_dict["errors"] = errors
        if error_summary is not UNSET:
            field_dict["error_summary"] = error_summary
        if performance is not UNSET:
            field_dict["performance"] = performance
        if ray_job_id is not UNSET:
            field_dict["ray_job_id"] = ray_job_id
        if celery_task_id is not UNSET:
            field_dict["celery_task_id"] = celery_task_id
        if source_documents_fetched is not UNSET:
            field_dict["source_documents_fetched"] = source_documents_fetched
        if documents_after_source_filter is not UNSET:
            field_dict["documents_after_source_filter"] = documents_after_source_filter
        if documents_missing_input_fields is not UNSET:
            field_dict["documents_missing_input_fields"] = documents_missing_input_fields
        if documents_submitted_to_engine is not UNSET:
            field_dict["documents_submitted_to_engine"] = documents_submitted_to_engine
        if documents_written is not UNSET:
            field_dict["documents_written"] = documents_written

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_error_detail import BatchErrorDetail
        from ..models.tier_task_info_error_summary_type_0 import TierTaskInfoErrorSummaryType0
        from ..models.tier_task_info_performance_type_0 import TierTaskInfoPerformanceType0

        d = dict(src_dict)
        tier_num = d.pop("tier_num")

        source_type = d.pop("source_type")

        def _parse_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_id = _parse_task_id(d.pop("task_id", UNSET))

        _status = d.pop("status", UNSET)
        status: TaskStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskStatusEnum(_status)

        collection_ids = cast(list[str], d.pop("collection_ids", UNSET))

        def _parse_source_collection_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_collection_ids_type_0 = cast(list[str], data)

                return source_collection_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        source_collection_ids = _parse_source_collection_ids(d.pop("source_collection_ids", UNSET))

        def _parse_parent_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_task_id = _parse_parent_task_id(d.pop("parent_task_id", UNSET))

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

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

        def _parse_duration_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        _errors = d.pop("errors", UNSET)
        errors: list[BatchErrorDetail] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = BatchErrorDetail.from_dict(errors_item_data)

                errors.append(errors_item)

        def _parse_error_summary(data: object) -> None | TierTaskInfoErrorSummaryType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_summary_type_0 = TierTaskInfoErrorSummaryType0.from_dict(data)

                return error_summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TierTaskInfoErrorSummaryType0 | Unset, data)

        error_summary = _parse_error_summary(d.pop("error_summary", UNSET))

        def _parse_performance(data: object) -> None | TierTaskInfoPerformanceType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                performance_type_0 = TierTaskInfoPerformanceType0.from_dict(data)

                return performance_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TierTaskInfoPerformanceType0 | Unset, data)

        performance = _parse_performance(d.pop("performance", UNSET))

        def _parse_ray_job_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ray_job_id = _parse_ray_job_id(d.pop("ray_job_id", UNSET))

        def _parse_celery_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        celery_task_id = _parse_celery_task_id(d.pop("celery_task_id", UNSET))

        def _parse_source_documents_fetched(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        source_documents_fetched = _parse_source_documents_fetched(d.pop("source_documents_fetched", UNSET))

        def _parse_documents_after_source_filter(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        documents_after_source_filter = _parse_documents_after_source_filter(
            d.pop("documents_after_source_filter", UNSET)
        )

        def _parse_documents_missing_input_fields(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        documents_missing_input_fields = _parse_documents_missing_input_fields(
            d.pop("documents_missing_input_fields", UNSET)
        )

        def _parse_documents_submitted_to_engine(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        documents_submitted_to_engine = _parse_documents_submitted_to_engine(
            d.pop("documents_submitted_to_engine", UNSET)
        )

        def _parse_documents_written(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        documents_written = _parse_documents_written(d.pop("documents_written", UNSET))

        tier_task_info = cls(
            tier_num=tier_num,
            source_type=source_type,
            task_id=task_id,
            status=status,
            collection_ids=collection_ids,
            source_collection_ids=source_collection_ids,
            parent_task_id=parent_task_id,
            started_at=started_at,
            completed_at=completed_at,
            duration_ms=duration_ms,
            errors=errors,
            error_summary=error_summary,
            performance=performance,
            ray_job_id=ray_job_id,
            celery_task_id=celery_task_id,
            source_documents_fetched=source_documents_fetched,
            documents_after_source_filter=documents_after_source_filter,
            documents_missing_input_fields=documents_missing_input_fields,
            documents_submitted_to_engine=documents_submitted_to_engine,
            documents_written=documents_written,
        )

        tier_task_info.additional_properties = d
        return tier_task_info

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
