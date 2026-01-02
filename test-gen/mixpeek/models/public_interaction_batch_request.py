from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.public_interaction_request import PublicInteractionRequest


T = TypeVar("T", bound="PublicInteractionBatchRequest")


@_attrs_define
class PublicInteractionBatchRequest:
    """Request to track multiple interactions in batch.

    Attributes:
        interactions (list[PublicInteractionRequest]): List of interactions to track (max 100 per batch)
    """

    interactions: list[PublicInteractionRequest]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interactions = []
        for interactions_item_data in self.interactions:
            interactions_item = interactions_item_data.to_dict()
            interactions.append(interactions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interactions": interactions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_interaction_request import PublicInteractionRequest

        d = dict(src_dict)
        interactions = []
        _interactions = d.pop("interactions")
        for interactions_item_data in _interactions:
            interactions_item = PublicInteractionRequest.from_dict(interactions_item_data)

            interactions.append(interactions_item)

        public_interaction_batch_request = cls(
            interactions=interactions,
        )

        public_interaction_batch_request.additional_properties = d
        return public_interaction_batch_request

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
