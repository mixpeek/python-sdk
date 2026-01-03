# StorageProvider

Supported external storage providers for ingestion and sync.  Mixpeek can connect to external storage providers to automatically ingest objects and keep them synchronized with your namespaces.  Providers:     GOOGLE_DRIVE: Google Drive and Google Workspace shared drives.         - Authentication: Service account or OAuth2         - Features: Shared drive support, real-time sync, metadata preservation         - Use cases: Marketing assets, team documents, knowledge bases         - Limitations: Rate limits apply (10,000 requests/100 seconds per user)      S3: Amazon S3 and S3-compatible storage (MinIO, DigitalOcean Spaces, etc).         - Authentication: Access keys or IAM role assumption         - Features: Bucket notifications, prefix filtering, versioning support         - Use cases: Data lakes, video archives, ML datasets, backups         - Limitations: IAM role assumption preferred over access keys      SNOWFLAKE: Snowflake data warehouse tables.         - Authentication: Key pair or username/password         - Features: Incremental sync via watermarks, row-level mapping, schema introspection         - Use cases: Customer data tables, product catalogs, transaction logs, metadata tables         - Limitations: Each row becomes one object; large tables require incremental column      SHAREPOINT: Microsoft SharePoint and OneDrive for Business.         - Authentication: Azure AD OAuth2 (client credentials or delegated)         - Features: Site/drive selection, folder sync, delta queries for incremental sync         - Use cases: Enterprise documents, team collaboration files, compliance archives         - Limitations: Requires Azure AD app registration; throttling limits apply  Connection Requirements:     - Valid credentials with read access to target files/buckets     - Network connectivity from Mixpeek infrastructure     - Appropriate IAM policies or share permissions configured  Examples:     - Use GOOGLE_DRIVE for syncing team marketing materials     - Use S3 for ingesting video archives from data lakes     - Use S3 with IAM role for secure production deployments     - Use SHAREPOINT for syncing enterprise SharePoint document libraries      TIGRIS: Tigris Data globally distributed object storage (S3-compatible).         - Authentication: Access keys (same format as S3)         - Features: S3-compatible API, global distribution, zero egress fees         - Use cases: Globally distributed media, low-latency content delivery         - Endpoint: https://fly.storage.tigris.dev      POSTGRESQL: PostgreSQL relational database.         - Authentication: Username/password         - Features: SQL queries, incremental sync via watermarks, row-level mapping         - Use cases: Customer data tables, product catalogs, transaction logs         - Limitations: Each row becomes one object; large tables require incremental column

## Enum

* `GOOGLE_DRIVE` (value: `'google_drive'`)

* `S3` (value: `'s3'`)

* `SNOWFLAKE` (value: `'snowflake'`)

* `SHAREPOINT` (value: `'sharepoint'`)

* `TIGRIS` (value: `'tigris'`)

* `POSTGRESQL` (value: `'postgresql'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


