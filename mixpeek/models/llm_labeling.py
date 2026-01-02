from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.anthropic_model import AnthropicModel
from ..models.google_model import GoogleModel
from ..models.llm_provider import LLMProvider
from ..models.open_ai_model import OpenAIModel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.llm_labeling_input import LLMLabelingInput
    from ..models.llm_labeling_parameters import LLMLabelingParameters
    from ..models.llm_labeling_response_shape_type_1 import LLMLabelingResponseShapeType1


T = TypeVar("T", bound="LLMLabeling")


@_attrs_define
class LLMLabeling:
    """Configuration for LLM-based cluster labeling.

    Supports multiple LLM providers with comprehensive model selection:
    - OpenAI: GPT-4o, GPT-4o-mini, GPT-4.1, O3-mini (best for quality)
    - Google: Gemini 2.5 Flash, Gemini 1.5 Flash (best for speed and cost)
    - Anthropic: Claude 3.5 Sonnet, Claude 3.5 Haiku (best for reasoning)

    All models are defined as enums and validated at API level.

        Attributes:
            enabled (bool | Unset): Whether to generate labels for clusters using LLM. When enabled, clusters will have
                semantic labels like 'High-Performance Laptops' instead of generic labels like 'Cluster 0'. Default: False.
            labeling_inputs (LLMLabelingInput | None | Unset): Input configuration for LLM labeling. Supports flexible input
                mappings for multimodal inputs (text, images, videos, audio). Use input_mappings for advanced multimodal
                labeling with providers like Gemini. If not provided (null/undefined), the full document payload will be
                serialized as JSON and sent to the LLM, providing complete context for semantic labeling.
            provider (LLMProvider | None | Unset): LLM provider to use for labeling. Supported providers:
                - openai: GPT models (GPT-4o, GPT-4o-mini, GPT-4.1, O3-mini)
                - google: Gemini models (Gemini 2.5 Flash, Gemini 1.5 Flash)
                - anthropic: Claude models (Claude 3.5 Sonnet, Claude 3.5 Haiku)

                If not specified, automatically inferred from model_name.
            model_name (AnthropicModel | GoogleModel | None | OpenAIModel | Unset): REQUIRED when enabled=True. Specific LLM
                model to use for cluster labeling. All models are defined as enums for type safety.

                OpenAI Models (provider='openai'):
                - gpt-4o-2024-08-06: Highest quality, best for production ($2.50/$10 per 1M tokens)
                - gpt-4o-mini-2024-07-18: Cost-effective, recommended for most use cases ($0.15/$0.60 per 1M tokens)
                - gpt-4.1-2025-04-14: Latest model, future-proofed
                - gpt-4.1-mini-2025-04-14: Latest cost-optimized model
                - o3-mini-2025-01-31: Advanced reasoning, best for complex clustering

                Google Models (provider='google'):
                - gemini-2.0-flash: Fastest, latest multimodal model, recommended ($0.075/$0.30 per 1M tokens)
                - gemini-2.0-flash-exp: Experimental version with latest features ($0.075/$0.30 per 1M tokens)

                Anthropic Models (provider='anthropic'):
                - claude-3-5-sonnet-20241022: Best reasoning, 200K context ($3/$15 per 1M tokens)
                - claude-3-5-haiku-20241022: Fast, cost-effective ($0.25/$1.25 per 1M tokens)

                Recommendation:
                - Use gemini-2.0-flash (DEFAULT) - cheapest option with multimodal support
                - Use gpt-4o-mini-2024-07-18 for OpenAI compatibility
                - Use gpt-4o-2024-08-06 for highest quality when cost is not a concern
            include_summary (bool | Unset): Whether to generate cluster summaries Default: True.
            include_keywords (bool | Unset): Whether to extract keywords for clusters Default: True.
            max_samples_per_cluster (int | Unset): Maximum representative documents to send to LLM per cluster for semantic
                analysis Default: 10.
            sample_text_max_length (int | Unset): Maximum characters per document sample text Default: 200.
            use_embedding_dedup (bool | Unset): Enable embedding-based label deduplication to prevent near-duplicate labels
                (requires sentence-transformers) Default: False.
            embedding_similarity_threshold (float | Unset): Cosine similarity threshold for duplicate label detection
                (labels above this are considered duplicates) Default: 0.8.
            cache_ttl_seconds (int | Unset): Time-to-live for cached labels in seconds. Labels for clusters with identical
                representative documents will be reused within this TTL window, reducing LLM API costs. Default: 604800 (7
                days). Set to 0 to disable caching. Default: 604800.
            custom_prompt (None | str | Unset): OPTIONAL. Custom prompt template for LLM labeling. NOT REQUIRED - uses
                default discriminative prompt if not provided. When provided, completely replaces the default prompt. Your
                custom prompt receives cluster information but you must format it yourself. Use when:   - Need domain-specific
                labeling (e.g., medical, legal, technical)   - Want different label format (e.g., emoji labels, code names)   -
                Require specific output structure   - Have custom business logic for categorization Default prompt includes:
                cluster document samples, forbidden labels for uniqueness, and JSON response format. See
                engine/clusters/labeling/prompts.py for reference. Example: 'Analyze these product clusters and generate SHORT
                category names (2-3 words max) focusing on product type and price range. Return JSON: [{"cluster_id": "cl_0",
                "label": "..."}]'
            response_shape (LLMLabelingResponseShapeType1 | None | str | Unset): OPTIONAL. Define custom structured output
                for LLM labeling. NOT REQUIRED - uses default structure (label, summary, keywords) if not provided. When
                provided, LLM output will match this structure and be stored in cluster documents.

                Two modes supported:
                1. Natural language prompt (string): Describe desired output in plain English
                   - Service automatically infers JSON schema from your description
                   - Example: 'Extract cluster category, confidence score (0-1), and top 3 representative terms'
                   - Auto-generates schema with appropriate types (string, number, array, etc.)

                2. Explicit JSON schema (dict): Provide complete JSON schema for output structure
                   - Full control over output structure, types, and constraints
                   - Example: {'type': 'object', 'properties': {'category': {'type': 'string'}, ...}}


                Use when:
                  - Need custom metadata fields (confidence scores, sentiment, complexity)
                  - Want domain-specific structure (taxonomy hierarchies, entity extractions)
                  - Require specific data types (arrays, nested objects, enums)
                  - Have downstream schema requirements


                Output fields are automatically added to cluster collection schema and stored in metadata.
                Default behavior (if not provided): label (string), summary (string), keywords (array of strings)
            parameters (LLMLabelingParameters | Unset): Provider-specific parameters forwarded to the LLM service. For
                OpenAI: temperature, max_tokens, top_p, json_output, etc. For Google: temperature, top_k, max_output_tokens,
                json_output, etc.
    """

    enabled: bool | Unset = False
    labeling_inputs: LLMLabelingInput | None | Unset = UNSET
    provider: LLMProvider | None | Unset = UNSET
    model_name: AnthropicModel | GoogleModel | None | OpenAIModel | Unset = UNSET
    include_summary: bool | Unset = True
    include_keywords: bool | Unset = True
    max_samples_per_cluster: int | Unset = 10
    sample_text_max_length: int | Unset = 200
    use_embedding_dedup: bool | Unset = False
    embedding_similarity_threshold: float | Unset = 0.8
    cache_ttl_seconds: int | Unset = 604800
    custom_prompt: None | str | Unset = UNSET
    response_shape: LLMLabelingResponseShapeType1 | None | str | Unset = UNSET
    parameters: LLMLabelingParameters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.llm_labeling_input import LLMLabelingInput
        from ..models.llm_labeling_response_shape_type_1 import LLMLabelingResponseShapeType1

        enabled = self.enabled

        labeling_inputs: dict[str, Any] | None | Unset
        if isinstance(self.labeling_inputs, Unset):
            labeling_inputs = UNSET
        elif isinstance(self.labeling_inputs, LLMLabelingInput):
            labeling_inputs = self.labeling_inputs.to_dict()
        else:
            labeling_inputs = self.labeling_inputs

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, LLMProvider):
            provider = self.provider.value
        else:
            provider = self.provider

        model_name: None | str | Unset
        if isinstance(self.model_name, Unset):
            model_name = UNSET
        elif isinstance(self.model_name, OpenAIModel):
            model_name = self.model_name.value
        elif isinstance(self.model_name, GoogleModel):
            model_name = self.model_name.value
        elif isinstance(self.model_name, AnthropicModel):
            model_name = self.model_name.value
        else:
            model_name = self.model_name

        include_summary = self.include_summary

        include_keywords = self.include_keywords

        max_samples_per_cluster = self.max_samples_per_cluster

        sample_text_max_length = self.sample_text_max_length

        use_embedding_dedup = self.use_embedding_dedup

        embedding_similarity_threshold = self.embedding_similarity_threshold

        cache_ttl_seconds = self.cache_ttl_seconds

        custom_prompt: None | str | Unset
        if isinstance(self.custom_prompt, Unset):
            custom_prompt = UNSET
        else:
            custom_prompt = self.custom_prompt

        response_shape: dict[str, Any] | None | str | Unset
        if isinstance(self.response_shape, Unset):
            response_shape = UNSET
        elif isinstance(self.response_shape, LLMLabelingResponseShapeType1):
            response_shape = self.response_shape.to_dict()
        else:
            response_shape = self.response_shape

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if labeling_inputs is not UNSET:
            field_dict["labeling_inputs"] = labeling_inputs
        if provider is not UNSET:
            field_dict["provider"] = provider
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if include_summary is not UNSET:
            field_dict["include_summary"] = include_summary
        if include_keywords is not UNSET:
            field_dict["include_keywords"] = include_keywords
        if max_samples_per_cluster is not UNSET:
            field_dict["max_samples_per_cluster"] = max_samples_per_cluster
        if sample_text_max_length is not UNSET:
            field_dict["sample_text_max_length"] = sample_text_max_length
        if use_embedding_dedup is not UNSET:
            field_dict["use_embedding_dedup"] = use_embedding_dedup
        if embedding_similarity_threshold is not UNSET:
            field_dict["embedding_similarity_threshold"] = embedding_similarity_threshold
        if cache_ttl_seconds is not UNSET:
            field_dict["cache_ttl_seconds"] = cache_ttl_seconds
        if custom_prompt is not UNSET:
            field_dict["custom_prompt"] = custom_prompt
        if response_shape is not UNSET:
            field_dict["response_shape"] = response_shape
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.llm_labeling_input import LLMLabelingInput
        from ..models.llm_labeling_parameters import LLMLabelingParameters
        from ..models.llm_labeling_response_shape_type_1 import LLMLabelingResponseShapeType1

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        def _parse_labeling_inputs(data: object) -> LLMLabelingInput | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labeling_inputs_type_0 = LLMLabelingInput.from_dict(data)

                return labeling_inputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LLMLabelingInput | None | Unset, data)

        labeling_inputs = _parse_labeling_inputs(d.pop("labeling_inputs", UNSET))

        def _parse_provider(data: object) -> LLMProvider | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provider_type_0 = LLMProvider(data)

                return provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LLMProvider | None | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        def _parse_model_name(data: object) -> AnthropicModel | GoogleModel | None | OpenAIModel | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_name_type_0 = OpenAIModel(data)

                return model_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_name_type_1 = GoogleModel(data)

                return model_name_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_name_type_2 = AnthropicModel(data)

                return model_name_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AnthropicModel | GoogleModel | None | OpenAIModel | Unset, data)

        model_name = _parse_model_name(d.pop("model_name", UNSET))

        include_summary = d.pop("include_summary", UNSET)

        include_keywords = d.pop("include_keywords", UNSET)

        max_samples_per_cluster = d.pop("max_samples_per_cluster", UNSET)

        sample_text_max_length = d.pop("sample_text_max_length", UNSET)

        use_embedding_dedup = d.pop("use_embedding_dedup", UNSET)

        embedding_similarity_threshold = d.pop("embedding_similarity_threshold", UNSET)

        cache_ttl_seconds = d.pop("cache_ttl_seconds", UNSET)

        def _parse_custom_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_prompt = _parse_custom_prompt(d.pop("custom_prompt", UNSET))

        def _parse_response_shape(data: object) -> LLMLabelingResponseShapeType1 | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_shape_type_1 = LLMLabelingResponseShapeType1.from_dict(data)

                return response_shape_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LLMLabelingResponseShapeType1 | None | str | Unset, data)

        response_shape = _parse_response_shape(d.pop("response_shape", UNSET))

        _parameters = d.pop("parameters", UNSET)
        parameters: LLMLabelingParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = LLMLabelingParameters.from_dict(_parameters)

        llm_labeling = cls(
            enabled=enabled,
            labeling_inputs=labeling_inputs,
            provider=provider,
            model_name=model_name,
            include_summary=include_summary,
            include_keywords=include_keywords,
            max_samples_per_cluster=max_samples_per_cluster,
            sample_text_max_length=sample_text_max_length,
            use_embedding_dedup=use_embedding_dedup,
            embedding_similarity_threshold=embedding_similarity_threshold,
            cache_ttl_seconds=cache_ttl_seconds,
            custom_prompt=custom_prompt,
            response_shape=response_shape,
            parameters=parameters,
        )

        llm_labeling.additional_properties = d
        return llm_labeling

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
