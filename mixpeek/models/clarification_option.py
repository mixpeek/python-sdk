from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ClarificationOption")


@_attrs_define
class ClarificationOption:
    """A single option presented to the user for clarifying intent.

    Attributes:
        label: Short label for the option (e.g., "Search existing data")
        description: Detailed explanation of what this option means
        action: Recommended tool/action to use if user selects this option

        Attributes:
            label (str): Option label
            description (str): Option description
            action (str): Recommended action/tool
    """

    label: str
    description: str
    action: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        description = self.description

        action = self.action

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "description": description,
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        description = d.pop("description")

        action = d.pop("action")

        clarification_option = cls(
            label=label,
            description=description,
            action=action,
        )

        clarification_option.additional_properties = d
        return clarification_option

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
