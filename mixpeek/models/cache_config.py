from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cache_statistics import CacheStatistics


T = TypeVar("T", bound="CacheConfig")


@_attrs_define
class CacheConfig:
    """Configuration for retriever result caching.

    Controls how retriever results are cached to improve performance
    and reduce redundant compute.

    Caching can be configured at specific stages in the retriever pipeline.
    If no stages are specified, the final results are cached by default.

        Attributes:
            enabled (bool | Unset): Whether caching is enabled for this retriever Default: True.
            ttl_seconds (int | Unset): Time-to-live for cached results in seconds. Default: 1 hour Default: 3600.
            cache_stage_names (list[str] | None | Unset): List of stage names to cache results after. Stage names must match
                the stage_name field in the retriever's stages. If not specified, caches the final results after all stages.
                Examples: ['semantic_search'], ['semantic_search', 'rerank']
            exclude_fields (list[str] | None | Unset): Fields to exclude from caching (e.g., PII fields)
            stats (CacheStatistics | None | Unset): Cache performance statistics
    """

    enabled: bool | Unset = True
    ttl_seconds: int | Unset = 3600
    cache_stage_names: list[str] | None | Unset = UNSET
    exclude_fields: list[str] | None | Unset = UNSET
    stats: CacheStatistics | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cache_statistics import CacheStatistics

        enabled = self.enabled

        ttl_seconds = self.ttl_seconds

        cache_stage_names: list[str] | None | Unset
        if isinstance(self.cache_stage_names, Unset):
            cache_stage_names = UNSET
        elif isinstance(self.cache_stage_names, list):
            cache_stage_names = self.cache_stage_names

        else:
            cache_stage_names = self.cache_stage_names

        exclude_fields: list[str] | None | Unset
        if isinstance(self.exclude_fields, Unset):
            exclude_fields = UNSET
        elif isinstance(self.exclude_fields, list):
            exclude_fields = self.exclude_fields

        else:
            exclude_fields = self.exclude_fields

        stats: dict[str, Any] | None | Unset
        if isinstance(self.stats, Unset):
            stats = UNSET
        elif isinstance(self.stats, CacheStatistics):
            stats = self.stats.to_dict()
        else:
            stats = self.stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if ttl_seconds is not UNSET:
            field_dict["ttl_seconds"] = ttl_seconds
        if cache_stage_names is not UNSET:
            field_dict["cache_stage_names"] = cache_stage_names
        if exclude_fields is not UNSET:
            field_dict["exclude_fields"] = exclude_fields
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cache_statistics import CacheStatistics

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        ttl_seconds = d.pop("ttl_seconds", UNSET)

        def _parse_cache_stage_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cache_stage_names_type_0 = cast(list[str], data)

                return cache_stage_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cache_stage_names = _parse_cache_stage_names(d.pop("cache_stage_names", UNSET))

        def _parse_exclude_fields(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_fields_type_0 = cast(list[str], data)

                return exclude_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclude_fields = _parse_exclude_fields(d.pop("exclude_fields", UNSET))

        def _parse_stats(data: object) -> CacheStatistics | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stats_type_0 = CacheStatistics.from_dict(data)

                return stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CacheStatistics | None | Unset, data)

        stats = _parse_stats(d.pop("stats", UNSET))

        cache_config = cls(
            enabled=enabled,
            ttl_seconds=ttl_seconds,
            cache_stage_names=cache_stage_names,
            exclude_fields=exclude_fields,
            stats=stats,
        )

        cache_config.additional_properties = d
        return cache_config

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
