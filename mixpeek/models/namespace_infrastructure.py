from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.compute_tier import ComputeTier
from ..types import UNSET, Unset

T = TypeVar("T", bound="NamespaceInfrastructure")


@_attrs_define
class NamespaceInfrastructure:
    """Infrastructure configuration associated with a namespace.

    Defines infrastructure resources for a specific namespace. This configuration
    can override organization-level defaults, enabling flexible deployment patterns
    where different namespaces use different infrastructure.

    Resolution Priority:
        When a namespace has infrastructure configured with DEDICATED tier, it takes
        precedence over organization-level infrastructure. This allows:
        - ENTERPRISE org with SHARED namespace (cost savings for dev/test)
        - ENTERPRISE org with dedicated GPU namespace (ML workloads)
        - Mixed infrastructure within a single organization

    Tier Behaviors:
        SHARED:
            - Namespace uses organization infrastructure (if configured)
            - Falls back to Mixpeek's shared infrastructure
            - All infrastructure URLs should be None
            - Lowest cost, multi-tenant

        DEDICATED_CPU:
            - Namespace uses its own dedicated CPU infrastructure
            - Requires qdrant_url, qdrant_api_key, ray_head_node_url
            - Single-tenant CPU compute
            - Medium cost

        DEDICATED_GPU:
            - Namespace uses its own dedicated GPU infrastructure
            - Requires qdrant_url, qdrant_api_key, ray_head_node_url
            - Requires gpu_type and gpus_per_worker configuration
            - Single-tenant GPU compute
            - Highest cost

    Use Cases:
        - Development namespace: Set compute_tier=SHARED to use organization's infrastructure
        - Production namespace: Inherit organization's DEDICATED infrastructure (don't override)
        - ML namespace: Override with DEDICATED_GPU and GPU configuration
        - Cost optimization: Override ENTERPRISE org to SHARED for dev/test namespaces

    Examples:
        Inherits organization infrastructure (no override):
            NamespaceInfrastructure(
                qdrant_collection="ns_production",
                compute_tier=ComputeTier.SHARED  # Uses org or shared infrastructure
            )

        Override to dedicated CPU:
            NamespaceInfrastructure(
                qdrant_url="http://qdrant-ns-prod:6333",
                qdrant_api_key="qdrant_key_ns_123",
                qdrant_collection="ns_production",
                ray_head_node_url="ray://ray-ns-prod:10001",
                ray_dashboard_url="http://ray-ns-dashboard:8265",
                compute_tier=ComputeTier.DEDICATED_CPU,
                max_concurrent_jobs=50
            )

        Override to dedicated GPU:
            NamespaceInfrastructure(
                qdrant_url="http://qdrant-gpu:6333",
                qdrant_api_key="qdrant_key_gpu",
                qdrant_collection="ns_ml",
                ray_head_node_url="ray://ray-gpu:10001",
                compute_tier=ComputeTier.DEDICATED_GPU,
                gpu_type="A100",
                gpus_per_worker=2
            )

        Attributes:
            qdrant_collection (str): Qdrant collection backing this namespace's vector data.
            ray_cluster_id (None | str | Unset): Dedicated Ray cluster identifier for this namespace.
            ray_head_node_url (None | str | Unset): Ray head node address for job submission (ray://host:port).
            ray_dashboard_url (None | str | Unset): Ray dashboard URL for monitoring (http://host:8265).
            qdrant_url (None | str | Unset): Dedicated Qdrant instance URL for this namespace. When set, this namespace uses
                its own Qdrant instance instead of organization or shared infrastructure. Format: http://hostname:port or
                https://hostname:port. REQUIRED when compute_tier is DEDICATED_CPU or DEDICATED_GPU. NOT REQUIRED for SHARED
                tier (inherits from organization or uses shared).
            qdrant_api_key (None | str | Unset): API key for dedicated Qdrant instance. REQUIRED when qdrant_url is set. NOT
                REQUIRED for shared tier.
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
            max_concurrent_jobs (int | Unset): Maximum concurrent Ray jobs allowed for the namespace. Default: 10.
            autoscaling_enabled (bool | Unset): Toggle autoscaling for dedicated clusters (ignored for shared tier).
                Default: True.
            min_workers (int | Unset): Lower bound for Ray workers when autoscaling is enabled. Default: 1.
            max_workers (int | Unset): Upper bound for Ray workers when autoscaling is enabled. Default: 10.
            gpu_type (None | str | Unset): GPU type for dedicated GPU clusters (e.g. A100, T4).
            gpus_per_worker (int | Unset): Number of GPUs allocated to each Ray worker when using GPUs. Default: 1.
    """

    qdrant_collection: str
    ray_cluster_id: None | str | Unset = UNSET
    ray_head_node_url: None | str | Unset = UNSET
    ray_dashboard_url: None | str | Unset = UNSET
    qdrant_url: None | str | Unset = UNSET
    qdrant_api_key: None | str | Unset = UNSET
    compute_tier: ComputeTier | Unset = UNSET
    max_concurrent_jobs: int | Unset = 10
    autoscaling_enabled: bool | Unset = True
    min_workers: int | Unset = 1
    max_workers: int | Unset = 10
    gpu_type: None | str | Unset = UNSET
    gpus_per_worker: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qdrant_collection = self.qdrant_collection

        ray_cluster_id: None | str | Unset
        if isinstance(self.ray_cluster_id, Unset):
            ray_cluster_id = UNSET
        else:
            ray_cluster_id = self.ray_cluster_id

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

        compute_tier: str | Unset = UNSET
        if not isinstance(self.compute_tier, Unset):
            compute_tier = self.compute_tier.value

        max_concurrent_jobs = self.max_concurrent_jobs

        autoscaling_enabled = self.autoscaling_enabled

        min_workers = self.min_workers

        max_workers = self.max_workers

        gpu_type: None | str | Unset
        if isinstance(self.gpu_type, Unset):
            gpu_type = UNSET
        else:
            gpu_type = self.gpu_type

        gpus_per_worker = self.gpus_per_worker

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "qdrant_collection": qdrant_collection,
            }
        )
        if ray_cluster_id is not UNSET:
            field_dict["ray_cluster_id"] = ray_cluster_id
        if ray_head_node_url is not UNSET:
            field_dict["ray_head_node_url"] = ray_head_node_url
        if ray_dashboard_url is not UNSET:
            field_dict["ray_dashboard_url"] = ray_dashboard_url
        if qdrant_url is not UNSET:
            field_dict["qdrant_url"] = qdrant_url
        if qdrant_api_key is not UNSET:
            field_dict["qdrant_api_key"] = qdrant_api_key
        if compute_tier is not UNSET:
            field_dict["compute_tier"] = compute_tier
        if max_concurrent_jobs is not UNSET:
            field_dict["max_concurrent_jobs"] = max_concurrent_jobs
        if autoscaling_enabled is not UNSET:
            field_dict["autoscaling_enabled"] = autoscaling_enabled
        if min_workers is not UNSET:
            field_dict["min_workers"] = min_workers
        if max_workers is not UNSET:
            field_dict["max_workers"] = max_workers
        if gpu_type is not UNSET:
            field_dict["gpu_type"] = gpu_type
        if gpus_per_worker is not UNSET:
            field_dict["gpus_per_worker"] = gpus_per_worker

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        qdrant_collection = d.pop("qdrant_collection")

        def _parse_ray_cluster_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ray_cluster_id = _parse_ray_cluster_id(d.pop("ray_cluster_id", UNSET))

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

        _compute_tier = d.pop("compute_tier", UNSET)
        compute_tier: ComputeTier | Unset
        if isinstance(_compute_tier, Unset):
            compute_tier = UNSET
        else:
            compute_tier = ComputeTier(_compute_tier)

        max_concurrent_jobs = d.pop("max_concurrent_jobs", UNSET)

        autoscaling_enabled = d.pop("autoscaling_enabled", UNSET)

        min_workers = d.pop("min_workers", UNSET)

        max_workers = d.pop("max_workers", UNSET)

        def _parse_gpu_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gpu_type = _parse_gpu_type(d.pop("gpu_type", UNSET))

        gpus_per_worker = d.pop("gpus_per_worker", UNSET)

        namespace_infrastructure = cls(
            qdrant_collection=qdrant_collection,
            ray_cluster_id=ray_cluster_id,
            ray_head_node_url=ray_head_node_url,
            ray_dashboard_url=ray_dashboard_url,
            qdrant_url=qdrant_url,
            qdrant_api_key=qdrant_api_key,
            compute_tier=compute_tier,
            max_concurrent_jobs=max_concurrent_jobs,
            autoscaling_enabled=autoscaling_enabled,
            min_workers=min_workers,
            max_workers=max_workers,
            gpu_type=gpu_type,
            gpus_per_worker=gpus_per_worker,
        )

        namespace_infrastructure.additional_properties = d
        return namespace_infrastructure

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
