from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logical_operator import LogicalOperator


T = TypeVar("T", bound="SourceFilters")


@_attrs_define
class SourceFilters:
    """Filters applied to source data when processing collections.

    Source filters determine which objects (from buckets) or documents (from collections)
    are processed by this collection. Filters use the same LogicalOperator model as
    list APIs throughout the system, supporting complex AND/OR/NOT logic.

    Use Cases:
        - Process only specific content types from mixed-content buckets
        - Filter by metadata fields (status, category, tags, dates)
        - Create specialized collections from broader sources
        - Exclude certain objects or documents from processing

    Examples:
        Process only video content:
            {
                "AND": [
                    {"field": "blobs.type", "operator": "eq", "value": "video"}
                ]
            }

        Process only active, published content:
            {
                "AND": [
                    {"field": "metadata.status", "operator": "eq", "value": "active"},
                    {"field": "metadata.published", "operator": "eq", "value": true}
                ]
            }

        Process content from last 30 days:
            {
                "AND": [
                    {"field": "created_at", "operator": "gte", "value": "2025-10-08T00:00:00Z"}
                ]
            }

        Process specific brands OR categories:
            {
                "OR": [
                    {"field": "brand_name", "operator": "in", "value": ["Acme", "TechCo"]},
                    {"field": "category", "operator": "eq", "value": "premium"}
                ]
            }

    Filter Operators:
        - eq (equals)
        - ne (not equals)
        - gt (greater than)
        - gte (greater than or equal)
        - lt (less than)
        - lte (less than or equal)
        - in (value in list)
        - nin (value not in list)
        - contains (string contains)
        - starts_with (string starts with)
        - ends_with (string ends with)

    Performance Considerations:
        - Filters are evaluated at batch creation time
        - Only matching objects/documents are included in processing
        - More selective filters = smaller batches = faster processing
        - Use indexed fields (metadata, timestamps) for better performance

    Relationship to Batch Filters:
        - Source filters: Applied at collection definition (consistent across all batches)
        - Batch filters: Applied at batch creation (ad-hoc, per-batch basis)
        - Both can be used together: source filters + batch filters = intersection

        Attributes:
            filters (LogicalOperator | None | Unset): Optional logical filters to apply to source data. Uses LogicalOperator
                model with AND/OR/NOT support. When specified, only objects/documents matching these filters will be processed
                by this collection. When null, all source data is processed (no filtering). Filters are consistent across all
                batch runs for this collection.
    """

    filters: LogicalOperator | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_operator import LogicalOperator

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, LogicalOperator):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logical_operator import LogicalOperator

        d = dict(src_dict)

        def _parse_filters(data: object) -> LogicalOperator | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = LogicalOperator.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LogicalOperator | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        source_filters = cls(
            filters=filters,
        )

        source_filters.additional_properties = d
        return source_filters

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
