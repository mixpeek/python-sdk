from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilenameRegexSource")


@_attrs_define
class FilenameRegexSource:
    r"""Extract value from filename using a regex pattern with capture groups.

    Useful when metadata is encoded in filenames following a naming convention.
    The regex must contain exactly one capture group to extract the value.

    Provider Compatibility: All providers (works on any filename)

    Example filenames and patterns:
        - "marketing_Q4_2024_final.mp4" with pattern "^(\w+)_Q\d+_" -> "marketing"
        - "user_12345_avatar.jpg" with pattern "user_(\d+)_" -> "12345"
        - "2024-01-15_meeting_notes.pdf" with pattern "^(\d{4}-\d{2}-\d{2})" -> "2024-01-15"
        - "IMG_20240115_143022.jpg" with pattern "IMG_(\d{8})_" -> "20240115"

    Note: Use raw strings in Python or double-escape backslashes in JSON.

    Attributes:
        type: Must be "filename_regex" to identify this source type
        pattern: Python regex with exactly one capture group
        default: Optional default value if regex doesn't match

        Attributes:
            pattern (str): Python regex pattern with exactly one capture group. The captured group becomes the extracted
                value. Pattern is applied to the filename only (not full path). Use non-capturing groups (?:...) for grouping
                without capturing. Remember to escape backslashes in JSON (\\d instead of \d).
            type_ (Literal['filename_regex'] | Unset): Source type identifier. Must be 'filename_regex' for regex
                extraction. Default: 'filename_regex'.
            default (None | str | Unset): Default value if regex doesn't match the filename. If None and regex doesn't
                match, the field is omitted from the object. Useful for ensuring a field always has a value.
    """

    pattern: str
    type_: Literal["filename_regex"] | Unset = "filename_regex"
    default: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pattern = self.pattern

        type_ = self.type_

        default: None | str | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pattern": pattern,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pattern = d.pop("pattern")

        type_ = cast(Literal["filename_regex"] | Unset, d.pop("type", UNSET))
        if type_ != "filename_regex" and not isinstance(type_, Unset):
            raise ValueError(f"type must match const 'filename_regex', got '{type_}'")

        def _parse_default(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        filename_regex_source = cls(
            pattern=pattern,
            type_=type_,
            default=default,
        )

        filename_regex_source.additional_properties = d
        return filename_regex_source

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
