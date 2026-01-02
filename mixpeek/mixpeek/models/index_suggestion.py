from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexSuggestion")


@_attrs_define
class IndexSuggestion:
    """Suggestion for creating a payload index.

    Attributes:
        field_name (str): Field name to index
        query_count_24h (int): Number of queries using this field in last 24 hours
        suggested_type (str): Suggested index type (keyword, integer, float, etc.)
        is_indexed (bool): Whether field is already indexed
        first_seen (datetime.datetime): First time field was seen in filters
        last_seen (datetime.datetime): Most recent usage
        query_count_7d (int | None | Unset): Number of queries in last 7 days
        estimated_performance_gain (None | str | Unset): Estimated query performance improvement (e.g., '60-80%')
    """

    field_name: str
    query_count_24h: int
    suggested_type: str
    is_indexed: bool
    first_seen: datetime.datetime
    last_seen: datetime.datetime
    query_count_7d: int | None | Unset = UNSET
    estimated_performance_gain: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        query_count_24h = self.query_count_24h

        suggested_type = self.suggested_type

        is_indexed = self.is_indexed

        first_seen = self.first_seen.isoformat()

        last_seen = self.last_seen.isoformat()

        query_count_7d: int | None | Unset
        if isinstance(self.query_count_7d, Unset):
            query_count_7d = UNSET
        else:
            query_count_7d = self.query_count_7d

        estimated_performance_gain: None | str | Unset
        if isinstance(self.estimated_performance_gain, Unset):
            estimated_performance_gain = UNSET
        else:
            estimated_performance_gain = self.estimated_performance_gain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_name": field_name,
                "query_count_24h": query_count_24h,
                "suggested_type": suggested_type,
                "is_indexed": is_indexed,
                "first_seen": first_seen,
                "last_seen": last_seen,
            }
        )
        if query_count_7d is not UNSET:
            field_dict["query_count_7d"] = query_count_7d
        if estimated_performance_gain is not UNSET:
            field_dict["estimated_performance_gain"] = estimated_performance_gain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("field_name")

        query_count_24h = d.pop("query_count_24h")

        suggested_type = d.pop("suggested_type")

        is_indexed = d.pop("is_indexed")

        first_seen = isoparse(d.pop("first_seen"))

        last_seen = isoparse(d.pop("last_seen"))

        def _parse_query_count_7d(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        query_count_7d = _parse_query_count_7d(d.pop("query_count_7d", UNSET))

        def _parse_estimated_performance_gain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_performance_gain = _parse_estimated_performance_gain(d.pop("estimated_performance_gain", UNSET))

        index_suggestion = cls(
            field_name=field_name,
            query_count_24h=query_count_24h,
            suggested_type=suggested_type,
            is_indexed=is_indexed,
            first_seen=first_seen,
            last_seen=last_seen,
            query_count_7d=query_count_7d,
            estimated_performance_gain=estimated_performance_gain,
        )

        index_suggestion.additional_properties = d
        return index_suggestion

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
