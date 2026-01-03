# OrganizationInfrastructure

Infrastructure configuration for an organization.  Defines dedicated infrastructure resources for ENTERPRISE tier organizations. When configured, all namespaces in the organization inherit these settings unless explicitly overridden at the namespace level.  Multi-Tenant Architecture:     SHARED (FREE/PRO tiers):         - Uses Mixpeek's shared Qdrant instance (settings.QDRANT_URL)         - Uses Mixpeek's shared Ray cluster (settings.RAY_ADDRESS)         - infrastructure field is None or not configured      DEDICATED (ENTERPRISE tier):         - Uses organization's dedicated Qdrant instance         - Uses organization's dedicated Ray cluster         - infrastructure field is configured with dedicated endpoints  Namespace Override:     Individual namespaces can override organization defaults by configuring     their own infrastructure settings in NamespaceInfrastructure.  Examples:     - FREE/PRO org: infrastructure=None (uses shared)     - ENTERPRISE org: infrastructure configured with dedicated URLs     - ENTERPRISE org namespace override: namespace.infrastructure overrides org.infrastructure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qdrant_url** | **str** | Dedicated Qdrant instance URL for this organization. When set, all requests from this organization route to this Qdrant instance. Format: http://hostname:port or https://hostname:port. REQUIRED for ENTERPRISE tier with dedicated infrastructure. NOT REQUIRED for SHARED tier (uses settings.QDRANT_URL). | [optional] 
**qdrant_api_key** | **str** | API key for dedicated Qdrant instance. REQUIRED when qdrant_url is set. NOT REQUIRED for shared tier. | [optional] 
**ray_head_node_url** | **str** | Dedicated Ray cluster head node URL for job submission. Format: ray://hostname:port. REQUIRED for ENTERPRISE tier with dedicated Ray cluster. NOT REQUIRED for SHARED tier (uses settings.RAY_ADDRESS). | [optional] 
**ray_dashboard_url** | **str** | Ray dashboard URL for monitoring and job submission. Format: http://hostname:port. REQUIRED for ENTERPRISE tier with dedicated Ray cluster. NOT REQUIRED for SHARED tier. | [optional] 
**compute_tier** | [**ComputeTier**](ComputeTier.md) | Default compute tier for all namespaces in this organization. Individual namespaces can override this setting. SHARED: Multi-tenant Mixpeek infrastructure. DEDICATED_CPU: Single-tenant CPU compute. DEDICATED_GPU: Single-tenant GPU compute. | [optional] 

## Example

```python
from mixpeek.models.organization_infrastructure import OrganizationInfrastructure

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationInfrastructure from a JSON string
organization_infrastructure_instance = OrganizationInfrastructure.from_json(json)
# print the JSON string representation of the object
print(OrganizationInfrastructure.to_json())

# convert the object into a dict
organization_infrastructure_dict = organization_infrastructure_instance.to_dict()
# create an instance of OrganizationInfrastructure from a dict
organization_infrastructure_from_dict = OrganizationInfrastructure.from_dict(organization_infrastructure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


