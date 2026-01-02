from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.evaluation_status import EvaluationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.evaluation_config import EvaluationConfig
    from ..models.evaluation_record_metrics_by_k_type_0 import EvaluationRecordMetricsByKType0
    from ..models.evaluation_record_overall_metrics_type_0 import EvaluationRecordOverallMetricsType0


T = TypeVar("T", bound="EvaluationRecord")


@_attrs_define
class EvaluationRecord:
    """Complete evaluation record with results.

    Attributes:
        evaluation_id (str): Unique evaluation identifier
        retriever_id (str): ID of retriever being evaluated
        dataset_id (str): ID of dataset used for evaluation
        dataset_name (str): Name of dataset
        config (EvaluationConfig): Configuration for an evaluation run.
        status (EvaluationStatus): Status of an evaluation run.
        created_at (datetime.datetime): When evaluation was created
        updated_at (datetime.datetime): Last update timestamp
        namespace_id (str): Namespace ID
        internal_id (str): Internal organization ID
        query_count (int): Number of queries evaluated
        completed_at (datetime.datetime | None | Unset): When evaluation completed
        overall_metrics (EvaluationRecordOverallMetricsType0 | None | Unset): Aggregated metrics across all queries
        metrics_by_k (EvaluationRecordMetricsByKType0 | None | Unset): Metrics broken down by K value (keys are string K
            values like '5', '10', '20')
        error_message (None | str | Unset): Error message if failed
    """

    evaluation_id: str
    retriever_id: str
    dataset_id: str
    dataset_name: str
    config: EvaluationConfig
    status: EvaluationStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    namespace_id: str
    internal_id: str
    query_count: int
    completed_at: datetime.datetime | None | Unset = UNSET
    overall_metrics: EvaluationRecordOverallMetricsType0 | None | Unset = UNSET
    metrics_by_k: EvaluationRecordMetricsByKType0 | None | Unset = UNSET
    error_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.evaluation_record_metrics_by_k_type_0 import EvaluationRecordMetricsByKType0
        from ..models.evaluation_record_overall_metrics_type_0 import EvaluationRecordOverallMetricsType0

        evaluation_id = self.evaluation_id

        retriever_id = self.retriever_id

        dataset_id = self.dataset_id

        dataset_name = self.dataset_name

        config = self.config.to_dict()

        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        namespace_id = self.namespace_id

        internal_id = self.internal_id

        query_count = self.query_count

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        overall_metrics: dict[str, Any] | None | Unset
        if isinstance(self.overall_metrics, Unset):
            overall_metrics = UNSET
        elif isinstance(self.overall_metrics, EvaluationRecordOverallMetricsType0):
            overall_metrics = self.overall_metrics.to_dict()
        else:
            overall_metrics = self.overall_metrics

        metrics_by_k: dict[str, Any] | None | Unset
        if isinstance(self.metrics_by_k, Unset):
            metrics_by_k = UNSET
        elif isinstance(self.metrics_by_k, EvaluationRecordMetricsByKType0):
            metrics_by_k = self.metrics_by_k.to_dict()
        else:
            metrics_by_k = self.metrics_by_k

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "evaluation_id": evaluation_id,
                "retriever_id": retriever_id,
                "dataset_id": dataset_id,
                "dataset_name": dataset_name,
                "config": config,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
                "namespace_id": namespace_id,
                "internal_id": internal_id,
                "query_count": query_count,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if overall_metrics is not UNSET:
            field_dict["overall_metrics"] = overall_metrics
        if metrics_by_k is not UNSET:
            field_dict["metrics_by_k"] = metrics_by_k
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evaluation_config import EvaluationConfig
        from ..models.evaluation_record_metrics_by_k_type_0 import EvaluationRecordMetricsByKType0
        from ..models.evaluation_record_overall_metrics_type_0 import EvaluationRecordOverallMetricsType0

        d = dict(src_dict)
        evaluation_id = d.pop("evaluation_id")

        retriever_id = d.pop("retriever_id")

        dataset_id = d.pop("dataset_id")

        dataset_name = d.pop("dataset_name")

        config = EvaluationConfig.from_dict(d.pop("config"))

        status = EvaluationStatus(d.pop("status"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        namespace_id = d.pop("namespace_id")

        internal_id = d.pop("internal_id")

        query_count = d.pop("query_count")

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

        def _parse_overall_metrics(data: object) -> EvaluationRecordOverallMetricsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                overall_metrics_type_0 = EvaluationRecordOverallMetricsType0.from_dict(data)

                return overall_metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EvaluationRecordOverallMetricsType0 | None | Unset, data)

        overall_metrics = _parse_overall_metrics(d.pop("overall_metrics", UNSET))

        def _parse_metrics_by_k(data: object) -> EvaluationRecordMetricsByKType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metrics_by_k_type_0 = EvaluationRecordMetricsByKType0.from_dict(data)

                return metrics_by_k_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EvaluationRecordMetricsByKType0 | None | Unset, data)

        metrics_by_k = _parse_metrics_by_k(d.pop("metrics_by_k", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        evaluation_record = cls(
            evaluation_id=evaluation_id,
            retriever_id=retriever_id,
            dataset_id=dataset_id,
            dataset_name=dataset_name,
            config=config,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            namespace_id=namespace_id,
            internal_id=internal_id,
            query_count=query_count,
            completed_at=completed_at,
            overall_metrics=overall_metrics,
            metrics_by_k=metrics_by_k,
            error_message=error_message,
        )

        evaluation_record.additional_properties = d
        return evaluation_record

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
