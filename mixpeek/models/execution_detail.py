from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_detail_budget import ExecutionDetailBudget
    from ..models.execution_detail_documents_item import ExecutionDetailDocumentsItem
    from ..models.execution_detail_optimization_summary_type_0 import ExecutionDetailOptimizationSummaryType0
    from ..models.execution_detail_pagination import ExecutionDetailPagination
    from ..models.retriever_execution_statistics import RetrieverExecutionStatistics


T = TypeVar("T", bound="ExecutionDetail")


@_attrs_define
class ExecutionDetail:
    """Alias wrapper for execution detail documentation.

    Attributes:
        execution_id (str): REQUIRED. Unique identifier for this execution run. Use this ID to track execution status,
            retrieve execution details, or query execution history. Format: 'exec_' prefix followed by alphanumeric token.
        status (str): REQUIRED. Execution status indicating current state. Common values: 'completed', 'failed',
            'processing', 'pending'. Check this field to determine if execution succeeded or requires retry.
        documents (list[ExecutionDetailDocumentsItem] | Unset): REQUIRED. Final document results after retriever
            completion. Contains documents that passed through all retriever stages. Each document may include: document_id,
            payload (full document data), score (relevance score), metadata (collection-specific fields), and any fields
            added by enrichment/join stages. Empty array indicates no documents matched the query criteria. Note: Legacy
            format may use 'final_results' instead of 'documents'.
        pagination (ExecutionDetailPagination | Unset): REQUIRED. Pagination metadata structure. Format varies by
            pagination method: Offset pagination: {total, limit, offset, has_next, has_previous}, Cursor pagination:
            {cursor, has_next, page_size}, Keyset pagination: {next_cursor, has_next}. Use this to navigate through result
            pages.
        stage_statistics (RetrieverExecutionStatistics | Unset): Aggregated execution statistics for an entire retriever
            execution run.
        budget (ExecutionDetailBudget | Unset): REQUIRED. Budget usage snapshot for this execution. Contains:
            credits_used (credits consumed), credits_remaining (remaining budget), time_used_ms (execution time), and budget
            limits. Use this to track resource consumption and enforce budget limits.
        error (None | str | Unset): OPTIONAL. Retriever-level error message if execution failed. Only present when
            status='failed'. Contains human-readable error description to help diagnose the failure. Check stage_statistics
            for stage-specific errors.
        optimization_applied (bool | Unset): OPTIONAL. Whether automatic pipeline optimizations were applied before
            execution. Mixpeek automatically optimizes retrieval pipelines for performance by reordering stages, merging
            operations, and pushing work to the database layer. Optimizations preserve logical equivalence - you get the
            same results, just faster. When true, see optimization_summary for details about what changed. Default: False.
        optimization_summary (ExecutionDetailOptimizationSummaryType0 | None | Unset): OPTIONAL. Summary of pipeline
            optimizations applied before execution. Only present when optimization_applied=true. Contains: -
            original_stage_count: Number of stages in your original pipeline - optimized_stage_count: Number of stages after
            optimization - optimization_time_ms: Time spent optimizing (typically <100ms) - rules_applied: List of
            optimization rules that fired - stage_reduction_pct: Percentage reduction in stage count Use this to understand
            how the optimizer improved your pipeline. See OptimizationRuleType enum for detailed rule descriptions.
        created_at (datetime.datetime | Unset): Timestamp when execution began
        completed_at (datetime.datetime | None | Unset): Timestamp when execution finished
        current_stage (None | str | Unset): Stage currently running when execution in-flight
        stages_completed (int | Unset): Number of stages finished so far Default: 0.
        total_stages (int | Unset): Total stages configured Default: 0.
    """

    execution_id: str
    status: str
    documents: list[ExecutionDetailDocumentsItem] | Unset = UNSET
    pagination: ExecutionDetailPagination | Unset = UNSET
    stage_statistics: RetrieverExecutionStatistics | Unset = UNSET
    budget: ExecutionDetailBudget | Unset = UNSET
    error: None | str | Unset = UNSET
    optimization_applied: bool | Unset = False
    optimization_summary: ExecutionDetailOptimizationSummaryType0 | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    current_stage: None | str | Unset = UNSET
    stages_completed: int | Unset = 0
    total_stages: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.execution_detail_optimization_summary_type_0 import ExecutionDetailOptimizationSummaryType0

        execution_id = self.execution_id

        status = self.status

        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        stage_statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stage_statistics, Unset):
            stage_statistics = self.stage_statistics.to_dict()

        budget: dict[str, Any] | Unset = UNSET
        if not isinstance(self.budget, Unset):
            budget = self.budget.to_dict()

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        optimization_applied = self.optimization_applied

        optimization_summary: dict[str, Any] | None | Unset
        if isinstance(self.optimization_summary, Unset):
            optimization_summary = UNSET
        elif isinstance(self.optimization_summary, ExecutionDetailOptimizationSummaryType0):
            optimization_summary = self.optimization_summary.to_dict()
        else:
            optimization_summary = self.optimization_summary

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        current_stage: None | str | Unset
        if isinstance(self.current_stage, Unset):
            current_stage = UNSET
        else:
            current_stage = self.current_stage

        stages_completed = self.stages_completed

        total_stages = self.total_stages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "execution_id": execution_id,
                "status": status,
            }
        )
        if documents is not UNSET:
            field_dict["documents"] = documents
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if stage_statistics is not UNSET:
            field_dict["stage_statistics"] = stage_statistics
        if budget is not UNSET:
            field_dict["budget"] = budget
        if error is not UNSET:
            field_dict["error"] = error
        if optimization_applied is not UNSET:
            field_dict["optimization_applied"] = optimization_applied
        if optimization_summary is not UNSET:
            field_dict["optimization_summary"] = optimization_summary
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if current_stage is not UNSET:
            field_dict["current_stage"] = current_stage
        if stages_completed is not UNSET:
            field_dict["stages_completed"] = stages_completed
        if total_stages is not UNSET:
            field_dict["total_stages"] = total_stages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_detail_budget import ExecutionDetailBudget
        from ..models.execution_detail_documents_item import ExecutionDetailDocumentsItem
        from ..models.execution_detail_optimization_summary_type_0 import ExecutionDetailOptimizationSummaryType0
        from ..models.execution_detail_pagination import ExecutionDetailPagination
        from ..models.retriever_execution_statistics import RetrieverExecutionStatistics

        d = dict(src_dict)
        execution_id = d.pop("execution_id")

        status = d.pop("status")

        _documents = d.pop("documents", UNSET)
        documents: list[ExecutionDetailDocumentsItem] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = ExecutionDetailDocumentsItem.from_dict(documents_item_data)

                documents.append(documents_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: ExecutionDetailPagination | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = ExecutionDetailPagination.from_dict(_pagination)

        _stage_statistics = d.pop("stage_statistics", UNSET)
        stage_statistics: RetrieverExecutionStatistics | Unset
        if isinstance(_stage_statistics, Unset):
            stage_statistics = UNSET
        else:
            stage_statistics = RetrieverExecutionStatistics.from_dict(_stage_statistics)

        _budget = d.pop("budget", UNSET)
        budget: ExecutionDetailBudget | Unset
        if isinstance(_budget, Unset):
            budget = UNSET
        else:
            budget = ExecutionDetailBudget.from_dict(_budget)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        optimization_applied = d.pop("optimization_applied", UNSET)

        def _parse_optimization_summary(data: object) -> ExecutionDetailOptimizationSummaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                optimization_summary_type_0 = ExecutionDetailOptimizationSummaryType0.from_dict(data)

                return optimization_summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExecutionDetailOptimizationSummaryType0 | None | Unset, data)

        optimization_summary = _parse_optimization_summary(d.pop("optimization_summary", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

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

        def _parse_current_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_stage = _parse_current_stage(d.pop("current_stage", UNSET))

        stages_completed = d.pop("stages_completed", UNSET)

        total_stages = d.pop("total_stages", UNSET)

        execution_detail = cls(
            execution_id=execution_id,
            status=status,
            documents=documents,
            pagination=pagination,
            stage_statistics=stage_statistics,
            budget=budget,
            error=error,
            optimization_applied=optimization_applied,
            optimization_summary=optimization_summary,
            created_at=created_at,
            completed_at=completed_at,
            current_stage=current_stage,
            stages_completed=stages_completed,
            total_stages=total_stages,
        )

        execution_detail.additional_properties = d
        return execution_detail

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
