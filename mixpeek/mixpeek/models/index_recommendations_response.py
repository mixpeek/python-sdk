from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.index_recommendation import IndexRecommendation
    from ..models.index_recommendations_response_summary import IndexRecommendationsResponseSummary


T = TypeVar("T", bound="IndexRecommendationsResponse")


@_attrs_define
class IndexRecommendationsResponse:
    """Response for index recommendations endpoint.

    Attributes:
        namespace_id (str): Namespace ID analyzed
        time_range_days (int): Number of days analyzed
        recommendations (list[IndexRecommendation]): Index recommendations
        summary (IndexRecommendationsResponseSummary): Summary statistics (high_priority, medium_priority, low_priority
            counts)
    """

    namespace_id: str
    time_range_days: int
    recommendations: list[IndexRecommendation]
    summary: IndexRecommendationsResponseSummary
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace_id = self.namespace_id

        time_range_days = self.time_range_days

        recommendations = []
        for recommendations_item_data in self.recommendations:
            recommendations_item = recommendations_item_data.to_dict()
            recommendations.append(recommendations_item)

        summary = self.summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace_id": namespace_id,
                "time_range_days": time_range_days,
                "recommendations": recommendations,
                "summary": summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.index_recommendation import IndexRecommendation
        from ..models.index_recommendations_response_summary import IndexRecommendationsResponseSummary

        d = dict(src_dict)
        namespace_id = d.pop("namespace_id")

        time_range_days = d.pop("time_range_days")

        recommendations = []
        _recommendations = d.pop("recommendations")
        for recommendations_item_data in _recommendations:
            recommendations_item = IndexRecommendation.from_dict(recommendations_item_data)

            recommendations.append(recommendations_item)

        summary = IndexRecommendationsResponseSummary.from_dict(d.pop("summary"))

        index_recommendations_response = cls(
            namespace_id=namespace_id,
            time_range_days=time_range_days,
            recommendations=recommendations,
            summary=summary,
        )

        index_recommendations_response.additional_properties = d
        return index_recommendations_response

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
