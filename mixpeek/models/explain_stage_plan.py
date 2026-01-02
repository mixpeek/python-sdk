from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExplainStagePlan")


@_attrs_define
class ExplainStagePlan:
    """Stage-level execution plan details for retriever explain endpoint.

    Provides detailed cost, performance, and optimization information for a single
    stage in the retriever pipeline. Use this to understand stage behavior, identify
    bottlenecks, and troubleshoot performance issues.

    This is analogous to a single row in MongoDB's explain plan output, showing
    how documents flow through the stage and what resources are consumed.

        Attributes:
            stage_index (int): Zero-based position of this stage in the execution pipeline. Stages execute sequentially in
                this order. REQUIRED.
            stage_name (str): Human-readable name of this stage instance. Corresponds to the 'stage_name' field in your
                retriever configuration. Use this to map explain plan output back to your pipeline definition. REQUIRED.
            stage_type (str): Stage type identifier indicating the category of operation. Common types: 'filter' (reduce
                documents), 'sort' (reorder), 'reduce' (aggregate), 'apply' (transform/enrich). REQUIRED.
            estimated_input (int): Estimated number of documents entering this stage. This is the output count from the
                previous stage (or initial collection size). Used to project document flow through the pipeline. REQUIRED.
            estimated_output (int): Estimated number of documents leaving this stage. For filter stages, this is typically
                less than estimated_input. For sort/reduce stages, this may be the same or less. REQUIRED.
            estimated_efficiency (float): Stage selectivity ratio (estimated_output / estimated_input). Values closer to 0
                indicate aggressive filtering. Values closer to 1 indicate most documents pass through. Use this to identify
                stages that might be too restrictive or too permissive. REQUIRED.
            estimated_cost_credits (float): Estimated credit cost for executing this stage. Credits are consumed for
                inference (embeddings, LLM calls), vector searches, and other computational operations. Filter/sort stages
                typically have near-zero cost. REQUIRED.
            estimated_duration_ms (float): Estimated latency contribution of this stage in milliseconds. High values
                indicate potential bottlenecks. Sum across stages gives total estimated execution time. REQUIRED.
            cache_likely (bool): Whether this stage is likely to hit cache based on recent execution history. True = cache
                hit likely (near-zero actual latency/cost). False = cache miss likely (full cost incurred). Use this to
                understand when queries will be fast vs slow. REQUIRED.
            optimization_notes (list[str] | Unset): Human-readable notes about optimizations applied to this stage.
                Examples: 'Pushed down from stage 2', 'Merged with previous filter', 'Grouping pushed to database layer'. Empty
                if no optimizations were applied. OPTIONAL.
            warnings (list[str] | Unset): Performance warnings or potential issues with this stage. Examples: 'High cost
                stage - consider reducing limit', 'Very low efficiency - may need filter tuning', 'LLM stage without prior
                filtering - expensive'. Empty if no warnings. OPTIONAL.
    """

    stage_index: int
    stage_name: str
    stage_type: str
    estimated_input: int
    estimated_output: int
    estimated_efficiency: float
    estimated_cost_credits: float
    estimated_duration_ms: float
    cache_likely: bool
    optimization_notes: list[str] | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_index = self.stage_index

        stage_name = self.stage_name

        stage_type = self.stage_type

        estimated_input = self.estimated_input

        estimated_output = self.estimated_output

        estimated_efficiency = self.estimated_efficiency

        estimated_cost_credits = self.estimated_cost_credits

        estimated_duration_ms = self.estimated_duration_ms

        cache_likely = self.cache_likely

        optimization_notes: list[str] | Unset = UNSET
        if not isinstance(self.optimization_notes, Unset):
            optimization_notes = self.optimization_notes

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage_index": stage_index,
                "stage_name": stage_name,
                "stage_type": stage_type,
                "estimated_input": estimated_input,
                "estimated_output": estimated_output,
                "estimated_efficiency": estimated_efficiency,
                "estimated_cost_credits": estimated_cost_credits,
                "estimated_duration_ms": estimated_duration_ms,
                "cache_likely": cache_likely,
            }
        )
        if optimization_notes is not UNSET:
            field_dict["optimization_notes"] = optimization_notes
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stage_index = d.pop("stage_index")

        stage_name = d.pop("stage_name")

        stage_type = d.pop("stage_type")

        estimated_input = d.pop("estimated_input")

        estimated_output = d.pop("estimated_output")

        estimated_efficiency = d.pop("estimated_efficiency")

        estimated_cost_credits = d.pop("estimated_cost_credits")

        estimated_duration_ms = d.pop("estimated_duration_ms")

        cache_likely = d.pop("cache_likely")

        optimization_notes = cast(list[str], d.pop("optimization_notes", UNSET))

        warnings = cast(list[str], d.pop("warnings", UNSET))

        explain_stage_plan = cls(
            stage_index=stage_index,
            stage_name=stage_name,
            stage_type=stage_type,
            estimated_input=estimated_input,
            estimated_output=estimated_output,
            estimated_efficiency=estimated_efficiency,
            estimated_cost_credits=estimated_cost_credits,
            estimated_duration_ms=estimated_duration_ms,
            cache_likely=cache_likely,
            optimization_notes=optimization_notes,
            warnings=warnings,
        )

        explain_stage_plan.additional_properties = d
        return explain_stage_plan

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
