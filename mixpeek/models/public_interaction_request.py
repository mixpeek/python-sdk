from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.interaction_type import InteractionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_interaction_request_metadata_type_0 import PublicInteractionRequestMetadataType0
    from ..models.public_interaction_request_query_snapshot_type_0 import PublicInteractionRequestQuerySnapshotType0


T = TypeVar("T", bound="PublicInteractionRequest")


@_attrs_define
class PublicInteractionRequest:
    """Request to track a single interaction from public retriever.

    Simplified wrapper around SearchInteraction for public API use.

        Attributes:
            document_id (str): ID of the document that was interacted with (from search results)
            interaction_type (list[InteractionType]): Type(s) of interaction that occurred
            position (int): Position in search results (0-indexed)
            execution_id (None | str | Unset): ID of the retriever execution that generated these results. HIGHLY
                RECOMMENDED for analytics.
            query_snapshot (None | PublicInteractionRequestQuerySnapshotType0 | Unset): Snapshot of the query that generated
                these results. HIGHLY RECOMMENDED for training optimization.
            document_score (float | None | Unset): Initial retrieval score of this document
            result_set_size (int | None | Unset): Total number of results shown
            session_id (None | str | Unset): Session identifier for tracking user journey
            metadata (None | PublicInteractionRequestMetadataType0 | Unset): Additional context about the interaction
    """

    document_id: str
    interaction_type: list[InteractionType]
    position: int
    execution_id: None | str | Unset = UNSET
    query_snapshot: None | PublicInteractionRequestQuerySnapshotType0 | Unset = UNSET
    document_score: float | None | Unset = UNSET
    result_set_size: int | None | Unset = UNSET
    session_id: None | str | Unset = UNSET
    metadata: None | PublicInteractionRequestMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.public_interaction_request_metadata_type_0 import PublicInteractionRequestMetadataType0
        from ..models.public_interaction_request_query_snapshot_type_0 import PublicInteractionRequestQuerySnapshotType0

        document_id = self.document_id

        interaction_type = []
        for interaction_type_item_data in self.interaction_type:
            interaction_type_item = interaction_type_item_data.value
            interaction_type.append(interaction_type_item)

        position = self.position

        execution_id: None | str | Unset
        if isinstance(self.execution_id, Unset):
            execution_id = UNSET
        else:
            execution_id = self.execution_id

        query_snapshot: dict[str, Any] | None | Unset
        if isinstance(self.query_snapshot, Unset):
            query_snapshot = UNSET
        elif isinstance(self.query_snapshot, PublicInteractionRequestQuerySnapshotType0):
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

        session_id: None | str | Unset
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PublicInteractionRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document_id": document_id,
                "interaction_type": interaction_type,
                "position": position,
            }
        )
        if execution_id is not UNSET:
            field_dict["execution_id"] = execution_id
        if query_snapshot is not UNSET:
            field_dict["query_snapshot"] = query_snapshot
        if document_score is not UNSET:
            field_dict["document_score"] = document_score
        if result_set_size is not UNSET:
            field_dict["result_set_size"] = result_set_size
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_interaction_request_metadata_type_0 import PublicInteractionRequestMetadataType0
        from ..models.public_interaction_request_query_snapshot_type_0 import PublicInteractionRequestQuerySnapshotType0

        d = dict(src_dict)
        document_id = d.pop("document_id")

        interaction_type = []
        _interaction_type = d.pop("interaction_type")
        for interaction_type_item_data in _interaction_type:
            interaction_type_item = InteractionType(interaction_type_item_data)

            interaction_type.append(interaction_type_item)

        position = d.pop("position")

        def _parse_execution_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        execution_id = _parse_execution_id(d.pop("execution_id", UNSET))

        def _parse_query_snapshot(data: object) -> None | PublicInteractionRequestQuerySnapshotType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                query_snapshot_type_0 = PublicInteractionRequestQuerySnapshotType0.from_dict(data)

                return query_snapshot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublicInteractionRequestQuerySnapshotType0 | Unset, data)

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

        def _parse_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_id = _parse_session_id(d.pop("session_id", UNSET))

        def _parse_metadata(data: object) -> None | PublicInteractionRequestMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = PublicInteractionRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublicInteractionRequestMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        public_interaction_request = cls(
            document_id=document_id,
            interaction_type=interaction_type,
            position=position,
            execution_id=execution_id,
            query_snapshot=query_snapshot,
            document_score=document_score,
            result_set_size=result_set_size,
            session_id=session_id,
            metadata=metadata,
        )

        public_interaction_request.additional_properties = d
        return public_interaction_request

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
