from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clarification_option import ClarificationOption
    from ..models.intent_classification_keywords_found import IntentClassificationKeywordsFound
    from ..models.suitable_collection import SuitableCollection


T = TypeVar("T", bound="IntentClassification")


@_attrs_define
class IntentClassification:
    """Result of intent detection analysis.

    This model represents the agent's understanding of whether the user wants to:
    - Execute queries on existing data (execution mode)
    - Create new resources/infrastructure (setup mode)
    - Or if the request is ambiguous and needs clarification

    Attributes:
        intent: The detected intent ("execution", "setup", or "ambiguous")
        confidence: Confidence score 0.0-1.0
        reasoning: Explanation of why this intent was detected
        suitable_collections: Existing collections that might fulfill the request
        recommended_action: What the agent should do next
        clarification_needed: Whether to ask user for clarification
        clarification_options: Options to present if clarification needed
        keywords_found: Keywords that influenced the classification

        Attributes:
            intent (str): Detected intent: 'execution', 'setup', or 'ambiguous'
            confidence (float): Confidence in classification
            reasoning (str): Why this intent was detected
            recommended_action (str): Next action to take (e.g., 'setup_pipeline', 'execute_retriever')
            clarification_needed (bool): Whether to ask user for clarification
            suitable_collections (list[SuitableCollection] | Unset): Existing collections that might help
            clarification_options (list[ClarificationOption] | Unset): Options for user if clarification needed
            keywords_found (IntentClassificationKeywordsFound | Unset): Keywords found (setup_keywords, execution_keywords,
                neutral_keywords)
    """

    intent: str
    confidence: float
    reasoning: str
    recommended_action: str
    clarification_needed: bool
    suitable_collections: list[SuitableCollection] | Unset = UNSET
    clarification_options: list[ClarificationOption] | Unset = UNSET
    keywords_found: IntentClassificationKeywordsFound | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        intent = self.intent

        confidence = self.confidence

        reasoning = self.reasoning

        recommended_action = self.recommended_action

        clarification_needed = self.clarification_needed

        suitable_collections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.suitable_collections, Unset):
            suitable_collections = []
            for suitable_collections_item_data in self.suitable_collections:
                suitable_collections_item = suitable_collections_item_data.to_dict()
                suitable_collections.append(suitable_collections_item)

        clarification_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clarification_options, Unset):
            clarification_options = []
            for clarification_options_item_data in self.clarification_options:
                clarification_options_item = clarification_options_item_data.to_dict()
                clarification_options.append(clarification_options_item)

        keywords_found: dict[str, Any] | Unset = UNSET
        if not isinstance(self.keywords_found, Unset):
            keywords_found = self.keywords_found.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "intent": intent,
                "confidence": confidence,
                "reasoning": reasoning,
                "recommended_action": recommended_action,
                "clarification_needed": clarification_needed,
            }
        )
        if suitable_collections is not UNSET:
            field_dict["suitable_collections"] = suitable_collections
        if clarification_options is not UNSET:
            field_dict["clarification_options"] = clarification_options
        if keywords_found is not UNSET:
            field_dict["keywords_found"] = keywords_found

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clarification_option import ClarificationOption
        from ..models.intent_classification_keywords_found import IntentClassificationKeywordsFound
        from ..models.suitable_collection import SuitableCollection

        d = dict(src_dict)
        intent = d.pop("intent")

        confidence = d.pop("confidence")

        reasoning = d.pop("reasoning")

        recommended_action = d.pop("recommended_action")

        clarification_needed = d.pop("clarification_needed")

        _suitable_collections = d.pop("suitable_collections", UNSET)
        suitable_collections: list[SuitableCollection] | Unset = UNSET
        if _suitable_collections is not UNSET:
            suitable_collections = []
            for suitable_collections_item_data in _suitable_collections:
                suitable_collections_item = SuitableCollection.from_dict(suitable_collections_item_data)

                suitable_collections.append(suitable_collections_item)

        _clarification_options = d.pop("clarification_options", UNSET)
        clarification_options: list[ClarificationOption] | Unset = UNSET
        if _clarification_options is not UNSET:
            clarification_options = []
            for clarification_options_item_data in _clarification_options:
                clarification_options_item = ClarificationOption.from_dict(clarification_options_item_data)

                clarification_options.append(clarification_options_item)

        _keywords_found = d.pop("keywords_found", UNSET)
        keywords_found: IntentClassificationKeywordsFound | Unset
        if isinstance(_keywords_found, Unset):
            keywords_found = UNSET
        else:
            keywords_found = IntentClassificationKeywordsFound.from_dict(_keywords_found)

        intent_classification = cls(
            intent=intent,
            confidence=confidence,
            reasoning=reasoning,
            recommended_action=recommended_action,
            clarification_needed=clarification_needed,
            suitable_collections=suitable_collections,
            clarification_options=clarification_options,
            keywords_found=keywords_found,
        )

        intent_classification.additional_properties = d
        return intent_classification

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
