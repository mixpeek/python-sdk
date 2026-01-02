from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.path_analysis_request_filters_type_0 import PathAnalysisRequestFiltersType0


T = TypeVar("T", bound="PathAnalysisRequest")


@_attrs_define
class PathAnalysisRequest:
    """API request model for multi-step path analysis.

    Discovers the most common sequences of intermediate steps documents take
    when progressing from from_step to to_step.

    Unlike the transitions endpoint which only analyzes direct A→B progressions,
    this endpoint reveals the actual paths taken (e.g., A → X → Y → B).

    Example:
        ```json
        {
            "collection_id": "col_emails",
            "taxonomy_id": "tax_sales_stages",
            "from_step": "inquiry",
            "to_step": "closed_won",
            "max_path_length": 10,
            "min_support": 5
        }
        ```

    Response includes:
        - Most common paths sorted by frequency
        - Count and percentage for each path
        - Average duration per path

        Attributes:
            collection_id (str): Collection to analyze
            taxonomy_id (str): Taxonomy ID
            from_step (str): Starting step
            to_step (str): Ending step
            max_path_length (int | Unset): Maximum number of steps in a path Default: 10.
            min_support (int | Unset): Minimum sequences required to include a path Default: 5.
            max_window_days (int | None | Unset): Maximum duration for path completion (in days)
            filters (None | PathAnalysisRequestFiltersType0 | Unset): Optional event filters
    """

    collection_id: str
    taxonomy_id: str
    from_step: str
    to_step: str
    max_path_length: int | Unset = 10
    min_support: int | Unset = 5
    max_window_days: int | None | Unset = UNSET
    filters: None | PathAnalysisRequestFiltersType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.path_analysis_request_filters_type_0 import PathAnalysisRequestFiltersType0

        collection_id = self.collection_id

        taxonomy_id = self.taxonomy_id

        from_step = self.from_step

        to_step = self.to_step

        max_path_length = self.max_path_length

        min_support = self.min_support

        max_window_days: int | None | Unset
        if isinstance(self.max_window_days, Unset):
            max_window_days = UNSET
        else:
            max_window_days = self.max_window_days

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, PathAnalysisRequestFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

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
        if max_path_length is not UNSET:
            field_dict["max_path_length"] = max_path_length
        if min_support is not UNSET:
            field_dict["min_support"] = min_support
        if max_window_days is not UNSET:
            field_dict["max_window_days"] = max_window_days
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.path_analysis_request_filters_type_0 import PathAnalysisRequestFiltersType0

        d = dict(src_dict)
        collection_id = d.pop("collection_id")

        taxonomy_id = d.pop("taxonomy_id")

        from_step = d.pop("from_step")

        to_step = d.pop("to_step")

        max_path_length = d.pop("max_path_length", UNSET)

        min_support = d.pop("min_support", UNSET)

        def _parse_max_window_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_window_days = _parse_max_window_days(d.pop("max_window_days", UNSET))

        def _parse_filters(data: object) -> None | PathAnalysisRequestFiltersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = PathAnalysisRequestFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PathAnalysisRequestFiltersType0 | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        path_analysis_request = cls(
            collection_id=collection_id,
            taxonomy_id=taxonomy_id,
            from_step=from_step,
            to_step=to_step,
            max_path_length=max_path_length,
            min_support=min_support,
            max_window_days=max_window_days,
            filters=filters,
        )

        path_analysis_request.additional_properties = d
        return path_analysis_request

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
