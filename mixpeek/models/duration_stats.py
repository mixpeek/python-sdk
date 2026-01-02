from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DurationStats")


@_attrs_define
class DurationStats:
    """Statistical distribution of durations for successful step transitions.

    Provides comprehensive percentile analysis to understand timing patterns.

    Attributes:
        mean: Average duration (seconds)
        median: Middle value (50th percentile)
        p50: 50th percentile (same as median, included for consistency)
        p90: 90th percentile (90% complete faster)
        p95: 95th percentile (95% complete faster)
        std_dev: Standard deviation (measure of spread)
        min: Fastest observed duration
        max: Slowest observed duration

    Example:
        ```python
        DurationStats(
            mean=432000.0,     # 5 days average
            median=345600.0,   # 4 days median
            p50=345600.0,
            p90=691200.0,      # 8 days (90th percentile)
            p95=864000.0,      # 10 days (95th percentile)
            std_dev=172800.0,  # 2 days std dev
            min=86400.0,       # 1 day minimum
            max=1209600.0      # 14 days maximum
        )
        ```

        Attributes:
            mean (float): Average duration in seconds
            median (float): Median duration in seconds
            p50 (float): 50th percentile (same as median)
            p90 (float): 90th percentile duration in seconds
            p95 (float): 95th percentile duration in seconds
            std_dev (float): Standard deviation in seconds
            min_ (float): Minimum duration observed in seconds
            max_ (float): Maximum duration observed in seconds
    """

    mean: float
    median: float
    p50: float
    p90: float
    p95: float
    std_dev: float
    min_: float
    max_: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mean = self.mean

        median = self.median

        p50 = self.p50

        p90 = self.p90

        p95 = self.p95

        std_dev = self.std_dev

        min_ = self.min_

        max_ = self.max_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mean": mean,
                "median": median,
                "p50": p50,
                "p90": p90,
                "p95": p95,
                "std_dev": std_dev,
                "min": min_,
                "max": max_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mean = d.pop("mean")

        median = d.pop("median")

        p50 = d.pop("p50")

        p90 = d.pop("p90")

        p95 = d.pop("p95")

        std_dev = d.pop("std_dev")

        min_ = d.pop("min")

        max_ = d.pop("max")

        duration_stats = cls(
            mean=mean,
            median=median,
            p50=p50,
            p90=p90,
            p95=p95,
            std_dev=std_dev,
            min_=min_,
            max_=max_,
        )

        duration_stats.additional_properties = d
        return duration_stats

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
