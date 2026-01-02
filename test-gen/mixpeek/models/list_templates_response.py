from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.base_template_model import BaseTemplateModel


T = TypeVar("T", bound="ListTemplatesResponse")


@_attrs_define
class ListTemplatesResponse:
    """Response model for listing templates.

    Attributes:
        results (list[BaseTemplateModel]): List of templates
        total_count (int): Total number of templates matching the query
    """

    results: list[BaseTemplateModel]
    total_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "total_count": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_template_model import BaseTemplateModel

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = BaseTemplateModel.from_dict(results_item_data)

            results.append(results_item)

        total_count = d.pop("total_count")

        list_templates_response = cls(
            results=results,
            total_count=total_count,
        )

        list_templates_response.additional_properties = d
        return list_templates_response

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
