from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.join_mode import JoinMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execute_taxonomy_request_source_documents_type_0_item import (
        ExecuteTaxonomyRequestSourceDocumentsType0Item,
    )
    from ..models.logical_operator import LogicalOperator
    from ..models.retriever_model import RetrieverModel
    from ..models.taxonomy_model import TaxonomyModel


T = TypeVar("T", bound="ExecuteTaxonomyRequest")


@_attrs_define
class ExecuteTaxonomyRequest:
    """Request model for on-demand taxonomy validation and testing ONLY.

    ⚠️ IMPORTANT: This endpoint is ONLY for testing taxonomy configuration with sample documents.

    DO NOT USE THIS FOR BATCH ENRICHMENT:
    ❌ Do NOT use this to enrich an entire collection
    ❌ Do NOT use source_collection_id expecting batch processing
    ❌ Do NOT use target_collection_id expecting persistence

    HOW TAXONOMY ENRICHMENT ACTUALLY WORKS:
    ✅ Automatic during ingestion: Attach taxonomies to collections via `taxonomy_applications`
    ✅ On-the-fly in retrieval: Add `taxonomy_join` stage to retriever pipelines

    This endpoint validates:
    - Taxonomy configuration is correct
    - Retriever can find matching taxonomy nodes
    - Enrichment fields are properly applied

    For production enrichment, see:
    - Collections API: attach taxonomies via `taxonomy_applications` field
    - Retrievers API: add `taxonomy_join` stage for on-the-fly enrichment

        Attributes:
            taxonomy (TaxonomyModel): Primary Pydantic model representing a taxonomy definition.
            retriever (None | RetrieverModel | Unset): Optional retriever configuration override for testing. If omitted,
                uses the retriever configured in the taxonomy.
            source_documents (list[ExecuteTaxonomyRequestSourceDocumentsType0Item] | None | Unset): Sample documents to test
                enrichment (typically 1-5 docs). Results are returned immediately, not persisted. ⚠️ Do NOT pass collection_id
                expecting batch processing!
            source_collection_id (None | str | Unset): ⚠️ IGNORED IN ON_DEMAND MODE. This field exists for legacy
                compatibility only. To enrich collections, use taxonomy_applications on the collection.
            target_collection_id (None | str | Unset): ⚠️ IGNORED IN ON_DEMAND MODE. This field exists for legacy
                compatibility only. Results are never persisted via this endpoint.
            join_mode (JoinMode | Unset):
            batch_size (int | Unset): Batch size for the scroll iterator Default: 1000.
            scroll_filters (LogicalOperator | None | Unset): Additional filters applied to the source collection prior to
                enrichment.
    """

    taxonomy: TaxonomyModel
    retriever: None | RetrieverModel | Unset = UNSET
    source_documents: list[ExecuteTaxonomyRequestSourceDocumentsType0Item] | None | Unset = UNSET
    source_collection_id: None | str | Unset = UNSET
    target_collection_id: None | str | Unset = UNSET
    join_mode: JoinMode | Unset = UNSET
    batch_size: int | Unset = 1000
    scroll_filters: LogicalOperator | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logical_operator import LogicalOperator
        from ..models.retriever_model import RetrieverModel

        taxonomy = self.taxonomy.to_dict()

        retriever: dict[str, Any] | None | Unset
        if isinstance(self.retriever, Unset):
            retriever = UNSET
        elif isinstance(self.retriever, RetrieverModel):
            retriever = self.retriever.to_dict()
        else:
            retriever = self.retriever

        source_documents: list[dict[str, Any]] | None | Unset
        if isinstance(self.source_documents, Unset):
            source_documents = UNSET
        elif isinstance(self.source_documents, list):
            source_documents = []
            for source_documents_type_0_item_data in self.source_documents:
                source_documents_type_0_item = source_documents_type_0_item_data.to_dict()
                source_documents.append(source_documents_type_0_item)

        else:
            source_documents = self.source_documents

        source_collection_id: None | str | Unset
        if isinstance(self.source_collection_id, Unset):
            source_collection_id = UNSET
        else:
            source_collection_id = self.source_collection_id

        target_collection_id: None | str | Unset
        if isinstance(self.target_collection_id, Unset):
            target_collection_id = UNSET
        else:
            target_collection_id = self.target_collection_id

        join_mode: str | Unset = UNSET
        if not isinstance(self.join_mode, Unset):
            join_mode = self.join_mode.value

        batch_size = self.batch_size

        scroll_filters: dict[str, Any] | None | Unset
        if isinstance(self.scroll_filters, Unset):
            scroll_filters = UNSET
        elif isinstance(self.scroll_filters, LogicalOperator):
            scroll_filters = self.scroll_filters.to_dict()
        else:
            scroll_filters = self.scroll_filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taxonomy": taxonomy,
            }
        )
        if retriever is not UNSET:
            field_dict["retriever"] = retriever
        if source_documents is not UNSET:
            field_dict["source_documents"] = source_documents
        if source_collection_id is not UNSET:
            field_dict["source_collection_id"] = source_collection_id
        if target_collection_id is not UNSET:
            field_dict["target_collection_id"] = target_collection_id
        if join_mode is not UNSET:
            field_dict["join_mode"] = join_mode
        if batch_size is not UNSET:
            field_dict["batch_size"] = batch_size
        if scroll_filters is not UNSET:
            field_dict["scroll_filters"] = scroll_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execute_taxonomy_request_source_documents_type_0_item import (
            ExecuteTaxonomyRequestSourceDocumentsType0Item,
        )
        from ..models.logical_operator import LogicalOperator
        from ..models.retriever_model import RetrieverModel
        from ..models.taxonomy_model import TaxonomyModel

        d = dict(src_dict)
        taxonomy = TaxonomyModel.from_dict(d.pop("taxonomy"))

        def _parse_retriever(data: object) -> None | RetrieverModel | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retriever_type_0 = RetrieverModel.from_dict(data)

                return retriever_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RetrieverModel | Unset, data)

        retriever = _parse_retriever(d.pop("retriever", UNSET))

        def _parse_source_documents(
            data: object,
        ) -> list[ExecuteTaxonomyRequestSourceDocumentsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_documents_type_0 = []
                _source_documents_type_0 = data
                for source_documents_type_0_item_data in _source_documents_type_0:
                    source_documents_type_0_item = ExecuteTaxonomyRequestSourceDocumentsType0Item.from_dict(
                        source_documents_type_0_item_data
                    )

                    source_documents_type_0.append(source_documents_type_0_item)

                return source_documents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ExecuteTaxonomyRequestSourceDocumentsType0Item] | None | Unset, data)

        source_documents = _parse_source_documents(d.pop("source_documents", UNSET))

        def _parse_source_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_collection_id = _parse_source_collection_id(d.pop("source_collection_id", UNSET))

        def _parse_target_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_collection_id = _parse_target_collection_id(d.pop("target_collection_id", UNSET))

        _join_mode = d.pop("join_mode", UNSET)
        join_mode: JoinMode | Unset
        if isinstance(_join_mode, Unset):
            join_mode = UNSET
        else:
            join_mode = JoinMode(_join_mode)

        batch_size = d.pop("batch_size", UNSET)

        def _parse_scroll_filters(data: object) -> LogicalOperator | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scroll_filters_type_0 = LogicalOperator.from_dict(data)

                return scroll_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LogicalOperator | None | Unset, data)

        scroll_filters = _parse_scroll_filters(d.pop("scroll_filters", UNSET))

        execute_taxonomy_request = cls(
            taxonomy=taxonomy,
            retriever=retriever,
            source_documents=source_documents,
            source_collection_id=source_collection_id,
            target_collection_id=target_collection_id,
            join_mode=join_mode,
            batch_size=batch_size,
            scroll_filters=scroll_filters,
        )

        execute_taxonomy_request.additional_properties = d
        return execute_taxonomy_request

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
