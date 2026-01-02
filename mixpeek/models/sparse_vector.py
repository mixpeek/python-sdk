from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SparseVector")


@_attrs_define
class SparseVector:
    """Sparse vector representation with indices and values.

    Only non-zero elements are stored for efficiency.

    Example:
    ```json
    {
        "indices": [0, 2, 4],
        "values": [0.1, 0.3, 0.5]
    }
    ```

        Attributes:
            indices (list[float | int]): Indices of non-zero elements
            values (list[float]): Values of non-zero elements
    """

    indices: list[float | int]
    values: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        indices = []
        for indices_item_data in self.indices:
            indices_item: float | int
            indices_item = indices_item_data
            indices.append(indices_item)

        values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "indices": indices,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        indices = []
        _indices = d.pop("indices")
        for indices_item_data in _indices:

            def _parse_indices_item(data: object) -> float | int:
                return cast(float | int, data)

            indices_item = _parse_indices_item(indices_item_data)

            indices.append(indices_item)

        values = cast(list[float], d.pop("values"))

        sparse_vector = cls(
            indices=indices,
            values=values,
        )

        sparse_vector.additional_properties = d
        return sparse_vector

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
