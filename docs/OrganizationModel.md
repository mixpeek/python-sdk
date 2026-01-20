# OrganizationModel

Organization document representing a tenant in the multi-tenant system.  Multi-Tenancy Architecture:     Organizations are the root tenant in Mixpeek's multi-tenant architecture.     Each organization has dual identifiers optimized for different purposes:      - internal_id: Backend tenant isolation (database queries, scoping)     - organization_id: Frontend/user-facing identifier (APIs, logs, support)  ID Usage Patterns:     Database Queries:         ✅ service = CollectionService(internal_id=org.internal_id)         ❌ service = CollectionService(internal_id=org.organization_id)  # Wrong!      Error Messages:         ✅ raise NotFoundError(details={\"organization_id\": org.organization_id})         ❌ raise NotFoundError(details={\"internal_id\": org.internal_id})  # Don't expose!      Logging:         ✅ logger.info(f\"Action for org {org.organization_id}\", extra={\"internal_id\": org.internal_id})         ❌ logger.info(f\"Action for org {org.internal_id}\")  # Not user-friendly!  Security Model:     - internal_id is HIGH-ENTROPY (24 chars) and treated as a secret     - organization_id is LOWER-ENTROPY (15 chars) and safe to expose     - Never expose internal_id in API responses or user-facing messages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_id** | **str** | Internal organization identifier for multi-tenancy. High-entropy secret (24 chars) used exclusively for database queries and tenant isolation. This ID is immutable and never exposed in user-facing contexts. Format: int_xxxxxxxxxxxxxxxxxxxxx. USAGE: Database scoping, service initialization, provider configuration. | [optional] 
**organization_id** | **str** | Public organization identifier exposed in APIs and user-facing contexts. Lower-entropy ID (15 chars) safe for logs, error messages, and API responses. This ID can be changed for rebranding without affecting backend operations. Format: org_xxxxxxxxxxxxx. USAGE: API responses, error messages, logs, support tickets, analytics. | [optional] 
**organization_name** | **str** | Display name of the organization. | 
**logo_url** | **str** | URL to organization&#39;s logo image. Automatically fetched from Google&#39;s favicon service based on user&#39;s email domain during org creation. Can be overridden with custom URL. Format: https://www.google.com/s2/favicons?domain&#x3D;... or custom URL. | [optional] 
**account_type** | [**AccountTier**](AccountTier.md) | Billing tier determining available features and limits. | [optional] 
**credit_count** | **int** | DEPRECATED: Legacy credit balance. Use current_month_usage instead. | [optional] [default to 0]
**free_tier_usage_limit** | **int** | Maximum usage allowed before payment method required. Once current_month_usage exceeds this AND auto_billing is disabled, API access is blocked until payment method is added. | [optional] [default to 1000]
**metadata** | **Dict[str, object]** | Custom metadata applied to the organization. | [optional] 
**billing_email** | **str** | Email address for invoices and billing notifications. | [optional] 
**stripe_customer_id** | **str** | Stripe Customer ID for usage-based billing. Created when organization sets up payment method. Format: cus_xxxxxxxxxxxxx | [optional] 
**default_payment_method_id** | **str** | Default Stripe PaymentMethod ID for automatic monthly billing. Set when organization attaches a payment method. Format: pm_xxxxxxxxxxxxx | [optional] 
**auto_billing_enabled** | **bool** | Whether automatic monthly billing is enabled. When True, organization is charged automatically at end of month for usage. When False, organization uses manual credit purchases (legacy mode). | [optional] [default to False]
**billing_cycle_start** | **int** | Day of month when billing cycle starts (1-31). Invoices are generated on this day each month. If day doesn&#39;t exist in month (e.g., 31 in Feb), uses last day of month. | [optional] [default to 1]
**current_month_usage** | **int** | Credits consumed in current billing cycle. Reset to 0 after invoice generation. Used for real-time usage display in dashboard. | [optional] [default to 0]
**last_invoice_date** | **datetime** | UTC timestamp of last invoice generation. Used to determine billing period and prevent duplicate invoices. | [optional] 
**billing_period_start** | **datetime** | UTC timestamp when current billing period started. Set when invoice is generated or billing enabled. | [optional] 
**monthly_spending_budget** | **int** | Soft spending limit in USD cents for the current billing cycle. When set, triggers alerts at specified thresholds but doesn&#39;t block API access. Example: 10000 &#x3D; $100 budget. None &#x3D; no budget limit (unlimited spending allowed). | [optional] 
**spending_alert_thresholds** | **List[int]** | Percentage thresholds for spending alerts (0-100). When current spending reaches each threshold, an alert is sent. Default: [50, 75, 90, 100] sends alerts at 50%, 75%, 90%, and 100% of budget. Only applies when monthly_spending_budget is set. | [optional] 
**spending_alerts_enabled** | **bool** | Whether to send spending alerts when thresholds are crossed. When False, no alerts are sent even if thresholds are exceeded. | [optional] [default to True]
**spending_alerts_sent** | **List[int]** | Track which alert thresholds have been triggered in current billing cycle. Prevents duplicate alert notifications. Reset to empty list when invoice is generated. Example: [50, 75] means 50% and 75% alerts have been sent. | [optional] 
**hard_spending_cap** | **int** | Hard spending limit in USD cents for the current billing cycle. When reached, API access is blocked (similar to free tier limit). Example: 100000 &#x3D; $1000 hard cap. None &#x3D; no hard cap (only soft alerts apply). IMPORTANT: When enabled, operations are rejected once cap is reached. | [optional] 
**hard_cap_enabled** | **bool** | Whether to enforce the hard spending cap. When True and hard_spending_cap is set, API access is blocked at cap. When False, hard_spending_cap is ignored (only soft alerts apply). Users must explicitly enable this for protection. | [optional] [default to False]
**rate_limits** | [**BaseRateLimits**](BaseRateLimits.md) | Effective rate-limit configuration for the organization. | [optional] 
**created_at** | **datetime** | UTC timestamp when the organization was created. | [optional] 
**updated_at** | **datetime** | UTC timestamp of the most recent organization update. | [optional] 
**users** | **List[Dict[str, object]]** | Deprecated nested user documents (maintained for backwards compatibility during migration). | [optional] 
**infrastructure** | [**OrganizationInfrastructure**](OrganizationInfrastructure.md) | Infrastructure configuration for dedicated resources. None for SHARED tier (FREE/PRO organizations using Mixpeek infrastructure). Configured for ENTERPRISE tier with dedicated Qdrant/Ray instances. Inherited by all namespaces unless overridden at namespace level. | [optional] 
**max_dedicated_clusters** | **int** | Maximum number of dedicated infrastructure clusters allowed for this organization. 0 for non-enterprise tiers (FREE, STARTER, PROFESSIONAL). Set based on enterprise tier package (e.g., 3, 5, 10, unlimited). Each cluster includes dedicated Anyscale/Ray compute + Qdrant database. | [optional] [default to 0]
**dedicated_cluster_ids** | **List[str]** | List of dedicated infrastructure cluster IDs owned by this organization. Only applicable for Enterprise tier. Format: iclstr_xxxxxxxxxxxxx | [optional] 
**secrets** | **Dict[str, str]** | Encrypted secrets vault for API integrations and external service credentials. Keys are secret names (e.g., &#39;stripe_api_key&#39;, &#39;github_token&#39;), values are encrypted strings stored using Fernet encryption. Used by api_call retriever stage for secure credential storage. Secrets are encrypted on write and decrypted on read using ENCRYPTION_KEY. NEVER expose decrypted values in API responses or logs. Note: Values are stored as encrypted strings (bytes), not EncryptedStr type. | [optional] 
**audit_settings** | [**AuditSettings**](AuditSettings.md) | Audit trail configuration for the organization. Controls whether read operations are logged to the audit trail. By default, only write operations (create, update, delete) are audited. | [optional] 

## Example

```python
from mixpeek.models.organization_model import OrganizationModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationModel from a JSON string
organization_model_instance = OrganizationModel.from_json(json)
# print the JSON string representation of the object
print(OrganizationModel.to_json())

# convert the object into a dict
organization_model_dict = organization_model_instance.to_dict()
# create an instance of OrganizationModel from a dict
organization_model_from_dict = OrganizationModel.from_dict(organization_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


