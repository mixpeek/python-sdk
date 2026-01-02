from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clone_collection_request_metadata_type_0 import CloneCollectionRequestMetadataType0
    from ..models.feature_extractor_config import FeatureExtractorConfig
    from ..models.source_config import SourceConfig
    from ..models.taxonomy_application_config import TaxonomyApplicationConfig


T = TypeVar("T", bound="CloneCollectionRequest")


@_attrs_define
class CloneCollectionRequest:
    """Request to clone a collection with optional modifications.

    **Purpose:**
    Cloning creates a NEW collection (with new ID) based on an existing one,
    allowing you to make changes that aren't allowed via PATCH (source,
    feature_extractor, field_passthrough). This is the recommended way to
    iterate on collection designs.

    **Clone vs Template vs Version:**
    - **Clone**: Copy THIS collection and modify it (for iteration/fixes)
    - **Template**: Create collection from a reusable pattern (for new projects)
    - **Version**: (Not implemented) - Use clone instead

    **Use Cases:**
    - Change feature extractor configuration without breaking production
    - Modify field_passthrough to include/exclude fields
    - Switch to different source (bucket or collection)
    - Test modifications before replacing production collection
    - Create variants (e.g., different embedding models)

    **All fields are OPTIONAL:**
    - Omit a field to keep the original value
    - Provide a field to override the original value
    - collection_name is REQUIRED (clones must have unique names)

        Attributes:
            collection_name (str): REQUIRED. Name for the cloned collection. Must be unique and different from the source
                collection.
            description (None | str | Unset): OPTIONAL. Description override. If omitted, copies from source collection.
            source (None | SourceConfig | Unset): OPTIONAL. Override source configuration. If omitted, copies from source
                collection. Allows switching between buckets or collections.
            feature_extractor (FeatureExtractorConfig | None | Unset): OPTIONAL. Override feature extractor configuration.
                If omitted, copies from source collection. This is where you'd change models, parameters, or field_passthrough.
            enabled (bool | None | Unset): OPTIONAL. Override enabled status. If omitted, copies from source collection.
            metadata (CloneCollectionRequestMetadataType0 | None | Unset): OPTIONAL. Override metadata. If omitted, copies
                from source collection.
            taxonomy_applications (list[TaxonomyApplicationConfig] | None | Unset): OPTIONAL. Override taxonomy
                applications. If omitted, copies from source collection.
    """

    collection_name: str
    description: None | str | Unset = UNSET
    source: None | SourceConfig | Unset = UNSET
    feature_extractor: FeatureExtractorConfig | None | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    metadata: CloneCollectionRequestMetadataType0 | None | Unset = UNSET
    taxonomy_applications: list[TaxonomyApplicationConfig] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.clone_collection_request_metadata_type_0 import CloneCollectionRequestMetadataType0
        from ..models.feature_extractor_config import FeatureExtractorConfig
        from ..models.source_config import SourceConfig

        collection_name = self.collection_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        source: dict[str, Any] | None | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, SourceConfig):
            source = self.source.to_dict()
        else:
            source = self.source

        feature_extractor: dict[str, Any] | None | Unset
        if isinstance(self.feature_extractor, Unset):
            feature_extractor = UNSET
        elif isinstance(self.feature_extractor, FeatureExtractorConfig):
            feature_extractor = self.feature_extractor.to_dict()
        else:
            feature_extractor = self.feature_extractor

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CloneCollectionRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        taxonomy_applications: list[dict[str, Any]] | None | Unset
        if isinstance(self.taxonomy_applications, Unset):
            taxonomy_applications = UNSET
        elif isinstance(self.taxonomy_applications, list):
            taxonomy_applications = []
            for taxonomy_applications_type_0_item_data in self.taxonomy_applications:
                taxonomy_applications_type_0_item = taxonomy_applications_type_0_item_data.to_dict()
                taxonomy_applications.append(taxonomy_applications_type_0_item)

        else:
            taxonomy_applications = self.taxonomy_applications

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_name": collection_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if source is not UNSET:
            field_dict["source"] = source
        if feature_extractor is not UNSET:
            field_dict["feature_extractor"] = feature_extractor
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if taxonomy_applications is not UNSET:
            field_dict["taxonomy_applications"] = taxonomy_applications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clone_collection_request_metadata_type_0 import CloneCollectionRequestMetadataType0
        from ..models.feature_extractor_config import FeatureExtractorConfig
        from ..models.source_config import SourceConfig
        from ..models.taxonomy_application_config import TaxonomyApplicationConfig

        d = dict(src_dict)
        collection_name = d.pop("collection_name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_source(data: object) -> None | SourceConfig | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_0 = SourceConfig.from_dict(data)

                return source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SourceConfig | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_feature_extractor(data: object) -> FeatureExtractorConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feature_extractor_type_0 = FeatureExtractorConfig.from_dict(data)

                return feature_extractor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FeatureExtractorConfig | None | Unset, data)

        feature_extractor = _parse_feature_extractor(d.pop("feature_extractor", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_metadata(data: object) -> CloneCollectionRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CloneCollectionRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CloneCollectionRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_taxonomy_applications(data: object) -> list[TaxonomyApplicationConfig] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                taxonomy_applications_type_0 = []
                _taxonomy_applications_type_0 = data
                for taxonomy_applications_type_0_item_data in _taxonomy_applications_type_0:
                    taxonomy_applications_type_0_item = TaxonomyApplicationConfig.from_dict(
                        taxonomy_applications_type_0_item_data
                    )

                    taxonomy_applications_type_0.append(taxonomy_applications_type_0_item)

                return taxonomy_applications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TaxonomyApplicationConfig] | None | Unset, data)

        taxonomy_applications = _parse_taxonomy_applications(d.pop("taxonomy_applications", UNSET))

        clone_collection_request = cls(
            collection_name=collection_name,
            description=description,
            source=source,
            feature_extractor=feature_extractor,
            enabled=enabled,
            metadata=metadata,
            taxonomy_applications=taxonomy_applications,
        )

        clone_collection_request.additional_properties = d
        return clone_collection_request

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
