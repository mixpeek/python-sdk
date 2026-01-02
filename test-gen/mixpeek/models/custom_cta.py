from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CustomCTA")


@_attrs_define
class CustomCTA:
    """Optional custom button in header that opens a markdown modal.

    Allows users to add a custom call-to-action button in the header bar
    that opens a modal with markdown content when clicked.

        Attributes:
            label (str): Button label text displayed in the header
            markdown_content (str): Markdown content displayed in the modal when button is clicked. Supports standard
                markdown syntax.
    """

    label: str
    markdown_content: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        markdown_content = self.markdown_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "markdown_content": markdown_content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        markdown_content = d.pop("markdown_content")

        custom_cta = cls(
            label=label,
            markdown_content=markdown_content,
        )

        custom_cta.additional_properties = d
        return custom_cta

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
