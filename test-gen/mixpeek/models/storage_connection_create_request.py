from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.storage_provider import StorageProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_connection_create_request_metadata_type_0 import StorageConnectionCreateRequestMetadataType0
    from ..models.storage_connection_create_request_provider_config import StorageConnectionCreateRequestProviderConfig


T = TypeVar("T", bound="StorageConnectionCreateRequest")


@_attrs_define
class StorageConnectionCreateRequest:
    """Request payload for creating a new storage connection.

    Use this to connect Mixpeek to external storage providers like Google Drive
    or S3. The connection will be tested before being saved (unless
    test_before_save is False).

    **Use Cases:**
    - Connect to team Google Drive for automated file ingestion
    - Link customer S3 buckets for batch processing
    - Set up storage connections for sync operations

    **Security:**
    - Credentials are encrypted at rest using MongoDB field-level encryption
    - Credentials never appear in API responses or logs
    - Connection is tested before saving to validate credentials

    **Examples:**
    ```python
    # Google Drive connection
    {
        "name": "Marketing Drive",
        "provider_type": "google_drive",
        "provider_config": {
            "credentials": {...},
            "shared_drive_id": "0AH-Xabc123"
        },
        "description": "Team drive for marketing assets"
    }
    ```

        Attributes:
            name (str): REQUIRED. Human-readable name for the storage connection. Must be unique within the organization.
                Displayed in dashboards and sync logs. Format: 1-100 characters, descriptive of the connection's purpose.
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
            provider_config (StorageConnectionCreateRequestProviderConfig): REQUIRED. Provider-specific configuration
                including credentials. Structure varies by provider_type. SECURITY: Sensitive credential fields (private_key,
                secret_access_key, client_secret, refresh_token, session_token) are automatically encrypted at rest and never
                appear in responses or logs.
            description (None | str | Unset): OPTIONAL. Description explaining the connection's purpose and scope. Helpful
                for team collaboration and documentation. Format: Up to 500 characters.
            metadata (None | StorageConnectionCreateRequestMetadataType0 | Unset): OPTIONAL. Arbitrary key-value metadata
                for tagging and categorization. Common uses: team tags, cost center codes, project identifiers.
            test_before_save (bool | Unset): OPTIONAL. Whether to validate credentials before saving the connection.
                Defaults to True. If True, connection will be tested against the provider before creation. If False, connection
                is saved without validation (use with caution). Default: True.
    """

    name: str
    provider_type: StorageProvider
    provider_config: StorageConnectionCreateRequestProviderConfig
    description: None | str | Unset = UNSET
    metadata: None | StorageConnectionCreateRequestMetadataType0 | Unset = UNSET
    test_before_save: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.storage_connection_create_request_metadata_type_0 import (
            StorageConnectionCreateRequestMetadataType0,
        )

        name = self.name

        provider_type = self.provider_type.value

        provider_config = self.provider_config.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, StorageConnectionCreateRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        test_before_save = self.test_before_save

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "provider_type": provider_type,
                "provider_config": provider_config,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if test_before_save is not UNSET:
            field_dict["test_before_save"] = test_before_save

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_connection_create_request_metadata_type_0 import (
            StorageConnectionCreateRequestMetadataType0,
        )
        from ..models.storage_connection_create_request_provider_config import (
            StorageConnectionCreateRequestProviderConfig,
        )

        d = dict(src_dict)
        name = d.pop("name")

        provider_type = StorageProvider(d.pop("provider_type"))

        provider_config = StorageConnectionCreateRequestProviderConfig.from_dict(d.pop("provider_config"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_metadata(data: object) -> None | StorageConnectionCreateRequestMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = StorageConnectionCreateRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StorageConnectionCreateRequestMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        test_before_save = d.pop("test_before_save", UNSET)

        storage_connection_create_request = cls(
            name=name,
            provider_type=provider_type,
            provider_config=provider_config,
            description=description,
            metadata=metadata,
            test_before_save=test_before_save,
        )

        storage_connection_create_request.additional_properties = d
        return storage_connection_create_request

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
