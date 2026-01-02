from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SuitableCollection")


@_attrs_define
class SuitableCollection:
    """Information about a collection that might fulfill the user's request.

    Attributes:
        collection_id: Collection identifier
        collection_name: Human-readable collection name
        feature_extractor: Extractor used in this collection
        capabilities: What this collection can do (e.g., "video search", "face detection")
        match_score: How well this collection matches the request (0.0-1.0)

        Attributes:
            collection_id (str): Collection ID
            collection_name (str): Collection name
            feature_extractor (str): Feature extractor name
            match_score (float): Match confidence
            capabilities (list[str] | Unset): Collection capabilities
    """

    collection_id: str
    collection_name: str
    feature_extractor: str
    match_score: float
    capabilities: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_id = self.collection_id

        collection_name = self.collection_name

        feature_extractor = self.feature_extractor

        match_score = self.match_score

        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_id": collection_id,
                "collection_name": collection_name,
                "feature_extractor": feature_extractor,
                "match_score": match_score,
            }
        )
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection_id = d.pop("collection_id")

        collection_name = d.pop("collection_name")

        feature_extractor = d.pop("feature_extractor")

        match_score = d.pop("match_score")

        capabilities = cast(list[str], d.pop("capabilities", UNSET))

        suitable_collection = cls(
            collection_id=collection_id,
            collection_name=collection_name,
            feature_extractor=feature_extractor,
            match_score=match_score,
            capabilities=capabilities,
        )

        suitable_collection.additional_properties = d
        return suitable_collection

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
