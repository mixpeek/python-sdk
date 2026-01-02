from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hierarchy_inference_strategy import HierarchyInferenceStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hierarchical_node import HierarchicalNode
    from ..models.input_mapping import InputMapping
    from ..models.step_analytics_config import StepAnalyticsConfig


T = TypeVar("T", bound="HierarchicalTaxonomyConfig")


@_attrs_define
class HierarchicalTaxonomyConfig:
    """Hybrid hierarchical taxonomy configuration supporting inference with manual additions.

    All hierarchical taxonomies are hybrid:
    - Base hierarchy can be inferred via schema, clustering, or LLM
    - Additional collections can be explicitly added with specific retrievers
    - Supports mixing inference strategies with manual additions/overrides

    Examples:
    1. Pure inference: Set inference_strategy + inference_collections
    2. Pure manual: Set hierarchical_nodes only
    3. Hybrid: Set inference_strategy + inference_collections + hierarchical_nodes
       (infers base from collections, adds/overrides with explicit nodes)

        Attributes:
            taxonomy_type (Literal['hierarchical'] | Unset): Discriminator identifying this as a hierarchical taxonomy.
                Default: 'hierarchical'.
            retriever_id (None | str | Unset): Default retriever to use for all nodes unless overridden per-node.
            input_mappings (list[InputMapping] | None | Unset): Default input mappings for all nodes unless overridden per-
                node.
            inference_strategy (HierarchyInferenceStrategy | None | Unset): Strategy for inferring hierarchy structure from
                collections. Can be 'schema' (overlap-based), 'cluster' (clustering-based), or 'llm' (AI-based). When set, will
                infer relationships from inference_collections.
            inference_collections (list[str] | None | Unset): Collection IDs to use for hierarchy inference. The
                inference_strategy will analyze these collections to discover relationships. Can be combined with
                hierarchical_nodes for hybrid configuration.
            llm_provider (Literal['openai_chat_v1'] | None | Unset): LLM provider to use for hierarchy inference (default
                openai_chat_v1)
            llm_model (None | str | Unset): LLM model name (e.g., gpt-4o-mini)
            llm_prompt_template (None | str | Unset): Optional prompt template. Variables available: {collection_id},
                {collection_name}.
            llm_sample_size (int | Unset): Optional number of sample docs to include in prompts (0 = disabled). Default: 0.
            cluster_ids (list[str] | None | Unset): Cluster IDs to use for CLUSTER inference strategy
            cluster_overlap_threshold (float | Unset): Minimum overlap ratio to establish parent-child relationship between
                clusters Default: 0.7.
            hierarchical_nodes (list[HierarchicalNode] | None | Unset): Explicit node definitions that either: 1) Define the
                entire hierarchy (when inference_strategy is None), 2) Add additional nodes to an inferred hierarchy, or 3)
                Override specific relationships in an inferred hierarchy. Supports true hybrid: infer from some collections,
                manually add others.
            step_analytics (None | StepAnalyticsConfig | Unset): Optional configuration for step transition analytics.
                Enables tracking how documents progress through hierarchical taxonomy nodes over time (e.g., content workflow
                tracking from 'draft' to 'published'). If not provided, only basic assignment events are logged.
    """

    taxonomy_type: Literal["hierarchical"] | Unset = "hierarchical"
    retriever_id: None | str | Unset = UNSET
    input_mappings: list[InputMapping] | None | Unset = UNSET
    inference_strategy: HierarchyInferenceStrategy | None | Unset = UNSET
    inference_collections: list[str] | None | Unset = UNSET
    llm_provider: Literal["openai_chat_v1"] | None | Unset = UNSET
    llm_model: None | str | Unset = UNSET
    llm_prompt_template: None | str | Unset = UNSET
    llm_sample_size: int | Unset = 0
    cluster_ids: list[str] | None | Unset = UNSET
    cluster_overlap_threshold: float | Unset = 0.7
    hierarchical_nodes: list[HierarchicalNode] | None | Unset = UNSET
    step_analytics: None | StepAnalyticsConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.step_analytics_config import StepAnalyticsConfig

        taxonomy_type = self.taxonomy_type

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

        inference_strategy: None | str | Unset
        if isinstance(self.inference_strategy, Unset):
            inference_strategy = UNSET
        elif isinstance(self.inference_strategy, HierarchyInferenceStrategy):
            inference_strategy = self.inference_strategy.value
        else:
            inference_strategy = self.inference_strategy

        inference_collections: list[str] | None | Unset
        if isinstance(self.inference_collections, Unset):
            inference_collections = UNSET
        elif isinstance(self.inference_collections, list):
            inference_collections = self.inference_collections

        else:
            inference_collections = self.inference_collections

        llm_provider: Literal["openai_chat_v1"] | None | Unset
        if isinstance(self.llm_provider, Unset):
            llm_provider = UNSET
        else:
            llm_provider = self.llm_provider

        llm_model: None | str | Unset
        if isinstance(self.llm_model, Unset):
            llm_model = UNSET
        else:
            llm_model = self.llm_model

        llm_prompt_template: None | str | Unset
        if isinstance(self.llm_prompt_template, Unset):
            llm_prompt_template = UNSET
        else:
            llm_prompt_template = self.llm_prompt_template

        llm_sample_size = self.llm_sample_size

        cluster_ids: list[str] | None | Unset
        if isinstance(self.cluster_ids, Unset):
            cluster_ids = UNSET
        elif isinstance(self.cluster_ids, list):
            cluster_ids = self.cluster_ids

        else:
            cluster_ids = self.cluster_ids

        cluster_overlap_threshold = self.cluster_overlap_threshold

        hierarchical_nodes: list[dict[str, Any]] | None | Unset
        if isinstance(self.hierarchical_nodes, Unset):
            hierarchical_nodes = UNSET
        elif isinstance(self.hierarchical_nodes, list):
            hierarchical_nodes = []
            for hierarchical_nodes_type_0_item_data in self.hierarchical_nodes:
                hierarchical_nodes_type_0_item = hierarchical_nodes_type_0_item_data.to_dict()
                hierarchical_nodes.append(hierarchical_nodes_type_0_item)

        else:
            hierarchical_nodes = self.hierarchical_nodes

        step_analytics: dict[str, Any] | None | Unset
        if isinstance(self.step_analytics, Unset):
            step_analytics = UNSET
        elif isinstance(self.step_analytics, StepAnalyticsConfig):
            step_analytics = self.step_analytics.to_dict()
        else:
            step_analytics = self.step_analytics

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if taxonomy_type is not UNSET:
            field_dict["taxonomy_type"] = taxonomy_type
        if retriever_id is not UNSET:
            field_dict["retriever_id"] = retriever_id
        if input_mappings is not UNSET:
            field_dict["input_mappings"] = input_mappings
        if inference_strategy is not UNSET:
            field_dict["inference_strategy"] = inference_strategy
        if inference_collections is not UNSET:
            field_dict["inference_collections"] = inference_collections
        if llm_provider is not UNSET:
            field_dict["llm_provider"] = llm_provider
        if llm_model is not UNSET:
            field_dict["llm_model"] = llm_model
        if llm_prompt_template is not UNSET:
            field_dict["llm_prompt_template"] = llm_prompt_template
        if llm_sample_size is not UNSET:
            field_dict["llm_sample_size"] = llm_sample_size
        if cluster_ids is not UNSET:
            field_dict["cluster_ids"] = cluster_ids
        if cluster_overlap_threshold is not UNSET:
            field_dict["cluster_overlap_threshold"] = cluster_overlap_threshold
        if hierarchical_nodes is not UNSET:
            field_dict["hierarchical_nodes"] = hierarchical_nodes
        if step_analytics is not UNSET:
            field_dict["step_analytics"] = step_analytics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hierarchical_node import HierarchicalNode
        from ..models.input_mapping import InputMapping
        from ..models.step_analytics_config import StepAnalyticsConfig

        d = dict(src_dict)
        taxonomy_type = cast(Literal["hierarchical"] | Unset, d.pop("taxonomy_type", UNSET))
        if taxonomy_type != "hierarchical" and not isinstance(taxonomy_type, Unset):
            raise ValueError(f"taxonomy_type must match const 'hierarchical', got '{taxonomy_type}'")

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

        def _parse_inference_strategy(data: object) -> HierarchyInferenceStrategy | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                inference_strategy_type_0 = HierarchyInferenceStrategy(data)

                return inference_strategy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HierarchyInferenceStrategy | None | Unset, data)

        inference_strategy = _parse_inference_strategy(d.pop("inference_strategy", UNSET))

        def _parse_inference_collections(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inference_collections_type_0 = cast(list[str], data)

                return inference_collections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        inference_collections = _parse_inference_collections(d.pop("inference_collections", UNSET))

        def _parse_llm_provider(data: object) -> Literal["openai_chat_v1"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            llm_provider_type_0 = cast(Literal["openai_chat_v1"], data)
            if llm_provider_type_0 != "openai_chat_v1":
                raise ValueError(f"llm_provider_type_0 must match const 'openai_chat_v1', got '{llm_provider_type_0}'")
            return llm_provider_type_0
            return cast(Literal["openai_chat_v1"] | None | Unset, data)

        llm_provider = _parse_llm_provider(d.pop("llm_provider", UNSET))

        def _parse_llm_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        llm_model = _parse_llm_model(d.pop("llm_model", UNSET))

        def _parse_llm_prompt_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        llm_prompt_template = _parse_llm_prompt_template(d.pop("llm_prompt_template", UNSET))

        llm_sample_size = d.pop("llm_sample_size", UNSET)

        def _parse_cluster_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cluster_ids_type_0 = cast(list[str], data)

                return cluster_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cluster_ids = _parse_cluster_ids(d.pop("cluster_ids", UNSET))

        cluster_overlap_threshold = d.pop("cluster_overlap_threshold", UNSET)

        def _parse_hierarchical_nodes(data: object) -> list[HierarchicalNode] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hierarchical_nodes_type_0 = []
                _hierarchical_nodes_type_0 = data
                for hierarchical_nodes_type_0_item_data in _hierarchical_nodes_type_0:
                    hierarchical_nodes_type_0_item = HierarchicalNode.from_dict(hierarchical_nodes_type_0_item_data)

                    hierarchical_nodes_type_0.append(hierarchical_nodes_type_0_item)

                return hierarchical_nodes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HierarchicalNode] | None | Unset, data)

        hierarchical_nodes = _parse_hierarchical_nodes(d.pop("hierarchical_nodes", UNSET))

        def _parse_step_analytics(data: object) -> None | StepAnalyticsConfig | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                step_analytics_type_0 = StepAnalyticsConfig.from_dict(data)

                return step_analytics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StepAnalyticsConfig | Unset, data)

        step_analytics = _parse_step_analytics(d.pop("step_analytics", UNSET))

        hierarchical_taxonomy_config = cls(
            taxonomy_type=taxonomy_type,
            retriever_id=retriever_id,
            input_mappings=input_mappings,
            inference_strategy=inference_strategy,
            inference_collections=inference_collections,
            llm_provider=llm_provider,
            llm_model=llm_model,
            llm_prompt_template=llm_prompt_template,
            llm_sample_size=llm_sample_size,
            cluster_ids=cluster_ids,
            cluster_overlap_threshold=cluster_overlap_threshold,
            hierarchical_nodes=hierarchical_nodes,
            step_analytics=step_analytics,
        )

        hierarchical_taxonomy_config.additional_properties = d
        return hierarchical_taxonomy_config

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
