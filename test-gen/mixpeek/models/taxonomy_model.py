from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flat_taxonomy_config import FlatTaxonomyConfig
    from ..models.hierarchical_taxonomy_config import HierarchicalTaxonomyConfig
    from ..models.input_mapping import InputMapping
    from ..models.taxonomy_model_metadata import TaxonomyModelMetadata


T = TypeVar("T", bound="TaxonomyModel")


@_attrs_define
class TaxonomyModel:
    """Primary Pydantic model representing a taxonomy definition.

    Attributes:
        taxonomy_name (str): A unique name for the taxonomy within the namespace.
        config (FlatTaxonomyConfig | HierarchicalTaxonomyConfig): Configuration specific to the taxonomy type.
        taxonomy_id (str | Unset): Unique identifier for the taxonomy
        version (int | Unset): Monotonic version number of the taxonomy configuration Default: 1.
        description (None | str | Unset): Optional human-readable description.
        retriever_id (None | str | Unset): Optional taxonomy-level retriever (prefer per-layer).
        input_mappings (list[InputMapping] | None | Unset): Optional taxonomy-level inputs (prefer per-layer).
        ready (bool | Unset): Whether the taxonomy is ready for use. False for async inference (cluster/LLM) that needs
            processing. True for flat/explicit hierarchies. Default: True.
        created_at (datetime.datetime | Unset): Creation timestamp for this taxonomy record
        metadata (TaxonomyModelMetadata | Unset): Additional user-defined metadata for the taxonomy
    """

    taxonomy_name: str
    config: FlatTaxonomyConfig | HierarchicalTaxonomyConfig
    taxonomy_id: str | Unset = UNSET
    version: int | Unset = 1
    description: None | str | Unset = UNSET
    retriever_id: None | str | Unset = UNSET
    input_mappings: list[InputMapping] | None | Unset = UNSET
    ready: bool | Unset = True
    created_at: datetime.datetime | Unset = UNSET
    metadata: TaxonomyModelMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.flat_taxonomy_config import FlatTaxonomyConfig

        taxonomy_name = self.taxonomy_name

        config: dict[str, Any]
        if isinstance(self.config, FlatTaxonomyConfig):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()

        taxonomy_id = self.taxonomy_id

        version = self.version

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        retriever_id: None | str | Unset
        if isinstance(self.retriever_id, Unset):
            retriever_id = UNSET
        else:
            retriever_id = self.retriever_id

        input_mappings: list[dict[str, Any]] | None | Unset
        if isinstance(self.input_mappings, Unset):
            input_mappings = UNSET
        elif isinstance(self.input_mappings, list):
            input_mappings = []
            for input_mappings_type_0_item_data in self.input_mappings:
                input_mappings_type_0_item = input_mappings_type_0_item_data.to_dict()
                input_mappings.append(input_mappings_type_0_item)

        else:
            input_mappings = self.input_mappings

        ready = self.ready

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taxonomy_name": taxonomy_name,
                "config": config,
            }
        )
        if taxonomy_id is not UNSET:
            field_dict["taxonomy_id"] = taxonomy_id
        if version is not UNSET:
            field_dict["version"] = version
        if description is not UNSET:
            field_dict["description"] = description
        if retriever_id is not UNSET:
            field_dict["retriever_id"] = retriever_id
        if input_mappings is not UNSET:
            field_dict["input_mappings"] = input_mappings
        if ready is not UNSET:
            field_dict["ready"] = ready
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flat_taxonomy_config import FlatTaxonomyConfig
        from ..models.hierarchical_taxonomy_config import HierarchicalTaxonomyConfig
        from ..models.input_mapping import InputMapping
        from ..models.taxonomy_model_metadata import TaxonomyModelMetadata

        d = dict(src_dict)
        taxonomy_name = d.pop("taxonomy_name")

        def _parse_config(data: object) -> FlatTaxonomyConfig | HierarchicalTaxonomyConfig:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = FlatTaxonomyConfig.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            config_type_1 = HierarchicalTaxonomyConfig.from_dict(data)

            return config_type_1

        config = _parse_config(d.pop("config"))

        taxonomy_id = d.pop("taxonomy_id", UNSET)

        version = d.pop("version", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_retriever_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retriever_id = _parse_retriever_id(d.pop("retriever_id", UNSET))

        def _parse_input_mappings(data: object) -> list[InputMapping] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                input_mappings_type_0 = []
                _input_mappings_type_0 = data
                for input_mappings_type_0_item_data in _input_mappings_type_0:
                    input_mappings_type_0_item = InputMapping.from_dict(input_mappings_type_0_item_data)

                    input_mappings_type_0.append(input_mappings_type_0_item)

                return input_mappings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InputMapping] | None | Unset, data)

        input_mappings = _parse_input_mappings(d.pop("input_mappings", UNSET))

        ready = d.pop("ready", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _metadata = d.pop("metadata", UNSET)
        metadata: TaxonomyModelMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = TaxonomyModelMetadata.from_dict(_metadata)

        taxonomy_model = cls(
            taxonomy_name=taxonomy_name,
            config=config,
            taxonomy_id=taxonomy_id,
            version=version,
            description=description,
            retriever_id=retriever_id,
            input_mappings=input_mappings,
            ready=ready,
            created_at=created_at,
            metadata=metadata,
        )

        taxonomy_model.additional_properties = d
        return taxonomy_model

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
