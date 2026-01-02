from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.confidence_distribution import ConfidenceDistribution


T = TypeVar("T", bound="ConfidenceResponse")


@_attrs_define
class ConfidenceResponse:
    """Taxonomy confidence distribution response.

    Attributes:
        taxonomy_id (str):
        distribution (list[ConfidenceDistribution]):
        avg_confidence (float):
        low_confidence_count (int): Count of assignments below 0.5 confidence
    """

    taxonomy_id: str
    distribution: list[ConfidenceDistribution]
    avg_confidence: float
    low_confidence_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        taxonomy_id = self.taxonomy_id

        distribution = []
        for distribution_item_data in self.distribution:
            distribution_item = distribution_item_data.to_dict()
            distribution.append(distribution_item)

        avg_confidence = self.avg_confidence

        low_confidence_count = self.low_confidence_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taxonomy_id": taxonomy_id,
                "distribution": distribution,
                "avg_confidence": avg_confidence,
                "low_confidence_count": low_confidence_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.confidence_distribution import ConfidenceDistribution

        d = dict(src_dict)
        taxonomy_id = d.pop("taxonomy_id")

        distribution = []
        _distribution = d.pop("distribution")
        for distribution_item_data in _distribution:
            distribution_item = ConfidenceDistribution.from_dict(distribution_item_data)

            distribution.append(distribution_item)

        avg_confidence = d.pop("avg_confidence")

        low_confidence_count = d.pop("low_confidence_count")

        confidence_response = cls(
            taxonomy_id=taxonomy_id,
            distribution=distribution,
            avg_confidence=avg_confidence,
            low_confidence_count=low_confidence_count,
        )

        confidence_response.additional_properties = d
        return confidence_response

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
