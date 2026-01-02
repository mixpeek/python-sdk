from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.query_expand_parameters_fusion_strategy import QueryExpandParametersFusionStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_expand_parameters_feature_search_config import QueryExpandParametersFeatureSearchConfig


T = TypeVar("T", bound="QueryExpandParameters")


@_attrs_define
class QueryExpandParameters:
    """Parameters for query expansion stage.

    This stage:
    1. Takes your original query
    2. Uses an LLM to generate semantically similar query variations
    3. Executes feature_search for each variation (original + expansions)
    4. Fuses results using Reciprocal Rank Fusion (RRF)

    Example - Basic query expansion (copy and run):
        ```python
        {
            "stages": [
                {
                    "stage": "query_expand",
                    "parameters": {
                        "num_expansions": 3,
                        "feature_search_config": {
                            "query": {"text": "{{INPUT.query}}"},
                            "feature_extractors": [
                                {"field_name": "content.text", "embedding_model": "text"}
                            ],
                            "top_k": 10
                        }
                    }
                }
            ]
        }
        ```

    Example - With custom expansion prompt:
        ```python
        {
            "stages": [
                {
                    "stage": "query_expand",
                    "parameters": {
                        "num_expansions": 5,
                        "expansion_prompt": "Generate {{NUM_EXPANSIONS}} alternative search queries for: {{QUERY}}.
    Focus on synonyms and related concepts. Return one query per line.",
                        "feature_search_config": {
                            "query": {"text": "{{INPUT.query}}"},
                            "feature_extractors": [
                                {"field_name": "content.text", "embedding_model": "text"}
                            ],
                            "top_k": 20
                        },
                        "rrf_k": 60
                    }
                }
            ]
        }

    Example - Multimodal query expansion:
        ```python
        {
            "stages": [
                {
                    "stage": "query_expand",
                    "parameters": {
                        "num_expansions": 3,
                        "feature_search_config": {
                            "query": {"text": "{{INPUT.query}}", "image": "{{INPUT.image_url}}"},
                            "feature_extractors": [
                                {"field_name": "content.text", "embedding_model": "text"},
                                {"field_name": "content.image", "embedding_model": "multimodal"}
                            ],
                            "top_k": 15
                        },
                        "include_original": true
                    }
                }
            ]
        }

    How it works:
        1. The original query (from feature_search_config.query.text) is sent to an LLM
        2. LLM generates `num_expansions` alternative queries
        3. feature_search runs for original query + each expansion
        4. Results are fused using RRF: score = sum(1 / (k + rank)) across all queries
        5. Documents appearing in multiple result sets get boosted

    Why use query expansion:
        - Handles vocabulary mismatch (user says "car", docs say "vehicle")
        - Captures related concepts the user might not have thought of
        - Improves recall without sacrificing precision (RRF handles fusion)
        - Works with any feature_search configuration (text, image, multimodal)

        Attributes:
            feature_search_config (QueryExpandParametersFeatureSearchConfig): Full feature_search configuration. This is the
                same config you would pass to a standalone feature_search stage. The query.text field will be replaced with each
                expanded query.
            num_expansions (int | Unset): Number of query variations to generate. More expansions = better recall but
                slower. Default: 3.
            expansion_prompt (None | str | Unset): Custom prompt for query expansion. Use {{QUERY}} for the original query
                and {{NUM_EXPANSIONS}} for the count. If not provided, uses a default prompt.
            expansion_model (str | Unset): LLM model to use for generating query expansions. Default: 'gpt-4o-mini'.
            include_original (bool | Unset): Whether to include the original query in addition to expansions. Default: True.
            rrf_k (int | Unset): RRF constant k. Higher values give more weight to lower-ranked results. Default of 60 is
                standard. Use lower (20-40) for precision, higher (80-100) for recall. Default: 60.
            fusion_strategy (QueryExpandParametersFusionStrategy | Unset): How to fuse results from multiple queries. 'rrf'
                = Reciprocal Rank Fusion (recommended), 'linear' = simple score averaging. Default:
                QueryExpandParametersFusionStrategy.RRF.
            deduplicate (bool | Unset): Whether to deduplicate results by document_id before returning. Default: True.
    """

    feature_search_config: QueryExpandParametersFeatureSearchConfig
    num_expansions: int | Unset = 3
    expansion_prompt: None | str | Unset = UNSET
    expansion_model: str | Unset = "gpt-4o-mini"
    include_original: bool | Unset = True
    rrf_k: int | Unset = 60
    fusion_strategy: QueryExpandParametersFusionStrategy | Unset = QueryExpandParametersFusionStrategy.RRF
    deduplicate: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_search_config = self.feature_search_config.to_dict()

        num_expansions = self.num_expansions

        expansion_prompt: None | str | Unset
        if isinstance(self.expansion_prompt, Unset):
            expansion_prompt = UNSET
        else:
            expansion_prompt = self.expansion_prompt

        expansion_model = self.expansion_model

        include_original = self.include_original

        rrf_k = self.rrf_k

        fusion_strategy: str | Unset = UNSET
        if not isinstance(self.fusion_strategy, Unset):
            fusion_strategy = self.fusion_strategy.value

        deduplicate = self.deduplicate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feature_search_config": feature_search_config,
            }
        )
        if num_expansions is not UNSET:
            field_dict["num_expansions"] = num_expansions
        if expansion_prompt is not UNSET:
            field_dict["expansion_prompt"] = expansion_prompt
        if expansion_model is not UNSET:
            field_dict["expansion_model"] = expansion_model
        if include_original is not UNSET:
            field_dict["include_original"] = include_original
        if rrf_k is not UNSET:
            field_dict["rrf_k"] = rrf_k
        if fusion_strategy is not UNSET:
            field_dict["fusion_strategy"] = fusion_strategy
        if deduplicate is not UNSET:
            field_dict["deduplicate"] = deduplicate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_expand_parameters_feature_search_config import QueryExpandParametersFeatureSearchConfig

        d = dict(src_dict)
        feature_search_config = QueryExpandParametersFeatureSearchConfig.from_dict(d.pop("feature_search_config"))

        num_expansions = d.pop("num_expansions", UNSET)

        def _parse_expansion_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expansion_prompt = _parse_expansion_prompt(d.pop("expansion_prompt", UNSET))

        expansion_model = d.pop("expansion_model", UNSET)

        include_original = d.pop("include_original", UNSET)

        rrf_k = d.pop("rrf_k", UNSET)

        _fusion_strategy = d.pop("fusion_strategy", UNSET)
        fusion_strategy: QueryExpandParametersFusionStrategy | Unset
        if isinstance(_fusion_strategy, Unset):
            fusion_strategy = UNSET
        else:
            fusion_strategy = QueryExpandParametersFusionStrategy(_fusion_strategy)

        deduplicate = d.pop("deduplicate", UNSET)

        query_expand_parameters = cls(
            feature_search_config=feature_search_config,
            num_expansions=num_expansions,
            expansion_prompt=expansion_prompt,
            expansion_model=expansion_model,
            include_original=include_original,
            rrf_k=rrf_k,
            fusion_strategy=fusion_strategy,
            deduplicate=deduplicate,
        )

        query_expand_parameters.additional_properties = d
        return query_expand_parameters

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
