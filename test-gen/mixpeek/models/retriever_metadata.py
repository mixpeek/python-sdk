from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retriever_metadata_capabilities import RetrieverMetadataCapabilities
    from ..models.retriever_metadata_collections_item import RetrieverMetadataCollectionsItem
    from ..models.retriever_metadata_stages_item import RetrieverMetadataStagesItem


T = TypeVar("T", bound="RetrieverMetadata")


@_attrs_define
class RetrieverMetadata:
    """Metadata explaining how the retriever works.

    This is separate from DisplayConfig and provides technical information
    about the retriever's architecture for developers/debugging.

        Attributes:
            stages (list[RetrieverMetadataStagesItem] | Unset): Pipeline stages used in this retriever
            collections (list[RetrieverMetadataCollectionsItem] | Unset): Collections and feature extractors used
            capabilities (RetrieverMetadataCapabilities | Unset): Capabilities and features of this retriever
    """

    stages: list[RetrieverMetadataStagesItem] | Unset = UNSET
    collections: list[RetrieverMetadataCollectionsItem] | Unset = UNSET
    capabilities: RetrieverMetadataCapabilities | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.to_dict()
                stages.append(stages_item)

        collections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.collections, Unset):
            collections = []
            for collections_item_data in self.collections:
                collections_item = collections_item_data.to_dict()
                collections.append(collections_item)

        capabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stages is not UNSET:
            field_dict["stages"] = stages
        if collections is not UNSET:
            field_dict["collections"] = collections
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retriever_metadata_capabilities import RetrieverMetadataCapabilities
        from ..models.retriever_metadata_collections_item import RetrieverMetadataCollectionsItem
        from ..models.retriever_metadata_stages_item import RetrieverMetadataStagesItem

        d = dict(src_dict)
        _stages = d.pop("stages", UNSET)
        stages: list[RetrieverMetadataStagesItem] | Unset = UNSET
        if _stages is not UNSET:
            stages = []
            for stages_item_data in _stages:
                stages_item = RetrieverMetadataStagesItem.from_dict(stages_item_data)

                stages.append(stages_item)

        _collections = d.pop("collections", UNSET)
        collections: list[RetrieverMetadataCollectionsItem] | Unset = UNSET
        if _collections is not UNSET:
            collections = []
            for collections_item_data in _collections:
                collections_item = RetrieverMetadataCollectionsItem.from_dict(collections_item_data)

                collections.append(collections_item)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: RetrieverMetadataCapabilities | Unset
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = RetrieverMetadataCapabilities.from_dict(_capabilities)

        retriever_metadata = cls(
            stages=stages,
            collections=collections,
            capabilities=capabilities,
        )

        retriever_metadata.additional_properties = d
        return retriever_metadata

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
