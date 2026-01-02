from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compute_tier import ComputeTier
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationInfrastructure")


@_attrs_define
class OrganizationInfrastructure:
    """Infrastructure configuration for an organization.

    Defines dedicated infrastructure resources for ENTERPRISE tier organizations.
    When configured, all namespaces in the organization inherit these settings
    unless explicitly overridden at the namespace level.

    Multi-Tenant Architecture:
        SHARED (FREE/PRO tiers):
            - Uses Mixpeek's shared Qdrant instance (settings.QDRANT_URL)
            - Uses Mixpeek's shared Ray cluster (settings.RAY_ADDRESS)
            - infrastructure field is None or not configured

        DEDICATED (ENTERPRISE tier):
            - Uses organization's dedicated Qdrant instance
            - Uses organization's dedicated Ray cluster
            - infrastructure field is configured with dedicated endpoints

    Namespace Override:
        Individual namespaces can override organization defaults by configuring
        their own infrastructure settings in NamespaceInfrastructure.

    Examples:
        - FREE/PRO org: infrastructure=None (uses shared)
        - ENTERPRISE org: infrastructure configured with dedicated URLs
        - ENTERPRISE org namespace override: namespace.infrastructure overrides org.infrastructure

        Attributes:
            qdrant_url (None | str | Unset): Dedicated Qdrant instance URL for this organization. When set, all requests
                from this organization route to this Qdrant instance. Format: http://hostname:port or https://hostname:port.
                REQUIRED for ENTERPRISE tier with dedicated infrastructure. NOT REQUIRED for SHARED tier (uses
                settings.QDRANT_URL).
            qdrant_api_key (None | str | Unset): API key for dedicated Qdrant instance. REQUIRED when qdrant_url is set. NOT
                REQUIRED for shared tier.
            ray_head_node_url (None | str | Unset): Dedicated Ray cluster head node URL for job submission. Format:
                ray://hostname:port. REQUIRED for ENTERPRISE tier with dedicated Ray cluster. NOT REQUIRED for SHARED tier (uses
                settings.RAY_ADDRESS).
            ray_dashboard_url (None | str | Unset): Ray dashboard URL for monitoring and job submission. Format:
                http://hostname:port. REQUIRED for ENTERPRISE tier with dedicated Ray cluster. NOT REQUIRED for SHARED tier.
            compute_tier (ComputeTier | Unset): Available compute tiers for namespace workloads.

                Compute tiers determine the infrastructure resources allocated to a namespace
                for ingestion pipelines, clustering, and other data processing operations.

                Tiers:
                    SHARED: Multi-tenant infrastructure with dynamic resource allocation.
                        - Best for: Development, testing, low-volume production workloads
                        - Resources: Shared CPU and memory pool
                        - Cost: Lowest cost option, pay-per-use credits
                        - SLA: Best-effort availability

                    DEDICATED_CPU: Single-tenant CPU compute nodes.
                        - Best for: Production workloads requiring consistent performance
                        - Resources: Reserved CPU cores and memory
                        - Cost: Fixed monthly cost plus usage credits
                        - SLA: 99.9% uptime guarantee

                    DEDICATED_GPU: Single-tenant GPU-accelerated compute nodes.
                        - Best for: Video processing, embedding generation, ML inference
                        - Resources: Reserved GPU(s), CPU cores, and memory
                        - Cost: Premium pricing, fixed monthly cost plus usage credits
                        - SLA: 99.9% uptime guarantee

                Examples:
                    - Use SHARED for development and staging environments
                    - Use DEDICATED_CPU for production document processing pipelines
                    - Use DEDICATED_GPU for large-scale video ingestion and analysis
    """

    qdrant_url: None | str | Unset = UNSET
    qdrant_api_key: None | str | Unset = UNSET
    ray_head_node_url: None | str | Unset = UNSET
    ray_dashboard_url: None | str | Unset = UNSET
    compute_tier: ComputeTier | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qdrant_url: None | str | Unset
        if isinstance(self.qdrant_url, Unset):
            qdrant_url = UNSET
        else:
            qdrant_url = self.qdrant_url

        qdrant_api_key: None | str | Unset
        if isinstance(self.qdrant_api_key, Unset):
            qdrant_api_key = UNSET
        else:
            qdrant_api_key = self.qdrant_api_key

        ray_head_node_url: None | str | Unset
        if isinstance(self.ray_head_node_url, Unset):
            ray_head_node_url = UNSET
        else:
            ray_head_node_url = self.ray_head_node_url

        ray_dashboard_url: None | str | Unset
        if isinstance(self.ray_dashboard_url, Unset):
            ray_dashboard_url = UNSET
        else:
            ray_dashboard_url = self.ray_dashboard_url

        compute_tier: str | Unset = UNSET
        if not isinstance(self.compute_tier, Unset):
            compute_tier = self.compute_tier.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qdrant_url is not UNSET:
            field_dict["qdrant_url"] = qdrant_url
        if qdrant_api_key is not UNSET:
            field_dict["qdrant_api_key"] = qdrant_api_key
        if ray_head_node_url is not UNSET:
            field_dict["ray_head_node_url"] = ray_head_node_url
        if ray_dashboard_url is not UNSET:
            field_dict["ray_dashboard_url"] = ray_dashboard_url
        if compute_tier is not UNSET:
            field_dict["compute_tier"] = compute_tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_qdrant_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qdrant_url = _parse_qdrant_url(d.pop("qdrant_url", UNSET))

        def _parse_qdrant_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qdrant_api_key = _parse_qdrant_api_key(d.pop("qdrant_api_key", UNSET))

        def _parse_ray_head_node_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ray_head_node_url = _parse_ray_head_node_url(d.pop("ray_head_node_url", UNSET))

        def _parse_ray_dashboard_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ray_dashboard_url = _parse_ray_dashboard_url(d.pop("ray_dashboard_url", UNSET))

        _compute_tier = d.pop("compute_tier", UNSET)
        compute_tier: ComputeTier | Unset
        if isinstance(_compute_tier, Unset):
            compute_tier = UNSET
        else:
            compute_tier = ComputeTier(_compute_tier)

        organization_infrastructure = cls(
            qdrant_url=qdrant_url,
            qdrant_api_key=qdrant_api_key,
            ray_head_node_url=ray_head_node_url,
            ray_dashboard_url=ray_dashboard_url,
            compute_tier=compute_tier,
        )

        organization_infrastructure.additional_properties = d
        return organization_infrastructure

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
