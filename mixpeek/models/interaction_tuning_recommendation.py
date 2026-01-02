from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InteractionTuningRecommendation")


@_attrs_define
class InteractionTuningRecommendation:
    """Recommendation for interaction tuning.

    Attributes:
        recommendation_type (str): Type of recommendation
        recommended_value (Any): Recommended value
        expected_impact (str): Expected performance impact
        confidence (float): Confidence score
        reasoning (str): Explanation of recommendation
        current_value (Any | None | Unset): Current setting value
    """

    recommendation_type: str
    recommended_value: Any
    expected_impact: str
    confidence: float
    reasoning: str
    current_value: Any | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recommendation_type = self.recommendation_type

        recommended_value = self.recommended_value

        expected_impact = self.expected_impact

        confidence = self.confidence

        reasoning = self.reasoning

        current_value: Any | None | Unset
        if isinstance(self.current_value, Unset):
            current_value = UNSET
        else:
            current_value = self.current_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recommendation_type": recommendation_type,
                "recommended_value": recommended_value,
                "expected_impact": expected_impact,
                "confidence": confidence,
                "reasoning": reasoning,
            }
        )
        if current_value is not UNSET:
            field_dict["current_value"] = current_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recommendation_type = d.pop("recommendation_type")

        recommended_value = d.pop("recommended_value")

        expected_impact = d.pop("expected_impact")

        confidence = d.pop("confidence")

        reasoning = d.pop("reasoning")

        def _parse_current_value(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        current_value = _parse_current_value(d.pop("current_value", UNSET))

        interaction_tuning_recommendation = cls(
            recommendation_type=recommendation_type,
            recommended_value=recommended_value,
            expected_impact=expected_impact,
            confidence=confidence,
            reasoning=reasoning,
            current_value=current_value,
        )

        interaction_tuning_recommendation.additional_properties = d
        return interaction_tuning_recommendation

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
