# NamespaceInfrastructure

Infrastructure configuration associated with a namespace.  Defines infrastructure resources for a specific namespace. This configuration can override organization-level defaults, enabling flexible deployment patterns where different namespaces use different infrastructure.  Resolution Priority:     When a namespace has infrastructure configured with DEDICATED tier, it takes     precedence over organization-level infrastructure. This allows:     - ENTERPRISE org with SHARED namespace (cost savings for dev/test)     - ENTERPRISE org with dedicated GPU namespace (ML workloads)     - Mixed infrastructure within a single organization  Tier Behaviors:     SHARED:         - Namespace uses organization infrastructure (if configured)         - Falls back to Mixpeek's shared infrastructure         - All infrastructure URLs should be None         - Lowest cost, multi-tenant      DEDICATED_CPU:         - Namespace uses its own dedicated CPU infrastructure         - Requires qdrant_url, qdrant_api_key, ray_head_node_url         - Single-tenant CPU compute         - Medium cost      DEDICATED_GPU:         - Namespace uses its own dedicated GPU infrastructure         - Requires qdrant_url, qdrant_api_key, ray_head_node_url         - Requires gpu_type and gpus_per_worker configuration         - Single-tenant GPU compute         - Highest cost  Use Cases:     - Development namespace: Set compute_tier=SHARED to use organization's infrastructure     - Production namespace: Inherit organization's DEDICATED infrastructure (don't override)     - ML namespace: Override with DEDICATED_GPU and GPU configuration     - Cost optimization: Override ENTERPRISE org to SHARED for dev/test namespaces  Examples:     Inherits organization infrastructure (no override):         NamespaceInfrastructure(             qdrant_collection=\"ns_production\",             compute_tier=ComputeTier.SHARED  # Uses org or shared infrastructure         )      Override to dedicated CPU:         NamespaceInfrastructure(             qdrant_url=\"http://qdrant-ns-prod:6333\",             qdrant_api_key=\"qdrant_key_ns_123\",             qdrant_collection=\"ns_production\",             ray_head_node_url=\"ray://ray-ns-prod:10001\",             ray_dashboard_url=\"http://ray-ns-dashboard:8265\",             compute_tier=ComputeTier.DEDICATED_CPU,             max_concurrent_jobs=50         )      Override to dedicated GPU:         NamespaceInfrastructure(             qdrant_url=\"http://qdrant-gpu:6333\",             qdrant_api_key=\"qdrant_key_gpu\",             qdrant_collection=\"ns_ml\",             ray_head_node_url=\"ray://ray-gpu:10001\",             compute_tier=ComputeTier.DEDICATED_GPU,             gpu_type=\"A100\",             gpus_per_worker=2         )

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ray_cluster_id** | **str** | Dedicated Ray cluster identifier for this namespace. | [optional] 
**ray_head_node_url** | **str** | Ray head node address for job submission (ray://host:port). | [optional] 
**ray_dashboard_url** | **str** | Ray dashboard URL for monitoring (http://host:8265). | [optional] 
**qdrant_url** | **str** | Dedicated Qdrant instance URL for this namespace. When set, this namespace uses its own Qdrant instance instead of organization or shared infrastructure. Format: http://hostname:port or https://hostname:port. REQUIRED when compute_tier is DEDICATED_CPU or DEDICATED_GPU. NOT REQUIRED for SHARED tier (inherits from organization or uses shared). | [optional] 
**qdrant_api_key** | **str** | API key for dedicated Qdrant instance. REQUIRED when qdrant_url is set. NOT REQUIRED for shared tier. | [optional] 
**qdrant_collection** | **str** | Qdrant collection backing this namespace&#39;s vector data. | 
**compute_tier** | [**ComputeTier**](ComputeTier.md) | Compute tier controlling isolation and performance characteristics. | [optional] 
**max_concurrent_jobs** | **int** | Maximum concurrent Ray jobs allowed for the namespace. | [optional] [default to 10]
**autoscaling_enabled** | **bool** | Toggle autoscaling for dedicated clusters (ignored for shared tier). | [optional] [default to True]
**min_workers** | **int** | Lower bound for Ray workers when autoscaling is enabled. | [optional] [default to 1]
**max_workers** | **int** | Upper bound for Ray workers when autoscaling is enabled. | [optional] [default to 10]
**gpu_type** | **str** | GPU type for dedicated GPU clusters (e.g. A100, T4). | [optional] 
**gpus_per_worker** | **int** | Number of GPUs allocated to each Ray worker when using GPUs. | [optional] [default to 1]

## Example

```python
from mixpeek.models.namespace_infrastructure import NamespaceInfrastructure

# TODO update the JSON string below
json = "{}"
# create an instance of NamespaceInfrastructure from a JSON string
namespace_infrastructure_instance = NamespaceInfrastructure.from_json(json)
# print the JSON string representation of the object
print(NamespaceInfrastructure.to_json())

# convert the object into a dict
namespace_infrastructure_dict = namespace_infrastructure_instance.to_dict()
# create an instance of NamespaceInfrastructure from a dict
namespace_infrastructure_from_dict = NamespaceInfrastructure.from_dict(namespace_infrastructure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


