from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LineageStep")


@_attrs_define
class LineageStep:
    """Single processing step in a document's lineage chain.

    Each step represents one transformation in the decomposition tree,
    tracking which collection and feature extractor produced the document.

    Example:
        ```python
        step = LineageStep(
            collection_id="col_video_frames",
            feature_extractor_id="multimodal_extractor_v1",
            document_id="doc_frame123",
            timestamp=datetime.now()
        )
        ```

        Attributes:
            collection_id (str): Collection ID where this processing step occurred
            feature_extractor_id (str): Feature extractor that processed the data in this step
            document_id (None | str | Unset): Document ID from this step (for intermediate steps). Allows tracing back
                through the decomposition tree.
            timestamp (datetime.datetime | Unset): When this processing step occurred
    """

    collection_id: str
    feature_extractor_id: str
    document_id: None | str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_id = self.collection_id

        feature_extractor_id = self.feature_extractor_id

        document_id: None | str | Unset
        if isinstance(self.document_id, Unset):
            document_id = UNSET
        else:
            document_id = self.document_id

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_id": collection_id,
                "feature_extractor_id": feature_extractor_id,
            }
        )
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection_id = d.pop("collection_id")

        feature_extractor_id = d.pop("feature_extractor_id")

        def _parse_document_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_id = _parse_document_id(d.pop("document_id", UNSET))

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        lineage_step = cls(
            collection_id=collection_id,
            feature_extractor_id=feature_extractor_id,
            document_id=document_id,
            timestamp=timestamp,
        )

        lineage_step.additional_properties = d
        return lineage_step

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
