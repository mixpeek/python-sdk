from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.compound_index_pattern import CompoundIndexPattern
    from ..models.field_performance_metrics import FieldPerformanceMetrics
    from ..models.field_query_metrics import FieldQueryMetrics
    from ..models.index_recommendation import IndexRecommendation
    from ..models.namespace_summary_response_summary import NamespaceSummaryResponseSummary


T = TypeVar("T", bound="NamespaceSummaryResponse")


@_attrs_define
class NamespaceSummaryResponse:
    """Comprehensive namespace analytics summary.

    Attributes:
        namespace_id (str): Namespace ID analyzed
        time_range_days (int): Number of days analyzed
        summary (NamespaceSummaryResponseSummary): Summary statistics (total_fields_analyzed, high_priority_indexes,
            etc.)
        recommendations (list[IndexRecommendation]): Top index recommendations
        most_queried_fields (list[FieldQueryMetrics]): Most frequently queried fields
        slowest_fields (list[FieldPerformanceMetrics]): Fields with highest latency
        compound_indexes (list[CompoundIndexPattern]): Compound index opportunities
    """

    namespace_id: str
    time_range_days: int
    summary: NamespaceSummaryResponseSummary
    recommendations: list[IndexRecommendation]
    most_queried_fields: list[FieldQueryMetrics]
    slowest_fields: list[FieldPerformanceMetrics]
    compound_indexes: list[CompoundIndexPattern]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace_id = self.namespace_id

        time_range_days = self.time_range_days

        summary = self.summary.to_dict()

        recommendations = []
        for recommendations_item_data in self.recommendations:
            recommendations_item = recommendations_item_data.to_dict()
            recommendations.append(recommendations_item)

        most_queried_fields = []
        for most_queried_fields_item_data in self.most_queried_fields:
            most_queried_fields_item = most_queried_fields_item_data.to_dict()
            most_queried_fields.append(most_queried_fields_item)

        slowest_fields = []
        for slowest_fields_item_data in self.slowest_fields:
            slowest_fields_item = slowest_fields_item_data.to_dict()
            slowest_fields.append(slowest_fields_item)

        compound_indexes = []
        for compound_indexes_item_data in self.compound_indexes:
            compound_indexes_item = compound_indexes_item_data.to_dict()
            compound_indexes.append(compound_indexes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace_id": namespace_id,
                "time_range_days": time_range_days,
                "summary": summary,
                "recommendations": recommendations,
                "most_queried_fields": most_queried_fields,
                "slowest_fields": slowest_fields,
                "compound_indexes": compound_indexes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compound_index_pattern import CompoundIndexPattern
        from ..models.field_performance_metrics import FieldPerformanceMetrics
        from ..models.field_query_metrics import FieldQueryMetrics
        from ..models.index_recommendation import IndexRecommendation
        from ..models.namespace_summary_response_summary import NamespaceSummaryResponseSummary

        d = dict(src_dict)
        namespace_id = d.pop("namespace_id")

        time_range_days = d.pop("time_range_days")

        summary = NamespaceSummaryResponseSummary.from_dict(d.pop("summary"))

        recommendations = []
        _recommendations = d.pop("recommendations")
        for recommendations_item_data in _recommendations:
            recommendations_item = IndexRecommendation.from_dict(recommendations_item_data)

            recommendations.append(recommendations_item)

        most_queried_fields = []
        _most_queried_fields = d.pop("most_queried_fields")
        for most_queried_fields_item_data in _most_queried_fields:
            most_queried_fields_item = FieldQueryMetrics.from_dict(most_queried_fields_item_data)

            most_queried_fields.append(most_queried_fields_item)

        slowest_fields = []
        _slowest_fields = d.pop("slowest_fields")
        for slowest_fields_item_data in _slowest_fields:
            slowest_fields_item = FieldPerformanceMetrics.from_dict(slowest_fields_item_data)

            slowest_fields.append(slowest_fields_item)

        compound_indexes = []
        _compound_indexes = d.pop("compound_indexes")
        for compound_indexes_item_data in _compound_indexes:
            compound_indexes_item = CompoundIndexPattern.from_dict(compound_indexes_item_data)

            compound_indexes.append(compound_indexes_item)

        namespace_summary_response = cls(
            namespace_id=namespace_id,
            time_range_days=time_range_days,
            summary=summary,
            recommendations=recommendations,
            most_queried_fields=most_queried_fields,
            slowest_fields=slowest_fields,
            compound_indexes=compound_indexes,
        )

        namespace_summary_response.additional_properties = d
        return namespace_summary_response

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
