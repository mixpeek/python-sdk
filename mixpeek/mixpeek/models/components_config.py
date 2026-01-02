from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.result_card_properties import ResultCardProperties


T = TypeVar("T", bound="ComponentsConfig")


@_attrs_define
class ComponentsConfig:
    """Configuration for UI components.

    Attributes:
        show_hero (bool | Unset): Whether to show the hero section with title and description Default: True.
        show_search (bool | Unset): Whether to show search input fields Default: True.
        show_filters (bool | Unset): Whether to show filters sidebar Default: False.
        show_results_header (bool | Unset): Whether to show the results header with count and sorting options Default:
            True.
        result_layout (str | Unset): Layout mode for results display Default: 'grid'.
        result_card (None | ResultCardProperties | Unset): Configuration for result card display
    """

    show_hero: bool | Unset = True
    show_search: bool | Unset = True
    show_filters: bool | Unset = False
    show_results_header: bool | Unset = True
    result_layout: str | Unset = "grid"
    result_card: None | ResultCardProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.result_card_properties import ResultCardProperties

        show_hero = self.show_hero

        show_search = self.show_search

        show_filters = self.show_filters

        show_results_header = self.show_results_header

        result_layout = self.result_layout

        result_card: dict[str, Any] | None | Unset
        if isinstance(self.result_card, Unset):
            result_card = UNSET
        elif isinstance(self.result_card, ResultCardProperties):
            result_card = self.result_card.to_dict()
        else:
            result_card = self.result_card

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if show_hero is not UNSET:
            field_dict["show_hero"] = show_hero
        if show_search is not UNSET:
            field_dict["show_search"] = show_search
        if show_filters is not UNSET:
            field_dict["show_filters"] = show_filters
        if show_results_header is not UNSET:
            field_dict["show_results_header"] = show_results_header
        if result_layout is not UNSET:
            field_dict["result_layout"] = result_layout
        if result_card is not UNSET:
            field_dict["result_card"] = result_card

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.result_card_properties import ResultCardProperties

        d = dict(src_dict)
        show_hero = d.pop("show_hero", UNSET)

        show_search = d.pop("show_search", UNSET)

        show_filters = d.pop("show_filters", UNSET)

        show_results_header = d.pop("show_results_header", UNSET)

        result_layout = d.pop("result_layout", UNSET)

        def _parse_result_card(data: object) -> None | ResultCardProperties | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_card_type_0 = ResultCardProperties.from_dict(data)

                return result_card_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResultCardProperties | Unset, data)

        result_card = _parse_result_card(d.pop("result_card", UNSET))

        components_config = cls(
            show_hero=show_hero,
            show_search=show_search,
            show_filters=show_filters,
            show_results_header=show_results_header,
            result_layout=result_layout,
            result_card=result_card,
        )

        components_config.additional_properties = d
        return components_config

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
