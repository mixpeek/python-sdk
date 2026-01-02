from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_info_parameters import ToolInfoParameters


T = TypeVar("T", bound="ToolInfo")


@_attrs_define
class ToolInfo:
    """Information about an available agent tool.

    Attributes:
        name: Tool name (use this in available_tools)
        description: What the tool does
        category: Tool category (search, read, create, etc.)
        parameters: Parameter definitions
        required_params: List of required parameter names

        Attributes:
            name (str): Tool name
            description (str): Tool description
            category (str): Tool category
            parameters (ToolInfoParameters | Unset): Parameter definitions
            required_params (list[str] | Unset): Required parameters
    """

    name: str
    description: str
    category: str
    parameters: ToolInfoParameters | Unset = UNSET
    required_params: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        category = self.category

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        required_params: list[str] | Unset = UNSET
        if not isinstance(self.required_params, Unset):
            required_params = self.required_params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "category": category,
            }
        )
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if required_params is not UNSET:
            field_dict["required_params"] = required_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_info_parameters import ToolInfoParameters

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        category = d.pop("category")

        _parameters = d.pop("parameters", UNSET)
        parameters: ToolInfoParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ToolInfoParameters.from_dict(_parameters)

        required_params = cast(list[str], d.pop("required_params", UNSET))

        tool_info = cls(
            name=name,
            description=description,
            category=category,
            parameters=parameters,
            required_params=required_params,
        )

        tool_info.additional_properties = d
        return tool_info

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
