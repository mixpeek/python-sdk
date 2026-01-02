from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rate_limit_tier import RateLimitTier
from ..types import UNSET, Unset

T = TypeVar("T", bound="RateLimitConfig")


@_attrs_define
class RateLimitConfig:
    """Rate limiting configuration for public retriever API.

    Controls how many requests can be made to the public endpoint
    to prevent abuse and manage infrastructure costs.

    You can either use a preset tier or specify custom limits.
    If both tier and custom limits are provided, custom limits override the tier defaults.

        Attributes:
            enabled (bool | Unset): Enable rate limiting for this published retriever. Set to False to disable all rate
                limiting (not recommended for public retrievers). Default: True.
            tier (RateLimitTier | Unset): Rate limit tier for public retrievers.

                Defines preset rate limit configurations for different use cases.

                Tiers:
                    STANDARD: Default tier for most public retrievers
                        - 10 requests/minute
                        - 100 requests/hour
                        - 1,000 requests/day
                        - Suitable for demos, prototypes, and low-traffic public applications

                    ELEVATED: Higher limits for trusted public applications
                        - 30 requests/minute (3x standard)
                        - 500 requests/hour (5x standard)
                        - 5,000 requests/day (5x standard)
                        - Suitable for production public apps with moderate traffic

                    ENTERPRISE: High limits for enterprise public deployments
                        - 100 requests/minute (10x standard)
                        - 2,000 requests/hour (20x standard)
                        - 20,000 requests/day (20x standard)
                        - Suitable for high-traffic public applications with monitoring

                    UNLIMITED: No rate limiting
                        - Use with extreme caution - only for fully trusted deployments
                        - Still respects max_results_per_query and IP limits if enabled
            requests_per_minute (int | None | Unset): Maximum requests per minute (OPTIONAL). If not specified, uses tier
                default. If specified, overrides tier default.
            requests_per_hour (int | None | Unset): Maximum requests per hour (OPTIONAL). If not specified, uses tier
                default. If specified, overrides tier default.
            requests_per_day (int | None | Unset): Maximum requests per day (OPTIONAL). If not specified, uses tier default.
                If specified, overrides tier default.
            max_results_per_query (int | Unset): Maximum number of results per search query (1-1000) Default: 100.
            enable_ip_limits (bool | Unset): Enable IP-based rate limiting in addition to retriever-level limits. Useful for
                preventing individual IPs from monopolizing the retriever. Default: False.
            max_requests_per_ip_hour (int | None | Unset): Maximum requests per IP address per hour (OPTIONAL). Only
                enforced if enable_ip_limits=True. Recommended: 100-500 for standard tier, 1000+ for elevated/enterprise.
    """

    enabled: bool | Unset = True
    tier: RateLimitTier | Unset = UNSET
    requests_per_minute: int | None | Unset = UNSET
    requests_per_hour: int | None | Unset = UNSET
    requests_per_day: int | None | Unset = UNSET
    max_results_per_query: int | Unset = 100
    enable_ip_limits: bool | Unset = False
    max_requests_per_ip_hour: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        tier: str | Unset = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier.value

        requests_per_minute: int | None | Unset
        if isinstance(self.requests_per_minute, Unset):
            requests_per_minute = UNSET
        else:
            requests_per_minute = self.requests_per_minute

        requests_per_hour: int | None | Unset
        if isinstance(self.requests_per_hour, Unset):
            requests_per_hour = UNSET
        else:
            requests_per_hour = self.requests_per_hour

        requests_per_day: int | None | Unset
        if isinstance(self.requests_per_day, Unset):
            requests_per_day = UNSET
        else:
            requests_per_day = self.requests_per_day

        max_results_per_query = self.max_results_per_query

        enable_ip_limits = self.enable_ip_limits

        max_requests_per_ip_hour: int | None | Unset
        if isinstance(self.max_requests_per_ip_hour, Unset):
            max_requests_per_ip_hour = UNSET
        else:
            max_requests_per_ip_hour = self.max_requests_per_ip_hour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if tier is not UNSET:
            field_dict["tier"] = tier
        if requests_per_minute is not UNSET:
            field_dict["requests_per_minute"] = requests_per_minute
        if requests_per_hour is not UNSET:
            field_dict["requests_per_hour"] = requests_per_hour
        if requests_per_day is not UNSET:
            field_dict["requests_per_day"] = requests_per_day
        if max_results_per_query is not UNSET:
            field_dict["max_results_per_query"] = max_results_per_query
        if enable_ip_limits is not UNSET:
            field_dict["enable_ip_limits"] = enable_ip_limits
        if max_requests_per_ip_hour is not UNSET:
            field_dict["max_requests_per_ip_hour"] = max_requests_per_ip_hour

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _tier = d.pop("tier", UNSET)
        tier: RateLimitTier | Unset
        if isinstance(_tier, Unset):
            tier = UNSET
        else:
            tier = RateLimitTier(_tier)

        def _parse_requests_per_minute(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        requests_per_minute = _parse_requests_per_minute(d.pop("requests_per_minute", UNSET))

        def _parse_requests_per_hour(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        requests_per_hour = _parse_requests_per_hour(d.pop("requests_per_hour", UNSET))

        def _parse_requests_per_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        requests_per_day = _parse_requests_per_day(d.pop("requests_per_day", UNSET))

        max_results_per_query = d.pop("max_results_per_query", UNSET)

        enable_ip_limits = d.pop("enable_ip_limits", UNSET)

        def _parse_max_requests_per_ip_hour(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_requests_per_ip_hour = _parse_max_requests_per_ip_hour(d.pop("max_requests_per_ip_hour", UNSET))

        rate_limit_config = cls(
            enabled=enabled,
            tier=tier,
            requests_per_minute=requests_per_minute,
            requests_per_hour=requests_per_hour,
            requests_per_day=requests_per_day,
            max_results_per_query=max_results_per_query,
            enable_ip_limits=enable_ip_limits,
            max_requests_per_ip_hour=max_requests_per_ip_hour,
        )

        rate_limit_config.additional_properties = d
        return rate_limit_config

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
