from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_diagnostics_performance_summary_type_0 import BatchDiagnosticsPerformanceSummaryType0
    from ..models.collection_diagnostic import CollectionDiagnostic
    from ..models.performance_insight import PerformanceInsight
    from ..models.tier_diagnostic import TierDiagnostic


T = TypeVar("T", bound="BatchDiagnostics")


@_attrs_define
class BatchDiagnostics:
    """Comprehensive batch diagnostics response.

    Combines batch status, task progress, collection info, and performance
    insights into a single response for easy frontend rendering.

        Attributes:
            batch_id (str): Batch ID
            batch_name (str): Batch name
            status (str): Overall batch status
            bucket_id (str): Source bucket ID
            current_tier (int | Unset): Current tier being processed Default: 0.
            total_tiers (int | Unset): Total number of tiers Default: 1.
            overall_progress (float | Unset): Overall progress percentage (0-100) Default: 0.0.
            created_at (datetime.datetime | None | Unset): When batch was created
            submitted_at (datetime.datetime | None | Unset): When batch was submitted
            started_at (datetime.datetime | None | Unset): When processing started
            completed_at (datetime.datetime | None | Unset): When processing completed
            duration_seconds (float | None | Unset): Total duration in seconds
            estimated_completion (datetime.datetime | None | Unset): Estimated completion time
            tiers (list[TierDiagnostic] | Unset): Diagnostic info for each tier
            collections (list[CollectionDiagnostic] | Unset): Status of target collections
            performance_summary (BatchDiagnosticsPerformanceSummaryType0 | None | Unset): Performance metrics summary
                (available after completion)
            insights (list[PerformanceInsight] | Unset): Performance insights and recommendations
            has_failures (bool | Unset): Whether batch has any failures Default: False.
            failed_tier_count (int | Unset): Number of failed tiers Default: 0.
            total_objects (int | Unset): Total objects in batch Default: 0.
            next_actions (list[str] | Unset): Recommended next steps for user
    """

    batch_id: str
    batch_name: str
    status: str
    bucket_id: str
    current_tier: int | Unset = 0
    total_tiers: int | Unset = 1
    overall_progress: float | Unset = 0.0
    created_at: datetime.datetime | None | Unset = UNSET
    submitted_at: datetime.datetime | None | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    duration_seconds: float | None | Unset = UNSET
    estimated_completion: datetime.datetime | None | Unset = UNSET
    tiers: list[TierDiagnostic] | Unset = UNSET
    collections: list[CollectionDiagnostic] | Unset = UNSET
    performance_summary: BatchDiagnosticsPerformanceSummaryType0 | None | Unset = UNSET
    insights: list[PerformanceInsight] | Unset = UNSET
    has_failures: bool | Unset = False
    failed_tier_count: int | Unset = 0
    total_objects: int | Unset = 0
    next_actions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_diagnostics_performance_summary_type_0 import BatchDiagnosticsPerformanceSummaryType0

        batch_id = self.batch_id

        batch_name = self.batch_name

        status = self.status

        bucket_id = self.bucket_id

        current_tier = self.current_tier

        total_tiers = self.total_tiers

        overall_progress = self.overall_progress

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        submitted_at: None | str | Unset
        if isinstance(self.submitted_at, Unset):
            submitted_at = UNSET
        elif isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at

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

        duration_seconds: float | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        estimated_completion: None | str | Unset
        if isinstance(self.estimated_completion, Unset):
            estimated_completion = UNSET
        elif isinstance(self.estimated_completion, datetime.datetime):
            estimated_completion = self.estimated_completion.isoformat()
        else:
            estimated_completion = self.estimated_completion

        tiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = []
            for tiers_item_data in self.tiers:
                tiers_item = tiers_item_data.to_dict()
                tiers.append(tiers_item)

        collections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.collections, Unset):
            collections = []
            for collections_item_data in self.collections:
                collections_item = collections_item_data.to_dict()
                collections.append(collections_item)

        performance_summary: dict[str, Any] | None | Unset
        if isinstance(self.performance_summary, Unset):
            performance_summary = UNSET
        elif isinstance(self.performance_summary, BatchDiagnosticsPerformanceSummaryType0):
            performance_summary = self.performance_summary.to_dict()
        else:
            performance_summary = self.performance_summary

        insights: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.insights, Unset):
            insights = []
            for insights_item_data in self.insights:
                insights_item = insights_item_data.to_dict()
                insights.append(insights_item)

        has_failures = self.has_failures

        failed_tier_count = self.failed_tier_count

        total_objects = self.total_objects

        next_actions: list[str] | Unset = UNSET
        if not isinstance(self.next_actions, Unset):
            next_actions = self.next_actions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "batch_id": batch_id,
                "batch_name": batch_name,
                "status": status,
                "bucket_id": bucket_id,
            }
        )
        if current_tier is not UNSET:
            field_dict["current_tier"] = current_tier
        if total_tiers is not UNSET:
            field_dict["total_tiers"] = total_tiers
        if overall_progress is not UNSET:
            field_dict["overall_progress"] = overall_progress
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if submitted_at is not UNSET:
            field_dict["submitted_at"] = submitted_at
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if estimated_completion is not UNSET:
            field_dict["estimated_completion"] = estimated_completion
        if tiers is not UNSET:
            field_dict["tiers"] = tiers
        if collections is not UNSET:
            field_dict["collections"] = collections
        if performance_summary is not UNSET:
            field_dict["performance_summary"] = performance_summary
        if insights is not UNSET:
            field_dict["insights"] = insights
        if has_failures is not UNSET:
            field_dict["has_failures"] = has_failures
        if failed_tier_count is not UNSET:
            field_dict["failed_tier_count"] = failed_tier_count
        if total_objects is not UNSET:
            field_dict["total_objects"] = total_objects
        if next_actions is not UNSET:
            field_dict["next_actions"] = next_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_diagnostics_performance_summary_type_0 import BatchDiagnosticsPerformanceSummaryType0
        from ..models.collection_diagnostic import CollectionDiagnostic
        from ..models.performance_insight import PerformanceInsight
        from ..models.tier_diagnostic import TierDiagnostic

        d = dict(src_dict)
        batch_id = d.pop("batch_id")

        batch_name = d.pop("batch_name")

        status = d.pop("status")

        bucket_id = d.pop("bucket_id")

        current_tier = d.pop("current_tier", UNSET)

        total_tiers = d.pop("total_tiers", UNSET)

        overall_progress = d.pop("overall_progress", UNSET)

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

        def _parse_submitted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = isoparse(data)

                return submitted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at", UNSET))

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

        def _parse_duration_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds", UNSET))

        def _parse_estimated_completion(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                estimated_completion_type_0 = isoparse(data)

                return estimated_completion_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        estimated_completion = _parse_estimated_completion(d.pop("estimated_completion", UNSET))

        _tiers = d.pop("tiers", UNSET)
        tiers: list[TierDiagnostic] | Unset = UNSET
        if _tiers is not UNSET:
            tiers = []
            for tiers_item_data in _tiers:
                tiers_item = TierDiagnostic.from_dict(tiers_item_data)

                tiers.append(tiers_item)

        _collections = d.pop("collections", UNSET)
        collections: list[CollectionDiagnostic] | Unset = UNSET
        if _collections is not UNSET:
            collections = []
            for collections_item_data in _collections:
                collections_item = CollectionDiagnostic.from_dict(collections_item_data)

                collections.append(collections_item)

        def _parse_performance_summary(data: object) -> BatchDiagnosticsPerformanceSummaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                performance_summary_type_0 = BatchDiagnosticsPerformanceSummaryType0.from_dict(data)

                return performance_summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BatchDiagnosticsPerformanceSummaryType0 | None | Unset, data)

        performance_summary = _parse_performance_summary(d.pop("performance_summary", UNSET))

        _insights = d.pop("insights", UNSET)
        insights: list[PerformanceInsight] | Unset = UNSET
        if _insights is not UNSET:
            insights = []
            for insights_item_data in _insights:
                insights_item = PerformanceInsight.from_dict(insights_item_data)

                insights.append(insights_item)

        has_failures = d.pop("has_failures", UNSET)

        failed_tier_count = d.pop("failed_tier_count", UNSET)

        total_objects = d.pop("total_objects", UNSET)

        next_actions = cast(list[str], d.pop("next_actions", UNSET))

        batch_diagnostics = cls(
            batch_id=batch_id,
            batch_name=batch_name,
            status=status,
            bucket_id=bucket_id,
            current_tier=current_tier,
            total_tiers=total_tiers,
            overall_progress=overall_progress,
            created_at=created_at,
            submitted_at=submitted_at,
            started_at=started_at,
            completed_at=completed_at,
            duration_seconds=duration_seconds,
            estimated_completion=estimated_completion,
            tiers=tiers,
            collections=collections,
            performance_summary=performance_summary,
            insights=insights,
            has_failures=has_failures,
            failed_tier_count=failed_tier_count,
            total_objects=total_objects,
            next_actions=next_actions,
        )

        batch_diagnostics.additional_properties = d
        return batch_diagnostics

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
