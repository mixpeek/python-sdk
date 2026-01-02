from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payload_index_config import PayloadIndexConfig


T = TypeVar("T", bound="PatchNamespaceRequest")


@_attrs_define
class PatchNamespaceRequest:
    """Request schema for partially updating a namespace (PATCH operation).

    Attributes:
        namespace_name (None | str | Unset): Updated name for the namespace Example: spotify_playlists_prod.
        description (None | str | Unset): Updated description for the namespace
        payload_indexes (list[PayloadIndexConfig] | None | Unset): Updated list of custom payload indexes for this
            namespace.
        auto_create_indexes (bool | None | Unset): Enable automatic creation of Qdrant payload indexes based on filter
            usage patterns. When enabled, the system tracks which fields are most frequently filtered (>100 queries/24h) and
            automatically creates indexes to improve query performance. Background task runs every 6 hours. Expected
            performance improvement: 50-90% latency reduction for filtered queries. Default: False. Example: True.
    """

    namespace_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    payload_indexes: list[PayloadIndexConfig] | None | Unset = UNSET
    auto_create_indexes: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace_name: None | str | Unset
        if isinstance(self.namespace_name, Unset):
            namespace_name = UNSET
        else:
            namespace_name = self.namespace_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        payload_indexes: list[dict[str, Any]] | None | Unset
        if isinstance(self.payload_indexes, Unset):
            payload_indexes = UNSET
        elif isinstance(self.payload_indexes, list):
            payload_indexes = []
            for payload_indexes_type_0_item_data in self.payload_indexes:
                payload_indexes_type_0_item = payload_indexes_type_0_item_data.to_dict()
                payload_indexes.append(payload_indexes_type_0_item)

        else:
            payload_indexes = self.payload_indexes

        auto_create_indexes: bool | None | Unset
        if isinstance(self.auto_create_indexes, Unset):
            auto_create_indexes = UNSET
        else:
            auto_create_indexes = self.auto_create_indexes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if namespace_name is not UNSET:
            field_dict["namespace_name"] = namespace_name
        if description is not UNSET:
            field_dict["description"] = description
        if payload_indexes is not UNSET:
            field_dict["payload_indexes"] = payload_indexes
        if auto_create_indexes is not UNSET:
            field_dict["auto_create_indexes"] = auto_create_indexes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payload_index_config import PayloadIndexConfig

        d = dict(src_dict)

        def _parse_namespace_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace_name = _parse_namespace_name(d.pop("namespace_name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_payload_indexes(data: object) -> list[PayloadIndexConfig] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payload_indexes_type_0 = []
                _payload_indexes_type_0 = data
                for payload_indexes_type_0_item_data in _payload_indexes_type_0:
                    payload_indexes_type_0_item = PayloadIndexConfig.from_dict(payload_indexes_type_0_item_data)

                    payload_indexes_type_0.append(payload_indexes_type_0_item)

                return payload_indexes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PayloadIndexConfig] | None | Unset, data)

        payload_indexes = _parse_payload_indexes(d.pop("payload_indexes", UNSET))

        def _parse_auto_create_indexes(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_create_indexes = _parse_auto_create_indexes(d.pop("auto_create_indexes", UNSET))

        patch_namespace_request = cls(
            namespace_name=namespace_name,
            description=description,
            payload_indexes=payload_indexes,
            auto_create_indexes=auto_create_indexes,
        )

        patch_namespace_request.additional_properties = d
        return patch_namespace_request

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
