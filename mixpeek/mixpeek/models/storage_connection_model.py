from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.storage_provider import StorageProvider
from ..models.task_status_enum import TaskStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_drive_config import GoogleDriveConfig
    from ..models.postgre_sql_config import PostgreSQLConfig
    from ..models.s3_config import S3Config
    from ..models.share_point_config import SharePointConfig
    from ..models.snowflake_config import SnowflakeConfig
    from ..models.storage_connection_model_metadata import StorageConnectionModelMetadata
    from ..models.storage_connection_model_provider_config_type_6 import StorageConnectionModelProviderConfigType6
    from ..models.tigris_config import TigrisConfig


T = TypeVar("T", bound="StorageConnectionModel")


@_attrs_define
class StorageConnectionModel:
    """Canonical representation of an external storage provider connection.

    Storage connections enable Mixpeek to access external cloud storage providers
    (Google Drive, S3, etc.) for automated file ingestion and synchronization.
    Each connection represents a configured integration with credentials, health
    monitoring, and usage tracking.

    Lifecycle States:
        - ACTIVE: Connection is healthy and ready for sync operations
        - SUSPENDED: Temporarily disabled by user (credentials preserved)
        - FAILED: Health checks failing (may need credential refresh)
        - ARCHIVED: Permanently retired (cannot be reactivated)

    Security:
        - Sensitive credential fields are encrypted at rest using MongoDB
          client-side field level encryption (CSFLE)
        - Credentials never appear in API responses or logs
        - Failed authentication attempts are logged in last_error
        - Consecutive failures trigger automatic suspension

    Use Cases:
        - Connect to team Google Drive for document ingestion
        - Sync files from customer S3 buckets
        - Monitor and process uploaded media files
        - Schedule periodic sync operations

    Health Monitoring:
        - Automatic health checks validate connectivity and credentials
        - consecutive_failures tracks authentication/network issues
        - Auto-disable after 5 consecutive failures to prevent lockout
        - last_error stores diagnostic information for debugging

        Attributes:
            internal_id (str): REQUIRED. Organization internal identifier for multi-tenancy scoping. All connection
                operations are scoped to this organization. Format: int_{24-character secure token}.
            provider_type (StorageProvider): Supported external storage providers for ingestion and sync.

                Mixpeek can connect to external storage providers to automatically
                ingest objects and keep them synchronized with your namespaces.

                Providers:
                    GOOGLE_DRIVE: Google Drive and Google Workspace shared drives.
                        - Authentication: Service account or OAuth2
                        - Features: Shared drive support, real-time sync, metadata preservation
                        - Use cases: Marketing assets, team documents, knowledge bases
                        - Limitations: Rate limits apply (10,000 requests/100 seconds per user)

                    S3: Amazon S3 and S3-compatible storage (MinIO, DigitalOcean Spaces, etc).
                        - Authentication: Access keys or IAM role assumption
                        - Features: Bucket notifications, prefix filtering, versioning support
                        - Use cases: Data lakes, video archives, ML datasets, backups
                        - Limitations: IAM role assumption preferred over access keys

                    SNOWFLAKE: Snowflake data warehouse tables.
                        - Authentication: Key pair or username/password
                        - Features: Incremental sync via watermarks, row-level mapping, schema introspection
                        - Use cases: Customer data tables, product catalogs, transaction logs, metadata tables
                        - Limitations: Each row becomes one object; large tables require incremental column

                    SHAREPOINT: Microsoft SharePoint and OneDrive for Business.
                        - Authentication: Azure AD OAuth2 (client credentials or delegated)
                        - Features: Site/drive selection, folder sync, delta queries for incremental sync
                        - Use cases: Enterprise documents, team collaboration files, compliance archives
                        - Limitations: Requires Azure AD app registration; throttling limits apply

                Connection Requirements:
                    - Valid credentials with read access to target files/buckets
                    - Network connectivity from Mixpeek infrastructure
                    - Appropriate IAM policies or share permissions configured

                Examples:
                    - Use GOOGLE_DRIVE for syncing team marketing materials
                    - Use S3 for ingesting video archives from data lakes
                    - Use S3 with IAM role for secure production deployments
                    - Use SHAREPOINT for syncing enterprise SharePoint document libraries

                    TIGRIS: Tigris Data globally distributed object storage (S3-compatible).
                        - Authentication: Access keys (same format as S3)
                        - Features: S3-compatible API, global distribution, zero egress fees
                        - Use cases: Globally distributed media, low-latency content delivery
                        - Endpoint: https://fly.storage.tigris.dev

                    POSTGRESQL: PostgreSQL relational database.
                        - Authentication: Username/password
                        - Features: SQL queries, incremental sync via watermarks, row-level mapping
                        - Use cases: Customer data tables, product catalogs, transaction logs
                        - Limitations: Each row becomes one object; large tables require incremental column
            provider_config (GoogleDriveConfig | PostgreSQLConfig | S3Config | SharePointConfig | SnowflakeConfig |
                StorageConnectionModelProviderConfigType6 | TigrisConfig): REQUIRED. Provider-specific configuration payload
                including credentials. Type depends on provider_type (GoogleDriveConfig, S3Config, etc.). SECURITY: Sensitive
                credential fields are encrypted at rest via MongoDB client-side field level encryption (CSFLE). Credentials
                never appear in API responses or logs. See provider_configs.py for detailed schemas.
            name (str): REQUIRED. Human-readable connection name for identification. Displayed in dashboards, sync logs, and
                API responses. Must be unique within the organization for clarity. Format: 1-100 characters, descriptive of the
                connection's purpose.
            created_by_user_id (str): REQUIRED. User identifier of the user who created this connection. Used for audit
                trails and permission checks. Format: usr_{15-character alphanumeric}. Immutable after creation.
            connection_id (str | Unset): Unique identifier for the storage connection. Auto-generated with 'conn_' prefix
                followed by secure random token. Format: conn_{15-character alphanumeric}. Used for API operations and audit
                trails.
            description (None | str | Unset): NOT REQUIRED. Optional description explaining the connection's purpose and
                scope. Helpful for team collaboration and documentation. Format: Up to 500 characters.
            status (TaskStatusEnum | Unset): Enumeration of task statuses for tracking asynchronous operations.

                Task statuses indicate the current state of asynchronous operations like
                batch processing, object ingestion, clustering, and taxonomy execution.

                Status Categories:
                    Operation Statuses: Track progress of async operations
                    Lifecycle Statuses: Track entity state (buckets, collections, namespaces)

                Values:
                    PENDING: Task is queued but has not started processing yet
                    IN_PROGRESS: Task is currently being executed
                    PROCESSING: Task is actively processing data (similar to IN_PROGRESS)
                    COMPLETED: Task finished successfully with no errors
                    COMPLETED_WITH_ERRORS: Task finished but some items failed (partial success)
                    FAILED: Task encountered an error and could not complete
                    CANCELED: Task was manually canceled by a user or system
                    UNKNOWN: Task status could not be determined
                    SKIPPED: Task was intentionally skipped
                    DRAFT: Task is in draft state and not yet submitted

                    ACTIVE: Entity is active and operational (for buckets, collections, etc.)
                    ARCHIVED: Entity has been archived
                    SUSPENDED: Entity has been temporarily suspended

                Terminal Statuses:
                    COMPLETED, COMPLETED_WITH_ERRORS, FAILED, CANCELED are terminal statuses.
                    Once a task reaches these states, it will not transition to another state.

                Partial Success Handling:
                    COMPLETED_WITH_ERRORS indicates that the operation completed but some
                    documents/items failed. The task result includes:
                    - List of successful items
                    - List of failed items with error details
                    - Success rate percentage
                    This allows clients to handle partial success scenarios appropriately.

                Polling Guidance:
                    - Poll tasks in PENDING, IN_PROGRESS, or PROCESSING states
                    - Stop polling when task reaches COMPLETED, COMPLETED_WITH_ERRORS, FAILED, or CANCELED
                    - Use exponential backoff (1s → 30s) when polling
            is_active (bool | Unset): Quick boolean flag for filtering active connections in queries. True when status is
                ACTIVE, False for SUSPENDED/FAILED/ARCHIVED. Maintained automatically when status changes. Use for efficient
                filtering: db.connections.find({'is_active': True}) Default: True.
            last_used_at (datetime.datetime | None | Unset): NOT REQUIRED. UTC timestamp of the most recent successful sync
                operation. Updated automatically after each successful file sync/list operation. None if connection has never
                been used. Useful for identifying stale connections and usage analytics.
            last_error (None | str | Unset): NOT REQUIRED. Most recent error message from failed health check or sync.
                Populated when authentication fails, network errors occur, or permissions denied. None when connection is
                healthy. Format: Error message truncated to 1000 characters. Used for diagnostics and troubleshooting.
            consecutive_failures (int | Unset): Counter tracking consecutive failed health checks or sync attempts.
                Incremented on each failure, reset to 0 on success. Used to implement automatic connection suspension. Auto-
                suspend after 5 consecutive failures to prevent account lockout. Range: 0 to infinity (typically 0-10). Default:
                0.
            created_at (datetime.datetime | Unset): UTC timestamp when the connection was created. Auto-generated using
                shared.utilities.helpers.current_time(). Immutable after creation. Format: ISO 8601 datetime.
            updated_at (datetime.datetime | Unset): UTC timestamp of the most recent update to the connection. Updated
                automatically on any field modification. Tracks configuration changes, status updates, and credential refreshes.
                Format: ISO 8601 datetime.
            metadata (StorageConnectionModelMetadata | Unset): Arbitrary key-value metadata provided by the user. Useful for
                tagging, categorization, and custom annotations. NOT REQUIRED - defaults to empty dictionary. Common uses: team
                tags, cost center codes, project identifiers.
    """

    internal_id: str
    provider_type: StorageProvider
    provider_config: (
        GoogleDriveConfig
        | PostgreSQLConfig
        | S3Config
        | SharePointConfig
        | SnowflakeConfig
        | StorageConnectionModelProviderConfigType6
        | TigrisConfig
    )
    name: str
    created_by_user_id: str
    connection_id: str | Unset = UNSET
    description: None | str | Unset = UNSET
    status: TaskStatusEnum | Unset = UNSET
    is_active: bool | Unset = True
    last_used_at: datetime.datetime | None | Unset = UNSET
    last_error: None | str | Unset = UNSET
    consecutive_failures: int | Unset = 0
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    metadata: StorageConnectionModelMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.google_drive_config import GoogleDriveConfig
        from ..models.postgre_sql_config import PostgreSQLConfig
        from ..models.s3_config import S3Config
        from ..models.share_point_config import SharePointConfig
        from ..models.snowflake_config import SnowflakeConfig
        from ..models.tigris_config import TigrisConfig

        internal_id = self.internal_id

        provider_type = self.provider_type.value

        provider_config: dict[str, Any]
        if isinstance(self.provider_config, GoogleDriveConfig):
            provider_config = self.provider_config.to_dict()
        elif isinstance(self.provider_config, S3Config):
            provider_config = self.provider_config.to_dict()
        elif isinstance(self.provider_config, SnowflakeConfig):
            provider_config = self.provider_config.to_dict()
        elif isinstance(self.provider_config, SharePointConfig):
            provider_config = self.provider_config.to_dict()
        elif isinstance(self.provider_config, TigrisConfig):
            provider_config = self.provider_config.to_dict()
        elif isinstance(self.provider_config, PostgreSQLConfig):
            provider_config = self.provider_config.to_dict()
        else:
            provider_config = self.provider_config.to_dict()

        name = self.name

        created_by_user_id = self.created_by_user_id

        connection_id = self.connection_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        is_active = self.is_active

        last_used_at: None | str | Unset
        if isinstance(self.last_used_at, Unset):
            last_used_at = UNSET
        elif isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        consecutive_failures = self.consecutive_failures

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internal_id": internal_id,
                "provider_type": provider_type,
                "provider_config": provider_config,
                "name": name,
                "created_by_user_id": created_by_user_id,
            }
        )
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if last_error is not UNSET:
            field_dict["last_error"] = last_error
        if consecutive_failures is not UNSET:
            field_dict["consecutive_failures"] = consecutive_failures
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_drive_config import GoogleDriveConfig
        from ..models.postgre_sql_config import PostgreSQLConfig
        from ..models.s3_config import S3Config
        from ..models.share_point_config import SharePointConfig
        from ..models.snowflake_config import SnowflakeConfig
        from ..models.storage_connection_model_metadata import StorageConnectionModelMetadata
        from ..models.storage_connection_model_provider_config_type_6 import StorageConnectionModelProviderConfigType6
        from ..models.tigris_config import TigrisConfig

        d = dict(src_dict)
        internal_id = d.pop("internal_id")

        provider_type = StorageProvider(d.pop("provider_type"))

        def _parse_provider_config(
            data: object,
        ) -> (
            GoogleDriveConfig
            | PostgreSQLConfig
            | S3Config
            | SharePointConfig
            | SnowflakeConfig
            | StorageConnectionModelProviderConfigType6
            | TigrisConfig
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_config_type_0 = GoogleDriveConfig.from_dict(data)

                return provider_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_config_type_1 = S3Config.from_dict(data)

                return provider_config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_config_type_2 = SnowflakeConfig.from_dict(data)

                return provider_config_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_config_type_3 = SharePointConfig.from_dict(data)

                return provider_config_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_config_type_4 = TigrisConfig.from_dict(data)

                return provider_config_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_config_type_5 = PostgreSQLConfig.from_dict(data)

                return provider_config_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            provider_config_type_6 = StorageConnectionModelProviderConfigType6.from_dict(data)

            return provider_config_type_6

        provider_config = _parse_provider_config(d.pop("provider_config"))

        name = d.pop("name")

        created_by_user_id = d.pop("created_by_user_id")

        connection_id = d.pop("connection_id", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _status = d.pop("status", UNSET)
        status: TaskStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TaskStatusEnum(_status)

        is_active = d.pop("is_active", UNSET)

        def _parse_last_used_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = isoparse(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at", UNSET))

        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("last_error", UNSET))

        consecutive_failures = d.pop("consecutive_failures", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _metadata = d.pop("metadata", UNSET)
        metadata: StorageConnectionModelMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = StorageConnectionModelMetadata.from_dict(_metadata)

        storage_connection_model = cls(
            internal_id=internal_id,
            provider_type=provider_type,
            provider_config=provider_config,
            name=name,
            created_by_user_id=created_by_user_id,
            connection_id=connection_id,
            description=description,
            status=status,
            is_active=is_active,
            last_used_at=last_used_at,
            last_error=last_error,
            consecutive_failures=consecutive_failures,
            created_at=created_at,
            updated_at=updated_at,
            metadata=metadata,
        )

        storage_connection_model.additional_properties = d
        return storage_connection_model

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
