from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.step_analytics_config import StepAnalyticsConfig
    from ..models.step_transition_request_filters_type_0 import StepTransitionRequestFiltersType0


T = TypeVar("T", bound="StepTransitionRequest")


@_attrs_define
class StepTransitionRequest:
    """API request model for step transition analytics.

    This model extends the engine query model with API-specific validation
    and documentation.

    Use this to analyze how documents transition from one taxonomy step to another,
    computing conversion rates, durations, and predictor lifts.

    Example:
        ```json
        {
            "collection_id": "col_emails",
            "taxonomy_id": "tax_sales_stages",
            "from_step": "inquiry",
            "to_step": "closed_won",
            "max_window_days": 90,
            "min_support": 10
        }
        ```

    Response includes:
        - Conversion rate (% reaching to_step)
        - Duration statistics (mean, median, p90, p95)
        - Top predictors (covariates with highest lift)

        Attributes:
            collection_id (str): Collection to analyze for step transitions
            taxonomy_id (str): Taxonomy ID (each taxonomy_id is immutable, clone creates new ID)
            from_step (str): Starting step label (e.g., 'inquiry', 'draft')
            to_step (str): Ending step label (e.g., 'closed_won', 'published')
            max_window_days (int | None | Unset): Maximum days between from_step and to_step. Sequences exceeding this are
                excluded.
            filters (None | StepTransitionRequestFiltersType0 | Unset): Optional filters for events (e.g.,
                {'metadata.region': 'US'})
            override_step_analytics (None | StepAnalyticsConfig | Unset): Override taxonomy's default step_analytics config
                for this query
            min_support (int | Unset): Minimum number of sequences required for valid analysis Default: 10.
    """

    collection_id: str
    taxonomy_id: str
    from_step: str
    to_step: str
    max_window_days: int | None | Unset = UNSET
    filters: None | StepTransitionRequestFiltersType0 | Unset = UNSET
    override_step_analytics: None | StepAnalyticsConfig | Unset = UNSET
    min_support: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.step_analytics_config import StepAnalyticsConfig
        from ..models.step_transition_request_filters_type_0 import StepTransitionRequestFiltersType0

        collection_id = self.collection_id

        taxonomy_id = self.taxonomy_id

        from_step = self.from_step

        to_step = self.to_step

        max_window_days: int | None | Unset
        if isinstance(self.max_window_days, Unset):
            max_window_days = UNSET
        else:
            max_window_days = self.max_window_days

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, StepTransitionRequestFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        override_step_analytics: dict[str, Any] | None | Unset
        if isinstance(self.override_step_analytics, Unset):
            override_step_analytics = UNSET
        elif isinstance(self.override_step_analytics, StepAnalyticsConfig):
            override_step_analytics = self.override_step_analytics.to_dict()
        else:
            override_step_analytics = self.override_step_analytics

        min_support = self.min_support

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_id": collection_id,
                "taxonomy_id": taxonomy_id,
                "from_step": from_step,
                "to_step": to_step,
            }
        )
        if max_window_days is not UNSET:
            field_dict["max_window_days"] = max_window_days
        if filters is not UNSET:
            field_dict["filters"] = filters
        if override_step_analytics is not UNSET:
            field_dict["override_step_analytics"] = override_step_analytics
        if min_support is not UNSET:
            field_dict["min_support"] = min_support

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_analytics_config import StepAnalyticsConfig
        from ..models.step_transition_request_filters_type_0 import StepTransitionRequestFiltersType0

        d = dict(src_dict)
        collection_id = d.pop("collection_id")

        taxonomy_id = d.pop("taxonomy_id")

        from_step = d.pop("from_step")

        to_step = d.pop("to_step")

        def _parse_max_window_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_window_days = _parse_max_window_days(d.pop("max_window_days", UNSET))

        def _parse_filters(data: object) -> None | StepTransitionRequestFiltersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = StepTransitionRequestFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StepTransitionRequestFiltersType0 | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_override_step_analytics(data: object) -> None | StepAnalyticsConfig | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                override_step_analytics_type_0 = StepAnalyticsConfig.from_dict(data)

                return override_step_analytics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StepAnalyticsConfig | Unset, data)

        override_step_analytics = _parse_override_step_analytics(d.pop("override_step_analytics", UNSET))

        min_support = d.pop("min_support", UNSET)

        step_transition_request = cls(
            collection_id=collection_id,
            taxonomy_id=taxonomy_id,
            from_step=from_step,
            to_step=to_step,
            max_window_days=max_window_days,
            filters=filters,
            override_step_analytics=override_step_analytics,
            min_support=min_support,
        )

        step_transition_request.additional_properties = d
        return step_transition_request

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
