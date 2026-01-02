from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.retriever_status import RetrieverStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cache_config import CacheConfig
    from ..models.collection_detail import CollectionDetail
    from ..models.creator_info import CreatorInfo
    from ..models.health_check import HealthCheck
    from ..models.retriever_model_metadata import RetrieverModelMetadata
    from ..models.retriever_schema import RetrieverSchema
    from ..models.revision_history_entry import RevisionHistoryEntry
    from ..models.stage_instance_config import StageInstanceConfig
    from ..models.usage_statistics import UsageStatistics


T = TypeVar("T", bound="RetrieverModel")


@_attrs_define
class RetrieverModel:
    """Retriever model.

    Attributes:
        retriever_name (str): Name of the retriever
        input_schema (RetrieverSchema): Schema definition for retriever inputs.
        collection_ids (list[str]): List of collection IDs
        stages (list[StageInstanceConfig]): List of stage configurations
        retriever_id (str | Unset): Unique identifier for the retriever
        description (None | str | Unset): Description of the retriever
        cache_config (CacheConfig | None | Unset): Cache configuration for this retriever. If not provided, caching is
            disabled.
        created_at (datetime.datetime | Unset): When the retriever was created
        updated_at (datetime.datetime | Unset): When the retriever was last modified
        last_executed_at (datetime.datetime | None | Unset): When the retriever was last executed
        enabled (bool | Unset): Whether the retriever is enabled (can be toggled on/off) Default: True.
        status (RetrieverStatus | Unset): Status of a retriever.
        usage_stats (None | Unset | UsageStatistics): Usage and performance statistics
        collections (list[CollectionDetail] | None | Unset): Expanded collection details with names and metadata
        metadata (RetrieverModelMetadata | Unset): Custom key-value metadata
        tags (list[str] | Unset): Tags for organization and filtering
        created_by (CreatorInfo | None | Unset): Information about who created this retriever
        updated_by (CreatorInfo | None | Unset): Information about who last updated this retriever
        version (int | Unset): Version number (increments on each update) Default: 1.
        revision_history (list[RevisionHistoryEntry] | Unset): History of changes (optional, last N changes)
        health (HealthCheck | None | Unset): Health status and diagnostics
    """

    retriever_name: str
    input_schema: RetrieverSchema
    collection_ids: list[str]
    stages: list[StageInstanceConfig]
    retriever_id: str | Unset = UNSET
    description: None | str | Unset = UNSET
    cache_config: CacheConfig | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    last_executed_at: datetime.datetime | None | Unset = UNSET
    enabled: bool | Unset = True
    status: RetrieverStatus | Unset = UNSET
    usage_stats: None | Unset | UsageStatistics = UNSET
    collections: list[CollectionDetail] | None | Unset = UNSET
    metadata: RetrieverModelMetadata | Unset = UNSET
    tags: list[str] | Unset = UNSET
    created_by: CreatorInfo | None | Unset = UNSET
    updated_by: CreatorInfo | None | Unset = UNSET
    version: int | Unset = 1
    revision_history: list[RevisionHistoryEntry] | Unset = UNSET
    health: HealthCheck | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cache_config import CacheConfig
        from ..models.creator_info import CreatorInfo
        from ..models.health_check import HealthCheck
        from ..models.usage_statistics import UsageStatistics

        retriever_name = self.retriever_name

        input_schema = self.input_schema.to_dict()

        collection_ids = self.collection_ids

        stages = []
        for stages_item_data in self.stages:
            stages_item = stages_item_data.to_dict()
            stages.append(stages_item)

        retriever_id = self.retriever_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        cache_config: dict[str, Any] | None | Unset
        if isinstance(self.cache_config, Unset):
            cache_config = UNSET
        elif isinstance(self.cache_config, CacheConfig):
            cache_config = self.cache_config.to_dict()
        else:
            cache_config = self.cache_config

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        last_executed_at: None | str | Unset
        if isinstance(self.last_executed_at, Unset):
            last_executed_at = UNSET
        elif isinstance(self.last_executed_at, datetime.datetime):
            last_executed_at = self.last_executed_at.isoformat()
        else:
            last_executed_at = self.last_executed_at

        enabled = self.enabled

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        usage_stats: dict[str, Any] | None | Unset
        if isinstance(self.usage_stats, Unset):
            usage_stats = UNSET
        elif isinstance(self.usage_stats, UsageStatistics):
            usage_stats = self.usage_stats.to_dict()
        else:
            usage_stats = self.usage_stats

        collections: list[dict[str, Any]] | None | Unset
        if isinstance(self.collections, Unset):
            collections = UNSET
        elif isinstance(self.collections, list):
            collections = []
            for collections_type_0_item_data in self.collections:
                collections_type_0_item = collections_type_0_item_data.to_dict()
                collections.append(collections_type_0_item)

        else:
            collections = self.collections

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        created_by: dict[str, Any] | None | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, CreatorInfo):
            created_by = self.created_by.to_dict()
        else:
            created_by = self.created_by

        updated_by: dict[str, Any] | None | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, CreatorInfo):
            updated_by = self.updated_by.to_dict()
        else:
            updated_by = self.updated_by

        version = self.version

        revision_history: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.revision_history, Unset):
            revision_history = []
            for revision_history_item_data in self.revision_history:
                revision_history_item = revision_history_item_data.to_dict()
                revision_history.append(revision_history_item)

        health: dict[str, Any] | None | Unset
        if isinstance(self.health, Unset):
            health = UNSET
        elif isinstance(self.health, HealthCheck):
            health = self.health.to_dict()
        else:
            health = self.health

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "retriever_name": retriever_name,
                "input_schema": input_schema,
                "collection_ids": collection_ids,
                "stages": stages,
            }
        )
        if retriever_id is not UNSET:
            field_dict["retriever_id"] = retriever_id
        if description is not UNSET:
            field_dict["description"] = description
        if cache_config is not UNSET:
            field_dict["cache_config"] = cache_config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if last_executed_at is not UNSET:
            field_dict["last_executed_at"] = last_executed_at
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if status is not UNSET:
            field_dict["status"] = status
        if usage_stats is not UNSET:
            field_dict["usage_stats"] = usage_stats
        if collections is not UNSET:
            field_dict["collections"] = collections
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tags is not UNSET:
            field_dict["tags"] = tags
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if version is not UNSET:
            field_dict["version"] = version
        if revision_history is not UNSET:
            field_dict["revision_history"] = revision_history
        if health is not UNSET:
            field_dict["health"] = health

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cache_config import CacheConfig
        from ..models.collection_detail import CollectionDetail
        from ..models.creator_info import CreatorInfo
        from ..models.health_check import HealthCheck
        from ..models.retriever_model_metadata import RetrieverModelMetadata
        from ..models.retriever_schema import RetrieverSchema
        from ..models.revision_history_entry import RevisionHistoryEntry
        from ..models.stage_instance_config import StageInstanceConfig
        from ..models.usage_statistics import UsageStatistics

        d = dict(src_dict)
        retriever_name = d.pop("retriever_name")

        input_schema = RetrieverSchema.from_dict(d.pop("input_schema"))

        collection_ids = cast(list[str], d.pop("collection_ids"))

        stages = []
        _stages = d.pop("stages")
        for stages_item_data in _stages:
            stages_item = StageInstanceConfig.from_dict(stages_item_data)

            stages.append(stages_item)

        retriever_id = d.pop("retriever_id", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_cache_config(data: object) -> CacheConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cache_config_type_0 = CacheConfig.from_dict(data)

                return cache_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CacheConfig | None | Unset, data)

        cache_config = _parse_cache_config(d.pop("cache_config", UNSET))

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

        def _parse_last_executed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_executed_at_type_0 = isoparse(data)

                return last_executed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_executed_at = _parse_last_executed_at(d.pop("last_executed_at", UNSET))

        enabled = d.pop("enabled", UNSET)

        _status = d.pop("status", UNSET)
        status: RetrieverStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RetrieverStatus(_status)

        def _parse_usage_stats(data: object) -> None | Unset | UsageStatistics:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                usage_stats_type_0 = UsageStatistics.from_dict(data)

                return usage_stats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UsageStatistics, data)

        usage_stats = _parse_usage_stats(d.pop("usage_stats", UNSET))

        def _parse_collections(data: object) -> list[CollectionDetail] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collections_type_0 = []
                _collections_type_0 = data
                for collections_type_0_item_data in _collections_type_0:
                    collections_type_0_item = CollectionDetail.from_dict(collections_type_0_item_data)

                    collections_type_0.append(collections_type_0_item)

                return collections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CollectionDetail] | None | Unset, data)

        collections = _parse_collections(d.pop("collections", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: RetrieverModelMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = RetrieverModelMetadata.from_dict(_metadata)

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_created_by(data: object) -> CreatorInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_type_0 = CreatorInfo.from_dict(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreatorInfo | None | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> CreatorInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_by_type_0 = CreatorInfo.from_dict(data)

                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreatorInfo | None | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        version = d.pop("version", UNSET)

        _revision_history = d.pop("revision_history", UNSET)
        revision_history: list[RevisionHistoryEntry] | Unset = UNSET
        if _revision_history is not UNSET:
            revision_history = []
            for revision_history_item_data in _revision_history:
                revision_history_item = RevisionHistoryEntry.from_dict(revision_history_item_data)

                revision_history.append(revision_history_item)

        def _parse_health(data: object) -> HealthCheck | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                health_type_0 = HealthCheck.from_dict(data)

                return health_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HealthCheck | None | Unset, data)

        health = _parse_health(d.pop("health", UNSET))

        retriever_model = cls(
            retriever_name=retriever_name,
            input_schema=input_schema,
            collection_ids=collection_ids,
            stages=stages,
            retriever_id=retriever_id,
            description=description,
            cache_config=cache_config,
            created_at=created_at,
            updated_at=updated_at,
            last_executed_at=last_executed_at,
            enabled=enabled,
            status=status,
            usage_stats=usage_stats,
            collections=collections,
            metadata=metadata,
            tags=tags,
            created_by=created_by,
            updated_by=updated_by,
            version=version,
            revision_history=revision_history,
            health=health,
        )

        retriever_model.additional_properties = d
        return retriever_model

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
