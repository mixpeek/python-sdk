from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_processing_model_history_type_0_item import InternalProcessingModelHistoryType0Item
    from ..models.internal_processing_model_last_health_check_type_0 import InternalProcessingModelLastHealthCheckType0
    from ..models.internal_processing_model_taxonomy_lineage_type_0_item import (
        InternalProcessingModelTaxonomyLineageType0Item,
    )


T = TypeVar("T", bound="InternalProcessingModel")


@_attrs_define
class InternalProcessingModel:
    """Processing and provenance tracking information.

    Consolidates all processing-related metadata including source URLs,
    processing history, and taxonomy enrichment lineage.

        Attributes:
            source_url (None | str | Unset): Original URL before S3 mirroring (for URL-based ingestion).
            object_key_source (None | str | Unset): S3 key source identifier.
            detected_mime_type (None | str | Unset): MIME type detected during canonicalization.
            history (list[InternalProcessingModelHistoryType0Item] | None | Unset): Processing steps history with timestamps
                and operations.
            taxonomy_lineage (list[InternalProcessingModelTaxonomyLineageType0Item] | None | Unset): Taxonomy enrichment
                entries applied to this document.
            last_health_check (InternalProcessingModelLastHealthCheckType0 | None | Unset): Last health check result (for
                batch processing).
    """

    source_url: None | str | Unset = UNSET
    object_key_source: None | str | Unset = UNSET
    detected_mime_type: None | str | Unset = UNSET
    history: list[InternalProcessingModelHistoryType0Item] | None | Unset = UNSET
    taxonomy_lineage: list[InternalProcessingModelTaxonomyLineageType0Item] | None | Unset = UNSET
    last_health_check: InternalProcessingModelLastHealthCheckType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.internal_processing_model_last_health_check_type_0 import (
            InternalProcessingModelLastHealthCheckType0,
        )

        source_url: None | str | Unset
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        object_key_source: None | str | Unset
        if isinstance(self.object_key_source, Unset):
            object_key_source = UNSET
        else:
            object_key_source = self.object_key_source

        detected_mime_type: None | str | Unset
        if isinstance(self.detected_mime_type, Unset):
            detected_mime_type = UNSET
        else:
            detected_mime_type = self.detected_mime_type

        history: list[dict[str, Any]] | None | Unset
        if isinstance(self.history, Unset):
            history = UNSET
        elif isinstance(self.history, list):
            history = []
            for history_type_0_item_data in self.history:
                history_type_0_item = history_type_0_item_data.to_dict()
                history.append(history_type_0_item)

        else:
            history = self.history

        taxonomy_lineage: list[dict[str, Any]] | None | Unset
        if isinstance(self.taxonomy_lineage, Unset):
            taxonomy_lineage = UNSET
        elif isinstance(self.taxonomy_lineage, list):
            taxonomy_lineage = []
            for taxonomy_lineage_type_0_item_data in self.taxonomy_lineage:
                taxonomy_lineage_type_0_item = taxonomy_lineage_type_0_item_data.to_dict()
                taxonomy_lineage.append(taxonomy_lineage_type_0_item)

        else:
            taxonomy_lineage = self.taxonomy_lineage

        last_health_check: dict[str, Any] | None | Unset
        if isinstance(self.last_health_check, Unset):
            last_health_check = UNSET
        elif isinstance(self.last_health_check, InternalProcessingModelLastHealthCheckType0):
            last_health_check = self.last_health_check.to_dict()
        else:
            last_health_check = self.last_health_check

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if object_key_source is not UNSET:
            field_dict["object_key_source"] = object_key_source
        if detected_mime_type is not UNSET:
            field_dict["detected_mime_type"] = detected_mime_type
        if history is not UNSET:
            field_dict["history"] = history
        if taxonomy_lineage is not UNSET:
            field_dict["taxonomy_lineage"] = taxonomy_lineage
        if last_health_check is not UNSET:
            field_dict["last_health_check"] = last_health_check

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_processing_model_history_type_0_item import InternalProcessingModelHistoryType0Item
        from ..models.internal_processing_model_last_health_check_type_0 import (
            InternalProcessingModelLastHealthCheckType0,
        )
        from ..models.internal_processing_model_taxonomy_lineage_type_0_item import (
            InternalProcessingModelTaxonomyLineageType0Item,
        )

        d = dict(src_dict)

        def _parse_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_url = _parse_source_url(d.pop("source_url", UNSET))

        def _parse_object_key_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_key_source = _parse_object_key_source(d.pop("object_key_source", UNSET))

        def _parse_detected_mime_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detected_mime_type = _parse_detected_mime_type(d.pop("detected_mime_type", UNSET))

        def _parse_history(data: object) -> list[InternalProcessingModelHistoryType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                history_type_0 = []
                _history_type_0 = data
                for history_type_0_item_data in _history_type_0:
                    history_type_0_item = InternalProcessingModelHistoryType0Item.from_dict(history_type_0_item_data)

                    history_type_0.append(history_type_0_item)

                return history_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InternalProcessingModelHistoryType0Item] | None | Unset, data)

        history = _parse_history(d.pop("history", UNSET))

        def _parse_taxonomy_lineage(
            data: object,
        ) -> list[InternalProcessingModelTaxonomyLineageType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                taxonomy_lineage_type_0 = []
                _taxonomy_lineage_type_0 = data
                for taxonomy_lineage_type_0_item_data in _taxonomy_lineage_type_0:
                    taxonomy_lineage_type_0_item = InternalProcessingModelTaxonomyLineageType0Item.from_dict(
                        taxonomy_lineage_type_0_item_data
                    )

                    taxonomy_lineage_type_0.append(taxonomy_lineage_type_0_item)

                return taxonomy_lineage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InternalProcessingModelTaxonomyLineageType0Item] | None | Unset, data)

        taxonomy_lineage = _parse_taxonomy_lineage(d.pop("taxonomy_lineage", UNSET))

        def _parse_last_health_check(data: object) -> InternalProcessingModelLastHealthCheckType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_health_check_type_0 = InternalProcessingModelLastHealthCheckType0.from_dict(data)

                return last_health_check_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InternalProcessingModelLastHealthCheckType0 | None | Unset, data)

        last_health_check = _parse_last_health_check(d.pop("last_health_check", UNSET))

        internal_processing_model = cls(
            source_url=source_url,
            object_key_source=object_key_source,
            detected_mime_type=detected_mime_type,
            history=history,
            taxonomy_lineage=taxonomy_lineage,
            last_health_check=last_health_check,
        )

        internal_processing_model.additional_properties = d
        return internal_processing_model

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
