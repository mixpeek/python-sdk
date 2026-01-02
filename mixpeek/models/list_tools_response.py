from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tool_info import ToolInfo


T = TypeVar("T", bound="ListToolsResponse")


@_attrs_define
class ListToolsResponse:
    """Response for listing available agent tools.

    Use this endpoint to discover available tools before creating a session.
    Pass tool names to available_tools in AgentConfig when creating a session.

    Attributes:
        results: List of available tools with descriptions
        total: Total number of tools available
        categories: Unique tool categories

    Example:
        ```python
        response = ListToolsResponse(
            results=[
                ToolInfo(name="smart_search", description="...", category="search"),
                ToolInfo(name="list_collections", description="...", category="read"),
            ],
            total=25,
            categories=["search", "read", "create"]
        )
        ```

        Attributes:
            results (list[ToolInfo]): Available tools
            total (int): Total number of tools
            categories (list[str]): Unique tool categories
    """

    results: list[ToolInfo]
    total: int
    categories: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        total = self.total

        categories = self.categories

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "total": total,
                "categories": categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_info import ToolInfo

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = ToolInfo.from_dict(results_item_data)

            results.append(results_item)

        total = d.pop("total")

        categories = cast(list[str], d.pop("categories"))

        list_tools_response = cls(
            results=results,
            total=total,
            categories=categories,
        )

        list_tools_response.additional_properties = d
        return list_tools_response

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
