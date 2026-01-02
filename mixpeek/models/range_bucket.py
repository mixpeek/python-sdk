from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RangeBucket")


@_attrs_define
class RangeBucket:
    """Configuration for range-based bucketing.

    Groups numeric values into ranges/buckets for histogram-style analysis.

    Requirements:
        - field: REQUIRED, numeric field to bucket
        - boundaries: REQUIRED, list of boundary values defining buckets
        - default_bucket: OPTIONAL, name for values outside boundaries

    Examples:
        - Video duration buckets: [0, 60, 300, 600] creates: 0-60s, 60-300s, 300-600s, 600+s
        - View count buckets: [0, 100, 1000, 10000] creates: 0-100, 100-1K, 1K-10K, 10K+ views

        Attributes:
            field (str): Numeric field to create buckets for. REQUIRED, must be a numeric field. Supports dot notation for
                nested fields. Values will be grouped into ranges defined by boundaries.
            boundaries (list[float | int]): List of boundary values defining bucket ranges. REQUIRED, must be sorted in
                ascending order. Creates N+1 buckets for N boundaries: [0, 10, 20] creates: <0, 0-10, 10-20, >20. Values on
                boundaries go into the lower bucket.
            default_bucket (None | str | Unset): Name for values outside defined boundaries. OPTIONAL, defaults to 'other'.
                Used for values below min or above max boundary.
    """

    field: str
    boundaries: list[float | int]
    default_bucket: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        boundaries = []
        for boundaries_item_data in self.boundaries:
            boundaries_item: float | int
            boundaries_item = boundaries_item_data
            boundaries.append(boundaries_item)

        default_bucket: None | str | Unset
        if isinstance(self.default_bucket, Unset):
            default_bucket = UNSET
        else:
            default_bucket = self.default_bucket

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "boundaries": boundaries,
            }
        )
        if default_bucket is not UNSET:
            field_dict["default_bucket"] = default_bucket

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        boundaries = []
        _boundaries = d.pop("boundaries")
        for boundaries_item_data in _boundaries:

            def _parse_boundaries_item(data: object) -> float | int:
                return cast(float | int, data)

            boundaries_item = _parse_boundaries_item(boundaries_item_data)

            boundaries.append(boundaries_item)

        def _parse_default_bucket(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_bucket = _parse_default_bucket(d.pop("default_bucket", UNSET))

        range_bucket = cls(
            field=field,
            boundaries=boundaries,
            default_bucket=default_bucket,
        )

        range_bucket.additional_properties = d
        return range_bucket

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
