from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sample_stage_config_strategy import SampleStageConfigStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="SampleStageConfig")


@_attrs_define
class SampleStageConfig:
    """Configuration for document sampling.

    **Stage Category**: REDUCE

    **Transformation**: N documents → M documents (where M ≤ N)

    **Purpose**: Sample a subset of documents using random or stratified sampling.
    Operates on in-memory results from previous stages.

    **When to Use**:
        - A/B testing different pipeline configurations
        - Reducing result set for expensive downstream stages
        - Exploration and discovery features
        - Ensuring proportional representation across categories
        - Creating reproducible experiments with seeded sampling

    **When NOT to Use**:
        - When you need all results (just use previous stage output)
        - For ranking/reordering (use SORT stages)
        - For filtering by criteria (use FILTER stages)

    **Sampling Strategies**:
        - `random`: Uniform random sampling
        - `stratified`: Proportional sampling across a field's values
        - `reservoir`: Reservoir sampling (for streaming scenarios)

    **Common Pipeline Position**: feature_search → (expensive stages) → sample

    Examples:
        Basic random sampling:
            ```json
            {
                "count": 10,
                "strategy": "random"
            }
            ```

        Stratified sampling by category:
            ```json
            {
                "count": 20,
                "strategy": "stratified",
                "stratify_by": "metadata.category"
            }
            ```

        Reproducible sampling with seed:
            ```json
            {
                "count": 50,
                "strategy": "random",
                "seed": 42
            }
            ```

        Preserve top results, sample rest:
            ```json
            {
                "count": 10,
                "strategy": "random",
                "preserve_top_k": 3
            }
            ```

        Attributes:
            count (int | Unset): REQUIRED. Number of documents to sample. If count > available documents, returns all
                documents. Default: 10.
            strategy (SampleStageConfigStrategy | Unset): OPTIONAL. Sampling strategy:
                - 'random': Uniform random sampling (default)
                - 'stratified': Proportional sampling across stratify_by field values
                - 'reservoir': Reservoir sampling (memory-efficient for large sets) Default: SampleStageConfigStrategy.RANDOM.
            stratify_by (None | str | Unset): OPTIONAL. Field to stratify on (required when strategy='stratified'). Samples
                proportionally from each unique value of this field. Supports dot notation for nested fields.
            min_per_stratum (int | Unset): OPTIONAL. Minimum documents per stratum (stratified mode). Ensures each category
                gets at least this many documents. Default: 1.
            seed (int | None | Unset): OPTIONAL. Random seed for reproducible sampling. Same seed + same input = same
                output. Leave None for non-deterministic sampling.
            preserve_top_k (int | Unset): OPTIONAL. Always keep the top K documents by score, sample from remainder. Useful
                when you want to guarantee top results are included. Default: 0 (no preservation, sample from all). Default: 0.
    """

    count: int | Unset = 10
    strategy: SampleStageConfigStrategy | Unset = SampleStageConfigStrategy.RANDOM
    stratify_by: None | str | Unset = UNSET
    min_per_stratum: int | Unset = 1
    seed: int | None | Unset = UNSET
    preserve_top_k: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        strategy: str | Unset = UNSET
        if not isinstance(self.strategy, Unset):
            strategy = self.strategy.value

        stratify_by: None | str | Unset
        if isinstance(self.stratify_by, Unset):
            stratify_by = UNSET
        else:
            stratify_by = self.stratify_by

        min_per_stratum = self.min_per_stratum

        seed: int | None | Unset
        if isinstance(self.seed, Unset):
            seed = UNSET
        else:
            seed = self.seed

        preserve_top_k = self.preserve_top_k

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if strategy is not UNSET:
            field_dict["strategy"] = strategy
        if stratify_by is not UNSET:
            field_dict["stratify_by"] = stratify_by
        if min_per_stratum is not UNSET:
            field_dict["min_per_stratum"] = min_per_stratum
        if seed is not UNSET:
            field_dict["seed"] = seed
        if preserve_top_k is not UNSET:
            field_dict["preserve_top_k"] = preserve_top_k

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        _strategy = d.pop("strategy", UNSET)
        strategy: SampleStageConfigStrategy | Unset
        if isinstance(_strategy, Unset):
            strategy = UNSET
        else:
            strategy = SampleStageConfigStrategy(_strategy)

        def _parse_stratify_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stratify_by = _parse_stratify_by(d.pop("stratify_by", UNSET))

        min_per_stratum = d.pop("min_per_stratum", UNSET)

        def _parse_seed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        seed = _parse_seed(d.pop("seed", UNSET))

        preserve_top_k = d.pop("preserve_top_k", UNSET)

        sample_stage_config = cls(
            count=count,
            strategy=strategy,
            stratify_by=stratify_by,
            min_per_stratum=min_per_stratum,
            seed=seed,
            preserve_top_k=preserve_top_k,
        )

        sample_stage_config.additional_properties = d
        return sample_stage_config

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
