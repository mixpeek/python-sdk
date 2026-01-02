from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.input_source_type import InputSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InputMapping")


@_attrs_define
class InputMapping:
    """Declarative mapping for building inputs from various sources.

    - input_key: The key used in the constructed inputs payload
    - source_type: Where to fetch the value (payload, literal, vector)
    - path: Dot-notation path when source_type is PAYLOAD or VECTOR
    - override: Static value when source_type is LITERAL

        Attributes:
            input_key (str): Key used in the constructed inputs payload.
            source_type (InputSourceType | None | Unset): Source of the value (payload, literal, vector).
            path (None | str | Unset): Dot-notation path inside payload/vector when source_type is PAYLOAD or VECTOR.
            override (Any | None | Unset): Static value used when source_type is LITERAL. Overrides any path.
    """

    input_key: str
    source_type: InputSourceType | None | Unset = UNSET
    path: None | str | Unset = UNSET
    override: Any | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_key = self.input_key

        source_type: None | str | Unset
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        elif isinstance(self.source_type, InputSourceType):
            source_type = self.source_type.value
        else:
            source_type = self.source_type

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        override: Any | None | Unset
        if isinstance(self.override, Unset):
            override = UNSET
        else:
            override = self.override

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input_key": input_key,
            }
        )
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if path is not UNSET:
            field_dict["path"] = path
        if override is not UNSET:
            field_dict["override"] = override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_key = d.pop("input_key")

        def _parse_source_type(data: object) -> InputSourceType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_type_type_0 = InputSourceType(data)

                return source_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InputSourceType | None | Unset, data)

        source_type = _parse_source_type(d.pop("source_type", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_override(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        override = _parse_override(d.pop("override", UNSET))

        input_mapping = cls(
            input_key=input_key,
            source_type=source_type,
            path=path,
            override=override,
        )

        input_mapping.additional_properties = d
        return input_mapping

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
