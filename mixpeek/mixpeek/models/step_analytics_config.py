from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.step_key_source import StepKeySource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.covariate_config import CovariateConfig


T = TypeVar("T", bound="StepAnalyticsConfig")


@_attrs_define
class StepAnalyticsConfig:
    """Configuration for step-by-step transition analytics on taxonomy assignments.

    Enables analysis of how documents progress through taxonomy labels as a temporal
    sequence, answering questions like:
    - How long from "inquiry" to "closed_won"?
    - What % of "inquiry" emails reach "proposal"?
    - Which sender domains correlate with faster progression?

    Use Cases:
        1. Email Thread Analysis:
           - Track progression: inquiry → followup → proposal → closed_won
           - Identify which subject lines correlate with faster closure

        2. Content Workflow Tracking:
           - Monitor: draft → review → approved → published
           - Find bottlenecks and optimization opportunities

        3. Safety Compliance Monitoring:
           - Trace: violation_detected → investigated → resolved
           - Track resolution times and success rates

    Attributes:
        timestamp_field: Document field containing event timestamp
        sequence_id_field: Field that groups related documents into sequences
        step_key_source: How to extract the step identifier (label/node_id/custom field)
        step_key_field_path: Required if step_key_source='field_path'
        covariates: List of predictor variables to analyze for conversion lift
        max_sequence_duration_days: Filter out sequences longer than this (data quality)

    Example:
        ```python
        # Email thread analysis configuration
        StepAnalyticsConfig(
            timestamp_field="Date",  # Email timestamp
            sequence_id_field="Thread-Index",  # Groups emails in same thread
            step_key_source="assignment_label",  # Use taxonomy label as step
            covariates=[
                CovariateConfig(
                    field_path="sender_domain",
                    covariate_type="categorical",
                    name="Sender Domain"
                ),
                CovariateConfig(
                    field_path="word_count",
                    covariate_type="numeric",
                    name="Email Length"
                )
            ],
            max_sequence_duration_days=90  # Ignore threads >90 days
        )
        ```

        Attributes:
            timestamp_field (str): Document field containing event timestamp (e.g., 'Date', 'created_at',
                'metadata.timestamp')
            sequence_id_field (str): Document field that groups related items into a sequence (e.g., 'Thread-Index',
                'session_id', 'user_id')
            step_key_source (StepKeySource | Unset): Defines how to extract the step key from documents for sequence
                analysis.

                The step key identifies which stage/state a document is in for transition analytics.

                Examples:
                    ASSIGNMENT_LABEL: Use the taxonomy's assigned label (e.g., "inquiry", "proposal")
                    ASSIGNMENT_NODE_ID: Use the taxonomy node ID (e.g., "node_sales_inquiry")
                    FIELD_PATH: Use a custom document field (e.g., "metadata.workflow_stage")
            step_key_field_path (None | str | Unset): Required if step_key_source='field_path'. Dot-notation path to step
                value in document.
            covariates (list[CovariateConfig] | Unset): Predictor fields to analyze for conversion lift (categorical,
                numeric, embedding, cluster)
            max_sequence_duration_days (int | None | Unset): Maximum allowed duration for a sequence. Sequences beyond this
                are flagged as data quality issues.
    """

    timestamp_field: str
    sequence_id_field: str
    step_key_source: StepKeySource | Unset = UNSET
    step_key_field_path: None | str | Unset = UNSET
    covariates: list[CovariateConfig] | Unset = UNSET
    max_sequence_duration_days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp_field = self.timestamp_field

        sequence_id_field = self.sequence_id_field

        step_key_source: str | Unset = UNSET
        if not isinstance(self.step_key_source, Unset):
            step_key_source = self.step_key_source.value

        step_key_field_path: None | str | Unset
        if isinstance(self.step_key_field_path, Unset):
            step_key_field_path = UNSET
        else:
            step_key_field_path = self.step_key_field_path

        covariates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.covariates, Unset):
            covariates = []
            for covariates_item_data in self.covariates:
                covariates_item = covariates_item_data.to_dict()
                covariates.append(covariates_item)

        max_sequence_duration_days: int | None | Unset
        if isinstance(self.max_sequence_duration_days, Unset):
            max_sequence_duration_days = UNSET
        else:
            max_sequence_duration_days = self.max_sequence_duration_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp_field": timestamp_field,
                "sequence_id_field": sequence_id_field,
            }
        )
        if step_key_source is not UNSET:
            field_dict["step_key_source"] = step_key_source
        if step_key_field_path is not UNSET:
            field_dict["step_key_field_path"] = step_key_field_path
        if covariates is not UNSET:
            field_dict["covariates"] = covariates
        if max_sequence_duration_days is not UNSET:
            field_dict["max_sequence_duration_days"] = max_sequence_duration_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.covariate_config import CovariateConfig

        d = dict(src_dict)
        timestamp_field = d.pop("timestamp_field")

        sequence_id_field = d.pop("sequence_id_field")

        _step_key_source = d.pop("step_key_source", UNSET)
        step_key_source: StepKeySource | Unset
        if isinstance(_step_key_source, Unset):
            step_key_source = UNSET
        else:
            step_key_source = StepKeySource(_step_key_source)

        def _parse_step_key_field_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        step_key_field_path = _parse_step_key_field_path(d.pop("step_key_field_path", UNSET))

        _covariates = d.pop("covariates", UNSET)
        covariates: list[CovariateConfig] | Unset = UNSET
        if _covariates is not UNSET:
            covariates = []
            for covariates_item_data in _covariates:
                covariates_item = CovariateConfig.from_dict(covariates_item_data)

                covariates.append(covariates_item)

        def _parse_max_sequence_duration_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_sequence_duration_days = _parse_max_sequence_duration_days(d.pop("max_sequence_duration_days", UNSET))

        step_analytics_config = cls(
            timestamp_field=timestamp_field,
            sequence_id_field=sequence_id_field,
            step_key_source=step_key_source,
            step_key_field_path=step_key_field_path,
            covariates=covariates,
            max_sequence_duration_days=max_sequence_duration_days,
        )

        step_analytics_config.additional_properties = d
        return step_analytics_config

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
