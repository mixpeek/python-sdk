from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duration_stats import DurationStats
    from ..models.predictor_lift import PredictorLift
    from ..models.step_transition_response_metadata import StepTransitionResponseMetadata


T = TypeVar("T", bound="StepTransitionResponse")


@_attrs_define
class StepTransitionResponse:
    """API response model for step transition analytics.

    Contains comprehensive statistics about the A→B transition including
    conversion metrics, duration analysis, and predictor insights.

    Example Response:
        ```json
        {
            "from_step": "inquiry",
            "to_step": "closed_won",
            "count": 1000,
            "converted": 350,
            "conversion_rate": 0.35,
            "durations_sec": {
                "mean": 432000.0,
                "median": 345600.0,
                "p50": 345600.0,
                "p90": 691200.0,
                "p95": 864000.0,
                "std_dev": 172800.0,
                "min": 86400.0,
                "max": 1209600.0
            },
            "top_predictors": [
                {
                    "field": "Sender Domain",
                    "value": "enterprise.com",
                    "count": 150,
                    "conversion_rate": 0.75,
                    "lift": 2.14
                }
            ],
            "metadata": {
                "collection_id": "col_emails",
                "taxonomy_id": "tax_sales_stages",
                "total_events_analyzed": 5432
            }
        }
        ```

        Attributes:
            from_step (str): Starting step
            to_step (str): Ending step
            count (int): Total number of sequences starting at from_step
            converted (int): Number of sequences that reached to_step
            conversion_rate (float): Percentage that converted (converted / count)
            durations_sec (DurationStats | None | Unset): Duration statistics (None if no conversions)
            top_predictors (list[PredictorLift] | Unset): Covariates with highest lift (sorted by absolute lift)
            metadata (StepTransitionResponseMetadata | Unset): Additional metadata (collection_id, event counts, etc.)
    """

    from_step: str
    to_step: str
    count: int
    converted: int
    conversion_rate: float
    durations_sec: DurationStats | None | Unset = UNSET
    top_predictors: list[PredictorLift] | Unset = UNSET
    metadata: StepTransitionResponseMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.duration_stats import DurationStats

        from_step = self.from_step

        to_step = self.to_step

        count = self.count

        converted = self.converted

        conversion_rate = self.conversion_rate

        durations_sec: dict[str, Any] | None | Unset
        if isinstance(self.durations_sec, Unset):
            durations_sec = UNSET
        elif isinstance(self.durations_sec, DurationStats):
            durations_sec = self.durations_sec.to_dict()
        else:
            durations_sec = self.durations_sec

        top_predictors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_predictors, Unset):
            top_predictors = []
            for top_predictors_item_data in self.top_predictors:
                top_predictors_item = top_predictors_item_data.to_dict()
                top_predictors.append(top_predictors_item)

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_step": from_step,
                "to_step": to_step,
                "count": count,
                "converted": converted,
                "conversion_rate": conversion_rate,
            }
        )
        if durations_sec is not UNSET:
            field_dict["durations_sec"] = durations_sec
        if top_predictors is not UNSET:
            field_dict["top_predictors"] = top_predictors
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.duration_stats import DurationStats
        from ..models.predictor_lift import PredictorLift
        from ..models.step_transition_response_metadata import StepTransitionResponseMetadata

        d = dict(src_dict)
        from_step = d.pop("from_step")

        to_step = d.pop("to_step")

        count = d.pop("count")

        converted = d.pop("converted")

        conversion_rate = d.pop("conversion_rate")

        def _parse_durations_sec(data: object) -> DurationStats | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                durations_sec_type_0 = DurationStats.from_dict(data)

                return durations_sec_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DurationStats | None | Unset, data)

        durations_sec = _parse_durations_sec(d.pop("durations_sec", UNSET))

        _top_predictors = d.pop("top_predictors", UNSET)
        top_predictors: list[PredictorLift] | Unset = UNSET
        if _top_predictors is not UNSET:
            top_predictors = []
            for top_predictors_item_data in _top_predictors:
                top_predictors_item = PredictorLift.from_dict(top_predictors_item_data)

                top_predictors.append(top_predictors_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: StepTransitionResponseMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = StepTransitionResponseMetadata.from_dict(_metadata)

        step_transition_response = cls(
            from_step=from_step,
            to_step=to_step,
            count=count,
            converted=converted,
            conversion_rate=conversion_rate,
            durations_sec=durations_sec,
            top_predictors=top_predictors,
            metadata=metadata,
        )

        step_transition_response.additional_properties = d
        return step_transition_response

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
