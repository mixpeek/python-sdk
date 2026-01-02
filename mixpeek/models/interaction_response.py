from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.interaction_type import InteractionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interaction_response_metadata_type_0 import InteractionResponseMetadataType0
    from ..models.interaction_response_query_snapshot_type_0 import InteractionResponseQuerySnapshotType0


T = TypeVar("T", bound="InteractionResponse")


@_attrs_define
class InteractionResponse:
    """Response model for a stored interaction.

    Extends SearchInteraction with system-assigned fields.

        Attributes:
            feature_id (str): ID of the document/feature that was interacted with. REQUIRED. This should be the document_id
                returned in retriever results. Used to track which specific items users engage with.
            interaction_type (list[InteractionType]): List of interaction types that occurred. REQUIRED. Multiple types can
                be recorded simultaneously (e.g., VIEW + CLICK + LONG_VIEW for a result the user engaged with). Use the
                InteractionType enum values.
            position (int): Position in search results where interaction occurred (0-indexed). REQUIRED. Critical for
                Learning to Rank - helps identify position bias. E.g., position=0 means first result, position=9 means 10th
                result. Higher engagement at lower positions suggests higher quality.
            interaction_id (str): Unique identifier for this interaction record. System-assigned UUID. Use this to reference
                the interaction in subsequent requests.
            metadata (InteractionResponseMetadataType0 | None | Unset): Additional context about the interaction. NOT
                REQUIRED. Can include device, duration, viewport info, etc. Use this to enrich interaction data with
                application-specific context.
            user_id (None | str | Unset): Customer's authenticated user identifier. NOT REQUIRED. Persists across sessions
                for long-term tracking. Enables personalization and user-specific metrics. Use your application's user ID
                format.
            session_id (None | str | Unset): Temporary identifier for a single search session. NOT REQUIRED. Typically
                30min-1hr duration. Tracks anonymous and authenticated users within a session. Use to group related queries and
                understand search journeys.
            execution_id (None | str | Unset): ID of the retriever execution that generated these results. NOT REQUIRED but
                HIGHLY RECOMMENDED for training and optimization. Links the interaction back to the exact search query, pipeline
                configuration, and stage execution that produced the results the user saw. Essential for: fine-tuning
                embeddings, training rerankers, query understanding, and tracing which pipeline configs produce better user
                engagement. Retrieve from the retriever execution response and pass to interactions.
            retriever_id (None | str | Unset): ID of the retriever that was executed. NOT REQUIRED but RECOMMENDED for
                multi-retriever analytics. Enables comparing performance across different retriever configurations. If
                execution_id is provided, retriever_id can be inferred from the execution record.
            query_snapshot (InteractionResponseQuerySnapshotType0 | None | Unset): Snapshot of the query input that
                generated these results. HIGHLY RECOMMENDED for training optimization. Storing the query directly enables
                10-100x faster training data extraction by avoiding expensive joins to execution records. Use the same format as
                retriever query input (e.g., {'text': '...', 'filters': {...}}). Essential for: embedding fine-tuning (query-
                document pairs), query expansion learning, and analyzing which query patterns lead to better engagement. NOT
                REQUIRED but strongly recommended for production use cases involving model training.
            document_score (float | None | Unset): Initial retrieval score of this document when shown to the user. HIGHLY
                RECOMMENDED for Learning to Rank (LTR). This is a critical feature for reranker training - helps the model learn
                how to adjust initial scores based on user engagement. Should match the score from the retriever execution
                results. NOT REQUIRED but strongly recommended for LTR and reranker training.
            result_set_size (int | None | Unset): Total number of results shown to the user in this search. NOT REQUIRED but
                useful for context. Helps understand interaction patterns - clicking position 5 of 10 results is different from
                position 5 of 100 results. Useful for position bias correction and CTR analysis.
            timestamp (None | str | Unset): ISO 8601 timestamp when the interaction was recorded. System-assigned. Used for
                time-based analysis, training data recency weighting, and temporal trends in user behavior.
    """

    feature_id: str
    interaction_type: list[InteractionType]
    position: int
    interaction_id: str
    metadata: InteractionResponseMetadataType0 | None | Unset = UNSET
    user_id: None | str | Unset = UNSET
    session_id: None | str | Unset = UNSET
    execution_id: None | str | Unset = UNSET
    retriever_id: None | str | Unset = UNSET
    query_snapshot: InteractionResponseQuerySnapshotType0 | None | Unset = UNSET
    document_score: float | None | Unset = UNSET
    result_set_size: int | None | Unset = UNSET
    timestamp: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.interaction_response_metadata_type_0 import InteractionResponseMetadataType0
        from ..models.interaction_response_query_snapshot_type_0 import InteractionResponseQuerySnapshotType0

        feature_id = self.feature_id

        interaction_type = []
        for interaction_type_item_data in self.interaction_type:
            interaction_type_item = interaction_type_item_data.value
            interaction_type.append(interaction_type_item)

        position = self.position

        interaction_id = self.interaction_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, InteractionResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        session_id: None | str | Unset
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        execution_id: None | str | Unset
        if isinstance(self.execution_id, Unset):
            execution_id = UNSET
        else:
            execution_id = self.execution_id

        retriever_id: None | str | Unset
        if isinstance(self.retriever_id, Unset):
            retriever_id = UNSET
        else:
            retriever_id = self.retriever_id

        query_snapshot: dict[str, Any] | None | Unset
        if isinstance(self.query_snapshot, Unset):
            query_snapshot = UNSET
        elif isinstance(self.query_snapshot, InteractionResponseQuerySnapshotType0):
            query_snapshot = self.query_snapshot.to_dict()
        else:
            query_snapshot = self.query_snapshot

        document_score: float | None | Unset
        if isinstance(self.document_score, Unset):
            document_score = UNSET
        else:
            document_score = self.document_score

        result_set_size: int | None | Unset
        if isinstance(self.result_set_size, Unset):
            result_set_size = UNSET
        else:
            result_set_size = self.result_set_size

        timestamp: None | str | Unset
        if isinstance(self.timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feature_id": feature_id,
                "interaction_type": interaction_type,
                "position": position,
                "interaction_id": interaction_id,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if execution_id is not UNSET:
            field_dict["execution_id"] = execution_id
        if retriever_id is not UNSET:
            field_dict["retriever_id"] = retriever_id
        if query_snapshot is not UNSET:
            field_dict["query_snapshot"] = query_snapshot
        if document_score is not UNSET:
            field_dict["document_score"] = document_score
        if result_set_size is not UNSET:
            field_dict["result_set_size"] = result_set_size
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interaction_response_metadata_type_0 import InteractionResponseMetadataType0
        from ..models.interaction_response_query_snapshot_type_0 import InteractionResponseQuerySnapshotType0

        d = dict(src_dict)
        feature_id = d.pop("feature_id")

        interaction_type = []
        _interaction_type = d.pop("interaction_type")
        for interaction_type_item_data in _interaction_type:
            interaction_type_item = InteractionType(interaction_type_item_data)

            interaction_type.append(interaction_type_item)

        position = d.pop("position")

        interaction_id = d.pop("interaction_id")

        def _parse_metadata(data: object) -> InteractionResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = InteractionResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InteractionResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_id = _parse_session_id(d.pop("session_id", UNSET))

        def _parse_execution_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        execution_id = _parse_execution_id(d.pop("execution_id", UNSET))

        def _parse_retriever_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retriever_id = _parse_retriever_id(d.pop("retriever_id", UNSET))

        def _parse_query_snapshot(data: object) -> InteractionResponseQuerySnapshotType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                query_snapshot_type_0 = InteractionResponseQuerySnapshotType0.from_dict(data)

                return query_snapshot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InteractionResponseQuerySnapshotType0 | None | Unset, data)

        query_snapshot = _parse_query_snapshot(d.pop("query_snapshot", UNSET))

        def _parse_document_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        document_score = _parse_document_score(d.pop("document_score", UNSET))

        def _parse_result_set_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        result_set_size = _parse_result_set_size(d.pop("result_set_size", UNSET))

        def _parse_timestamp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

        interaction_response = cls(
            feature_id=feature_id,
            interaction_type=interaction_type,
            position=position,
            interaction_id=interaction_id,
            metadata=metadata,
            user_id=user_id,
            session_id=session_id,
            execution_id=execution_id,
            retriever_id=retriever_id,
            query_snapshot=query_snapshot,
            document_score=document_score,
            result_set_size=result_set_size,
            timestamp=timestamp,
        )

        interaction_response.additional_properties = d
        return interaction_response

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
