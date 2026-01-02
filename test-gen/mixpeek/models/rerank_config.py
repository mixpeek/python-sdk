from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RerankConfig")


@_attrs_define
class RerankConfig:
    """Configuration for reranking documents using cross-encoder models.

    Reranking refines search results by computing query-document relevance
    scores using cross-encoder models (e.g., BGE reranker). More accurate
    than vector similarity but slower, so typically used on top-K results.

    Common Pipeline:
        feature_filter (retrieve 100) → rerank (refine to 10) → sort_relevance

        Attributes:
            inference_name (str | Unset): Reranking inference service name. Must be a reranking service. Use GET
                /engine/inference to list available rerankers. Default: 'baai_bge_reranker_v2_m3'.
            query (str | Unset): Query text to compare against documents. Supports template variables: {{INPUT.query}}, etc.
                Default: '{{INPUT.query}}'.
            document_field (str | Unset): Document field path containing text to rerank against Default: 'content'.
            top_k (int | None | Unset): Number of top documents to keep after reranking. If None, returns all documents in
                reranked order.
            score_field (str | Unset): Document field path to store reranking scores Default: 'scores.rerank'.
            batch_size (int | Unset): Batch size for reranking inference calls Default: 32.
    """

    inference_name: str | Unset = "baai_bge_reranker_v2_m3"
    query: str | Unset = "{{INPUT.query}}"
    document_field: str | Unset = "content"
    top_k: int | None | Unset = UNSET
    score_field: str | Unset = "scores.rerank"
    batch_size: int | Unset = 32
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inference_name = self.inference_name

        query = self.query

        document_field = self.document_field

        top_k: int | None | Unset
        if isinstance(self.top_k, Unset):
            top_k = UNSET
        else:
            top_k = self.top_k

        score_field = self.score_field

        batch_size = self.batch_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inference_name is not UNSET:
            field_dict["inference_name"] = inference_name
        if query is not UNSET:
            field_dict["query"] = query
        if document_field is not UNSET:
            field_dict["document_field"] = document_field
        if top_k is not UNSET:
            field_dict["top_k"] = top_k
        if score_field is not UNSET:
            field_dict["score_field"] = score_field
        if batch_size is not UNSET:
            field_dict["batch_size"] = batch_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inference_name = d.pop("inference_name", UNSET)

        query = d.pop("query", UNSET)

        document_field = d.pop("document_field", UNSET)

        def _parse_top_k(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        top_k = _parse_top_k(d.pop("top_k", UNSET))

        score_field = d.pop("score_field", UNSET)

        batch_size = d.pop("batch_size", UNSET)

        rerank_config = cls(
            inference_name=inference_name,
            query=query,
            document_field=document_field,
            top_k=top_k,
            score_field=score_field,
            batch_size=batch_size,
        )

        rerank_config.additional_properties = d
        return rerank_config

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
