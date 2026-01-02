from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NamedDenseVectors")


@_attrs_define
class NamedDenseVectors:
    """Root model mapping vector names → dense float lists.

    Accepts JSON like:
    ```json
    {
        "vector_a": [0.1, 0.2, 0.3],
        "vector_b": [0.4, 0.5, 0.6]
    }
    ```

    """

    additional_properties: dict[str, list[float]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        named_dense_vectors = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = cast(list[float], prop_dict)

            additional_properties[prop_name] = additional_property

        named_dense_vectors.additional_properties = additional_properties
        return named_dense_vectors

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[float]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[float]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
