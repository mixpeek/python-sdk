from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.aggregation_function import AggregationFunction
from ..types import UNSET, Unset

T = TypeVar("T", bound="AggregationOperation")


@_attrs_define
class AggregationOperation:
    """Configuration for an aggregation operation.

    Defines a calculation to perform on grouped data.

    Requirements:
        - function: REQUIRED, the aggregation function to apply
        - field: REQUIRED for most functions (except COUNT), field to aggregate
        - alias: REQUIRED, name for the result in output

    Examples:
        - Count: AggregationOperation(function="count", alias="total_count")
        - Sum: AggregationOperation(function="sum", field="metadata.views", alias="total_views")
        - Average: AggregationOperation(function="avg", field="metadata.duration", alias="avg_duration")

        Attributes:
            function (AggregationFunction): Supported aggregation functions.

                These functions can be applied to fields during aggregation operations.

                Values:
                    COUNT: Count total number of items in each group
                    COUNT_DISTINCT: Count unique values in a field
                    SUM: Sum numeric values
                    AVG: Calculate average of numeric values
                    MIN: Find minimum value
                    MAX: Find maximum value
                    FIRST: Get first value in group
                    LAST: Get last value in group
                    PUSH: Collect all values into an array
                    ADD_TO_SET: Collect unique values into an array

                Examples:
                    - Use COUNT for total items per category
                    - Use COUNT_DISTINCT for unique users per day
                    - Use SUM for total revenue
                    - Use AVG for average video duration
            alias (str): Name for the aggregation result in output. REQUIRED for all operations. Should be descriptive of
                the calculation. Used to reference results in post-filtering.
            field (None | str | Unset): The field to aggregate. REQUIRED for all functions except COUNT. NOT REQUIRED for
                COUNT (counts documents). Supports dot notation for nested fields. Field type must be compatible with function.
            distinct_field (None | str | Unset): Field to count distinct values from. REQUIRED when function is
                COUNT_DISTINCT. NOT REQUIRED for other functions. Supports dot notation for nested fields.
    """

    function: AggregationFunction
    alias: str
    field: None | str | Unset = UNSET
    distinct_field: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        function = self.function.value

        alias = self.alias

        field: None | str | Unset
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        distinct_field: None | str | Unset
        if isinstance(self.distinct_field, Unset):
            distinct_field = UNSET
        else:
            distinct_field = self.distinct_field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "function": function,
                "alias": alias,
            }
        )
        if field is not UNSET:
            field_dict["field"] = field
        if distinct_field is not UNSET:
            field_dict["distinct_field"] = distinct_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        function = AggregationFunction(d.pop("function"))

        alias = d.pop("alias")

        def _parse_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field = _parse_field(d.pop("field", UNSET))

        def _parse_distinct_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        distinct_field = _parse_distinct_field(d.pop("distinct_field", UNSET))

        aggregation_operation = cls(
            function=function,
            alias=alias,
            field=field,
            distinct_field=distinct_field,
        )

        aggregation_operation.additional_properties = d
        return aggregation_operation

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
