from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_mode import SyncMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_mapping import SchemaMapping
    from ..models.sync_create_request_file_filters_type_0 import SyncCreateRequestFileFiltersType0
    from ..models.sync_create_request_metadata_type_0 import SyncCreateRequestMetadataType0


T = TypeVar("T", bound="SyncCreateRequest")


@_attrs_define
class SyncCreateRequest:
    """Request to create a bucket sync configuration.

    Establishes automated synchronization between a storage connection and a bucket.
    The sync monitors the source path for changes and ingests files according to
    the specified mode and filters.

    Supported Storage Providers:
        - google_drive: Google Drive and Workspace shared drives
        - s3: Amazon S3 and S3-compatible (MinIO, DigitalOcean Spaces, Wasabi)
        - snowflake: Snowflake data warehouse tables (rows become objects)
        - sharepoint: Microsoft SharePoint and OneDrive for Business
        - tigris: Tigris globally distributed object storage

    Robustness Features (built-in):
        - Dead Letter Queue (DLQ): Failed objects tracked with 3 retries before quarantine
        - Idempotent ingestion: Deduplication via (bucket_id, source_provider, source_object_id)
        - Distributed locking: Prevents concurrent execution of same sync config
        - Rate limit handling: Automatic backoff on provider 429 responses
        - Metrics: Duration, files synced/failed, batches created, rate limit hits

    Sync Modes:
        - continuous: Real-time monitoring with polling interval
        - one_time: Single bulk import then stops
        - scheduled: Polling-based batch imports

    Requirements:
        - connection_id: REQUIRED, must be an existing connection
        - source_path: REQUIRED, path must exist in the storage provider
        - sync_mode: OPTIONAL, defaults to 'continuous'
        - All other fields are OPTIONAL with sensible defaults

        Attributes:
            connection_id (str): REQUIRED. Storage connection identifier to sync from. Must reference an existing connection
                created via POST /organizations/connections. The connection defines the storage provider and credentials.
                Supported providers: google_drive, s3, snowflake, sharepoint, tigris.
            source_path (str): REQUIRED. Source path within the storage provider to monitor and sync. Path format varies by
                provider: - s3/tigris: 'bucket-name/prefix' or 'bucket-name'. - google_drive: folder ID or path like
                '/Marketing/Assets'. - sharepoint: '/sites/SiteName/Shared Documents/folder'. - snowflake:
                'DATABASE.SCHEMA.TABLE' or just 'TABLE' if defaults set.
            sync_mode (SyncMode | Unset): Supported sync modes for external storage ingestion.
            file_filters (None | SyncCreateRequestFileFiltersType0 | Unset): OPTIONAL. Filters to control which files are
                synced. When omitted, all files in source_path are synced. Supported filters: - include_patterns: Glob patterns
                to include (e.g., ['*.mp4', '*.mov']). - exclude_patterns: Glob patterns to exclude (e.g., ['*.tmp',
                '.DS_Store']). - extensions: File extensions to include (e.g., ['.mp4', '.jpg']). - min_size_bytes: Minimum file
                size in bytes. - max_size_bytes: Maximum file size in bytes. - modified_after: ISO datetime, only sync files
                modified after this time. - mime_types: List of MIME types to include (e.g., ['video/*', 'image/jpeg']).
            schema_mapping (None | SchemaMapping | Unset): OPTIONAL. Defines how source data maps to bucket schema fields
                and blobs. When provided, enables structured extraction of metadata from the sync source. Keys are target bucket
                schema field names, values define the source extraction method.

                **Blob Mappings** (target_type='blob'): Map files or URLs to blob fields. Use source.type='file' for the synced
                file itself, or source.type='column'/'metadata' for URLs.

                **Field Mappings** (target_type='field'): Map metadata to schema fields. Source options by provider: -
                S3/Tigris: 'tag' (object tags), 'metadata' (x-amz-meta-*) - Snowflake: 'column' (table columns) - Google Drive:
                'drive_property' (file properties) - All: 'filename_regex', 'folder_path', 'constant'

                If omitted, default behavior depends on provider - typically maps file to 'content' blob.
            polling_interval_seconds (int | Unset): Interval in seconds between polling checks for new files. OPTIONAL.
                Defaults to 300 seconds (5 minutes). Must be between 30 and 900 seconds (0.5 to 15 minutes). Only applies to
                'continuous' and 'scheduled' sync modes. Lower values mean faster detection but higher API usage. Default: 300.
            batch_size (int | Unset): Number of files to process in each batch during sync. OPTIONAL. Defaults to 50 files
                per batch. Must be between 1 and 100. Larger batches improve throughput but require more memory. Smaller batches
                provide more granular progress tracking. Default: 50.
            skip_batch_submission (bool | Unset): If True, sync objects to the bucket without creating or submitting batches
                for collection processing. Objects are created in the bucket but no tier processing is triggered. Useful for
                bulk data migration or when you want to manually control when processing occurs. OPTIONAL. Defaults to False
                (batches are created and submitted). Default: False.
            metadata (None | SyncCreateRequestMetadataType0 | Unset): Optional custom metadata to attach to the sync
                configuration. NOT REQUIRED. Arbitrary key-value pairs for tagging and organization. Common uses: project tags,
                environment labels, cost centers. Maximum 50 keys, values must be JSON-serializable.
    """

    connection_id: str
    source_path: str
    sync_mode: SyncMode | Unset = UNSET
    file_filters: None | SyncCreateRequestFileFiltersType0 | Unset = UNSET
    schema_mapping: None | SchemaMapping | Unset = UNSET
    polling_interval_seconds: int | Unset = 300
    batch_size: int | Unset = 50
    skip_batch_submission: bool | Unset = False
    metadata: None | SyncCreateRequestMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.schema_mapping import SchemaMapping
        from ..models.sync_create_request_file_filters_type_0 import SyncCreateRequestFileFiltersType0
        from ..models.sync_create_request_metadata_type_0 import SyncCreateRequestMetadataType0

        connection_id = self.connection_id

        source_path = self.source_path

        sync_mode: str | Unset = UNSET
        if not isinstance(self.sync_mode, Unset):
            sync_mode = self.sync_mode.value

        file_filters: dict[str, Any] | None | Unset
        if isinstance(self.file_filters, Unset):
            file_filters = UNSET
        elif isinstance(self.file_filters, SyncCreateRequestFileFiltersType0):
            file_filters = self.file_filters.to_dict()
        else:
            file_filters = self.file_filters

        schema_mapping: dict[str, Any] | None | Unset
        if isinstance(self.schema_mapping, Unset):
            schema_mapping = UNSET
        elif isinstance(self.schema_mapping, SchemaMapping):
            schema_mapping = self.schema_mapping.to_dict()
        else:
            schema_mapping = self.schema_mapping

        polling_interval_seconds = self.polling_interval_seconds

        batch_size = self.batch_size

        skip_batch_submission = self.skip_batch_submission

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, SyncCreateRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection_id": connection_id,
                "source_path": source_path,
            }
        )
        if sync_mode is not UNSET:
            field_dict["sync_mode"] = sync_mode
        if file_filters is not UNSET:
            field_dict["file_filters"] = file_filters
        if schema_mapping is not UNSET:
            field_dict["schema_mapping"] = schema_mapping
        if polling_interval_seconds is not UNSET:
            field_dict["polling_interval_seconds"] = polling_interval_seconds
        if batch_size is not UNSET:
            field_dict["batch_size"] = batch_size
        if skip_batch_submission is not UNSET:
            field_dict["skip_batch_submission"] = skip_batch_submission
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schema_mapping import SchemaMapping
        from ..models.sync_create_request_file_filters_type_0 import SyncCreateRequestFileFiltersType0
        from ..models.sync_create_request_metadata_type_0 import SyncCreateRequestMetadataType0

        d = dict(src_dict)
        connection_id = d.pop("connection_id")

        source_path = d.pop("source_path")

        _sync_mode = d.pop("sync_mode", UNSET)
        sync_mode: SyncMode | Unset
        if isinstance(_sync_mode, Unset):
            sync_mode = UNSET
        else:
            sync_mode = SyncMode(_sync_mode)

        def _parse_file_filters(data: object) -> None | SyncCreateRequestFileFiltersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                file_filters_type_0 = SyncCreateRequestFileFiltersType0.from_dict(data)

                return file_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SyncCreateRequestFileFiltersType0 | Unset, data)

        file_filters = _parse_file_filters(d.pop("file_filters", UNSET))

        def _parse_schema_mapping(data: object) -> None | SchemaMapping | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schema_mapping_type_0 = SchemaMapping.from_dict(data)

                return schema_mapping_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SchemaMapping | Unset, data)

        schema_mapping = _parse_schema_mapping(d.pop("schema_mapping", UNSET))

        polling_interval_seconds = d.pop("polling_interval_seconds", UNSET)

        batch_size = d.pop("batch_size", UNSET)

        skip_batch_submission = d.pop("skip_batch_submission", UNSET)

        def _parse_metadata(data: object) -> None | SyncCreateRequestMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SyncCreateRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SyncCreateRequestMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        sync_create_request = cls(
            connection_id=connection_id,
            source_path=source_path,
            sync_mode=sync_mode,
            file_filters=file_filters,
            schema_mapping=schema_mapping,
            polling_interval_seconds=polling_interval_seconds,
            batch_size=batch_size,
            skip_batch_submission=skip_batch_submission,
            metadata=metadata,
        )

        sync_create_request.additional_properties = d
        return sync_create_request

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
