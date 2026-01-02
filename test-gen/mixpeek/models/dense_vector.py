from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DenseVector")


@_attrs_define
class DenseVector:
    """Basic dense vector representation with flexible key naming.

    Accepts a single key-value pair where the key can be any string
    and the value must be a list of floats.

    Example:
    ```json
    {
        "embedding": [0.1, 0.2, 0.3, 0.4, 0.5]
    }
    ```
    or
    ```json
    {
        "my_custom_vector": [0.1, 0.2, 0.3, 0.4, 0.5]
    }
    ```

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dense_vector = cls()

        dense_vector.additional_properties = d
        return dense_vector

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
