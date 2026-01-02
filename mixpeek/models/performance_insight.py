from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PerformanceInsight")


@_attrs_define
class PerformanceInsight:
    """Performance insight or recommendation.

    Attributes:
        type_ (str): Insight type (bottleneck, optimization, warning)
        severity (str): Severity (info, warning, critical)
        message (str): Human-readable message
        stage (None | str | Unset): Related stage name
        metric_value (float | None | Unset): Related metric value
        recommendation (None | str | Unset): Recommended action
    """

    type_: str
    severity: str
    message: str
    stage: None | str | Unset = UNSET
    metric_value: float | None | Unset = UNSET
    recommendation: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        severity = self.severity

        message = self.message

        stage: None | str | Unset
        if isinstance(self.stage, Unset):
            stage = UNSET
        else:
            stage = self.stage

        metric_value: float | None | Unset
        if isinstance(self.metric_value, Unset):
            metric_value = UNSET
        else:
            metric_value = self.metric_value

        recommendation: None | str | Unset
        if isinstance(self.recommendation, Unset):
            recommendation = UNSET
        else:
            recommendation = self.recommendation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "severity": severity,
                "message": message,
            }
        )
        if stage is not UNSET:
            field_dict["stage"] = stage
        if metric_value is not UNSET:
            field_dict["metric_value"] = metric_value
        if recommendation is not UNSET:
            field_dict["recommendation"] = recommendation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        severity = d.pop("severity")

        message = d.pop("message")

        def _parse_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage = _parse_stage(d.pop("stage", UNSET))

        def _parse_metric_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        metric_value = _parse_metric_value(d.pop("metric_value", UNSET))

        def _parse_recommendation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recommendation = _parse_recommendation(d.pop("recommendation", UNSET))

        performance_insight = cls(
            type_=type_,
            severity=severity,
            message=message,
            stage=stage,
            metric_value=metric_value,
            recommendation=recommendation,
        )

        performance_insight.additional_properties = d
        return performance_insight

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
