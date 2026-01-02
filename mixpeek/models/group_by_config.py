from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_by_config_output_mode import GroupByConfigOutputMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupByConfig")


@_attrs_define
class GroupByConfig:
    """Configuration for grouping documents by field value.

    Stage Category: REDUCE

    Transformation: N documents → M groups (where M ≤ N)

    Purpose: Groups documents by a common field value, aggregating chunks
    back to parent objects. Essential for decompose/recompose workflows
    where chunks are searched individually then grouped to show context.

    Performance: Runs in API layer (fast stage, ~10-50ms for 100-500 docs).
    Integrates with optimizer for filter push-down before grouping. Future
    optimization will push grouping into Qdrant for 10-100x speedup.

    When to Use:
        - After chunk-level search to group back to objects
        - To deduplicate results by a field
        - To aggregate related documents
        - For decompose→search→recompose workflows
        - Show top N results per category/author/parent

    When NOT to Use:
        - For initial document retrieval (use FILTER stages: hybrid_search)
        - For ordering documents (use SORT stages: sort_relevance)
        - For enriching documents (use APPLY stages: document_enrich)
        - For expanding documents (use APPLY 1-N stages: taxonomy_enrich)

    Operational Behavior:
        - Fast stage: runs in API layer (no Engine delegation)
        - In-memory grouping: Python dict-based grouping
        - Groups documents with same field value
        - Sorts within groups by score (highest first)
        - Limits documents per group (configurable)
        - Reports metrics to ClickHouse for learned optimizations

    Common Pipeline Position: FILTER → SORT → REDUCE (this stage)

    Requirements:
        - group_by_field: REQUIRED
        - max_per_group: OPTIONAL, defaults to 10
        - output_mode: OPTIONAL, defaults to "all"

    Use Cases:
        - Decompose/recompose: Search 50 scenes, group to 10 videos
        - Deduplication: Group by unique_id, keep top match
        - Analytics: Group by category, show top docs per category
        - Multi-tier results: Show top 3 products per brand

    Examples:
        - Group video scenes back to parent videos
        - Deduplicate search results by product_id
        - Show top 3 articles per author
        - Display best match per category

        Attributes:
            group_by_field (str | Unset): Field path to group documents by using dot notation. Documents with the same field
                value are grouped together. Common fields: 'source_object_id' (parent object from decomposition),
                'root_object_id' (top-level ancestor in hierarchy), 'metadata.category' (nested categorical field), 'video_id'
                (media grouping), 'product_id' (e-commerce). Use dot notation for nested fields: 'metadata.user_id',
                'lineage.source_id'. Performance: Indexed fields are faster for future Qdrant native grouping optimization.
                Template support: Use {{inputs.group_field}} for dynamic grouping. Default: 'source_object_id'.
            max_per_group (int | Unset): OPTIONAL. Maximum number of documents to keep per group. Documents are sorted by
                score (highest first) before limiting. Default: 10. Use 1 for deduplication (keeps only highest scoring doc per
                group). Use 3-5 for preview results (show top chunks per parent). Use 50+ for comprehensive results (show many
                chunks per parent). Performance: Lower values reduce response size and improve latency. Typical values: 1
                (dedup), 5 (preview), 10 (default), 20 (detailed), 50 (comprehensive). Default: 10.
            output_mode (GroupByConfigOutputMode | Unset): OPTIONAL. Controls what documents are returned per group.
                'first': Return only the top document per group (deduplication, fastest).          Use for: unique results per
                group (e.g., one video per brand). 'all': Return all documents grouped by field (default, shows full context).
                Use for: showing chunks within each parent object. 'flatten': Return all documents as flat list (loses group
                structure).            Use for: need all docs but don't care about grouping metadata. Default: 'all'.
                Performance: 'first' is fastest (smallest response), 'all' preserves grouping, 'flatten' is lightest (no group
                metadata). Default: GroupByConfigOutputMode.ALL.
    """

    group_by_field: str | Unset = "source_object_id"
    max_per_group: int | Unset = 10
    output_mode: GroupByConfigOutputMode | Unset = GroupByConfigOutputMode.ALL
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_by_field = self.group_by_field

        max_per_group = self.max_per_group

        output_mode: str | Unset = UNSET
        if not isinstance(self.output_mode, Unset):
            output_mode = self.output_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_by_field is not UNSET:
            field_dict["group_by_field"] = group_by_field
        if max_per_group is not UNSET:
            field_dict["max_per_group"] = max_per_group
        if output_mode is not UNSET:
            field_dict["output_mode"] = output_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_by_field = d.pop("group_by_field", UNSET)

        max_per_group = d.pop("max_per_group", UNSET)

        _output_mode = d.pop("output_mode", UNSET)
        output_mode: GroupByConfigOutputMode | Unset
        if isinstance(_output_mode, Unset):
            output_mode = UNSET
        else:
            output_mode = GroupByConfigOutputMode(_output_mode)

        group_by_config = cls(
            group_by_field=group_by_field,
            max_per_group=max_per_group,
            output_mode=output_mode,
        )

        group_by_config.additional_properties = d
        return group_by_config

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
