from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.postgre_sql_credentials import PostgreSQLCredentials


T = TypeVar("T", bound="PostgreSQLConfig")


@_attrs_define
class PostgreSQLConfig:
    """PostgreSQL database configuration for table-based sync and SQL queries.

    Enables syncing PostgreSQL table rows as JSON objects and running SQL queries
    via the SQL Lookup retriever stage. Each row becomes one object, with
    incremental sync via watermark columns.

    Authentication:
        - Username/Password: Standard PostgreSQL authentication

    Requirements:
        - PostgreSQL 12+ recommended
        - Read access to target tables
        - Network connectivity to PostgreSQL server

    Use Cases:
        - Sync customer data tables for AI/ML pipelines
        - Run SQL lookups to enrich documents in retriever pipelines
        - Ingest product catalog for search/recommendations
        - Process transaction logs for analytics

    Example:
        ```python
        config = {
            "provider_type": "postgresql",
            "credentials": {
                "type": "username_password",
                "username": "mixpeek_sync",
                "password": "secure_password",
            },
            "host": "db.example.com",
            "port": 5432,
            "database": "production",
            "schema": "public",
            "ssl_mode": "require",
        }
        ```

        Attributes:
            credentials (PostgreSQLCredentials): PostgreSQL username/password authentication.

                Standard username/password authentication for PostgreSQL databases.
                Password is encrypted at rest using MongoDB CSFLE.

                Security:
                    - password field is encrypted at rest via CSFLE
                    - Consider using SSL mode 'require' for production
                    - Use dedicated read-only database user for sync operations
            host (str): REQUIRED. PostgreSQL server hostname or IP address. Examples: 'localhost', 'db.example.com',
                '192.168.1.100'
            database (str): REQUIRED. Database name to connect to. User must have CONNECT privilege on this database.
            provider_type (Literal['postgresql'] | Unset):  Default: 'postgresql'.
            port (int | Unset): PostgreSQL server port. Default: 5432 (standard PostgreSQL port) Default: 5432.
            schema (None | str | Unset): Schema name for default context. Default: 'public'. User must have USAGE privilege
                on this schema. Default: 'public'.
            ssl_mode (str | Unset): SSL/TLS connection mode. Options: 'disable', 'allow', 'prefer', 'require', 'verify-ca',
                'verify-full'. Default: 'prefer'. RECOMMENDED: Use 'require' or stricter for production environments. Default:
                'prefer'.
            incremental_column (None | str | Unset): NOT REQUIRED. Column name for incremental sync watermark. Should be a
                TIMESTAMP or DATE column that tracks row modifications. Common values: updated_at, modified_at, last_updated. If
                omitted, full table scan on every sync.
            primary_key_columns (list[str] | None | Unset): NOT REQUIRED. Column names forming the primary key for stable
                object IDs. Used to generate deterministic file_id for deduplication. If omitted, uses hash of entire row
                content.
            query_timeout_seconds (int | Unset): Query timeout in seconds. Default: 300 seconds (5 minutes). Increase for
                large tables or complex queries. Default: 300.
            fetch_size (int | Unset): Number of rows to fetch per batch. Higher values reduce network overhead but increase
                memory usage. Default: 1000 rows. Default: 1000.
    """

    credentials: PostgreSQLCredentials
    host: str
    database: str
    provider_type: Literal["postgresql"] | Unset = "postgresql"
    port: int | Unset = 5432
    schema: None | str | Unset = "public"
    ssl_mode: str | Unset = "prefer"
    incremental_column: None | str | Unset = UNSET
    primary_key_columns: list[str] | None | Unset = UNSET
    query_timeout_seconds: int | Unset = 300
    fetch_size: int | Unset = 1000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials = self.credentials.to_dict()

        host = self.host

        database = self.database

        provider_type = self.provider_type

        port = self.port

        schema: None | str | Unset
        if isinstance(self.schema, Unset):
            schema = UNSET
        else:
            schema = self.schema

        ssl_mode = self.ssl_mode

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
                "host": host,
                "database": database,
            }
        )
        if provider_type is not UNSET:
            field_dict["provider_type"] = provider_type
        if port is not UNSET:
            field_dict["port"] = port
        if schema is not UNSET:
            field_dict["schema"] = schema
        if ssl_mode is not UNSET:
            field_dict["ssl_mode"] = ssl_mode
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
        from ..models.postgre_sql_credentials import PostgreSQLCredentials

        d = dict(src_dict)
        credentials = PostgreSQLCredentials.from_dict(d.pop("credentials"))

        host = d.pop("host")

        database = d.pop("database")

        provider_type = cast(Literal["postgresql"] | Unset, d.pop("provider_type", UNSET))
        if provider_type != "postgresql" and not isinstance(provider_type, Unset):
            raise ValueError(f"provider_type must match const 'postgresql', got '{provider_type}'")

        port = d.pop("port", UNSET)

        def _parse_schema(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        ssl_mode = d.pop("ssl_mode", UNSET)

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

        postgre_sql_config = cls(
            credentials=credentials,
            host=host,
            database=database,
            provider_type=provider_type,
            port=port,
            schema=schema,
            ssl_mode=ssl_mode,
            incremental_column=incremental_column,
            primary_key_columns=primary_key_columns,
            query_timeout_seconds=query_timeout_seconds,
            fetch_size=fetch_size,
        )

        postgre_sql_config.additional_properties = d
        return postgre_sql_config

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
