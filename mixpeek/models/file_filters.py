from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileFilters")


@_attrs_define
class FileFilters:
    """Filter rules controlling which files are synced from storage providers.

    All filters are optional and combined with AND logic.
    Files must pass ALL specified filters to be synced.

    **Pattern Matching:** Uses glob patterns (*, ?, [abc], etc.)
    **Size Filtering:** Bytes-based, inclusive bounds
    **Time Filtering:** ISO 8601 datetime, based on provider's modified timestamp

        Attributes:
            include_patterns (list[str] | None | Unset): Glob patterns to include (e.g. ['*.mp4', '*.mov']).
            exclude_patterns (list[str] | None | Unset): Glob patterns to exclude (e.g. ['*/drafts/*', '*_temp.*']).
            min_size_bytes (int | None | Unset): Minimum file size (bytes). Files smaller are skipped.
            max_size_bytes (int | None | Unset): Maximum file size (bytes). Files larger are skipped.
            modified_after (datetime.datetime | None | Unset): Only sync files modified after this timestamp.
            modified_before (datetime.datetime | None | Unset): Only sync files modified before this timestamp.
            mime_types (list[str] | None | Unset): Optional list of MIME types to include.
    """

    include_patterns: list[str] | None | Unset = UNSET
    exclude_patterns: list[str] | None | Unset = UNSET
    min_size_bytes: int | None | Unset = UNSET
    max_size_bytes: int | None | Unset = UNSET
    modified_after: datetime.datetime | None | Unset = UNSET
    modified_before: datetime.datetime | None | Unset = UNSET
    mime_types: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_patterns: list[str] | None | Unset
        if isinstance(self.include_patterns, Unset):
            include_patterns = UNSET
        elif isinstance(self.include_patterns, list):
            include_patterns = self.include_patterns

        else:
            include_patterns = self.include_patterns

        exclude_patterns: list[str] | None | Unset
        if isinstance(self.exclude_patterns, Unset):
            exclude_patterns = UNSET
        elif isinstance(self.exclude_patterns, list):
            exclude_patterns = self.exclude_patterns

        else:
            exclude_patterns = self.exclude_patterns

        min_size_bytes: int | None | Unset
        if isinstance(self.min_size_bytes, Unset):
            min_size_bytes = UNSET
        else:
            min_size_bytes = self.min_size_bytes

        max_size_bytes: int | None | Unset
        if isinstance(self.max_size_bytes, Unset):
            max_size_bytes = UNSET
        else:
            max_size_bytes = self.max_size_bytes

        modified_after: None | str | Unset
        if isinstance(self.modified_after, Unset):
            modified_after = UNSET
        elif isinstance(self.modified_after, datetime.datetime):
            modified_after = self.modified_after.isoformat()
        else:
            modified_after = self.modified_after

        modified_before: None | str | Unset
        if isinstance(self.modified_before, Unset):
            modified_before = UNSET
        elif isinstance(self.modified_before, datetime.datetime):
            modified_before = self.modified_before.isoformat()
        else:
            modified_before = self.modified_before

        mime_types: list[str] | None | Unset
        if isinstance(self.mime_types, Unset):
            mime_types = UNSET
        elif isinstance(self.mime_types, list):
            mime_types = self.mime_types

        else:
            mime_types = self.mime_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_patterns is not UNSET:
            field_dict["include_patterns"] = include_patterns
        if exclude_patterns is not UNSET:
            field_dict["exclude_patterns"] = exclude_patterns
        if min_size_bytes is not UNSET:
            field_dict["min_size_bytes"] = min_size_bytes
        if max_size_bytes is not UNSET:
            field_dict["max_size_bytes"] = max_size_bytes
        if modified_after is not UNSET:
            field_dict["modified_after"] = modified_after
        if modified_before is not UNSET:
            field_dict["modified_before"] = modified_before
        if mime_types is not UNSET:
            field_dict["mime_types"] = mime_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_include_patterns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                include_patterns_type_0 = cast(list[str], data)

                return include_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        include_patterns = _parse_include_patterns(d.pop("include_patterns", UNSET))

        def _parse_exclude_patterns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_patterns_type_0 = cast(list[str], data)

                return exclude_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclude_patterns = _parse_exclude_patterns(d.pop("exclude_patterns", UNSET))

        def _parse_min_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_size_bytes = _parse_min_size_bytes(d.pop("min_size_bytes", UNSET))

        def _parse_max_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_size_bytes = _parse_max_size_bytes(d.pop("max_size_bytes", UNSET))

        def _parse_modified_after(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_after_type_0 = isoparse(data)

                return modified_after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        modified_after = _parse_modified_after(d.pop("modified_after", UNSET))

        def _parse_modified_before(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_before_type_0 = isoparse(data)

                return modified_before_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        modified_before = _parse_modified_before(d.pop("modified_before", UNSET))

        def _parse_mime_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mime_types_type_0 = cast(list[str], data)

                return mime_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        mime_types = _parse_mime_types(d.pop("mime_types", UNSET))

        file_filters = cls(
            include_patterns=include_patterns,
            exclude_patterns=exclude_patterns,
            min_size_bytes=min_size_bytes,
            max_size_bytes=max_size_bytes,
            modified_after=modified_after,
            modified_before=modified_before,
            mime_types=mime_types,
        )

        file_filters.additional_properties = d
        return file_filters

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
