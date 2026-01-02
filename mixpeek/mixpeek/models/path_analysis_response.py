from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transition_path import TransitionPath


T = TypeVar("T", bound="PathAnalysisResponse")


@_attrs_define
class PathAnalysisResponse:
    """API response model for multi-step path analysis.

    Contains discovered transition paths with frequency and duration statistics.

    Example Response:
        ```json
        {
            "from_step": "inquiry",
            "to_step": "closed_won",
            "total_sequences": 1000,
            "completed_sequences": 350,
            "completion_rate": 0.35,
            "paths": [
                {
                    "path": ["inquiry", "followup", "proposal", "closed_won"],
                    "count": 120,
                    "percentage": 34.3,
                    "avg_duration_sec": 604800.0
                },
                {
                    "path": ["inquiry", "proposal", "closed_won"],
                    "count": 90,
                    "percentage": 25.7,
                    "avg_duration_sec": 432000.0
                },
                {
                    "path": ["inquiry", "closed_won"],
                    "count": 70,
                    "percentage": 20.0,
                    "avg_duration_sec": 172800.0
                }
            ]
        }
        ```

        Attributes:
            from_step (str):
            to_step (str):
            total_sequences (int): Total sequences that started at from_step
            completed_sequences (int): Number of sequences that reached to_step
            completion_rate (float): Percentage that completed the path
            paths (list[TransitionPath]): List of paths sorted by frequency (most common first)
    """

    from_step: str
    to_step: str
    total_sequences: int
    completed_sequences: int
    completion_rate: float
    paths: list[TransitionPath]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_step = self.from_step

        to_step = self.to_step

        total_sequences = self.total_sequences

        completed_sequences = self.completed_sequences

        completion_rate = self.completion_rate

        paths = []
        for paths_item_data in self.paths:
            paths_item = paths_item_data.to_dict()
            paths.append(paths_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_step": from_step,
                "to_step": to_step,
                "total_sequences": total_sequences,
                "completed_sequences": completed_sequences,
                "completion_rate": completion_rate,
                "paths": paths,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transition_path import TransitionPath

        d = dict(src_dict)
        from_step = d.pop("from_step")

        to_step = d.pop("to_step")

        total_sequences = d.pop("total_sequences")

        completed_sequences = d.pop("completed_sequences")

        completion_rate = d.pop("completion_rate")

        paths = []
        _paths = d.pop("paths")
        for paths_item_data in _paths:
            paths_item = TransitionPath.from_dict(paths_item_data)

            paths.append(paths_item)

        path_analysis_response = cls(
            from_step=from_step,
            to_step=to_step,
            total_sequences=total_sequences,
            completed_sequences=completed_sequences,
            completion_rate=completion_rate,
            paths=paths,
        )

        path_analysis_response.additional_properties = d
        return path_analysis_response

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
