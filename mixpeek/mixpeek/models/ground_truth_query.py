from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ground_truth_query_query_input import GroundTruthQueryQueryInput
    from ..models.ground_truth_query_relevance_scores_type_0 import GroundTruthQueryRelevanceScoresType0


T = TypeVar("T", bound="GroundTruthQuery")


@_attrs_define
class GroundTruthQuery:
    """Single query with ground truth relevance labels.

    This represents one query in an evaluation dataset, along with the list
    of documents that are considered relevant for that query.

        Attributes:
            query_id (str): Unique identifier for this query within the dataset
            query_input (GroundTruthQueryQueryInput): Query input in the same format as retriever execution (e.g., {'text':
                '...'})
            relevant_documents (list[str]): List of feature_ids that are relevant for this query
            relevance_scores (GroundTruthQueryRelevanceScoresType0 | None | Unset): Optional graded relevance scores (doc_id
                -> score, 0-5 where 5 is most relevant). Used for NDCG calculation.
    """

    query_id: str
    query_input: GroundTruthQueryQueryInput
    relevant_documents: list[str]
    relevance_scores: GroundTruthQueryRelevanceScoresType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ground_truth_query_relevance_scores_type_0 import GroundTruthQueryRelevanceScoresType0

        query_id = self.query_id

        query_input = self.query_input.to_dict()

        relevant_documents = self.relevant_documents

        relevance_scores: dict[str, Any] | None | Unset
        if isinstance(self.relevance_scores, Unset):
            relevance_scores = UNSET
        elif isinstance(self.relevance_scores, GroundTruthQueryRelevanceScoresType0):
            relevance_scores = self.relevance_scores.to_dict()
        else:
            relevance_scores = self.relevance_scores

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query_id": query_id,
                "query_input": query_input,
                "relevant_documents": relevant_documents,
            }
        )
        if relevance_scores is not UNSET:
            field_dict["relevance_scores"] = relevance_scores

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ground_truth_query_query_input import GroundTruthQueryQueryInput
        from ..models.ground_truth_query_relevance_scores_type_0 import GroundTruthQueryRelevanceScoresType0

        d = dict(src_dict)
        query_id = d.pop("query_id")

        query_input = GroundTruthQueryQueryInput.from_dict(d.pop("query_input"))

        relevant_documents = cast(list[str], d.pop("relevant_documents"))

        def _parse_relevance_scores(data: object) -> GroundTruthQueryRelevanceScoresType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                relevance_scores_type_0 = GroundTruthQueryRelevanceScoresType0.from_dict(data)

                return relevance_scores_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GroundTruthQueryRelevanceScoresType0 | None | Unset, data)

        relevance_scores = _parse_relevance_scores(d.pop("relevance_scores", UNSET))

        ground_truth_query = cls(
            query_id=query_id,
            query_input=query_input,
            relevant_documents=relevant_documents,
            relevance_scores=relevance_scores,
        )

        ground_truth_query.additional_properties = d
        return ground_truth_query

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
