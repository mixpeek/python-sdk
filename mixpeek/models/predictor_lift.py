from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PredictorLift")


@_attrs_define
class PredictorLift:
    """Lift calculation for a specific covariate value.

    Lift measures how much a specific value increases/decreases conversion likelihood
    compared to the baseline. Lift > 1.0 means the value helps conversion.

    Attributes:
        field: Name of the covariate (e.g., "Sender Domain", "Word Count Q3")
        value: Specific value or bin (e.g., "gmail.com", "Q3")
        count: Number of sequences with this value
        conversion_rate: Conversion rate for this value (0.0 to 1.0)
        lift: Conversion rate / baseline rate (1.0 = no effect, >1.0 = positive, <1.0 = negative)

    Example:
        ```python
        # Sender domain "enterprise.com" has 2.5x baseline conversion
        PredictorLift(
            field="Sender Domain",
            value="enterprise.com",
            count=150,
            conversion_rate=0.75,  # 75% conversion
            lift=2.5  # 2.5x the baseline rate
        )
        ```

    Interpretation:
        - lift = 1.5: This value increases conversion by 50%
        - lift = 1.0: No effect on conversion
        - lift = 0.5: This value decreases conversion by 50%

        Attributes:
            field (str): Covariate field name
            value (str): Specific value or bin label
            count (int): Number of sequences with this value
            conversion_rate (float): Conversion rate for this value
            lift (float): Lift relative to baseline (>1.0 = positive, <1.0 = negative)
    """

    field: str
    value: str
    count: int
    conversion_rate: float
    lift: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        value = self.value

        count = self.count

        conversion_rate = self.conversion_rate

        lift = self.lift

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "value": value,
                "count": count,
                "conversion_rate": conversion_rate,
                "lift": lift,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        value = d.pop("value")

        count = d.pop("count")

        conversion_rate = d.pop("conversion_rate")

        lift = d.pop("lift")

        predictor_lift = cls(
            field=field,
            value=value,
            count=count,
            conversion_rate=conversion_rate,
            lift=lift,
        )

        predictor_lift.additional_properties = d
        return predictor_lift

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
