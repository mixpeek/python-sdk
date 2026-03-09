# ProviderConfig

REQUIRED. Provider-specific configuration payload including credentials. Type depends on provider_type (GoogleDriveConfig, S3Config, etc.). SECURITY: Sensitive credential fields are encrypted at rest via MongoDB client-side field level encryption (CSFLE). Credentials never appear in API responses or logs. See provider_configs.py for detailed schemas.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **str** |  | [optional] [default to 'box']
**credentials** | [**Credentials**](Credentials.md) |  | 
**shared_drive_id** | **str** | NOT REQUIRED. Google Workspace shared drive (Team Drive) identifier. When provided, sync operations are scoped to this shared drive only. When omitted, syncs from &#39;My Drive&#39; of the authenticated account. Find ID: Open shared drive in browser, copy ID from URL. Format: 0A{alphanumeric-string} | [optional] 
**impersonate_user** | **str** | NOT REQUIRED. Email address to impersonate when using service account credentials. Requires domain-wide delegation to be enabled for the service account. Used in G Suite environments to access files as a specific user. When omitted, uses the service account&#39;s own access. Format: Valid email address in the G Suite domain. | [optional] 
**region** | **str** | Region for Tigris. Typically &#39;auto&#39; for automatic global distribution. Tigris automatically distributes data globally, so region is usually &#39;auto&#39;. Default: auto | [default to 'auto']
**endpoint_url** | **str** | Tigris S3-compatible endpoint URL. Default: https://fly.storage.tigris.dev This is the standard Tigris endpoint and usually doesn&#39;t need to be changed. | [optional] [default to 'https://fly.storage.tigris.dev']
**use_ssl** | **bool** | Whether to use TLS/SSL encryption for connections to S3. RECOMMENDED: Always True for production environments. Set to False only for local development with unencrypted endpoints. Default: True | [optional] [default to True]
**verify_ssl** | **bool** | Whether to verify TLS/SSL certificates when connecting. RECOMMENDED: Always True for production to prevent MITM attacks. Set to False only for development with self-signed certificates. Requires use_ssl&#x3D;True to have any effect. Default: True | [optional] [default to True]
**account** | **str** | REQUIRED. Snowflake account identifier. Format: {account_locator}.{cloud_region} or {org_name}-{account_name} Find in: Snowflake UI &gt; Account dropdown &gt; Account URL | 
**warehouse** | **str** | REQUIRED. Warehouse name for compute resources. Must have USAGE privilege on this warehouse. Warehouse will be used for all sync queries. Consider: Use dedicated warehouse for sync operations to isolate costs. | 
**database** | **str** | REQUIRED. Database name to connect to. User must have CONNECT privilege on this database. | 
**var_schema** | **str** | Schema name for default context. Default: &#39;public&#39;. User must have USAGE privilege on this schema. | [optional] [default to 'public']
**role** | **str** | NOT REQUIRED. Snowflake role to use for operations. If omitted, uses user&#39;s default role. Role must have SELECT on target tables and USAGE on database/schema/warehouse. Best practice: Create dedicated read-only role for sync operations. | [optional] 
**incremental_column** | **str** | NOT REQUIRED. Column name for incremental sync watermark. Should be a TIMESTAMP or DATE column that tracks row modifications. Common values: updated_at, modified_at, last_updated. If omitted, full table scan on every sync. | [optional] 
**primary_key_columns** | **List[str]** | NOT REQUIRED. Column names forming the primary key for stable object IDs. Used to generate deterministic file_id for deduplication. If omitted, uses hash of entire row content. | [optional] 
**query_timeout_seconds** | **int** | Query timeout in seconds. Default: 300 seconds (5 minutes). Increase for large tables or complex queries. | [optional] [default to 300]
**fetch_size** | **int** | Number of rows to fetch per batch. Higher values reduce network overhead but increase memory usage. Default: 1000 rows. | [optional] [default to 1000]
**site_id** | **str** | NOT REQUIRED if using personal OneDrive. SharePoint site identifier for targeting a specific site. Format: &#39;{hostname},{site-collection-id},{web-id}&#39; or site URL. Find via: Microsoft Graph API GET /sites?search&#x3D;{keyword} Example: &#39;contoso.sharepoint.com,12345678-...,87654321-...&#39; | [optional] 
**drive_id** | **str** | NOT REQUIRED if you want to use the default document library. Specific drive (document library) ID within the site. Find via: GET /sites/{site-id}/drives Format: Base64-encoded ID starting with &#39;b!&#39; | [optional] 
**folder_path** | **str** | NOT REQUIRED. Path within the drive to sync from. If omitted, syncs from the root of the drive. Format: Forward-slash separated path (e.g., &#39;/Documents/Marketing&#39;). Note: Leading slash is optional. | [optional] 
**host** | **str** | REQUIRED. PostgreSQL server hostname or IP address. Examples: &#39;localhost&#39;, &#39;db.example.com&#39;, &#39;192.168.1.100&#39; | 
**port** | **int** | PostgreSQL server port. Default: 5432 (standard PostgreSQL port) | [optional] [default to 5432]
**ssl_mode** | **str** | SSL/TLS connection mode. Options: &#39;disable&#39;, &#39;allow&#39;, &#39;prefer&#39;, &#39;require&#39;, &#39;verify-ca&#39;, &#39;verify-full&#39;. Default: &#39;prefer&#39;. RECOMMENDED: Use &#39;require&#39; or stricter for production environments. | [optional] [default to 'prefer']
**scopes** | **List[str]** | OAuth scopes granted during authorization. | [optional] [default to [user.info.basic, video.list]]
**business_account_id** | **str** | Instagram Business Account ID if different from the user ID. Auto-populated from OAuth flow. | [optional] 
**user_agent** | **str** | User-Agent header for API requests. | [optional] [default to 'Mixpeek HTTP API Sync/1.0']
**request_timeout** | **int** | HTTP request timeout in seconds. | [optional] [default to 30]
**http_method** | **str** | HTTP method to use when calling the API. | [optional] [default to 'GET']
**request_body** | **Dict[str, object]** | Optional JSON body for POST requests. | [optional] 
**items_path** | **str** | Dot-notation path to the array of items in the JSON response. Examples: &#39;hits&#39; for {hits: [...]}, &#39;data.items&#39; for {data: {items: [...]}}. Leave empty if the response is a top-level array. | [optional] [default to '']
**item_id_field** | **str** | REQUIRED. Field name in each item used as a unique ID for deduplication. Examples: &#39;id&#39;, &#39;objectID&#39;, &#39;uuid&#39;. | 
**item_modified_field** | **str** | Optional field name for a timestamp used for incremental sync. Supports ISO 8601 strings and Unix timestamps. Examples: &#39;updated_at&#39;, &#39;created_at&#39;, &#39;modified&#39;. | [optional] 
**response_content_type** | **str** | Response format: &#39;json&#39; (default) or &#39;jsonl&#39; (newline-delimited JSON). | [optional] [default to 'json']
**folder_id** | **str** | Box folder ID to sync from. Default &#39;0&#39; is the root folder. Find folder ID: Open folder in Box web UI, copy the numeric ID from the URL. Example URL: https://app.box.com/folder/123456789 → folder_id&#x3D;&#39;123456789&#39; | [optional] [default to '0']

## Example

```python
from mixpeek.models.provider_config import ProviderConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderConfig from a JSON string
provider_config_instance = ProviderConfig.from_json(json)
# print the JSON string representation of the object
print(ProviderConfig.to_json())

# convert the object into a dict
provider_config_dict = provider_config_instance.to_dict()
# create an instance of ProviderConfig from a dict
provider_config_from_dict = ProviderConfig.from_dict(provider_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


