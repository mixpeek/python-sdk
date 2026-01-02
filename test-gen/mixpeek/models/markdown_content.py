from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MarkdownContent")


@_attrs_define
class MarkdownContent:
    """Reusable markdown content model with title and content.

    This model provides a structured way to include rich markdown content
    anywhere in the published retriever configuration. Includes safety
    constraints to prevent database issues.

        Attributes:
            title (str): Title for the markdown content section
            content (str): Markdown-formatted content. Supports standard markdown syntax including headers, lists, links,
                images, code blocks, and emphasis. Limited to 50KB to prevent database issues.
    """

    title: str
    content: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        content = d.pop("content")

        markdown_content = cls(
            title=title,
            content=content,
        )

        markdown_content.additional_properties = d
        return markdown_content

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
