from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.explain_retriever_response_estimated_cost import ExplainRetrieverResponseEstimatedCost
    from ..models.explain_retriever_response_optimization_details_type_0 import (
        ExplainRetrieverResponseOptimizationDetailsType0,
    )
    from ..models.explain_retriever_response_optimization_suggestions_item import (
        ExplainRetrieverResponseOptimizationSuggestionsItem,
    )
    from ..models.explain_stage_plan import ExplainStagePlan


T = TypeVar("T", bound="ExplainRetrieverResponse")


@_attrs_define
class ExplainRetrieverResponse:
    """Execution plan analysis for a retriever.

    Provides comprehensive diagnostics about retriever execution characteristics
    without actually running the query. Similar to MongoDB's explain plan or SQL's
    EXPLAIN command, this helps troubleshoot performance, estimate costs, and
    understand optimizer behavior.

    Use Cases:
        - Identify bottleneck stages before execution
        - Estimate costs for budget planning
        - Debug slow retrievers by analyzing stage efficiency
        - Understand optimizer transformations
        - Compare different retriever configurations
        - Troubleshoot accuracy issues via document flow analysis

        Attributes:
            retriever_id (str): Unique identifier of the retriever being explained. REQUIRED.
            retriever_name (str): Human-readable name of the retriever. REQUIRED.
            estimated_cost (ExplainRetrieverResponseEstimatedCost): Estimated total cost breakdown for executing this
                retriever. Contains: 'total_credits' (credit cost), 'total_duration_ms' (latency). Sum of all stage costs. Use
                for budget planning. REQUIRED.
            total_estimated_stages (int): Total number of stages in the optimized execution plan. This may differ from your
                original stage count if optimizations were applied. Compare with optimization_details.original_stage_count to
                see reduction. REQUIRED.
            execution_plan (list[ExplainStagePlan] | Unset): Ordered list of stage execution plans showing the OPTIMIZED
                pipeline. Each entry shows cost, latency, document flow, and warnings for one stage. Stages execute in this
                order. REQUIRED (may be empty for invalid retrievers).
            optimization_suggestions (list[ExplainRetrieverResponseOptimizationSuggestionsItem] | Unset): Actionable
                suggestions for improving retriever performance. Each suggestion includes: 'type' (suggestion category), 'stage'
                (affected stage name), 'message' (human-readable description). Common types: 'reduce_limit', 'add_filter',
                'reorder_stages', 'enable_cache'. OPTIONAL (empty if no suggestions).
            bottleneck_stages (list[str] | Unset): Names of stages expected to dominate execution time. Includes stages with
                duration >= 80%% of the slowest stage. Focus optimization efforts on these stages. OPTIONAL (empty if all stages
                have similar duration).
            optimization_level (str | Unset): Optimization level applied by the optimizer. Values: 'none' (no optimization),
                'mvp' (basic optimizations), 'advanced' (all optimizations). REQUIRED. Default: 'mvp'.
            optimization_applied (bool | Unset): Whether automatic pipeline optimizations were applied. When true,
                execution_plan shows OPTIMIZED stages (after transformations like filter push-down, stage fusion, grouping
                optimization). When false, execution_plan matches your original configuration. Check optimization_details to see
                what changed. REQUIRED. Default: False.
            optimization_details (ExplainRetrieverResponseOptimizationDetailsType0 | None | Unset): Detailed breakdown of
                optimization transformations applied. Only present when optimization_applied=true.

                Fields:
                - original_stage_count: Stage count before optimization
                - optimized_stage_count: Stage count after optimization
                - optimization_time_ms: Time spent on optimization (typically <100ms)
                - stage_reduction_pct: Percentage reduction in stage count
                - decisions: Array of optimization decisions


                Each decision contains:
                - rule_type: Optimization rule that fired
                - applied: Whether the rule was applied
                - reason: Human-readable explanation
                - stages_before/after: Stage counts before/after this rule


                Common rule types:
                - push_down_filters: Move filters earlier to reduce downstream work
                - group_by_push_down: Push grouping to database layer (10-100x faster)
                - merge_consecutive_filters: Combine adjacent filters
                - eliminate_redundant_sorts: Remove duplicate sort operations


                OPTIONAL (null when optimization_applied=false).
    """

    retriever_id: str
    retriever_name: str
    estimated_cost: ExplainRetrieverResponseEstimatedCost
    total_estimated_stages: int
    execution_plan: list[ExplainStagePlan] | Unset = UNSET
    optimization_suggestions: list[ExplainRetrieverResponseOptimizationSuggestionsItem] | Unset = UNSET
    bottleneck_stages: list[str] | Unset = UNSET
    optimization_level: str | Unset = "mvp"
    optimization_applied: bool | Unset = False
    optimization_details: ExplainRetrieverResponseOptimizationDetailsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.explain_retriever_response_optimization_details_type_0 import (
            ExplainRetrieverResponseOptimizationDetailsType0,
        )

        retriever_id = self.retriever_id

        retriever_name = self.retriever_name

        estimated_cost = self.estimated_cost.to_dict()

        total_estimated_stages = self.total_estimated_stages

        execution_plan: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.execution_plan, Unset):
            execution_plan = []
            for execution_plan_item_data in self.execution_plan:
                execution_plan_item = execution_plan_item_data.to_dict()
                execution_plan.append(execution_plan_item)

        optimization_suggestions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.optimization_suggestions, Unset):
            optimization_suggestions = []
            for optimization_suggestions_item_data in self.optimization_suggestions:
                optimization_suggestions_item = optimization_suggestions_item_data.to_dict()
                optimization_suggestions.append(optimization_suggestions_item)

        bottleneck_stages: list[str] | Unset = UNSET
        if not isinstance(self.bottleneck_stages, Unset):
            bottleneck_stages = self.bottleneck_stages

        optimization_level = self.optimization_level

        optimization_applied = self.optimization_applied

        optimization_details: dict[str, Any] | None | Unset
        if isinstance(self.optimization_details, Unset):
            optimization_details = UNSET
        elif isinstance(self.optimization_details, ExplainRetrieverResponseOptimizationDetailsType0):
            optimization_details = self.optimization_details.to_dict()
        else:
            optimization_details = self.optimization_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retriever_id": retriever_id,
                "retriever_name": retriever_name,
                "estimated_cost": estimated_cost,
                "total_estimated_stages": total_estimated_stages,
            }
        )
        if execution_plan is not UNSET:
            field_dict["execution_plan"] = execution_plan
        if optimization_suggestions is not UNSET:
            field_dict["optimization_suggestions"] = optimization_suggestions
        if bottleneck_stages is not UNSET:
            field_dict["bottleneck_stages"] = bottleneck_stages
        if optimization_level is not UNSET:
            field_dict["optimization_level"] = optimization_level
        if optimization_applied is not UNSET:
            field_dict["optimization_applied"] = optimization_applied
        if optimization_details is not UNSET:
            field_dict["optimization_details"] = optimization_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.explain_retriever_response_estimated_cost import ExplainRetrieverResponseEstimatedCost
        from ..models.explain_retriever_response_optimization_details_type_0 import (
            ExplainRetrieverResponseOptimizationDetailsType0,
        )
        from ..models.explain_retriever_response_optimization_suggestions_item import (
            ExplainRetrieverResponseOptimizationSuggestionsItem,
        )
        from ..models.explain_stage_plan import ExplainStagePlan

        d = dict(src_dict)
        retriever_id = d.pop("retriever_id")

        retriever_name = d.pop("retriever_name")

        estimated_cost = ExplainRetrieverResponseEstimatedCost.from_dict(d.pop("estimated_cost"))

        total_estimated_stages = d.pop("total_estimated_stages")

        _execution_plan = d.pop("execution_plan", UNSET)
        execution_plan: list[ExplainStagePlan] | Unset = UNSET
        if _execution_plan is not UNSET:
            execution_plan = []
            for execution_plan_item_data in _execution_plan:
                execution_plan_item = ExplainStagePlan.from_dict(execution_plan_item_data)

                execution_plan.append(execution_plan_item)

        _optimization_suggestions = d.pop("optimization_suggestions", UNSET)
        optimization_suggestions: list[ExplainRetrieverResponseOptimizationSuggestionsItem] | Unset = UNSET
        if _optimization_suggestions is not UNSET:
            optimization_suggestions = []
            for optimization_suggestions_item_data in _optimization_suggestions:
                optimization_suggestions_item = ExplainRetrieverResponseOptimizationSuggestionsItem.from_dict(
                    optimization_suggestions_item_data
                )

                optimization_suggestions.append(optimization_suggestions_item)

        bottleneck_stages = cast(list[str], d.pop("bottleneck_stages", UNSET))

        optimization_level = d.pop("optimization_level", UNSET)

        optimization_applied = d.pop("optimization_applied", UNSET)

        def _parse_optimization_details(
            data: object,
        ) -> ExplainRetrieverResponseOptimizationDetailsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                optimization_details_type_0 = ExplainRetrieverResponseOptimizationDetailsType0.from_dict(data)

                return optimization_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExplainRetrieverResponseOptimizationDetailsType0 | None | Unset, data)

        optimization_details = _parse_optimization_details(d.pop("optimization_details", UNSET))

        explain_retriever_response = cls(
            retriever_id=retriever_id,
            retriever_name=retriever_name,
            estimated_cost=estimated_cost,
            total_estimated_stages=total_estimated_stages,
            execution_plan=execution_plan,
            optimization_suggestions=optimization_suggestions,
            bottleneck_stages=bottleneck_stages,
            optimization_level=optimization_level,
            optimization_applied=optimization_applied,
            optimization_details=optimization_details,
        )

        explain_retriever_response.additional_properties = d
        return explain_retriever_response

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
