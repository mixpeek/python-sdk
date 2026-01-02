from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snowflake_key_pair_credentials import SnowflakeKeyPairCredentials
    from ..models.snowflake_username_password_credentials import SnowflakeUsernamePasswordCredentials


T = TypeVar("T", bound="SnowflakeConfig")


@_attrs_define
class SnowflakeConfig:
    r"""Snowflake data warehouse configuration for table-based sync.

    Enables syncing Snowflake table rows as JSON objects in Mixpeek buckets.
    Each row becomes one object, with incremental sync via watermark columns.

    Authentication Options:
        - Key Pair: Recommended for production (secure, password-less)
        - Username/Password: Fallback option (simpler setup)

    Requirements:
        - Snowflake account with read access to target tables
        - Warehouse with compute resources
        - SELECT permissions on target tables/schemas
        - USAGE permissions on database, schema, warehouse

    Use Cases:
        - Sync customer data tables for AI/ML pipelines
        - Ingest product catalog for search/recommendations
        - Process transaction logs for analytics
        - Mirror metadata tables for vector search

    Example:
        Production setup with key pair auth:
        ```python
        config = {
            "provider_type": "snowflake",
            "credentials": {
                "type": "key_pair",
                "username": "MIXPEEK_SYNC",
                "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
            },
            "account": "xy12345.us-east-1",
            "warehouse": "MIXPEEK_SYNC_WH",
            "database": "PRODUCTION",
            "schema": "PUBLIC",
            "role": "SYNC_ROLE",
            "incremental_column": "updated_at",
            "primary_key_columns": ["id"],
        }
        ```

        Attributes:
            credentials (SnowflakeKeyPairCredentials | SnowflakeUsernamePasswordCredentials): REQUIRED. Authentication
                credentials for Snowflake. Choose key_pair for production (recommended) or username_password for simpler setup.
                The 'type' field determines which credential mechanism is used.
            account (str): REQUIRED. Snowflake account identifier. Format: {account_locator}.{cloud_region} or
                {org_name}-{account_name} Find in: Snowflake UI > Account dropdown > Account URL
            warehouse (str): REQUIRED. Warehouse name for compute resources. Must have USAGE privilege on this warehouse.
                Warehouse will be used for all sync queries. Consider: Use dedicated warehouse for sync operations to isolate
                costs.
            provider_type (Literal['snowflake'] | Unset):  Default: 'snowflake'.
            database (None | str | Unset): NOT REQUIRED if fully qualified table name used in source_path. Database name for
                default context. Can be omitted if source_path uses {DATABASE}.{SCHEMA}.{TABLE} format. Must have USAGE
                privilege if specified.
            schema (None | str | Unset): NOT REQUIRED if fully qualified table name used in source_path. Schema name for
                default context. Can be omitted if source_path uses {SCHEMA}.{TABLE} or {DATABASE}.{SCHEMA}.{TABLE}. Must have
                USAGE privilege if specified.
            role (None | str | Unset): NOT REQUIRED. Snowflake role to use for operations. If omitted, uses user's default
                role. Role must have SELECT on target tables and USAGE on database/schema/warehouse. Best practice: Create
                dedicated read-only role for sync operations.
            incremental_column (None | str | Unset): NOT REQUIRED. Column name for incremental sync watermark. Should be a
                TIMESTAMP, TIMESTAMP_NTZ, or DATE column that tracks row modifications. When set, only rows with
                {incremental_column} > last_sync_watermark are synced. Common values: updated_at, modified_at, last_updated,
                ingestion_timestamp. If omitted, full table scan on every sync (not recommended for large tables).
            primary_key_columns (list[str] | None | Unset): NOT REQUIRED. Column names forming the primary key for stable
                object IDs. Used to generate deterministic file_id for deduplication. If omitted, uses hash of entire row
                content (less stable). Recommendation: Always specify for production to ensure idempotent syncs.
            query_timeout_seconds (int | Unset): Query timeout in seconds. Prevents long-running queries from blocking sync
                operations. Default: 300 seconds (5 minutes). Increase for large tables or complex queries. Default: 300.
            fetch_size (int | Unset): Number of rows to fetch per network round-trip. Higher values reduce network overhead
                but increase memory usage. Default: 1000 rows. Tune based on row size and available memory. Default: 1000.
    """

    credentials: SnowflakeKeyPairCredentials | SnowflakeUsernamePasswordCredentials
    account: str
    warehouse: str
    provider_type: Literal["snowflake"] | Unset = "snowflake"
    database: None | str | Unset = UNSET
    schema: None | str | Unset = UNSET
    role: None | str | Unset = UNSET
    incremental_column: None | str | Unset = UNSET
    primary_key_columns: list[str] | None | Unset = UNSET
    query_timeout_seconds: int | Unset = 300
    fetch_size: int | Unset = 1000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.snowflake_key_pair_credentials import SnowflakeKeyPairCredentials

        credentials: dict[str, Any]
        if isinstance(self.credentials, SnowflakeKeyPairCredentials):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials.to_dict()

        account = self.account

        warehouse = self.warehouse

        provider_type = self.provider_type

        database: None | str | Unset
        if isinstance(self.database, Unset):
            database = UNSET
        else:
            database = self.database

        schema: None | str | Unset
        if isinstance(self.schema, Unset):
            schema = UNSET
        else:
            schema = self.schema

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        incremental_column: None | str | Unset
        if isinstance(self.incremental_column, Unset):
            incremental_column = UNSET
        else:
            incremental_column = self.incremental_column

        primary_key_columns: list[str] | None | Unset
        if isinstance(self.primary_key_columns, Unset):
            primary_key_columns = UNSET
        elif isinstance(self.primary_key_columns, list):
            primary_key_columns = self.primary_key_columns

        else:
            primary_key_columns = self.primary_key_columns

        query_timeout_seconds = self.query_timeout_seconds

        fetch_size = self.fetch_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
                "account": account,
                "warehouse": warehouse,
            }
        )
        if provider_type is not UNSET:
            field_dict["provider_type"] = provider_type
        if database is not UNSET:
            field_dict["database"] = database
        if schema is not UNSET:
            field_dict["schema"] = schema
        if role is not UNSET:
            field_dict["role"] = role
        if incremental_column is not UNSET:
            field_dict["incremental_column"] = incremental_column
        if primary_key_columns is not UNSET:
            field_dict["primary_key_columns"] = primary_key_columns
        if query_timeout_seconds is not UNSET:
            field_dict["query_timeout_seconds"] = query_timeout_seconds
        if fetch_size is not UNSET:
            field_dict["fetch_size"] = fetch_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snowflake_key_pair_credentials import SnowflakeKeyPairCredentials
        from ..models.snowflake_username_password_credentials import SnowflakeUsernamePasswordCredentials

        d = dict(src_dict)

        def _parse_credentials(data: object) -> SnowflakeKeyPairCredentials | SnowflakeUsernamePasswordCredentials:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = SnowflakeKeyPairCredentials.from_dict(data)

                return credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            credentials_type_1 = SnowflakeUsernamePasswordCredentials.from_dict(data)

            return credentials_type_1

        credentials = _parse_credentials(d.pop("credentials"))

        account = d.pop("account")

        warehouse = d.pop("warehouse")

        provider_type = cast(Literal["snowflake"] | Unset, d.pop("provider_type", UNSET))
        if provider_type != "snowflake" and not isinstance(provider_type, Unset):
            raise ValueError(f"provider_type must match const 'snowflake', got '{provider_type}'")

        def _parse_database(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        database = _parse_database(d.pop("database", UNSET))

        def _parse_schema(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_incremental_column(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        incremental_column = _parse_incremental_column(d.pop("incremental_column", UNSET))

        def _parse_primary_key_columns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                primary_key_columns_type_0 = cast(list[str], data)

                return primary_key_columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        primary_key_columns = _parse_primary_key_columns(d.pop("primary_key_columns", UNSET))

        query_timeout_seconds = d.pop("query_timeout_seconds", UNSET)

        fetch_size = d.pop("fetch_size", UNSET)

        snowflake_config = cls(
            credentials=credentials,
            account=account,
            warehouse=warehouse,
            provider_type=provider_type,
            database=database,
            schema=schema,
            role=role,
            incremental_column=incremental_column,
            primary_key_columns=primary_key_columns,
            query_timeout_seconds=query_timeout_seconds,
            fetch_size=fetch_size,
        )

        snowflake_config.additional_properties = d
        return snowflake_config

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
