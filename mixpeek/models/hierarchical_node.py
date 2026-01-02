from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enrichment_field import EnrichmentField
    from ..models.input_mapping import InputMapping


T = TypeVar("T", bound="HierarchicalNode")


@_attrs_define
class HierarchicalNode:
    """A node in a hierarchical taxonomy representing one level in the tree structure.

    Each node represents a collection containing documents at a specific hierarchy level.
    Nodes form parent-child relationships to create multi-level taxonomies with
    property inheritance. When a document matches a child node, it inherits all
    properties from parent nodes up to the root.

    Use Cases:
        - Define organizational hierarchies: employees → managers → executives
        - Create product categorizations: products → electronics → phones → smartphones
        - Build classification trees: industries → technology → software
        - Implement face recognition hierarchies: people → employees → team members
        - Enable property inheritance: child nodes get all parent properties

    Hierarchy Behavior:
        - Root nodes: parent_collection_id = None (top of hierarchy)
        - Child nodes: parent_collection_id references parent node's collection_id
        - Property inheritance: Children inherit all parent enrichment_fields
        - Path construction: Creates path array from root to leaf
        - Multi-level matching: Documents matched at deepest applicable level

    Configuration:
        - Per-node retrievers: Override taxonomy-level retriever for specific nodes
        - Per-node enrichment: Override which fields to enrich at each level
        - Per-node input mappings: Customize retriever inputs per hierarchy level
        - Labels/summaries: Human-readable metadata for UI display

    Related Models:
        - HierarchicalTaxonomyConfig: Contains list of hierarchical nodes
        - TaxonomyAssignment: Result of matching documents to nodes
        - EnrichmentField: Specifies which fields to enrich from node

    Requirements:
        - collection_id: REQUIRED - must reference an existing collection
        - parent_collection_id: REQUIRED for non-root nodes (None for root)
        - All other fields: OPTIONAL with inheritance from taxonomy-level config

        Attributes:
            collection_id (str): REQUIRED. Collection ID representing this node in the hierarchy. Must reference an existing
                collection containing documents for this hierarchy level. Format: 'col_' prefix followed by
                alphanumeric/underscore characters. Used to: Match documents against this level, identify node in path, store
                enrichment data. Example: 'col_executives' for executive level, 'col_products_phones' for phones category.
            parent_collection_id (None | str | Unset): OPTIONAL. Collection ID of the parent node in the hierarchy. When
                None: This is a root node (top of hierarchy). When set: References parent node's collection_id, creating parent-
                child relationship. Format: Same as collection_id ('col_' prefix). Used to: Build hierarchy tree, determine
                inheritance order, construct path arrays. Example: 'col_managers' is parent of 'col_executives', 'col_products'
                is parent of 'col_electronics'. Validation: Must reference a valid collection_id from another node in same
                taxonomy.
            label (None | str | Unset): OPTIONAL. Human-readable display name for this hierarchy node. Used in UI,
                visualizations, and taxonomy assignment results. NOT REQUIRED - When None: collection name or auto-generated
                label may be used. Format: Free text, typically title case, 2-50 characters. Examples: 'Executive Leadership',
                'Mobile Phones', 'Engineering Team'. Can be LLM-generated or manually specified during taxonomy creation.
            summary (None | str | Unset): OPTIONAL. Brief description of this hierarchy level and its contents. Used for:
                Documentation, UI tooltips, understanding hierarchy structure. NOT REQUIRED - When None: no summary available
                for this node. Format: Free text, typically 1-3 sentences, up to 500 characters. Can be LLM-generated or
                manually provided.
            keywords (list[str] | None | Unset): OPTIONAL. Keywords or tags describing this hierarchy level. Used for:
                Search, filtering, categorization, LLM understanding. NOT REQUIRED - When None: no keywords defined for this
                node. Format: List of strings, typically 3-10 keywords per node. Can be LLM-generated from collection contents
                or manually specified.
            retriever_id (None | str | Unset): OPTIONAL. Retriever to use for matching documents at this hierarchy level.
                When None: Uses taxonomy-level retriever_id (inheritance from parent config). When set: Overrides taxonomy-level
                retriever for this specific node. Format: 'ret_' prefix followed by alphanumeric characters. Use for:
                Specialized matching at certain levels (e.g., face recognition for employees, semantic search for products).
                Must reference an existing RetrieverModel.
            enrichment_fields (list[EnrichmentField] | None | Unset): OPTIONAL. Fields to enrich into documents when they
                match this hierarchy level. Specifies which properties from node collection to copy to matched documents. When
                None: No field-level enrichment (only taxonomy assignment recorded). Format: List of EnrichmentField objects
                with field_path and merge_mode. Inheritance: Child nodes inherit all parent enrichment_fields plus their own.
                Example: executives node adds 'executive_level' on top of inherited 'employee_id', 'department'.
            input_mappings (list[InputMapping] | None | Unset): OPTIONAL. Custom input mappings for the retriever at this
                hierarchy level. Specifies how to construct retriever inputs from document features. When None: Uses taxonomy-
                level input_mappings (inheritance). When set: Overrides taxonomy-level mappings for this specific node. Format:
                List of InputMapping objects specifying input_key, source_type, path. Use for: Different matching strategies at
                different levels (e.g., face at employee level, text at department level).
    """

    collection_id: str
    parent_collection_id: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    retriever_id: None | str | Unset = UNSET
    enrichment_fields: list[EnrichmentField] | None | Unset = UNSET
    input_mappings: list[InputMapping] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_id = self.collection_id

        parent_collection_id: None | str | Unset
        if isinstance(self.parent_collection_id, Unset):
            parent_collection_id = UNSET
        else:
            parent_collection_id = self.parent_collection_id

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        keywords: list[str] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords

        else:
            keywords = self.keywords

        retriever_id: None | str | Unset
        if isinstance(self.retriever_id, Unset):
            retriever_id = UNSET
        else:
            retriever_id = self.retriever_id

        enrichment_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.enrichment_fields, Unset):
            enrichment_fields = UNSET
        elif isinstance(self.enrichment_fields, list):
            enrichment_fields = []
            for enrichment_fields_type_0_item_data in self.enrichment_fields:
                enrichment_fields_type_0_item = enrichment_fields_type_0_item_data.to_dict()
                enrichment_fields.append(enrichment_fields_type_0_item)

        else:
            enrichment_fields = self.enrichment_fields

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_id": collection_id,
            }
        )
        if parent_collection_id is not UNSET:
            field_dict["parent_collection_id"] = parent_collection_id
        if label is not UNSET:
            field_dict["label"] = label
        if summary is not UNSET:
            field_dict["summary"] = summary
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if retriever_id is not UNSET:
            field_dict["retriever_id"] = retriever_id
        if enrichment_fields is not UNSET:
            field_dict["enrichment_fields"] = enrichment_fields
        if input_mappings is not UNSET:
            field_dict["input_mappings"] = input_mappings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enrichment_field import EnrichmentField
        from ..models.input_mapping import InputMapping

        d = dict(src_dict)
        collection_id = d.pop("collection_id")

        def _parse_parent_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_collection_id = _parse_parent_collection_id(d.pop("parent_collection_id", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_retriever_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retriever_id = _parse_retriever_id(d.pop("retriever_id", UNSET))

        def _parse_enrichment_fields(data: object) -> list[EnrichmentField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                enrichment_fields_type_0 = []
                _enrichment_fields_type_0 = data
                for enrichment_fields_type_0_item_data in _enrichment_fields_type_0:
                    enrichment_fields_type_0_item = EnrichmentField.from_dict(enrichment_fields_type_0_item_data)

                    enrichment_fields_type_0.append(enrichment_fields_type_0_item)

                return enrichment_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EnrichmentField] | None | Unset, data)

        enrichment_fields = _parse_enrichment_fields(d.pop("enrichment_fields", UNSET))

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

        hierarchical_node = cls(
            collection_id=collection_id,
            parent_collection_id=parent_collection_id,
            label=label,
            summary=summary,
            keywords=keywords,
            retriever_id=retriever_id,
            enrichment_fields=enrichment_fields,
            input_mappings=input_mappings,
        )

        hierarchical_node.additional_properties = d
        return hierarchical_node

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
