from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.join_response_results_type_0_item import JoinResponseResultsType0Item
    from ..models.join_stats import JoinStats


T = TypeVar("T", bound="JoinResponse")


@_attrs_define
class JoinResponse:
    """
    Attributes:
        stats (JoinStats):
        results (list[JoinResponseResultsType0Item] | None | Unset):
    """

    stats: JoinStats
    results: list[JoinResponseResultsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stats = self.stats.to_dict()

        results: list[dict[str, Any]] | None | Unset
        if isinstance(self.results, Unset):
            results = UNSET
        elif isinstance(self.results, list):
            results = []
            for results_type_0_item_data in self.results:
                results_type_0_item = results_type_0_item_data.to_dict()
                results.append(results_type_0_item)

        else:
            results = self.results

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stats": stats,
            }
        )
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.join_response_results_type_0_item import JoinResponseResultsType0Item
        from ..models.join_stats import JoinStats

        d = dict(src_dict)
        stats = JoinStats.from_dict(d.pop("stats"))

        def _parse_results(data: object) -> list[JoinResponseResultsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                results_type_0 = []
                _results_type_0 = data
                for results_type_0_item_data in _results_type_0:
                    results_type_0_item = JoinResponseResultsType0Item.from_dict(results_type_0_item_data)

                    results_type_0.append(results_type_0_item)

                return results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JoinResponseResultsType0Item] | None | Unset, data)

        results = _parse_results(d.pop("results", UNSET))

        join_response = cls(
            stats=stats,
            results=results,
        )

        join_response.additional_properties = d
        return join_response

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
