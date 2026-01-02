from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aggregation_operation import AggregationOperation
    from ..models.group_by_field import GroupByField
    from ..models.having_condition import HavingCondition
    from ..models.object_aggregation_request_filters_type_0 import ObjectAggregationRequestFiltersType0
    from ..models.range_bucket import RangeBucket


T = TypeVar("T", bound="ObjectAggregationRequest")


@_attrs_define
class ObjectAggregationRequest:
    """Aggregation request for bucket objects.

    Extends the base AggregationRequest with object-specific context.
    Inherits all fields from AggregationRequest.

    Requirements:
        - group_by: REQUIRED, fields to group by
        - aggregations: REQUIRED, aggregation operations to perform
        - All other fields from AggregationRequest are available

    Examples:
        - Count objects by status
        - Daily upload statistics
        - Category-based analytics with filtering

        Attributes:
            group_by (list[GroupByField]): Fields to group results by. REQUIRED, at least one field. Can include field
                transformations (date_trunc, date_part). Results will have one row per unique combination of group_by values.
            aggregations (list[AggregationOperation]): Aggregation operations to perform. REQUIRED, at least one operation.
                Each operation produces a calculated field in results. Can combine multiple functions (COUNT, SUM, AVG, etc.).
            filters (None | ObjectAggregationRequestFiltersType0 | Unset): Pre-aggregation filters to apply to source data.
                OPTIONAL, filters data before grouping. Uses same syntax as standard query filters. Applied before GROUP BY.
            having (list[HavingCondition] | None | Unset): Post-aggregation filters to apply to results. OPTIONAL, filters
                groups after aggregation. Uses aggregation aliases as field names. Applied after GROUP BY and aggregation
                calculations.
            unwind (None | str | Unset): Array field to unwind before aggregation. OPTIONAL, creates one document per array
                element. Useful for aggregating over array contents. Example: 'blobs' to analyze each blob separately.
            range_buckets (list[RangeBucket] | None | Unset): Range-based bucketing for numeric fields. OPTIONAL, creates
                histogram-style buckets. Groups numeric values into defined ranges. Applied during grouping stage.
            sort_by (None | str | Unset): Field to sort results by. OPTIONAL, can be group_by field or aggregation alias.
                Defaults to no specific order. Use with sort_direction to control order.
            sort_direction (str | Unset): Sort direction. OPTIONAL, defaults to 'desc' (descending). Valid values: 'asc'
                (ascending), 'desc' (descending). Used with sort_by field. Default: 'desc'.
            limit (int | None | Unset): Maximum number of results to return. OPTIONAL, no limit if not specified. Applied
                after sorting. Useful for 'top N' queries.
    """

    group_by: list[GroupByField]
    aggregations: list[AggregationOperation]
    filters: None | ObjectAggregationRequestFiltersType0 | Unset = UNSET
    having: list[HavingCondition] | None | Unset = UNSET
    unwind: None | str | Unset = UNSET
    range_buckets: list[RangeBucket] | None | Unset = UNSET
    sort_by: None | str | Unset = UNSET
    sort_direction: str | Unset = "desc"
    limit: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.object_aggregation_request_filters_type_0 import ObjectAggregationRequestFiltersType0

        group_by = []
        for group_by_item_data in self.group_by:
            group_by_item = group_by_item_data.to_dict()
            group_by.append(group_by_item)

        aggregations = []
        for aggregations_item_data in self.aggregations:
            aggregations_item = aggregations_item_data.to_dict()
            aggregations.append(aggregations_item)

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, ObjectAggregationRequestFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        having: list[dict[str, Any]] | None | Unset
        if isinstance(self.having, Unset):
            having = UNSET
        elif isinstance(self.having, list):
            having = []
            for having_type_0_item_data in self.having:
                having_type_0_item = having_type_0_item_data.to_dict()
                having.append(having_type_0_item)

        else:
            having = self.having

        unwind: None | str | Unset
        if isinstance(self.unwind, Unset):
            unwind = UNSET
        else:
            unwind = self.unwind

        range_buckets: list[dict[str, Any]] | None | Unset
        if isinstance(self.range_buckets, Unset):
            range_buckets = UNSET
        elif isinstance(self.range_buckets, list):
            range_buckets = []
            for range_buckets_type_0_item_data in self.range_buckets:
                range_buckets_type_0_item = range_buckets_type_0_item_data.to_dict()
                range_buckets.append(range_buckets_type_0_item)

        else:
            range_buckets = self.range_buckets

        sort_by: None | str | Unset
        if isinstance(self.sort_by, Unset):
            sort_by = UNSET
        else:
            sort_by = self.sort_by

        sort_direction = self.sort_direction

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_by": group_by,
                "aggregations": aggregations,
            }
        )
        if filters is not UNSET:
            field_dict["filters"] = filters
        if having is not UNSET:
            field_dict["having"] = having
        if unwind is not UNSET:
            field_dict["unwind"] = unwind
        if range_buckets is not UNSET:
            field_dict["range_buckets"] = range_buckets
        if sort_by is not UNSET:
            field_dict["sort_by"] = sort_by
        if sort_direction is not UNSET:
            field_dict["sort_direction"] = sort_direction
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aggregation_operation import AggregationOperation
        from ..models.group_by_field import GroupByField
        from ..models.having_condition import HavingCondition
        from ..models.object_aggregation_request_filters_type_0 import ObjectAggregationRequestFiltersType0
        from ..models.range_bucket import RangeBucket

        d = dict(src_dict)
        group_by = []
        _group_by = d.pop("group_by")
        for group_by_item_data in _group_by:
            group_by_item = GroupByField.from_dict(group_by_item_data)

            group_by.append(group_by_item)

        aggregations = []
        _aggregations = d.pop("aggregations")
        for aggregations_item_data in _aggregations:
            aggregations_item = AggregationOperation.from_dict(aggregations_item_data)

            aggregations.append(aggregations_item)

        def _parse_filters(data: object) -> None | ObjectAggregationRequestFiltersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = ObjectAggregationRequestFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ObjectAggregationRequestFiltersType0 | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_having(data: object) -> list[HavingCondition] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                having_type_0 = []
                _having_type_0 = data
                for having_type_0_item_data in _having_type_0:
                    having_type_0_item = HavingCondition.from_dict(having_type_0_item_data)

                    having_type_0.append(having_type_0_item)

                return having_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HavingCondition] | None | Unset, data)

        having = _parse_having(d.pop("having", UNSET))

        def _parse_unwind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unwind = _parse_unwind(d.pop("unwind", UNSET))

        def _parse_range_buckets(data: object) -> list[RangeBucket] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                range_buckets_type_0 = []
                _range_buckets_type_0 = data
                for range_buckets_type_0_item_data in _range_buckets_type_0:
                    range_buckets_type_0_item = RangeBucket.from_dict(range_buckets_type_0_item_data)

                    range_buckets_type_0.append(range_buckets_type_0_item)

                return range_buckets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RangeBucket] | None | Unset, data)

        range_buckets = _parse_range_buckets(d.pop("range_buckets", UNSET))

        def _parse_sort_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sort_by = _parse_sort_by(d.pop("sort_by", UNSET))

        sort_direction = d.pop("sort_direction", UNSET)

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        object_aggregation_request = cls(
            group_by=group_by,
            aggregations=aggregations,
            filters=filters,
            having=having,
            unwind=unwind,
            range_buckets=range_buckets,
            sort_by=sort_by,
            sort_direction=sort_direction,
            limit=limit,
        )

        object_aggregation_request.additional_properties = d
        return object_aggregation_request

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
