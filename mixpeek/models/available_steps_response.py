from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.step_info import StepInfo


T = TypeVar("T", bound="AvailableStepsResponse")


@_attrs_define
class AvailableStepsResponse:
    """Response containing all available steps for a taxonomy/collection.

    This endpoint helps users discover what steps exist in their analytics data
    before querying transitions or paths.

    Example Response:
        ```json
        {
            "taxonomy_id": "tax_sales_stages",
            "collection_id": "col_emails",
            "total_events": 5432,
            "total_sequences": 1000,
            "steps": [
                {
                    "step_key": "inquiry",
                    "event_count": 1000,
                    "sequence_count": 1000,
                    "first_seen": "2025-11-01T00:00:00Z",
                    "last_seen": "2025-12-07T00:00:00Z"
                },
                {
                    "step_key": "followup",
                    "event_count": 450,
                    "sequence_count": 450,
                    "first_seen": "2025-11-02T00:00:00Z",
                    "last_seen": "2025-12-06T00:00:00Z"
                },
                {
                    "step_key": "closed_won",
                    "event_count": 350,
                    "sequence_count": 350,
                    "first_seen": "2025-11-05T00:00:00Z",
                    "last_seen": "2025-12-07T00:00:00Z"
                }
            ]
        }
        ```

        Attributes:
            taxonomy_id (str): Taxonomy ID
            collection_id (str): Collection ID
            total_events (int): Total events in dataset
            total_sequences (int): Total unique sequences
            steps (list[StepInfo]): Available steps sorted by count
    """

    taxonomy_id: str
    collection_id: str
    total_events: int
    total_sequences: int
    steps: list[StepInfo]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        taxonomy_id = self.taxonomy_id

        collection_id = self.collection_id

        total_events = self.total_events

        total_sequences = self.total_sequences

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taxonomy_id": taxonomy_id,
                "collection_id": collection_id,
                "total_events": total_events,
                "total_sequences": total_sequences,
                "steps": steps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_info import StepInfo

        d = dict(src_dict)
        taxonomy_id = d.pop("taxonomy_id")

        collection_id = d.pop("collection_id")

        total_events = d.pop("total_events")

        total_sequences = d.pop("total_sequences")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = StepInfo.from_dict(steps_item_data)

            steps.append(steps_item)

        available_steps_response = cls(
            taxonomy_id=taxonomy_id,
            collection_id=collection_id,
            total_events=total_events,
            total_sequences=total_sequences,
            steps=steps,
        )

        available_steps_response.additional_properties = d
        return available_steps_response

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
