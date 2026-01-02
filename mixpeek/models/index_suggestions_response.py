from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.index_suggestion import IndexSuggestion


T = TypeVar("T", bound="IndexSuggestionsResponse")


@_attrs_define
class IndexSuggestionsResponse:
    """Response containing index suggestions for a namespace.

    Attributes:
        namespace_id (str): Namespace being analyzed
        analysis_period (str): Time period analyzed (e.g., '24h', '7d')
        suggestions (list[IndexSuggestion]): List of index suggestions
        auto_create_enabled (bool): Whether auto-indexing is enabled for this namespace
        next_auto_create_run (datetime.datetime | None | Unset): Next scheduled auto-creation run (if enabled)
    """

    namespace_id: str
    analysis_period: str
    suggestions: list[IndexSuggestion]
    auto_create_enabled: bool
    next_auto_create_run: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace_id = self.namespace_id

        analysis_period = self.analysis_period

        suggestions = []
        for suggestions_item_data in self.suggestions:
            suggestions_item = suggestions_item_data.to_dict()
            suggestions.append(suggestions_item)

        auto_create_enabled = self.auto_create_enabled

        next_auto_create_run: None | str | Unset
        if isinstance(self.next_auto_create_run, Unset):
            next_auto_create_run = UNSET
        elif isinstance(self.next_auto_create_run, datetime.datetime):
            next_auto_create_run = self.next_auto_create_run.isoformat()
        else:
            next_auto_create_run = self.next_auto_create_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace_id": namespace_id,
                "analysis_period": analysis_period,
                "suggestions": suggestions,
                "auto_create_enabled": auto_create_enabled,
            }
        )
        if next_auto_create_run is not UNSET:
            field_dict["next_auto_create_run"] = next_auto_create_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.index_suggestion import IndexSuggestion

        d = dict(src_dict)
        namespace_id = d.pop("namespace_id")

        analysis_period = d.pop("analysis_period")

        suggestions = []
        _suggestions = d.pop("suggestions")
        for suggestions_item_data in _suggestions:
            suggestions_item = IndexSuggestion.from_dict(suggestions_item_data)

            suggestions.append(suggestions_item)

        auto_create_enabled = d.pop("auto_create_enabled")

        def _parse_next_auto_create_run(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_auto_create_run_type_0 = isoparse(data)

                return next_auto_create_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_auto_create_run = _parse_next_auto_create_run(d.pop("next_auto_create_run", UNSET))

        index_suggestions_response = cls(
            namespace_id=namespace_id,
            analysis_period=analysis_period,
            suggestions=suggestions,
            auto_create_enabled=auto_create_enabled,
            next_auto_create_run=next_auto_create_run,
        )

        index_suggestions_response.additional_properties = d
        return index_suggestions_response

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
